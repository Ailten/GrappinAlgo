
from .block import Block
from .grappin import Grappin

import re
from time import sleep
import os

from typing import Optional

class Map:
    __m: Optional['Map'] = None  # singleton instance.

    width: int
    height: int

    blocks: list['Block']

    grappin: 'Grappin'

    map_ascii_expected: str|None

    is_error_find: bool
    error_message: str|None

    wait_update: float

    def __fake_init__(self):
        self.width = 16
        self.height = 4
        self.blocks = []
        self.grappin = Grappin()
        self.map_ascii_expected = None
        self.is_error_find = False
        self.error_message = None
        self.wait_update = 0.3
        
    # singleton.
    def __new__(cls):
        if cls.__m is None:
            cls.__m = super().__new__(cls)
            cls.__m.__fake_init__()
        return cls.__m
    

    def drawMap(self) -> str:
        frame = []
        for y in range(self.height):
            line = []
            for x in range(self.width):
                pos = (x, y)

                # draw grappin (or block taken by grappin).
                if self.grappin.pos == pos:
                    line.append(self.grappin.sprite)
                    continue

                # draw rope of grappin.
                if pos[0] == self.grappin.pos[0] and pos[1] < self.grappin.pos[1]:
                    line.append('¦')  # '│'.
                    continue
                
                # draw block.
                block_find = next([ b for b in self.blocks if b.pos == pos ].__iter__(), None)
                if block_find != None:
                    line.append(block_find.sprite)
                    continue

                # draw empty space.
                line.append(' ')

            frame.append(''.join(line))

        return '\n'.join(frame)
    
    def drawUpdate(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(self.addBorderToMapAscii(self.drawMap()))
        sleep(self.wait_update)
    
    @staticmethod
    def addBorderToMapAscii(map_ascii: str) -> str:
        frame = map_ascii.split('\n')
        width = len(frame[0])
        return (
            '╔'+'═'*width+'╗\n║' +
            '║\n║'.join(frame) +
            '║\n╚'+'═'*width+'╝'
        )
    
    @staticmethod
    def removeBorderToMapAscii(map_ascii: str) -> str:
        # remove border first and last line.
        map_ascii = re.sub(r'^╔═*╗\n║', '', map_ascii)
        map_ascii = re.sub(r'║\n╚═*╝$', '', map_ascii)
        # remove border before and after eatch line.
        map_ascii = re.sub(r'║\n║', '\n', map_ascii)
        return map_ascii
    

    def checkError(self, error_str: str) -> bool:
        match error_str:
            case 'grappin_out_of_range':
                if self.grappin.x < 0 or self.grappin.x >= self.width:
                    self.is_error_find = True
                    self.error_message = '< grappin sorti de la zone ! >'
            case 'grappin_is_full':
                if self.grappin.is_take_something:
                    self.is_error_find = True
                    self.error_message = '< grappin déja occupé ! >'
            case 'no_block_in_column_grappin':
                if next([ b for b in self.blocks if b.x == self.grappin.x ].__iter__(), None) == None:
                    self.is_error_find = True
                    self.error_message = '< aucun block a prendre ! >'
            case 'grappin_is_empty':
                if not self.grappin.is_take_something:
                    self.is_error_find = True
                    self.error_message = '< grappin vide ! >'
            case 'column_is_full':
                if next([ b for b in self.blocks if b.pos == (self.grappin.x, 1) ].__iter__(), None) != None:
                    self.is_error_find = True
                    self.error_message = '< collone pleine ! >'
                    
        return self.is_error_find
            


# build a map (from ascii representation).
def makeExercice(map_ascii: str, map_ascii_expected: str, is_bordered: bool=True):

    # remove border.
    if is_bordered:
        map_ascii = Map.removeBorderToMapAscii(map_ascii)
        map_ascii_expected = Map.removeBorderToMapAscii(map_ascii_expected)

    # eval map size.
    frame = map_ascii.split('\n')
    height = len(frame)
    width = len(frame[0])

    # check resolution.
    frame_expected = map_ascii_expected.split('\n')
    height_expected = len(frame_expected)
    width_expected = len(frame_expected[0])
    if width != width_expected or height != height_expected:
        raise Exception('/!\\ --- resolution attendue diférente --- /!\\')
    if (
        all([ len(l) == width for l in frame_expected[0] ]) and
        all([ len(l) == width for l in frame[0] ])
    ):
        raise Exception('/!\\ --- resolution attendue diférente --- /!\\')
    
    # make the map.
    map = Map()
    map.width = width
    map.height = height
    map.map_ascii_expected = map_ascii_expected

    # place grappin.
    grappin_find = re.search(r'\^', frame[0])
    if grappin_find != None:
        pos_x_grappin = grappin_find.start()
        map.grappin.x = pos_x_grappin

    # place blocks.
    for match_block in re.finditer(r'[^\^\n ]', map_ascii):
        block_sprite = match_block.group()
        block_pos_y = match_block.start() // (width + 1)
        block_pos_x = match_block.start() - (block_pos_y * (width + 1))
        map.blocks.append(Block(
            pos=(
                block_pos_x,
                block_pos_y
            ), 
            sprite=block_sprite
        ))
    if len(map.blocks) == 0:
        raise Exception('/!\\ --- aucun block trouvé --- /!\\')
    
    # draw first frame.
    map.drawUpdate()


def checkIsExerciceSuccess():
    map = Map()
    if map.is_error_find:
        return
    message = '< Essaye encore >'

    # check if success.
    if re.sub(r'\^', ' ', map.drawMap()) == re.sub(r'\^', ' ', map.map_ascii_expected):
        message = '< Réussi ! >'
    
    # center message.
    space_message = max(((map.width + 2) - len(message)) // 2, 0)
    message = message.rjust(space_message + len(message), ' ')

    print(message)