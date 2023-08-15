import multiprocessing
import time

def print_numbers():
    for i in range(1, 11):
        print(multiprocessing.current_process().name, i)
        time.sleep(1)

if __name__ == '__main__':
    processes = []

    for _ in range(3):
        process = multiprocessing.Process(target=print_numbers)
        processes.append(process)
        process.start()

    for process in processes:
        process.join()