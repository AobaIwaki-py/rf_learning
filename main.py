import os
from config import PARAMS
from utils import dump_params


def main():
    result_dir = f'result/{PARAMS.run_date}'  # 結果出力ディレクトリ
    os.mkdir(result_dir)  # 実行日時を名前とするディレクトリを作成
    dump_params(PARAMS, f'{result_dir}')  # パラメータを出力
    
    # do something...


if __name__ == "__main__":
    main()
