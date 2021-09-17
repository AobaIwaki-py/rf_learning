"""便利な関数群"""
import torch
import subprocess
import logging
import json


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


def update_json(json_file, dict):
    """jsonファイルをupdateするプログラム
        import json が必要
    Parameters
    ----------
    json_file : str
        jsonファイルのpath
    dict : dict
        追加もしくは更新したいdict
    """
    with open(json_file) as f:
        df = json.load(f)

    df.update(dict)

    with open(json_file, 'w') as f:
        json.dump(df, f, indent=4)

def get_gpu_info(nvidia_smi_path='nvidia-smi', no_units=True):
    """
    空いているgpuの番号を持ってくるプログラム
    :return: 空いているgpu番号 or 'cpu'
    """
    keys = (
    'index',
    'uuid',
    'name',
    'timestamp',
    'memory.total',
    'memory.free',
    'memory.used',
    'utilization.gpu',
    'utilization.memory'
    )   
    if torch.cuda.is_available():
        nu_opt = '' if not no_units else ',nounits'
        cmd = '%s --query-gpu=%s --format=csv,noheader%s' % (nvidia_smi_path, ','.join(keys), nu_opt)
        output = subprocess.check_output(cmd, shell=True)
        lines = output.decode().split('\n')
        lines = [ line.strip() for line in lines if line.strip() != '' ]

        gpu_info =  [{ k: v for k, v in zip(keys, line.split(', ')) } for line in lines]

        min_gpu_index = 0
        min_gpu_memory_used = 100
        for gpu in gpu_info:
            gpu_index = gpu['index']
            gpu_memory = int(gpu['utilization.gpu'])
            if min_gpu_memory_used >= gpu_memory:
                min_gpu_memory_used = gpu_memory
                min_gpu_index = gpu_index

        return "cuda:" + str(int(min_gpu_index))
    else:
        return 'cpu'
