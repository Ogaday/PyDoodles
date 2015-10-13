# lastlinetimer.py
# Python 3.4.3
# Author: Ogaday
# Date: 2015/10/7

import csv
import os
import random
import subprocess
import timeit


N = 100000    # length of csv file.

# Set up example file
def numbergen(n=N):
    for i in range(n):
        yield random.randint(0,1000)+random.random()

with open("temp.csv", 'w') as f:
    intwriter = csv.writer(f)
    for num in numbergen():
        intwriter.writerow((num,))

        
# Test OS method
def get_last_line_OS(file):
    return os.popen("tail -n 1 %s " % file).readline().strip()

# Test seek method
def get_last_line_seek(file):
    with open(file, 'rb') as f:
        f.seek(-64, os.SEEK_END)
        #This method reads "random.number\r\n" and the others "random.number\n". Something to do with the decoding.
        return f.readlines()[-1].decode().strip()

# Test iteration method
def get_last_line_iter(file):
    with open(file, 'r') as f:
        for line in f:
            pass
        return line.strip()

if __name__ == "__main__":
    print("Starting timer OS...")
    OS_time = timeit.timeit('get_last_line_OS("temp.csv")', globals=globals(), number=1000)
    print("Starting timer seek...")
    seek_time = timeit.timeit('get_last_line_seek("temp.csv")', globals=globals(), number=1000)
    print("Starting timer iter...")
    iter_time = timeit.timeit('get_last_line_iter("temp.csv")', globals=globals(), number=1000)

    #OS_last, seek_last, iter_last = get_last_line_OS("temp.csv"), get_last_line_seek("temp.csv"), get_last_line_iter("temp.csv")

    # Cleanup/Teardown
    print(OS_last, seek_last, iter_last)
    assert(OS_last == seek_last == iter_last)
    os.remove("temp.csv")

    # Produce Results
    print("OS method took:       ", OS_time)
    print("Seek method took:     ", seek_time)
    print("Iteration method took:", iter_time)

    # Notes:
    # Could definitely use the set up method in timeit to create a new csv file each time.
    # Would like to put in some sort of assert to make sure that these line reading things are getting the same values.