import os
import shutil
import subprocess
from datetime import datetime

def main():
    # ディレクトリの削除
    if os.path.exists('dist'):
        shutil.rmtree('dist')
    if os.path.exists('build'):
        shutil.rmtree('build')

    # Poetryでビルド
    subprocess.run(['poetry', 'run', 'build'], check=True)

    # バージョン、日付、サイズの取得
    version = datetime.now().strftime('%y.%m.%d')
    date = datetime.now().strftime('%Y%m%d')
    size = round(sum(f.stat().st_size for f in os.scandir('./dist') if f.is_file()) / 1024)

    # NSISでインストーラーを作成
    nsis_command = [
        'C:\\Program Files (x86)\\NSIS\\makensis.exe',
        f'/DVERSION={version}',
        f'/DDATE={date}',
        f'/DSIZE={size}',
        'install.nsi'
    ]
    subprocess.run(nsis_command, check=True)
