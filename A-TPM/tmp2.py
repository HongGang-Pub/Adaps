import numpy as np
import matplotlib.pyplot as plt
import gc

# 创建示例数据
data1 = np.random.rand(10, 10)
data2 = np.random.rand(20, 30)

# 创建一个图像和坐标轴
fig, ax = plt.subplots()
cax = ax.imshow(data1, cmap='viridis')
colorbar = fig.colorbar(cax, ax=ax)


# 更新函数
def update_plot(data):
    # 清除当前图像
    cax.clear()

    # 更新图像数据
    cax.set_data(data)

    # 更新颜色范围
    cax.set_clim(vmin=np.min(data), vmax=np.max(data))

    # 重新绘制 colorbar
    colorbar.update_normal(cax)

    # 手动调用垃圾回收
    gc.collect()

    # 刷新图像
    ax.figure.canvas.draw()


# 显示初始图像
plt.show()

# 使用新数据更新图像
update_plot(data2)
