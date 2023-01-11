import os
import subprocess
import sys


def main():
    command = sys.argv[3]
    args = sys.argv[4:]

    completed_process = subprocess.run([command, *args])
    exit(completed_process.returncode)


if __name__ == "__main__":
    main()
