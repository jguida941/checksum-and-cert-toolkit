#!/usr/bin/env python3
import socket
import subprocess
import sys
import time
import webbrowser
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
CMD = ["./mvnw", "spring-boot:run"]
URL = "https://localhost:8443/hash"
PORT = 8443


def wait_for_port(host: str, port: int, timeout: int = 120) -> bool:
    deadline = time.time() + timeout
    while time.time() < deadline:
        try:
            with socket.create_connection((host, port), timeout=2):
                return True
        except OSError:
            time.sleep(1)
    return False


def main() -> None:
    print(f"Starting server with: {' '.join(CMD)}")
    proc = subprocess.Popen(CMD, cwd=REPO_ROOT)
    try:
        if not wait_for_port("127.0.0.1", PORT):
            print(f"Server did not open port {PORT} in time; shutting down.")
            proc.terminate()
            try:
                proc.wait(10)
            except subprocess.TimeoutExpired:
                proc.kill()
            sys.exit(1)

        print(f"Opening {URL}")
        webbrowser.open(URL)
        proc.wait()
    except KeyboardInterrupt:
        print("Interrupted, stopping server...")
    finally:
        if proc.poll() is None:
            proc.terminate()
            try:
                proc.wait(10)
            except subprocess.TimeoutExpired:
                proc.kill()


if __name__ == "__main__":
    main()
