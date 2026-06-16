from .map import Map

def droite():
    """
    Fait avencer le grappin d'un vers la droite.
    """
    map = Map()
    
    # move to right.
    map.grappin.x += 1

    # draw.
    map.drawUpdate()

    # check error.
    if map.checkError('grappin_out_of_range'):
        print(map.error_message)
        raise Exception(map.error_message)


def gauche():
    """
    Fait avencer le grappin d'un vers la gauche.
    """
    map = Map()
    
    # move to right.
    map.grappin.x -= 1

    # draw.
    map.drawUpdate()

    # check error.
    if map.checkError('grappin_out_of_range'):
        print(map.error_message)
        raise Exception(map.error_message)


def prendre():
    """
    Fait prendre un block par le grappin.
    """
    map = Map()
    
    # check if grappin is free.
    if map.checkError('grappin_is_full'):
        print(map.error_message)
        raise Exception(map.error_message)

    # check if block in column grappin (throw before grappin fall).
    is_no_block = map.checkError('no_block_in_column_grappin')
    
    # make grappin fall.
    for y in range(1, map.height):
        block_find = next([ b for b in map.blocks if b.pos == (map.grappin.x, y) ].__iter__(), None)

        if block_find == None:

            # error, no block to take.
            if is_no_block and y == map.height - 1:
                print(map.error_message)
                raise Exception(map.error_message)
        
        else:

            # take the block.
            map.grappin.block_taken = block_find
            map.blocks.remove(block_find)

        # make grappin fall.
        map.grappin.y = y

        # draw.
        map.drawUpdate()

        # stop falling if has take something.
        if map.grappin.is_take_something:
            break
    
    # grappin go's up.
    for y in range(map.grappin.y - 1, -1, -1):
        map.grappin.y = y

        # draw.
        map.drawUpdate()

    
def poser():
    """
    Fait poser le block que tien le grappin.
    """
    map = Map()
    
    # check if grappin is full.
    if map.checkError('grappin_is_empty'):
        print(map.error_message)
        raise Exception(map.error_message)
    
    # check if column is full.
    if map.checkError('column_is_full'):
        print(map.error_message)
        raise Exception(map.error_message)
    
    # eval pos y of grappin should be end fall (an place block).
    blocks_in_column = [ b for b in map.blocks if b.x == map.grappin.x ]
    blocks_in_column.sort(key=lambda b: b.y)
    pos_y_end = map.height if len(blocks_in_column) == 0 else blocks_in_column[0].y
    
    # grappin fall.
    for y in range(1, pos_y_end):
        map.grappin.y = y

        # draw.
        map.drawUpdate()

    # place block.
    map.grappin.block_taken.pos = (map.grappin.x, map.grappin.y)
    map.blocks.append(map.grappin.block_taken)
    map.grappin.block_taken = None

    # grappin go's up.
    for y in range(map.grappin.y - 1, -1, -1):
        map.grappin.y = y

        # draw.
        map.drawUpdate()


def blockTenu() -> str:
    """
    Retourn le block tenu par le grappin (si le grappin n'en porte pas, il retourn du vide).
    """
    map = Map()
    
    return '' if not map.grappin.is_take_something else map.grappin.block_taken.sprite


def hauteurColonne() -> int:
    """
    Retourn la hauteur de la colonne (les block empilé).
    """
    map = Map()

    # get max height of column.
    blocks_height = [ b.y for b in map.blocks if b.x == map.grappin.x ]
    blocks_height.sort(reverse=True)
    max_height = 0 if len(blocks_height) == 0 else blocks_height[0]
    return max_height


def positionDuGrappin() -> int:
    """
    Retourn la position du grappin dans le tableau (horizontalement).
    """
    map = Map()

    return map.grappin.x + 1
    
    

    

    
