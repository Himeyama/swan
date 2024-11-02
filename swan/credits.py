import os
import re
import subprocess

def main():
    path = 'dist\_internal'

    # ディレクトリ一覧を取得
    directories = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    directories = [item for item in directories if not re.match(r'importlib_metadata-.*', item)]

    if os.path.isdir("dist") and os.path.isdir(path):
        with open("dist\credits.txt", "w") as file:
            for pkg in directories:
                result = subprocess.run(["pip", "show", pkg], capture_output=True, text=True)
                result = result.stdout.split("\n")
                result = [item for item in result if not item.startswith('Location:')]
                result = "\n".join(result)
                file.write(result + "\n")
    else:
        print("ビルドされていません")
