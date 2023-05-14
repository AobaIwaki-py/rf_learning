from typing import Any, Tuple, List
from logging import getLogger
import numpy as np
import argparse
# 
from config import common_args, Parameters
from utils import set_logging, setup_params


logger = getLogger(__name__)

class Agent:
    __X: int
    __Y: int
    
    def __init__(self, params) -> None:
        self.map_width = params.map_width
        self.map_height = params.map_height

    def set_position(self, X: int, Y: int) -> None:
        self.__X = X
        self.__Y = Y
        
    def set_random_position(self):
        self.set_position(np.random.randint(1, self.map_width+1), np.random.randint(1, self.map_height+1))
        
    def get_position(self) -> Tuple[int, int]:
        return self.__X, self.__Y
    
    def get_next_position(self, direction:str =None) -> Tuple[int, int]:
        if direction in ['up', 'w']:
            return self.__X, self.__Y+1
        elif direction in ['down', 's']:
            return self.__X, self.__Y-1
        elif direction in ['right', 'd']:
            return self.__X+1, self.__Y
        elif direction in ['left', 'a']:
            return self.__X-1, self.__Y
        else:
            return -1, -1
        
    def move(self, direction) -> None:
        '''Move the agent to the direction.'''
        if direction is None:
            direction = input("Please enter a direction (w/a/s/d) : ")
        if direction in ['up', 'w']:
            logger.info('Move up')
            self.__Y += 1
        elif direction in ['down', 's']:
            logger.info('Move down')
            self.__Y -= 1
        elif direction in ['right', 'd']:
            logger.info('Move right')
            self.__X += 1
        elif direction in ['left', 'a']:
            logger.info('Move left')
            self.__X -= 1
        else:
            raise ValueError(f'Invalid direction: {direction}')
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser = common_args(parser)  # コマンドライン引数引数を読み込み
    args = parser.parse_args()
    params = Parameters(**setup_params(vars(args), args.parameters))  # args，run_date，git_revisionなどを追加した辞書を取得

    set_logging(result_dir='log', file_name='agent')
    logger.info('Start')
    
    agent = Agent(params)
    agent.set_position(1,3)
    logger.info(f'agent position: {agent.get_position()}')
    agent.move()
    logger.info(f'agent position: {agent.get_position()}')
    agent.move()
    logger.info(f'agent position: {agent.get_position()}')
    agent.move()
    logger.info(f'agent position: {agent.get_position()}')
    agent.move()
    logger.info(f'agent position: {agent.get_position()}')