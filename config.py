"""
プロジェクト内のパラメータを管理するためのモジュール．

A) プログラムを書くときにやること．
  1) デフォルトパラメータを `Parameters` クラス内で定義する．
  2) コマンドライン引数を `cmd_args` 内で定義する．
  3) 変数 `PARAMS` にデータクラスとしてパラメータが保管されるので，これを他のモジュールから以下のように参照する．
  >>> from config import PARAMS
  >>> print(PARAMS.param1)
  4) 結果出力用ディレクトリに以下のようにファイル出力する．
  >>> utils.dump_params(PARAMS, 'path_to_output_dir')

B) パラメータを指定して実行するときにやること．
  1) `python config.py` とすると，デフォルトパラメータが `parameters.json` というファイルに書き出される．
  2) パラメータを指定する際は，Parametersクラスを書き換えるのではなく，jsonファイル内の値を書き換えて，
  `python -p parameters.json main.py`
  のようにjsonファイルを指定する．

"""
from dataclasses import dataclass, field
import argparse
from utils import setup_params, dump_params


@dataclass(frozen=True)
class Parameters:
    """
    プログラム全体を通して共通のパラメータを保持するクラス．
    ここにプロジェクト内で使うパラメータを一括管理する．
    """
    args: dict  # コマンドライン引数
    run_date: str  # 実行時の時刻
    git_revision: str  # 実行時のプログラムのGitのバージョン
    
    param1: int = 0  # パラメータを定義する例
    param2: dict = field(default_factory=lambda: {'k1': 'v1', 'k2': 'v2'})  # リストや辞書で与える例


def cmd_args():
    """
    コマンドライン引数を定義する関数．
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--parameters", help="パラメータ設定ファイルのパスを指定．デフォルトはNone", type=str, default=None)
    parser.add_argument("-a", "--arg1", type=int, help="arg1の説明", default=0)  # コマンドライン引数を指定
    parser.add_argument("--arg2", type=float, help="arg2の説明", default=1.0)  # コマンドライン引数を指定
    return parser.parse_args()


args = cmd_args()  # コマンドライン引数を取得
PARAMS = Parameters(**setup_params(vars(args), args.parameters))  # args，run_date，git_revisionなどを追加した辞書を取得


if __name__ == "__main__":
    dump_params(PARAMS, './', partial=True)
