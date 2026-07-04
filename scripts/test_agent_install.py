#!/usr/bin/env python3
"""Smoke-test project/user install, verification, update, conflicts, and uninstall."""
from __future__ import annotations

import argparse
import os
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INSTALLER = ROOT / "scripts" / "agent_install.py"
MARKER = "<!-- PRODUCT-DESIGN-ORCHESTRATOR:START -->"


def run(args: list[str], *, env: dict[str, str] | None = None, expect: int = 0) -> subprocess.CompletedProcess[str]:
    command = [sys.executable, str(INSTALLER), *args]
    result = subprocess.run(command, text=True, capture_output=True, env=env)
    if result.returncode != expect:
        raise AssertionError(
            f"Command returned {result.returncode}, expected {expect}: {' '.join(command)}\n"
            f"STDOUT:\n{result.stdout}\nSTDERR:\n{result.stderr}"
        )
    return result


def count_dirs(path: Path) -> int:
    return sum(1 for child in path.iterdir() if child.is_dir())


def project_roundtrip(base: Path, env: dict[str, str]) -> None:
    project = base / "project"
    project.mkdir()
    agents_original = "# Existing Codex rules\nKeep this.\n"
    claude_original = "# Existing Claude rules\nKeep this too.\n"
    (project / "AGENTS.md").write_text(agents_original, encoding="utf-8")
    (project / "CLAUDE.md").write_text(claude_original, encoding="utf-8")

    run(["install", "--agent", "both", "--scope", "project", "--project", str(project), "--dry-run"], env=env)
    assert not (project / ".agents").exists(), "dry-run wrote Codex files"
    assert not (project / ".claude").exists(), "dry-run wrote Claude files"

    run(["install", "--agent", "both", "--scope", "project", "--project", str(project)], env=env)
    run(["verify", "--agent", "both", "--scope", "project", "--project", str(project)], env=env)
    assert count_dirs(project / ".agents" / "skills") == 70
    assert count_dirs(project / ".claude" / "skills" / "product-design-orchestrator" / "skills") == 70
    assert MARKER in (project / "AGENTS.md").read_text(encoding="utf-8")
    assert MARKER in (project / "CLAUDE.md").read_text(encoding="utf-8")

    # Idempotent update.
    run(["install", "--agent", "both", "--scope", "project", "--project", str(project)], env=env)
    run(["verify", "--agent", "both", "--scope", "project", "--project", str(project)], env=env)

    run(["uninstall", "--agent", "both", "--scope", "project", "--project", str(project)], env=env)
    assert (project / "AGENTS.md").read_text(encoding="utf-8") == agents_original
    assert (project / "CLAUDE.md").read_text(encoding="utf-8") == claude_original
    assert not (project / ".agents" / "product-design-orchestrator").exists()
    assert not (project / ".claude" / "skills" / "product-design-orchestrator").exists()


def user_roundtrip(base: Path, env: dict[str, str]) -> None:
    project = base / "user-project"
    project.mkdir()
    run(["install", "--agent", "both", "--scope", "user", "--project", str(project), "--activate-global"], env=env)
    run(["verify", "--agent", "both", "--scope", "user", "--project", str(project)], env=env)
    home = Path(env["HOME"])
    assert count_dirs(home / ".agents" / "skills") == 70
    assert (home / ".claude" / "skills" / "product-design-orchestrator" / ".claude-plugin" / "plugin.json").is_file()
    assert MARKER in (Path(env["CODEX_HOME"]) / "AGENTS.md").read_text(encoding="utf-8")
    assert MARKER in (home / ".claude" / "CLAUDE.md").read_text(encoding="utf-8")
    run(["uninstall", "--agent", "both", "--scope", "user", "--project", str(project)], env=env)
    assert not (home / ".agents" / "product-design-orchestrator").exists()
    assert not (home / ".claude" / "skills" / "product-design-orchestrator").exists()


def orchestrated_profile(base: Path, env: dict[str, str]) -> None:
    project = base / "orchestrated"
    project.mkdir()
    run([
        "install", "--agent", "codex", "--scope", "project", "--project", str(project),
        "--profile", "orchestrated", "--no-guidance"
    ], env=env)
    assert count_dirs(project / ".agents" / "skills") == 5
    run(["verify", "--agent", "codex", "--scope", "project", "--project", str(project)], env=env)
    run(["uninstall", "--agent", "codex", "--scope", "project", "--project", str(project)], env=env)


def profile_switch(base: Path, env: dict[str, str]) -> None:
    project = base / "switch-profile"
    project.mkdir()

    # A full install can be reduced to the context-light gateway profile without
    # leaving stale, installer-owned native skills behind.
    run(["install", "--agent", "codex", "--scope", "project", "--project", str(project),
         "--profile", "full"], env=env)
    assert count_dirs(project / ".agents" / "skills") == 70
    run(["install", "--agent", "codex", "--scope", "project", "--project", str(project),
         "--profile", "orchestrated"], env=env)
    assert count_dirs(project / ".agents" / "skills") == 5
    run(["verify", "--agent", "codex", "--scope", "project", "--project", str(project)], env=env)
    run(["uninstall", "--agent", "codex", "--scope", "project", "--project", str(project)], env=env)
    assert not (project / "AGENTS.md").exists(), "installer-created guidance was not removed"


def guidance_lifecycle(base: Path, env: dict[str, str]) -> None:
    # User guidance can be activated, then intentionally retired on update.
    user_project = base / "guidance-toggle"
    user_project.mkdir()
    run(["install", "--agent", "both", "--scope", "user", "--project", str(user_project),
         "--activate-global"], env=env)
    home = Path(env["HOME"])
    codex_agents = Path(env["CODEX_HOME"]) / "AGENTS.md"
    claude_md = home / ".claude" / "CLAUDE.md"
    assert codex_agents.is_file() and claude_md.is_file()
    run(["install", "--agent", "both", "--scope", "user", "--project", str(user_project),
         "--no-guidance"], env=env)
    assert not codex_agents.exists(), "retired Codex global guidance remains"
    assert not claude_md.exists(), "retired Claude global guidance remains"
    run(["uninstall", "--agent", "both", "--scope", "user", "--project", str(user_project)], env=env)


def conflict_preflight(base: Path, env: dict[str, str]) -> None:
    project = base / "conflict"
    conflict = project / ".agents" / "skills" / "pdo-color"
    conflict.mkdir(parents=True)
    (conflict / "SKILL.md").write_text("---\nname: pdo-color\ndescription: unrelated\n---\n", encoding="utf-8")
    result = run(["install", "--agent", "both", "--scope", "project", "--project", str(project)], env=env, expect=2)
    assert "unmanaged Codex skill directory" in result.stderr
    # Preflight must prevent a partial install of either agent.
    assert not (project / ".agents" / "product-design-orchestrator").exists()
    assert not (project / ".claude" / "skills" / "product-design-orchestrator").exists()
    assert (conflict / "SKILL.md").is_file()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--group",
        choices=["all", "project", "user", "orchestrated", "profile-switch", "guidance", "conflict"],
        default="all",
        help="Run one fixture group or the complete smoke suite",
    )
    args = parser.parse_args()

    groups = [
        ("project", "project install/update/uninstall", project_roundtrip),
        ("user", "user install/update/uninstall", user_roundtrip),
        ("orchestrated", "context-light profile", orchestrated_profile),
        ("profile-switch", "full-to-context-light profile switch", profile_switch),
        ("guidance", "global guidance lifecycle", guidance_lifecycle),
        ("conflict", "conflict preflight", conflict_preflight),
    ]
    selected = groups if args.group == "all" else [item for item in groups if item[0] == args.group]

    with tempfile.TemporaryDirectory(prefix="pdo-agent-install-test-") as tmp:
        base = Path(tmp)
        home = base / "home"
        home.mkdir()
        env = os.environ.copy()
        env["HOME"] = str(home)
        env["USERPROFILE"] = str(home)
        env["CODEX_HOME"] = str(home / "custom-codex")
        for index, (_, label, function) in enumerate(selected, start=1):
            print(f"[{index}/{len(selected)}] {label}", flush=True)
            function(base, env)
    print("Agent installer smoke tests passed")


if __name__ == "__main__":
    main()
