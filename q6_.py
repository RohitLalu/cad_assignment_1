
import time
import psutil
import os
import matplotlib.pyplot as plt
import extract_data as ed
import plot_blocks as pb
from printer_func import print_set
from overlap_checker import partial_overlap_check


no_overlap_in_block_list=[]

def abutt_q6():
    #pre processing
    process = psutil.Process(os.getpid())
    mem_before = process.memory_info().rss / 1024  # kB
    filename = input("Enter the filename: ")
    blocks_list,t1 = ed.ext_blocks(filename) 

    start_time = time.time()
    #logic:
    overlapping_blocks = list() #overlapping groups of blocks
    all_overlapping_blocks = set() #element wise unique overlapping blocks
    overlap_list=[] #overlapping blocks seen with one common block
    n = len(blocks_list)

    for i in range(n):
        for j in range(n):
            if (i != j) and (blocks_list[j].block_id not in all_overlapping_blocks):
                overlap_type,direction = partial_overlap_check(blocks_list[i], blocks_list[j])
                if overlap_type ==3:
                    overlap_list = [blocks_list[i].block_id]
                    if direction==1:
                        overlap_list.append('e')
                    elif direction==2:
                        overlap_list.append('w')
                    elif direction==3:
                        overlap_list.append('n')
                    else:
                        overlap_list.append('s')
                    overlap_list.append(blocks_list[j].block_id)
                    all_overlapping_blocks.add(blocks_list[i])
                    all_overlapping_blocks.add(blocks_list[j])
                    overlapping_blocks.append(overlap_list)
                    overlap_list=[]

    
    elapsed_time = time.time() - start_time
    mem_after = process.memory_info().rss / 1024  # kB
    print_set(overlapping_blocks)
    print(f"\nTime taken for data processing in Q6: {elapsed_time:.4f} seconds")
    #plot both graphs
    t2=pb.plot_blocks(blocks_list, show=False) 
    t3=pb.plot_blocks(all_overlapping_blocks, show=False,title="Abutting Blocks")
    plt.show()
    print(f"\nTotal time taken for Q6: {t1+elapsed_time+t2+t3:.4f} seconds")
    print(f"Memory used: {mem_after - mem_before:.4f} kB")

if __name__ == "__main__":
    abutt_q6()