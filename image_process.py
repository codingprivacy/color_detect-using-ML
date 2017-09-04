import cv2
import pickle
import numpy as np
import glob

count=0
list2=[]
listy=[]
for img in glob.glob("C:\Users\Anindita\PycharmProjects\Img_process\color/img*.jpg"):    #reading all the images from the color folder
    img1=cv2.imread(img)

    height,width,type=img1.shape                                     #bifurcating pixels

    suma=0
    sumb=0
    sumc=0
    list1=[]
    count=count+1
    for i in range(height):

        for j in range(width):

            #print(img1[i][j])
            a=img1[i][j][0]           #value of the blue color
            suma=suma+a
            b=img1[i][j][1]           #value of the green color
            sumb=sumb+b
            c=img1[i][j][2]           #value of the red color
            sumc=sumc+c

    avga=suma/(height*width)                   #taking average of the bgr color i.e 50x50
    avgb=sumb/(height*width)
    avgc=sumc/(height*width)
    list1.append([avga])
    list1.append([avgb])
    list1.append([avgc])
    list2.append(list1)
    print(list2)

    if (avgc>=200):
        y=1                         #setting the trained  output for red pixel

    else:
        y=0
    listy.append(y)

list2=np.array(list2).reshape(84,3)     #reshaping example inputs into 84x3 matrix
listy=np.array(listy).reshape(84,1)     #reshaping trained outputs into 84x1 matrix

g=open("sample_output","wb")
pickle.dump(listy,g)                      #saves the trained output in sample_output
f=open("sample_data","wb")
pickle.dump(list2,f)                      #saves the examples in sample_data
print("successfull")

    
