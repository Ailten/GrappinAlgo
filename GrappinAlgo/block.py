
class Block:
    sprite: str
    pos: tuple[int, int]

    def __init__(self, pos: tuple[int, int] , sprite: str='#'):
        self.pos = pos
        self.sprite = sprite

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