import os
from makemkv.info import read_file_output

def main():
    print(read_file_output(os.path.dirname(os.path.realpath(__file__)) + '/makemkv/info-sample.txt'))

if __name__ == "__main__":
    main()