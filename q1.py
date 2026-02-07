
import extract_data as ed
import plot_blocks as pb

def plot_q1():
    #pre processing
    filename = input("Enter the filename: ")
    blocks_list,t1 = ed.ext_blocks(filename)
    t2=pb.plot_blocks(blocks_list)
    print(f"\nTotal time taken for Q1: {t1+t2:.4f} seconds")

if __name__ == "__main__":
    plot_q1()


