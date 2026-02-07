import time
import matplotlib.pyplot as plt
import attribute_rect as ar
import matplotlib.patches as patches

def plot_blocks(blocks_list, point=None, show=True,title="Block Placement"):
    start_time = time.time()
    fig, ax = plt.subplots()
    
    for block in blocks_list:
        x, y = tuple(block.left_bottom_coord)
        # print(f"{x},{y}")
        rect = patches.Rectangle((x, y), block.width, block.height, linewidth=4, edgecolor=block.colour_code, facecolor='none')
        ax.add_patch(rect)

    
    if point:
        ax.plot(point[0], point[1], 'ro') 

    #fit all blocks in view
    ax.relim()
    ax.autoscale_view()

    elapsed_time = time.time() - start_time
    print(f"\nTime taken for block placement: {elapsed_time:.4f} seconds")
    
    ax.set_aspect('auto', adjustable='box')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title(title)
    plt.grid()
    
    if show:
        plt.show()

    return elapsed_time