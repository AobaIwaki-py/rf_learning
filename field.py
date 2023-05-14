from logging import getLogger
from utils import set_logging
from object.object import Object
import argparse
from typing import Any, Tuple, List
import numpy as np
# 
from config import common_args, Parameters
from utils import set_logging, setup_params

logger = getLogger(__name__)

class Field:
    '''Class for the field of the game. It is a rectangle with width and height.'''

    def __init__(self, params) -> None:
        self.__map: np.ndarray = np.zeros((params.map_width+1, params.map_height+1))
        logger.info(f'Field size: {self.__map.shape}')
        self.__map_char: dict = params.map_char
        self.obj_num: dict = params.obj_num
        self.wall_ratio: float = params.wall_ratio
        
        self.set_wall(self.wall_ratio)
    
    def __str__(self) -> str:
        return self.__map.__str__()
    
    def set_object(self, object: Object) -> None:
        logger.debug('Set object')
        name = object.name
        self.__map = np.where(self.__map == self.obj_num[name], self.obj_num['Road'], self.__map)
        self.__map[object.get_position()] = self.obj_num[name]
    
    def set_wall(self, ratio: float) -> None:
        for x in range(self.__map.shape[0]):
            for y in range(self.__map.shape[1]):
                if np.random.rand() < ratio:
                    self.__map[x, y] = -1
                    
    def is_wall(self, X: int, Y: int) -> bool:
        '''Check whether the agent is on the wall or not.'''
        return self.__map[X, Y] == -1
    
    def get_random_position(self) -> Tuple[int, int]:
        '''Get a random position on the field.'''
        pos = tuple(np.random.randint(1, self.__map.shape[i]) for i in range(2))
        while(self.is_something(*pos)):
            pos = tuple(np.random.randint(1, self.__map.shape[i]) for i in range(2))
        return pos
    
    def is_something(self, X: int, Y: int) -> bool:
        '''Check whether the agent is on something or not.'''
        return self.__map[X, Y] != 0
    
    def render(self) -> None:
        '''Render the field with the agent.'''
        for x in range(1, self.__map.T.shape[0]):
            for y in range(1, self.__map.T.shape[1]):
                print(self.__map_char[self.__map.T[-x,y]], end='')
            print()
        
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser = common_args(parser)  # コマンドライン引数引数を読み込み
    args = parser.parse_args()
    params = Parameters(**setup_params(vars(args), args.parameters))  # args，run_date，git_revisionなどを追加した辞書を取得

    set_logging(result_dir='log', file_name='field', stdout_log_level='DEBUG')
    logger.info('Start')
    
    field = Field(params)
    print(field)
    agent_pos = tuple(input('Please enter the agent position (x,y): ').split())
    agent_pos = tuple(int(i) for i in agent_pos)
    print(agent_pos)
    field.set_agent(*agent_pos)
    field.render()
    
    logger.info('End')
