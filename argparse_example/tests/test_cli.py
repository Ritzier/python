# tests/test_main.py
import subprocess


def test_login_qr():
    result = subprocess.run(
        ["poetry", "run", "run", "login", "qr"],
        capture_output=True,
        text=True,
    )
    assert "Logging in with QR code..." in result.stdout


def test_login_code():
    result = subprocess.run(
        ["poetry", "run", "run", "login", "code"],
        capture_output=True,
        text=True,
    )
    assert "Logging in with verification code..." in result.stdout


def test_login_browser():
    result = subprocess.run(
        ["poetry", "run", "run", "login", "browser"],
        capture_output=True,
        text=True,
    )
    assert "Logging in via browser..." in result.stdout


def test_chat():
    result = subprocess.run(
        ["poetry", "run", "run", "chat"], capture_output=True, text=True
    )
    assert "Starting chat..." in result.stdout


def test_ls():
    result = subprocess.run(
        ["poetry", "run", "run", "ls"], capture_output=True, text=True
    )
    assert "Listing files..." in result.stdout
