import sys
import hashlib


def md5(file_name):
    hash_md5 = hashlib.md5()
    with open(file_name, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def main():
    file_name = sys.argv[1]
    md5_hash = md5(file_name)
    print('{} {}'.format(md5_hash, file_name))

if __name__ == '__main__':
    main()
