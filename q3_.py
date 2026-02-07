
import time
import matplotlib.pyplot as plt
import extract_data as ed
import plot_blocks as pb
from printer_func import printer

no_overlap_in_block_list=[]

def overlap_check(block1, block2):
    """Returns True if blocks overlap (including touching edges), False otherwise"""
    x1_min = block1.left_bottom_coord[0]
    y1_min = block1.left_bottom_coord[1]
    x1_max = x1_min + block1.width
    y1_max = y1_min + block1.height
    
    x2_min = block2.left_bottom_coord[0]
    y2_min = block2.left_bottom_coord[1]
    x2_max = x2_min + block2.width
    y2_max = y2_min + block2.height
    
    # Blocks overlap if they intersect on both axes
    return not (x1_max <= x2_min or x1_min >= x2_max or y1_max <= y2_min or y1_min >= y2_max)


def no_overlap_q3():
    #pre processing
    filename = input("Enter the filename: ")
    blocks_list,t1 = ed.ext_blocks(filename) 

    start_time = time.time()
    #logic: track blocks with overlaps instead of checking each against all
    overlapping_blocks = set()
    n = len(blocks_list)
    
    for i in range(n):
        for j in range(i + 1, n):
            if overlap_check(blocks_list[i], blocks_list[j]):
                overlapping_blocks.add(blocks_list[i].block_id)
                overlapping_blocks.add(blocks_list[j].block_id)

    non_overlap_list = [b for b in blocks_list if b.block_id not in overlapping_blocks] #seems optimised for time
    # non_overlap_list = list(set([b for b in blocks_list if b.block_id not in overlapping_blocks])) #:not optimised
    printer(non_overlap_list)
    elapsed_time = time.time() - start_time
    print(f"\nTime taken for data processing in Q3: {elapsed_time:.4f} seconds")
    #plot both graphs
    t2=pb.plot_blocks(blocks_list, show=False) 
    t3=pb.plot_blocks(non_overlap_list, show=False,title="Non-Overlapping Blocks")
    plt.show()
    print(f"\nTotal time taken for Q3: {t1+elapsed_time+t2+t3:.4f} seconds")


if __name__ == "__main__":
    no_overlap_q3()