from typing import Any, Tuple, List
from logging import getLogger
import argparse
# 
from config import common_args, Parameters
from utils import set_logging, setup_params
from object.object import Object


logger = getLogger(__name__)

class Agent(Object):
    def __init__(self) -> None:
        super().__init__()
    
    def get_next_position(self, direction:str =None) -> Tuple[int, int]:
        x, y = self.get_position()
        if direction in ['up', 'w']:
            return x, y+1
        elif direction in ['down', 's']:
            return x, y-1
        elif direction in ['right', 'd']:
            return x+1, y
        elif direction in ['left', 'a']:
            return x-1, y
        else:
            return -1, -1
        
    def move(self, direction) -> None:
        '''Move the agent to the direction.'''
        if direction is None:
            direction = input("Please enter a direction (w/a/s/d) : ")
        if direction in ['up', 'w', 'down', 's', 'right', 'd', 'left', 'a']:
            self.set_position(*self.get_next_position(direction))
        else:
            raise ValueError(f'Invalid direction: {direction}')
         
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
    