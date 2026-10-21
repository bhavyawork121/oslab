import threading 
import time 

task = [
    ("task1", 2),
    ("task2", 3),
    ("task3", 1)
]

def do_task(task_name, wait_time):
    print(f"{task_name} started, will take {wait_time} seconds.")
    time.sleep(wait_time)
    print(f"{task_name} completed.")

def single_threaded():
    print("\n--- Single Threaded  ---")
    start_time = time.perf_counter()
    for task_name, wait_time in task:
        do_task(task_name, wait_time)
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print(f"single-threaded execution time: {elapsed_time:.2f} seconds")
    return elapsed_time

def multithreaded():
    print("\n--- Multithreaded  ---")
    start_time = time.perf_counter()
    threads = []
    for task_name, wait_time in task:
        thread = threading.Thread(target=do_task, args=(task_name, wait_time))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print(f"multithreaded execution time: {elapsed_time:.2f} seconds")
    return elapsed_time

def main():
    single_time = single_threaded()
    multi_time = multithreaded()

    print("\n--- Final Summary ---")
    print(f"Single threaded: {single_time:.2f} seconds")
    print(f"Multithreaded:   {multi_time:.2f} seconds")

if __name__ == "__main__":
    main()