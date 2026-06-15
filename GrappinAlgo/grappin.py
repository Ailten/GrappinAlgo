from .block import Block

class Grappin:
    pos: tuple[int, int]
    block_taken: Block|None

    def __init__(self, pos: tuple[int, int]=(0, 0)):
        self.pos = pos
        self.block_taken = None


    @property
    def is_take_something(self) -> bool:
        return self.block_taken != None

    @property
    def sprite(self) -> str:
        if self.is_take_something:
            return self.block_taken.sprite
        return '^'
    

    @property
    def x(self) -> int:
        return self.pos[0]
    @property
    def y(self) -> int:
        return self.pos[1]
    @x.setter
    def x(self, value: int):
        self.pos = (value, self.pos[1])
    @y.setter
    def y(self, value: int):
        self.pos = (self.pos[0], value)
