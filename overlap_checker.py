from attribute_rect import block

def partial_overlap_check(block1, block2):
    """
    Check type of overlap between two blocks.
    Returns:
        0: No overlap
        1: Partial overlap
        2: Full overlap (one block fully inside another)
        3: Abutting (touching at one edge only)
    """
    x1_min = block1.left_bottom_coord[0]
    y1_min = block1.left_bottom_coord[1]
    x1_max = x1_min + block1.width
    y1_max = y1_min + block1.height
    
    x2_min = block2.left_bottom_coord[0]
    y2_min = block2.left_bottom_coord[1]
    x2_max = x2_min + block2.width
    y2_max = y2_min + block2.height
    
    # con1: Check if blocks intersect (overlap, inside, or abutting)
    blocks_intersect = not (x1_max < x2_min or x1_min > x2_max or y1_max < y2_min or y1_min > y2_max)
    
    # con2: Check if block1 is fully inside block2 including one side abutting
    block1_inside_block2 = (x2_min <= x1_min and x1_max <= x2_max and y2_min <= y1_min and y1_max <= y2_max)
    
    # con3: Check if they are abutting (touching at exactly one edge) and not fully inside
    east = x1_max==x2_min
    west = x1_min==x2_max
    north = y1_max==y2_min
    south = y1_min==y2_max
    abutting = (
        (east or west) and (y1_min < y2_max and y1_max > y2_min)  # Abutting on x-axis
    ) or (
        (north or south) and (x1_min < x2_max and x1_max > x2_min)  # Abutting on y-axis
    )
    direction = east*1 + west*2 + north*3 + south*4  # 0: east, 1: west, 2: north, 3: south (if abutting)
    
    # Return based on constraints
    if not blocks_intersect and not abutting:
        return 0,0  # No overlap
    elif abutting and not block1_inside_block2:
        return 3,direction  # Abutting
    elif block1_inside_block2:
        return 2,0  # Full overlap (one inside another)
    else:
        return 1,0  # Partial overlap