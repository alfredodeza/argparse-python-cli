import os
import argparse

def calculate(file):
    bytes_size = os.path.getsize(file)
    mb_size = int(bytes_size/1024**2)
    print(mb_size, "MB")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("path", help="Filepath to calculate the size")
    args = parser.parse_args()
    return calculate(args.path)

if __name__ == '__main__':
    main()
