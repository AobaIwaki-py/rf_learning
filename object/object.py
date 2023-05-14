from typing import Tuple

class Object():
    __X: int
    __Y: int
    
    def __init__(self) -> None:
        self.__name = self.__class__.__name__

    @property
    def name(self) -> str:
        return self.__name
    
    def set_position(self, X: int, Y: int) -> None:
        self.__X = X
        self.__Y = Y
        
    def get_position(self) -> Tuple[int, int]:
        return self.__X, self.__Y
    
    
    
if __name__=='__main__':
    pass    