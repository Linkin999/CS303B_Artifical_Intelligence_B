import numpy as np
import cv2
import matplotlib.pyplot as plt

#exercise 1
def histogram(input_image):
    hist=[]
    H,W=input_image.shape
    total=H*W
    for i in range(256):
        hist.append(np.sum(input_image==i)/(total))
    
    return hist
#exercise 2
def histogram_change(input_image):
    hist_change=[]
    H,W=input_image.shape
    total=H*W
    for i in range(128):
        hist_change.append(np.sum(input_image==i)/(total))
    #normalised
    return hist_change/np.sum(hist_change)

#exercise 3
def distance_calculate(histogram1,histogram2):
    chi_square=0
    euclidean_distance=0
    for i in range(256):
        if(histogram1[i]==0 and histogram2[i]==0):
            chi_square=chi_square
        else:
            chi_square=chi_square+0.5*np.power(histogram1[i]-histogram2[i],2)/(histogram1[i]+histogram2[i])
        euclidean_distance=np.power(histogram1[i]-histogram2[i],2)
    euclidean_distance=np.sqrt(euclidean_distance)
    return [chi_square,euclidean_distance]

if  __name__=='__main__':
    image_path="D:/Study_in_SUSTech\First semester of senior year\Artifical Intelligence B/lab/lab2/LabImages/Image/lena.bmp"
    img=cv2.imread(image_path,cv2.IMREAD_GRAYSCALE)
    cv2.imshow('lena',img)

    #exercise 1
    hist1=histogram(img)
    x=np.arange(256)
    plt.bar(x,hist1)
    plt.title('histogram  of input image_lena')
    plt.show()

    #exercise 2
    hist1_2=histogram_change(img)
    x2=np.arange(128)
    plt.bar(x2,hist1_2)
    plt.title('histogram_change_bins  of input image_lena')
    plt.show()

    image_path2="D:/Study_in_SUSTech\First semester of senior year\Artifical Intelligence B/lab/lab2/LabImages/Image/lena_inst_scale.bmp"
    img2=cv2.imread(image_path2,cv2.IMREAD_GRAYSCALE)
    cv2.imshow('lena_inst_scale',img2)

    #exercise 1
    hist2=histogram(img2)
    plt.bar(x,hist2)
    plt.title('histogram  of input image_lena_inst_scale')
    plt.show()

    #exercise 2
    hist2_2=histogram_change(img2)
    plt.bar(x2,hist2_2)
    plt.title('histogram_change_bins  of input image_lena_inst_scale')
    plt.show()

    image_path3="D:/Study_in_SUSTech\First semester of senior year\Artifical Intelligence B/lab/lab2/LabImages/Image/panda.jpg"
    img3=cv2.imread(image_path3,cv2.IMREAD_GRAYSCALE)
    cv2.imshow('panda',img3)

    #exercise 1
    hist3=histogram(img3)
    plt.bar(x,hist3)
    plt.title('histogram  of input image_panda')
    plt.show()

    #exercise 2
    hist3_2=histogram_change(img3)
    plt.bar(x2,hist3_2)
    plt.title('histogram_change_bins  of input image_panda')
    plt.show()

    cv2.waitKey(0)

    #exercise 3
    [chi_square_1_2,euclidean_distance_1_2]=distance_calculate(hist1,hist2)
    [chi_square_1_3,euclidean_distance_1_3]=distance_calculate(hist1,hist3)
    [chi_square_2_3,euclidean_distance_2_3]=distance_calculate(hist2,hist3)
    print(chi_square_1_2,euclidean_distance_1_2)
    print(chi_square_1_3,euclidean_distance_1_3)
    print(chi_square_2_3,euclidean_distance_2_3)

    # a=np.array([1,2,3])
    # b=np.array([4,5,6])
    # print(a-b)
    # print(np.power(a-b,2))
    # print(np.sum(a))