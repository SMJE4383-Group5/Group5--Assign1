import os
import time
from multiprocessing import Process

def increment_numbers(shared_list):
    child_pid = os.getpid()
    print(f"Child process {child_pid} is starting...")

    for i in range(len(shared_list)):
        shared_list[i] += 1

    print(f"Child process {child_pid} finished operation. List after incrementing: {shared_list}")

def main():
    shared_list = [5, 10, 15, 20, 25]

    parent_pid = os.getpid()
    print(f"Parent process {parent_pid} is starting...")

    process = Process(target=increment_numbers, args=(shared_list,))
    process.start()

    print(f"Parent process {parent_pid} is waiting for child process {process.pid} to finish...")
    process.join()
    print(f"Parent process {parent_pid} resumed operation. List before doubling: {shared_list}")

    for i in range(len(shared_list)):
        shared_list[i] *= 2

    print(f"Parent process {parent_pid} finished operation. List after doubling: {shared_list}")

if __name__ == "__main__":
    shared_list = [5, 10, 15, 20, 25]
    print(f"Original shared list: {shared_list}")

    main()