import glob
from subprocess import Popen as popen

def main():
    file_list = glob.glob("*")
    for each in file_list:
        process = popen(["python3", "md5_single.py", each])
        process.wait()


if __name__ == '__main__':
    main()
