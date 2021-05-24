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