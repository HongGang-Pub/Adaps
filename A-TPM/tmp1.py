from SelfDefinedPackge.PubMethod import *
import struct

# data1 = read_file(fname=r"C:\Users\honggang.li\Downloads\test01.bin")

fname=r"C:\Users\honggang.li\Downloads\test01.bin"

binfile = open(fname, "rb")
size = os.path.getsize(fname)  # 获得文件大小
print(size)

# for i in range(1):
#     data = binfile.read(4)
#     print(data)
#     num = struct.unpack('ii', data)
#     print(num[0])

data = binfile.read()
num = struct.unpack('ii', data)
print(num[0])

# data = binfile.readlines()
# print(len(data))
# print(data[0])
