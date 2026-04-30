import os
import sys
import site

venv_p, venv_n = os.path.split(os.getenv("VIRTUAL_ENV", ""))
inst_path = site.getsitepackages()[0]


def venv_detect() -> None:
    if os.environ.get("VIRTUAL_ENV"):
        print("MATRIX STATUS: Welcome to the construct")
        print()
        print(f"Current pyhton: {sys.executable}")
        print(f"Virtutal Enviorment: {venv_n}")
        print(f"Environment Path: {venv_p}")
        print()
        print("Success: You're in a isolated environment!")
        print("Safe to install packages without affecting")
        print("the global system")
        print()
        print("Package installation path")
        print(f"{inst_path}")
    else:
        print("MATRIX STATUS: You're still plugged in")
        print()
        print(f"Current pyhton: {sys.executable}")
        print(f"Virtutal Enviorment: {os.environ.get('VIRTUAL_ENV')} detected")
        print()
        print("WARNING: You're in the global environment!")
        print("The Machine can see everything you install")
        print()
        print("to enter the constuct, run:")
        print("python3 -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env\\Scripts\\activete")
        print()
        print("Then run this program again.")


if __name__ == "__main__":
    venv_detect()
