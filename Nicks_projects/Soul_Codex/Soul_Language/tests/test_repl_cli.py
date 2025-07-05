import subprocess
import sys


def test_sqly_help():
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "src.sqly.repl",
            "--help",
        ],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert "usage" in result.stdout.lower()


def test_sqly_stdin_smoke():
    proc = subprocess.run(
        [sys.executable, "-m", "src.sqly.repl", "--stdin"],
        input="GLYPH #signal-demo",
        text=True,
        capture_output=True,
    )
    assert proc.returncode == 0
    assert "Frames:" in proc.stdout
