import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import mplcursors

def coor_show():
    cursor = mplcursors.cursor(multiple=True)
    # @cursor.connect("add")
    # def on_add(sel):
    #     x_val = int(sel.target[0])
    #     y_val = sel.target[1]
    #     # sel.annotation.xy = (x_val, y_val)
    #     # print(sel.annotation.xy)
    #     # sel.annotation.set_text(int(sel.index))


def self_plt_show():
    coor_show()
    plt.show()