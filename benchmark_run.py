import os, sys
from time import perf_counter as time
from random import shuffle


write_size_MB = [1024, 10] # size MB to save
write_block_size_kB = [1024*100, 1024*10]
read_size_MB = 1000
read_block_size_kB = 1024*100


def read_test(directory, block_size, blocks_count):
    print("%d block size, %d blocks" % ( block_size, blocks_count))
    f = os.open(directory, os.O_RDONLY | os.O_BINARY)
    offsets = list(range(0, blocks_count*block_size, block_size))
    shuffle(offsets)
    took = []
    for i, offset in enumerate(offsets):
        print("%d iteration, %d offset" % (i, offset))
        bytes_read = 0
        start = time()
        test = ""
        position_cursor = os.lseek(f, offset, os.SEEK_SET)

        while bytes_read < block_size:
            buff = os.read(f, block_size-bytes_read)
            print("%d postition cursor, %d offset" % (position_cursor, offset))
            print("%d block bytes remainning" % (block_size-bytes_read))
            print("%d buff size" % (len(buff)))
            # print(buff)
            bytes_read = bytes_read + len(buff)
            if (len(buff)>0):
                test = buff[0]
            if len( buff) ==0:
                print("EOF reached")
                break  # if EOF reached
            print("%d bytes_read " % (bytes_read))
        t = time() - start
        
        took.append(t)

    os.close(f)
    result=block_size*blocks_count / 1024/1024/sum(took)
    print("Reading speed result: %.2f MB/s" % result)


def write_test(directory, block_size, blocks_count):
    print("%s block size, %s blocks" % ( block_size, blocks_count))
    f = os.open(directory, os.O_CREAT | os.O_WRONLY)
    took = []
    for i in range(blocks_count):
        buff = os.urandom(block_size)
        start = time()
        os.write(f, buff)
        os.fsync(f)
        t = time() -start
        took.append(t)
    os.close(f)
    result = block_size*blocks_count / 1024/1024/sum(took)
    print("Writing speed result: %.2f MB/s" % result)
    return result


def read_test2(directory, block_size, blocks_count):
    print("%d block size, %d blocks" % ( block_size, blocks_count))
    with open(directory, 'r') as f:
        buff = f.read()
    print(buff)
    # offsets = list(range(0, blocks_count*block_size, block_size))
    # shuffle(offsets)
    # took = []
    # for i, offset in enumerate(offsets):
    #     print("%d iteration" % (i))
    #     bytes_read = 0
    #     start = time()
    #     while bytes_read < block_size:
    #         # os.lseek(f, offset+bytes_read, os.SEEK_SET)
            
    #         # print("%d block bytes remainning" % (block_size-bytes_read))
    #         # print("%d buff size" % (len(buff)))
    #         bytes_read = bytes_read + len(buff)
    #         if len( buff) ==0:
    #             print("EOF reached")
    #             break  # if EOF reached
    #         # print("%d bytes_read " % (bytes_read))
    #     t = time() - start
        
    #     took.append(t)

    # os.close(f)
    # result=block_size*blocks_count / 1024/1024/sum(took)
    # print("Reading speed result: %.2f MB/s" % result)


def main():
    directory = 'E:\\testy'
    # directory = 'C:\\Users\\wojci\\testy'
    # for i in range(len(write_size_MB)):
    i = 0
    write_test(directory, write_block_size_kB[i]*1024, int(write_size_MB[i]*1024/write_block_size_kB[i]))
    # read_test(directory, read_block_size_kB*1024,int(read_size_MB * 1024 / read_block_size_kB))


# main()

