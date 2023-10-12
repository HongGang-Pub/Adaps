import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
# matplotlib.use('Qt5A1gg')

fig = plt.figure("bbbb")

imgs = []
row = 576
col = 768
array = np.zeros([row, col])


ax = fig.gca()


def update(i):
    global imgs
    global array
    ax.cla()

    array[i:i+10, i:i+10] = 1
    imgs = ax.imshow(X=array)
    if i == 4999:
        print("Ending")
    return imgs


ani = animation.FuncAnimation(fig, update, range(500), interval=100, blit=False, repeat=False)

plt.show()
