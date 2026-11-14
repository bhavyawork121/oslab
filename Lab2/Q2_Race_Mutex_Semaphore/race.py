import sys
import threading
import time

sys.setswitchinterval(1e-6)

NUM_THREADS = 4
INCREMENTS = 20_000
EXPECTED = NUM_THREADS * INCREMENTS

counter = 0
mutex = threading.Lock()
binary_sem = threading.Semaphore(1)  


def unsafe_worker():
    global counter
    for _ in range(INCREMENTS):
        temp = counter      
        temp += 1          
        time.sleep(0)       
        counter = temp      


def mutex_worker():
    global counter
    for _ in range(INCREMENTS):
        with mutex:
            temp = counter
            temp += 1
            counter = temp


def semaphore_worker():
    global counter
    for _ in range(INCREMENTS):
        binary_sem.acquire()    
        temp = counter
        temp += 1
        counter = temp
        binary_sem.release()    


def run(name, worker):
    global counter
    counter = 0
    threads = [threading.Thread(target=worker) for _ in range(NUM_THREADS)]
    start = time.perf_counter()
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    elapsed = time.perf_counter() - start
    status = "CORRECT" if counter == EXPECTED else "WRONG (race condition)"
    print(f"{name:<18} expected={EXPECTED}  actual={counter}  "
          f"time={elapsed:.4f}s  -> {status}")


if __name__ == "__main__":
    print(f"Threads: {NUM_THREADS}, increments per thread: {INCREMENTS}\n")
    run("Unsafe", unsafe_worker)
    run("Mutex", mutex_worker)
    run("Binary Semaphore", semaphore_worker)