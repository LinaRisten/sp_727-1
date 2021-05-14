import typing as tp
import sys
from threading import Thread, Lock
from queue import Queue
from pathlib import Path
from md5_single import compute_file_hash


mutex = Lock()


def worker(input_queue: Queue, output_queue: Queue):
    while True:
        with mutex:
            next_filename: tp.Optional[Path] = input_queue.get()
            if next_filename is None:
                return
            else:
                result_hash = compute_file_hash(next_filename)
                output_queue.put((next_filename, result_hash))

def get_md5_for_all_files_in_directory(path_to_directory: Path, num_workers: int = 4) -> None:
    if not path_to_directory.is_dir():
        raise RuntimeError(f"Path {path_to_directory} is not directory")

    task_queue = Queue()
    result_queue = Queue()

    for object_path in path_to_directory.iterdir():
        if object_path.is_file():
            task_queue.put(object_path)

    for _ in range(num_workers):
        task_queue.put(None)

    workers = [Thread(target=worker, args=(task_queue, result_queue)) for _ in range(num_workers)]

    for w in workers:
        w.start()

    for w in workers:
        w.join()

    while not result_queue.empty():
        filename, hash = result_queue.get()
        print(f"{filename} = {hash}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
       raise RuntimeError("You should pass path")

    path = Path(sys.argv[1])

    get_md5_for_all_files_in_directory(path, 3)
