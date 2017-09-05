__author__ = 'Harsh'
#this code is used to partition the image into blocks so that we can crop the image and get its segments
#d_one is no. of blocks horizontally and d_two is no. of blocks vertically
#the image will automaically be stored
import cv2
import numpy as np
img_new=np.zeros((50,50,3),(np.uint8))
image1=cv2.imread("new/sample12.jpg")
height,width,type=image1.shape
d_one=5
d_two=5
i1=width/d_one
i2=height/d_two
print(i2)
print(i1)

def doit():
    
        count=126

        for i in range (d_one):
            
            for j in range(d_two):
                try:
                    count+=1
                    new=image1[i2*i+10:i2*i+60,i1*j+10:i1*j+60]
                    img_new[0:50,0:50]=new
                    #cv2.imshow('img',img_new)
                    name="img"+str(count)+".jpg"
                    cv2.imwrite("new/"+name,img_new)
                except ValueError:
                    
                    print("error")
                   
                    continue
        print(count)
        
#new=image1[0:80,0:78]
#i[50:130,50:128]=new

doit()

cv2.waitKey(0)
