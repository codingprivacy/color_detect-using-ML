__author__ = 'Harsh'
import numpy as np

import pickle
import cv2

f=open("theta","rb")
theta=pickle.load(f)
f.close()

def sigmoid(z):

    den = 1.0 + np.e ** (-1.0 * z)

    d = 1.0 / den
    #print(d)
    return d

def testing(X):
    X=np.array(X)
    X=X/1000.0
    X=np.insert(X,0,[1],axis=0)
    #print(X)
    p=100*(sigmoid(X.dot(theta)))
    print("probability:",p)
    if(p>=70):
        print("Given Image is Red")
    elif(p<60):
        print("Image is Not Red")
    else:
        print("Unsure about result but is Containing Red Content")
n=''
while(n!='exit'):
    n=raw_input("Enter Your image location:")
    img=cv2.imread(n)
    height,width,type=img.shape
    #print(img)
    a=0
    b=0
    c=0
    for i in range(height):   #going through each column pixel

            for j in range(width):  #taking all the pixels of that column i.e. all row pixels of i
                #print(img1[i][j])#printing each one
                a+=img[i][j][0]

                b+=img[i][j][1]
                c+=img[i][j][2]
    total=height*width
    avga=(a/total)
    avgb=(b/total)
    avgc=(c/total)
    to_test=[avga,avgb,avgc]
    testing(to_test)
    raw_input()

