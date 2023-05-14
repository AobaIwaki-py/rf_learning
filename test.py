from typing import Any, Tuple, List
from logging import getLogger
import argparse
# 
from config import common_args, Parameters
from utils import set_logging, setup_params
from object.agent import Agent

logger = getLogger(__name__)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser = common_args(parser)  # コマンドライン引数引数を読み込み
    args = parser.parse_args()
    params = Parameters(**setup_params(vars(args), args.parameters))  # args，run_date，git_revisionなどを追加した辞書を取得

    set_logging(result_dir='log', file_name='agent')
    logger.info('Start')
    
    agent = Agent()
    print(agent.name)
    agent.set_position(1, 1)
    print(agent.get_position())
    print(agent.get_next_position('s'))
    agent.move('d')
    print(agent.get_position())