import numpy as np
import os
from SelfDefinedPackge import PubMethod
fname = r"C:\Users\honggang.li\Downloads\Sony\test01.bin"

data = np.fromfile(fname, dtype=np.int16, offset=4)
data.shape = 18912, 1280

datac = data[0]
print(datac.shape)

fname = r"C:\Users\honggang.li\Downloads\Sony\test01.txt"
f_data = PubMethod.read_file(fname)

for i in range(197):
    data1 = f_data[i].split("\t")
    data2 = list(map(int, data1))
    data_np1 = np.array(data2)
    data_np2 = data[i]
    if (data_np1 == data_np2).all():
        print(i, "Compare Correct")
    else:
        raise ValueError
        print(i, "Compare Error")
