import numpy as np
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


def fig_close():
    for fig in plt.get_fignums():
        per_fig = plt.figure(fig)
        plt.close()
        pass


def fig_save():
    # print(plt.get_fignums())
    for fig in plt.get_fignums():
        per_fig = plt.figure(fig)
        title = per_fig.axes[0].axes.get_title()
        plt.savefig(f'..\\figs\\{title}.png', dpi=300)