"""
本文件仅用于将.raw图片中指定段的光强展示
"""
from SelfDefinedPackge.MatplotExtension import *

def do_work(image):
    ini_img = np.fromfile(image, dtype='uint32')
    # 利用numpy中array的reshape函数将读取到的数据进行重新排列
    ini_img = ini_img.reshape(576, 768, 1)
    plt.imshow(ini_img, vmax=50, cmap="gray")
    # SCANMODE_1D(ini_img)
    cursor = mplcursors.cursor(multiple=True)
    plt.show()
    return


if __name__ == '__main__':
    image = r"D:\Program Files\Software\SpadisApp\InternalRelease_SpadisApp_v4.0-150-g89df\SavedImages\Record_Open6pixel_PCM_2024_04_15_11_58_54\GrayImage_frame_0_0.raw"
    do_work(image)
