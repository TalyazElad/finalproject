# This is a sample Python script.
import cv2
import matplotlib.pyplot as plt
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import numpy as np

def print_hi():
    im = cv2.imread("yaelbit_before.jpg", 0)  # read as gray scale
    blurred = cv2.GaussianBlur(im, (7, 7), 1.166)  # apply gaussian blur to the image
    plt.imsave('yaelbit_afterblurr.png', blurred)
    #print(blurred)
    blurred_sq = blurred * blurred
    plt.imsave('yaelbit_afterdoubleblurr.png', blurred_sq)
    sigma = cv2.GaussianBlur(im * im, (7, 7), 1.166)
    sigma = (sigma - blurred_sq) ** 0.5
    sigma = sigma + 1.0 / 255  # to make sure the denominator doesn't give DivideByZero Exception
    structdis = (im - blurred) / sigma  # final MSCN(i, j) image
    plt.imsave('yaelbit_after.png', structdis)
    # indices to calculate pair-wise products (H, V, D1, D2)
    shifts = [[0, 1], [1, 0], [1, 1], [-1, 1]]
    print(structdis.shape)
    #ShiftArr = np.zeros(structdis.shape)
    # calculate pairwise components in each orientation
    for itr_shift in range(1, len(shifts) + 1):
        OrigArr = structdis
        reqshift = shifts[itr_shift - 1]  # shifting index
        M = np.float32([[1, 0, reqshift[1]], [0, 1, reqshift[0]]])
        ShiftArr = cv2.warpAffine(OrigArr, M, (structdis.shape[1], structdis.shape[0]))
    #     for i in range(structdis.shape[0]):
    #         for j in range(structdis.shape[1]):
    #             if (i + reqshift[0] >= 0 and i + reqshift[0] < structdis.shape[0] and j + reqshift[1] >= 0
    #                     and j  + reqshift[1] < structdis.shape[1]):
    #                 ShiftArr[i, j] = OrigArr[i + reqshift[0], j + reqshift[1]]
    #             else:
    #                 ShiftArr[i, j] = 0
    # # print(ShiftArr)
    plt.imsave('ShiftArr.png', ShiftArr)
    # # load the model from allmodel file
    # model = svmutil.svm_load_model("allmodel")
    # # create svm node array from features list
    # x, idx = gen_svm_nodearray(x[1:], isKernel=(model.param.kernel_type == PRECOMPUTED))
    # nr_classifier = 1  # fixed for svm type as EPSILON_SVR (regression)
    # prob_estimates = (c_double * nr_classifier)()
    #
    # # predict quality score of an image using libsvm module
    # qualityscore = svmutil.libsvm.svm_predict_probability(model, x, dec_values)


    # Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
