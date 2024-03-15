"""本方法只用于读取 RAW文件并成图"""


import numpy as np
import matplotlib.pyplot as plt


# 首先确定原图片的基本信息：数据格式，行数列数，通道数
rows = 576  # 图像的行数
cols = 768  # 图像的列数
channels = 1  # 图像的通道数，灰度图为1
file = r"D:\Git\Adaps\Sony\figs\1.5%反射率+0.5m+50v PVDD.raw"

"""利用numpy的fromfile函数读取raw文件，并指定数据格式"""
img = np.fromfile(file, dtype='uint32')
"""利用numpy中array的reshape函数将读取到的数据进行重新排列"""
# img = img.reshape(1800*9, 1000*4, 1)

# img = np.where(img > 0, 1, 0)

plt.figure()
plt.subplot(1, 1, 1)
# plt.title('Image: max_bin:{}, min_bin:{}, median_bin:{}'.format(
#     np.max(img), np.min(img), np.median(img)))
plt.plot(img)
# plt.colorbar()
plt.show()