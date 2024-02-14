import threading
import time
import os
from random import randint

# Задание 1
def thread_info(index):
    print(f"Thread {index} is running.")

threads = []
for i in range(10):
    t = threading.Thread(target=thread_info, args=(i,))
    threads.append(t)
    t.start()

# Задание 2
def func1():
    print("Function 1 is running.")
    time.sleep(2)

def func2():
    print("Function 2 is running.")
    time.sleep(2)

def func3():
    print("Function 3 is running.")
    time.sleep(2)

thread1 = threading.Thread(target=func1)
thread2 = threading.Thread(target=func2)
thread3 = threading.Thread(target=func3)

thread1.start()
thread2.start()
thread3.start()

# Задание 3
def write_to_file(num_lines, filename):
    with open(filename, 'w') as file:
        for i in range(num_lines):
            file.write(f"Line {i+1}\n")

start_time = time.time()
thread1 = threading.Thread(target=write_to_file, args=(1000, "file1.txt"))
thread2 = threading.Thread(target=write_to_file, args=(1000, "file2.txt"))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

end_time = time.time()
print("Time taken to execute threads:", end_time - start_time, "seconds")

# Задание 4
class MyThreadClass(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.duration = randint(1, 10)

    def run(self):
        print(f"Thread {self.name} is running. PID: {os.getpid()}")
        time.sleep(self.duration)

start_time = time.time()
threads = []
for i in range(10):
    t = MyThreadClass(str(i))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

end_time = time.time()
print("Time taken to execute MyThreadClass threads:", end_time - start_time, "seconds")

# Задание 5
lock = threading.Lock()

def write_with_lock(num_lines, filename):
    with lock:
        with open(filename, 'w') as file:
            for i in range(num_lines):
                file.write(f"Line {i+1}\n")

start_time = time.time()
thread1 = threading.Thread(target=write_with_lock, args=(1000, "file1.txt"))
thread2 = threading.Thread(target=write_with_lock, args=(1000, "file2.txt"))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

end_time = time.time()
print("Time taken to execute threads with lock:", end_time - start_time, "seconds")

# Задание 6
def daemon_thread():
    print("Daemon thread is running.")
    time.sleep(2)

def non_daemon_thread():
    print("Non-daemon thread is running.")
    time.sleep(2)

daemon_thread = threading.Thread(target=daemon_thread)
non_daemon_thread = threading.Thread(target=non_daemon_thread)

daemon_thread.daemon = True

daemon_thread.start()
non_daemon_thread.start()

# Задание 7
def sum_array(arr):
    total = sum(arr)
    print("Sum of array:", total)

arr = [i for i in range(1, 1000001)]

start_time = time.time()
threads = []
for _ in range(10):
    t = threading.Thread(target=sum_array, args=(arr,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

end_time = time.time()
print("Time taken to execute sum_array threads:", end_time - start_time, "seconds")

# Задание 8
def write_to_file1():
    with open("text1.txt", 'w') as file:
        for i in range(10):
            file.write(f"Line {i+1} for text1\n")

def write_to_file2():
    with open("text2.txt", 'w') as file:
        for i in range(10):
            file.write(f"Line {i+1} for text2\n")

def read_from_files():
    try:
        with open("text1.txt", 'r') as file1:
            print("Contents of text1.txt:", file1.read())
    except FileNotFoundError:
        print("File text1.txt not found.")

    try:
        with open("text2.txt", 'r') as file2:
            print("Contents of text2.txt:", file2.read())
    except FileNotFoundError:
        print("File text2.txt not found.")

thread1 = threading.Thread(target=write_to_file1)
thread2 = threading.Thread(target=write_to_file2)
thread3 = threading.Thread(target=read_from_files)

thread1.start()
thread2.start()
thread3.start()
