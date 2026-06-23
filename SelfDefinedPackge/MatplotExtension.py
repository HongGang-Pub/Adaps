# import numpy as np
# import matplotlib.pyplot as plt
# import mplcursors


def coor_show():
    import mplcursors
    cursor = mplcursors.cursor(multiple=True, highlight=True)
    # @cursor.connect("add")
    # def on_add(sel):
    #     x_val = int(sel.target[0])
    #     y_val = sel.target[1]
    #     # sel.text_annotations.xy = (x_val, y_val)
    #     # print(sel.text_annotations.xy)
    #     # sel.text_annotations.set_text(int(sel.index))
    return


def self_plt_show():
    import matplotlib.pyplot as plt
    coor_show()
    plt.show()


def fig_close():
    import matplotlib.pyplot as plt
    for fig in plt.get_fignums():
        per_fig = plt.figure(fig, clear=True)
        plt.close()
        pass


def fig_save():
    import matplotlib.pyplot as plt
    # print(plt.get_fignums())
    for fig in plt.get_fignums():
        per_fig = plt.figure(fig)
        title = per_fig.axes[0].axes.get_title()
        plt.savefig(f'..\\figs\\{title}.png', dpi=300)


if __name__ == '__main__':
    import numpy as np
    import matplotlib.pyplot as plt
    import mplcursors
    arr = np.random.rand(100, 100, 3)
    cursor = mplcursors.cursor(multiple=True)
    plt.imshow(arr)
    plt.show()
    # self_plt_show()
