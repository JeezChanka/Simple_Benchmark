import os, sys
from time import perf_counter as time
write_size_MB = 10  # size MB to save
write_block_size_kB = 1024
def main():
    f = os.open('testy', os.O_CREAT | os.O_WRONLY)
    took = []
    for i in range(int(write_size_MB*1024/write_block_size_kB)):
        buff = os.urandom(write_block_size_kB*1024)
        start = time()
        os.write(f, buff)
        os.fsync(f)
        t = time() -start
        took.append(t)
    os.close(f)
    result = write_size_MB / sum(took)
    print("Writing speed result: %.2f MB/s" % result) 

main()