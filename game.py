from agent import Agent
from field import Field
from logging import getLogger
import argparse
import numpy as np

from config import common_args, Parameters
from utils import set_logging, setup_params

logger = getLogger(__name__)

class Game:
    __direction: str = None
    def __init__(self, params,) -> None:
        self.__map_width = params.map_width
        self.__map_height = params.map_height
        self.__field = Field(params)
        self.__agent = Agent(params)
        # Set Initial Position
        self.__agent.set_position(np.random.randint(1, self.__map_width), np.random.randint(1, self.__map_height))

    def get_instruction(self) -> bool:
        self.__direction = input('Please enter a direction (w/a/s/d) : ')
        self.__next_pos = self.__agent.get_next_position(self.__direction)
        assert type(self.__next_pos) == tuple, 'next position must be tuple'
        assert len(self.__next_pos) == 2, 'next position must be 2D'

    def check_next_position(self) -> bool:
        if self.__next_pos == (-1, -1):
            logger.info('Invalid direction!')
            return False
        elif self.__next_pos[0] <= 0 or self.__next_pos[0] > self.__map_width or self.__next_pos[1] <= 0 or self.__next_pos[1] > self.__map_height:
            logger.info('You are out of the field!')
            return False
        elif self.__field.is_wall(*self.__next_pos):
            logger.info('You hit the wall!')
            return False
        else:
            return True
    
    def update_field(self) -> None:
        if self.__direction:
            self.__agent.move(self.__direction)
        self.__field.set_agent(*self.__agent.get_position())
        
    def render_field(self) -> None:
        logger.info(f'Agent position: {self.__agent.get_position()}')
        self.__field.render()
        
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser = common_args(parser)  # コマンドライン引数引数を読み込み
    args = parser.parse_args()
    params = Parameters(**setup_params(vars(args), args.parameters))  # args，run_date，git_revisionなどを追加した辞書を取得

    set_logging(result_dir='log', file_name='game')
    logger.info('Start')
    
    game = Game(params)
    game.update_field()
    game.render_field()
    while True:
        game.get_instruction()
        if game.check_next_position():
            game.update_field()
            game.render_field()
        
    
    logger.info('End')