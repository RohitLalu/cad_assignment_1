import time
import math as m
import psutil
import os
from attribute_rect import block
from attribute_rect import LineEquation as leq
import matplotlib.colors as mcolors

mcolors_list = list(mcolors.CSS4_COLORS.keys())


def equation_creator(x1, y1, x2, y2):
    a = y2 - y1
    b = x1 - x2
    c = a * x1 + b * y1
    return (a, b, c)   

def ext_blocks(filename):
    start_time = time.time()
    process = psutil.Process(os.getpid())
    mem_before = process.memory_info().rss / 1024  # kB
    
    blocks_list = []
    colour_code = 0
    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip() #assuming no comments and only one rectangle per line
                if not line:
                    continue
                
                values = line.replace('{', '').replace('}', '').split(',')
                values=values[0:5]
                values = [int(v.strip()) for v in values]
                
                if len(values) == 5:
                    rect_id,x1,y1,x2,y2=values
                    height = m.fabs(y2 - y1)
                    width = m.fabs(x2 - x1)
                    colour_code += 20
                    rect = block(block_id=rect_id, colour_code=mcolors_list[colour_code % len(mcolors_list)], height=height, width=width, left_bottom_coord=(x1, y1), west=leq(*equation_creator(x1, y1, x1, y2)), south=leq(*equation_creator(x1, y1, x2, y1)))
                    blocks_list.append(rect)
                else:
                    print(f"Warning: Line '{line}' does not contain exactly 5 values. Skipping.")
    
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return []
    
    mem_after = process.memory_info().rss / 1024  # kB
    elapsed_time = time.time() - start_time
    
    print(f"\nData Extraction Summary:")
    print(f"Rectangles loaded: {len(blocks_list)}")
    print(f"Memory used: {mem_after - mem_before:.4f} kB")
    print(f"Time taken for extraction: {elapsed_time:.4f} seconds")
    
    return blocks_list,elapsed_time
