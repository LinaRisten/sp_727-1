from pathlib import Path
from hashlib import md5
import sys

def compute_file_hash(path: Path) -> str:
        with path.open("rb") as f:
            hash_md5 = md5()
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
            return hash_md5.hexdigest()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise RuntimeError("You should pass name of file")

    print(compute_file_hash(Path(sys.argv[1])))
