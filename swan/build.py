import os
import shutil
import subprocess
from swan import credits

def main():
    if os.path.isdir("build"):
        shutil.rmtree("build")
    if os.path.isdir("dist"):
        shutil.rmtree("dist")
    command = ["poetry", "run", "pyinstaller", "swan.spec", "-y"]
    result = subprocess.run(command, capture_output=True, text=True)
    print(result.stdout)
    print(result.stderr)
    credits.main()
