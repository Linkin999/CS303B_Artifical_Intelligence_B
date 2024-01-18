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
def threshold_50(input_image):
    H,W=input_image.shape
    for i in range(H):
        for j in range(W):
            if(input_image[i][j]>=50):
                input_image[i][j]=255
            else:
                input_image[i][j]=0
    return input_image

#exercise 3
def threshold_75(input_image):
    H,W=input_image.shape
    for i in range(H):
        for j in range(W):
            if(input_image[i][j]>=1):
                input_image[i][j]=255
            else:
                input_image[i][j]=0
    return input_image

# exercise 4
def Ostu(input_image,grayScale):
    input_image=np.array(input_image).ravel().astype(np.uint8)
    u1=0.0 # the mean of class 1
    u2=0.0 # the mean of class 2
    threshold=0.0

    total=input_image.size
    

    Pixcount=np.zeros(grayScale)
    Pixrate=np.zeros(grayScale)
    for i in range(total):
        Pixvalue=input_image[i]
        Pixcount[Pixvalue]=Pixcount[Pixvalue]+1

    for j in range(grayScale):
        Pixrate[j]=Pixcount[j]*1.0/total

    max_var=0.0
    for i in range(1,grayScale):# avoid w1 is 0
        u1_tem=0.0
        u2_tem=0.0

        # the rate of class 1
        w1=np.sum(Pixrate[:i])
        # the rate of class 2
        w2=1.0-w1

        if (w1==0 or w2==0):
            pass
        else:
            for m in range(i):
                u1_tem=u1_tem+Pixrate[m]*m
            u1=u1_tem*1.0/w1

            for n in range(i,grayScale):
                u2_tem=u2_tem+Pixrate[n]*n
            u2=u2_tem*1.0/w2

            tem_var=w1*w2*np.power(u1-u2,2)

            if(max_var<tem_var):
                max_var=tem_var
                threshold=i
    return threshold

    


if  __name__=='__main__':
    image_path="D:/Study_in_SUSTech\First semester of senior year\Artifical Intelligence B/lab/lab2/LabImages/Image/coins.png"
    img=cv2.imread(image_path,cv2.IMREAD_GRAYSCALE)
    cv2.imshow('coin',img)

    #exercise 1
    hist1=histogram(img)
    x=np.arange(256)
    plt.bar(x,hist1)
    plt.title('histogram  of input image_coin')
    plt.show()

    #exercise 2
    threshold50=threshold_50(img)
    cv2.imshow("threshold50",threshold50)

    #exercise 3
    threshold75=threshold_75(img)
    cv2.imshow("threshold75",threshold75)

    cv2.waitKey(0)

    th=Ostu(img,256)
    print(th)
