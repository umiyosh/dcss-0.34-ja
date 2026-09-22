#!/usr/bin/env python3
"""Exercise real TextDB and Lua lookup without modifying data or user saves.

Build a FULLDEBUG Console executable, then run this script from any directory.
The Japanese strings are test fixtures only; no adopted translation is added.
"""

import argparse
from pathlib import Path
import shutil
import subprocess
import tempfile


def run_fixture(source: Path, executable: Path, language: str) -> None:
    fixtures = source / "util/tests/message-translation"
    with tempfile.TemporaryDirectory(prefix="crawl-message-translation-") as name:
        sandbox = Path(name)
        data = sandbox / "dat"
        data.mkdir()
        for child in (source / "dat").iterdir():
            if child.name != "database":
                (data / child.name).symlink_to(
                    child, target_is_directory=child.is_dir())
        database = data / "database"
        database.mkdir()
        for child in (source / "dat/database").iterdir():
            if child.name != "ja":
                (database / child.name).symlink_to(
                    child, target_is_directory=child.is_dir())
        japanese = database / "ja"
        japanese.mkdir()
        original_ja = source / "dat/database/ja"
        if original_ja.is_dir():
            for child in original_ja.iterdir():
                if child.name != "messages.txt":
                    (japanese / child.name).symlink_to(child)
        # Keep meaningful key whitespace out of the fixture file's line ends.
        dictionary = (fixtures / "messages.txt").read_text(encoding="utf-8")
        (japanese / "messages.txt").write_text(
            dictionary.replace("@TRAILING_SPACE@", " "), encoding="utf-8")
        tests = sandbox / "test"
        tests.mkdir()
        shutil.copyfile(fixtures / f"{language}.lua",
                        tests / "message-fixture.lua")
        rc = sandbox / "empty.rc"
        rc.touch()
        command = [str(executable), "-dir", str(sandbox), "-rc", str(rc),
                   "-extra-opt-last", f"language={language}"]
        for action in (["-builddb"], ["-test", "message-fixture"]):
            result = subprocess.run(
                command + action, cwd=sandbox, text=True,
                stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=120,
            )
            if result.returncode != 0:
                raise RuntimeError(f"{language} fixture failed:\n{result.stdout}")
        if "1 tests, 1 succeeded, 0 failed" not in result.stdout:
            raise RuntimeError(f"{language} test did not run:\n{result.stdout}")
        print(f"{language}: real TextDB lookup, Lua API and message output passed")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    source = Path(__file__).resolve().parents[1]
    parser.add_argument("--crawl", type=Path, default=source / "crawl")
    args = parser.parse_args()
    for language in ("ja", "en"):
        run_fixture(source, args.crawl.resolve(), language)


if __name__ == "__main__":
    main()
