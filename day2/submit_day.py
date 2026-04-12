from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
from pathlib import Path

_LAB_RE = re.compile(r"^lab\d+$")
_IGNORE = shutil.ignore_patterns("__pycache__", ".pytest_cache", "*.pyc", "*.pyo")


def _lab_sort_key(name: str) -> tuple[int, str]:
    try:
        return (int(name.removeprefix("lab")), name)
    except ValueError:
        return (10**9, name)


def _discover_labs(day_dir: Path) -> list[str]:
    labs = [p.name for p in day_dir.iterdir() if p.is_dir() and _LAB_RE.match(p.name)]
    labs.sort(key=_lab_sort_key)
    return labs


def _run_pytest(day_dir: Path, lab_name: str) -> None:
    tests_dir = day_dir / lab_name / "tests"
    if not tests_dir.exists():
        raise RuntimeError(f"tests folder not found: {tests_dir}")

    cmd = [sys.executable, "-m", "pytest", "-q", str(tests_dir)]
    completed = subprocess.run(cmd, cwd=str(day_dir.parent))
    if completed.returncode != 0:
        raise RuntimeError(f"verification failed for {lab_name}")


def _reset_lab(day_dir: Path, starter_dir: Path, lab_name: str) -> None:
    src = starter_dir / lab_name
    dst = day_dir / lab_name

    if not src.exists():
        raise RuntimeError(f"starter snapshot not found: {src}")

    if dst.exists():
        shutil.rmtree(dst)

    shutil.copytree(src, dst, ignore=_IGNORE)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Reset this day's lab folders back to starter code. "
            "Default: reset only (no tests)."
        )
    )
    parser.add_argument(
        "--labs",
        nargs="*",
        default=[],
        help="Which labs to reset (example: --labs lab1 lab2). Default: all lab* folders.",
    )
    parser.add_argument(
        "--verify",
        action="store_true",
        help="Run each lab's tests before resetting.",
    )

    args = parser.parse_args(argv)

    day_dir = Path(__file__).resolve().parent
    starter_dir = day_dir / "_starter"

    if not starter_dir.exists():
        print(f"[error] Missing starter snapshot folder: {starter_dir}")
        print("This day should include a _starter/ folder for git-free resets.")
        return 2

    all_labs = _discover_labs(day_dir)
    if not all_labs:
        print(f"[error] No labs found under {day_dir} (expected lab1, lab2, ...)")
        return 2

    labs = args.labs or all_labs
    for lab_name in labs:
        if not _LAB_RE.match(lab_name):
            print(f"[error] Invalid lab name '{lab_name}' (expected lab1/lab2/...)")
            return 2
        if lab_name not in all_labs:
            print(f"[error] Lab folder not found: {day_dir / lab_name}")
            return 2

    if args.verify:
        for lab_name in labs:
            print(f"Verifying {day_dir.name}/{lab_name}...", flush=True)
            try:
                _run_pytest(day_dir, lab_name)
            except RuntimeError as exc:
                print(f"[error] {exc}")
                return 1

    for lab_name in labs:
        print(f"Resetting {day_dir.name}/{lab_name}...", flush=True)
        try:
            _reset_lab(day_dir, starter_dir, lab_name)
        except RuntimeError as exc:
            print(f"[error] {exc}")
            return 1

    print("Done.")
    print(f"Tip: reference solutions live in {day_dir.name}/solution/")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
