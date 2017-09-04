
#this code is used to partition the image into blocks so that we can crop the image and get its segments
#d_one is no. of blocks horizontally and d_two is no. of blocks vertically
#the image will automaically be stored
#user will assign d_one and d_two manually based on the sample color pallete
import cv2
import numpy as np
img_new=np.zeros((50,50,3),(np.uint8))
image1=cv2.imread("samples\sample4.jpg")    #reading the image
height,width,type=image1.shape
d_one=4                  #no of horizontal blocks
d_two=5                  #np of vertical blocks
i1=width/d_one
i2=height/d_two
print(i2)
print(i1)

def doit():
    count=1
    for i in range (d_one):

        for j in range(d_two):
            count+=1
            new=image1[i1*j+10:i1*j+60,i2*i+10:i2*i+60]
            img_new[0:50,0:50]=new                         # cropping image into 50x50
            cv2.imshow('img',img_new)
            name="img"+str(count)+".jpg"    #here i have put number count and concateneted to provide diffrent name each time

            cv2.imwrite(name,img_new)  #here this function is to save it with name "name"

doit()

cv2.waitKey(0)