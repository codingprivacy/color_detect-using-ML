
# this code is used to print rgb code of each pixel of the image and save it to list
# the list will then be saved into sample_data file on which logistic regression is performed
import numpy as np
import cv2
import pickle
#y=[0,0,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,1,0,1,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0]
y=[0]*173+[1]*64+[1,0,0,0,0,0,0,1,1,1]


y_list=[]
list2=[]
examples=247
import numpy as np
for i in range(1,examples+1):
    list=[]

    print(i)

    img1=cv2.imread('C:\Users\Anindita\PycharmProjects\color_detect-using-ML\data\input_data\samples\img'+str(i)+".jpg")
    try:
        height,width,type=img1.shape  #finding the height and width of the image
    except AttributeError:
        continue
    count=0
    #cv2.dlmwrite('textFile_name.txt', img1, '\n');
    #f=open("list_add.txt","w")
    #then we will loop through all the pixels and print its value
    a=0
    b=0
    c=0
    for i in range(height):   #going through each column pixel

        for j in range(width):  #taking all the pixels of that column i.e. all row pixels of i
            #print(img1[i][j])#printing each one
            a+=img1[i][j][0]

            b+=img1[i][j][1]
            c+=img1[i][j][2]

    list.append(a/(width*height))         #calculating the average of all the pixels and adding it to the list
    list.append(b/(width*height))
    list.append(c/(width*height))
    # if(c/(width*height)>=200):            #putting the value of y to 1 if the red pixel is above 200 and appending to the list
    #     y_list.append([1])
    # else:
    #     y_list.append([0])
    count=count+1


    list2.append(list)
#print(len(list2))
#print(len(y))

list2=np.array(list2).reshape(247,3)
print(list2)
y_list=np.array(y).reshape(247,1)
print(y_list)
f=open("sample_data","wb")
pickle.dump(list2,f)
f.close()
f=open("sample_output","wb")
pickle.dump(y_list,f)
f.close()
print("successfull")


# #taken photo , patitioned, taken each pixel of the image and stored into the database
# #database is our training set x and providing corrosponding value of y
# #appllying algorithm
# #implementing it
#
raw_input()

