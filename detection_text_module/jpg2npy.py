# -- coding: utf-8 --
# @Time : 2020/4/8 下午9:25
# @Author : Gao Shang
# @File : jpg2npy.py
# @Software : PyCharm

import numpy as np
import scipy.misc
import cv2

imgs_test = np.load('./template/watermark1_laplace.npy') #读入.npy文件
print(imgs_test.shape)
for i in range(imgs_test.shape[0]):
    B = imgs_test[i, :, 0]
    # scipy.misc.imsave("_testResults.jpg", B)  #保存为png格式，也可将png换位jpg等其他格式
    cv2.imwrite("_testResults.jpg", B)

# import cv2
# import numpy as np
# image = cv2.imread('./template/watermark1_laplace.jpg')
# # np.save('test.npy', image)
# # print('source', np.load('test.npy'))
# print(image)
# print('target', np.load('./template/watermark1_laplace.npy'))
# cv2.imwrite('testjpg.jpg', np.load('./template/watermark1_laplace.npy'))