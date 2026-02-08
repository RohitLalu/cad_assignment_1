
import psutil
import os
import extract_data as ed
import plot_blocks as pb

def plot_q1():
    #pre processing
    process = psutil.Process(os.getpid())
    mem_before_q1 = process.memory_info().rss / 1024  # kB
    filename = input("Enter the filename: ")
    blocks_list,t1 = ed.ext_blocks(filename)
    t2=pb.plot_blocks(blocks_list)
    mem_after_q1 = process.memory_info().rss / 1024  # kB

    print(f"\nTotal time taken for Q1: {t1+t2:.4f} seconds")
    print(f"Memory used: {mem_after_q1 - mem_before_q1:.4f} kB")

if __name__ == "__main__":
    plot_q1()


