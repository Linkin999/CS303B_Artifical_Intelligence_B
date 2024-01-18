import numpy as np
import cv2
from PIL import Image

def inversion(input_image):
    output_image=255-input_image
    output_image=output_image.astype(np.uint8)
    return output_image

def contrast_scaling(input_image):
    output_image=input_image
    H,W=input_image.shape
    for i in range(0,H):
        for j in range(0,W):
            if(input_image[i][j]<=100):
                output_image[i][j]=0
            elif(input_image[i][j]>=200):
                output_image[i][j]=255
            else:
                output_image[i][j]=(input_image[i][j]-100)/100*255
    output_image=output_image.astype(np.uint8)
    return output_image

def multiply(input_image):
    H,W=input_image.shape
    output_image=np.zeros([H,W],dtype=np.float16)
    for i in range(0,H):
        for j in range(0,W):
            if(input_image[i][j]<=100):
                output_image[i][j]=input_image[i][j]*2
            elif(input_image[i][j]>200):
                output_image[i][j]=float(input_image[i][j])
            else:
                output_image[i][j]=input_image[i][j]*3
    print(output_image.dtype)
    print(output_image)
    a=np.max(output_image)
    b=np.min(output_image)
    for i in range(0,H):
        for j in range(0,W):
            output_image[i][j]=(output_image[i][j]-b)/(a-b)*255
    output_image=output_image.astype(np.uint8)
    return output_image






if  __name__=='__main__':
    image_path="D:/Study_in_SUSTech\First semester of senior year\Artifical Intelligence B/lab/lab2/LabImages/Image/lena.bmp"
    img=cv2.imread(image_path,cv2.IMREAD_GRAYSCALE)
    cv2.imshow('origin',img)

    out_img1=inversion(img)
    #print(out_img1)
    cv2.imshow('inversion',out_img1)

    out_img2=contrast_scaling(img)
    cv2.imshow('contrast_sscaling',out_img2)
    save_path="D:/Study_in_SUSTech\First semester of senior year\Artifical Intelligence B/lab/lab2/LabImages/Image/"
    savedimage2=Image.fromarray(out_img2)
    savedimage2.save(save_path+'lena_inst_scale.bmp')

    out_img3=multiply(img)
    cv2.imshow('multiply',out_img3)  


    cv2.waitKey(0)
    

