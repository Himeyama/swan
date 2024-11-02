import socket
import time


def check_tcp_connectivity(host: str, port: int, interval: int = 0, retries: int = 1):
    """
    指定されたホストとポートにTCP接続できるかを確認します。
    :param host: 接続先ホスト名またはIPアドレス
    :param port: 接続先ポート番号
    :param interval: 接続試行の間隔（秒）
    :param retries: リトライ回数
    :return: 接続成功ならTrue、失敗なら False
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    for _ in range(retries):
        try:
            s.connect((host, port))
            s.close()
            return True
        except socket.error:
            time.sleep(interval)
            s.close()
    return False

def get_random_port():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('', 0))
        return s.getsockname()[1]
