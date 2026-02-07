
import time
from attribute_rect import block
from attribute_rect import LineEquation as leq
import extract_data as ed
import plot_blocks as pb
from printer_func import printer

point_in_block_list=[]

def point_check(block, x, y):
    if (block.left_bottom_coord[0] <= x <= block.left_bottom_coord[0]+block.width) and (block.left_bottom_coord[1] <= y <= block.left_bottom_coord[1]+block.height):
        return True
    return False

def points_in_blocks_q2():
    #pre processing
    filename = input("Enter the filename: ")
    blocks_list,t1 = ed.ext_blocks(filename)
    x1=int(input("Enter x1: "))
    y1=int(input("Enter y1: "))   

    start_time = time.time()
    for block in blocks_list:
        if point_check(block, x1, y1):
            point_in_block_list.append(block.block_id)
    printer(point_in_block_list)
    elapsed_time = time.time() - start_time
    print(f"\nTime taken for data processing in Q2: {elapsed_time:.4f} seconds")
    #plot with point
    t2=pb.plot_blocks(blocks_list,(x1,y1)) 
    print(f"\nTotal time taken for Q2: {t1+elapsed_time+t2:.4f} seconds")


if __name__ == "__main__":
    points_in_blocks_q2()