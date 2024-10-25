import numpy as np
from numba import njit, prange


@njit(parallel=True)
def convolve2d_numba(image, kernel):
    image_height, image_width = image.shape
    kernel_height, kernel_width = kernel.shape

    pad_height = kernel_height // 2
    pad_width = kernel_width // 2

    # 手动填充图像
    padded_image = np.zeros((image_height + 2 * pad_height, image_width + 2 * pad_width))
    padded_image[pad_height:pad_height + image_height, pad_width:pad_width + image_width] = image

    output = np.zeros_like(image)

    for i in prange(image_height):
        for j in prange(image_width):
            region = padded_image[i:i + kernel_height, j:j + kernel_width]
            output[i, j] = np.sum(region * kernel)

    return output


# 测试
if __name__ == "__main__":
    image = np.random.rand(512, 512)
    kernel = np.array([[1, 0, -1],
                       [1, 0, -1],
                       [1, 0, -1]])

    result = convolve2d_numba(image, kernel)
    print(result.shape)
