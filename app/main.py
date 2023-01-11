import os
import subprocess
import sys
import tempfile
import shutil


def main():
    command = sys.argv[3]
    args = sys.argv[4:]

    with tempfile.TemporaryDirectory() as chroot_dir:
        # Copy executable into chroot
        os.makedirs(os.path.join(chroot_dir, os.path.dirname(command).strip("/")))
        shutil.copy(command, os.path.join(chroot_dir, command.strip("/")))

        os.chroot(chroot_dir)

        completed_process = subprocess.run([command, *args])
        exit(completed_process.returncode)


if __name__ == "__main__":
    main()
