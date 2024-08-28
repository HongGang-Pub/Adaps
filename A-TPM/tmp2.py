import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

# 创建示例数据
data1 = np.random.rand(10, 10)  # 第一张图像数据
data2 = np.random.rand(20, 30)  # 第二张图像数据，大小不同

# 创建一个图像和坐标轴
fig, ax = plt.subplots()
cax = ax.imshow(data1, cmap='viridis')

# 添加 colorbar
colorbar = fig.colorbar(cax, ax=ax)


# 更新函数，用于更新图像、刻度和颜色条
def update_plot(data):
    # 更新图像数据
    cax.set_data(data)

    # 设置新的图像范围
    cax.set_extent([0, data.shape[1], 0, data.shape[0]])

    # 更新 x 轴和 y 轴的刻度
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))

    # 更新图像的颜色范围
    cax.set_clim(vmin=np.min(data), vmax=np.max(data))

    # 重新绘制 colorbar
    colorbar.update_normal(cax)

    # 刷新图像
    ax.figure.canvas.draw()


# 显示第一张图像
plt.show()

# 使用第二张图像数据更新图像、刻度和 colorbar
update_plot(data2)
