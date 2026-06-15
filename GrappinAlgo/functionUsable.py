from .map import Map

def droite():
    """
    Fait avencer le grappin d'un vers la droite.
    """
    map = Map()
    if map.is_error_find:
        return
    
    # move to right.
    map.grappin.x += 1

    # draw.
    map.drawUpdate()

    # check error.
    if map.checkError('grappin_out_of_range'):
        print(map.error_message)


def gauche():
    """
    Fait avencer le grappin d'un vers la gauche.
    """
    map = Map()
    if map.is_error_find:
        return
    
    # move to right.
    map.grappin.x -= 1

    # draw.
    map.drawUpdate()

    # check error.
    if map.checkError('grappin_out_of_range'):
        print(map.error_message)


def prendre():
    """
    Fait prendre un block par le grappin.
    """
    map = Map()
    if map.is_error_find:
        return
    
    # check if grappin is free.
    if map.checkError('grappin_is_full'):
        print(map.error_message)
        return

    # check if block in column grappin (throw before grappin fall).
    is_no_block = map.checkError('no_block_in_column_grappin')
    
    # make grappin fall.
    for y in range(1, map.height):
        block_find = next([ b for b in map.blocks if b.pos == (map.grappin.x, y) ].__iter__(), None)

        if block_find == None:

            # error, no block to take.
            if is_no_block and y == map.height - 1:
                print(map.error_message)
                return
        
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
    if map.is_error_find:
        return
    
    # check if grappin is full.
    if map.checkError('grappin_is_empty'):
        print(map.error_message)
        return
    
    # check if column is full.
    if map.checkError('column_is_full'):
        print(map.error_message)
        return
    
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





    

    
