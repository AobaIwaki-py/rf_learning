"""便利な関数群"""
import torch
import subprocess


def get_device():
    """
    実行環境のデバイス(GPU or CPU) を取得
    :return: デバイス (Device)
    """
    if torch.cuda.is_available():
        device = torch.device('cuda')
    else:
        device = torch.device('cpu')
    return device


def get_git_revision():
    """
    現在のGitのリビジョンを取得
    :return: revision ID (str)
    """
    cmd = "git rev-parse HEAD"
    revision = subprocess.check_output(cmd.split())  # 現在のコードのgitのリビジョンを取得
    return revision.decode()


def set_logging(result_dir):
    """
    ログを標準出力とファイルに書き出すよう設定する関数．
    :param result_dir: ログの出力先
    :return: 設定済みのrootのlogger
    
    Example: 
    >>> logger = logging.getLogger(__name__)
    >>> set_logging(result_dir)
    >>> logger.info('log message...')
    """
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)  # ログレベル
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')  # ログのフォーマット
    # 標準出力へのログ出力設定
    handler = logging.StreamHandler()
    handler.setLevel(logging.INFO)  # 出力ログレベル
    handler.setFormatter(formatter)  # フォーマットを指定
    logger.addHandler(handler)
    # ファイル出力へのログ出力設定
    file_handler = logging.FileHandler(f'{result_dir}log.log', 'w')  # ログ出力ファイル
    file_handler.setLevel(logging.DEBUG)  # 出力ログレベル
    file_handler.setFormatter(formatter)  # フォーマットを指定
    logger.addHandler(file_handler)
    return logger