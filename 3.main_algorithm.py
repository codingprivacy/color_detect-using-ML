__author__ = 'Harsh'
import numpy as np
import matplotlib.pyplot as pl
import math
import pickle
f=open("sample_data","rb")
X=pickle.load(f)
f.close()
f=open("sample_output","rb")
y=pickle.load(f)
f.close()
print(y)
X=X/1000.0
print(X)

# f=open("theta","rb")
# theta=pickle.load(f)
# f.close()
#pl.plot(theta,'ro')
#pl.show()


features=3

X=np.insert(X,0,[1],axis=1)   #input  trained

y=np.array(y)   #output trained
m=247             #No of examples
alpha=2     #learning rate
theta=np.array([0]*int(features+1)).reshape(int(features+1),1)    #initializing theta





def sigmoid(z):

    den = 1.0 + np.e ** (-1.0 * z)

    d = 1.0 / den
    #print(d)
    return d

def cost(theta):

    sigmoid_value=X.dot(theta)
                                                    #print(sigmoid_value)

                                                    # value1=sigmoid(sigmoid_value)
                                                    # value2=np.log(sigmoid(sigmoid_value))
                                                    # value3= 1-sigmoid(sigmoid_value)
                                                    # value4=np.log( 1-sigmoid(sigmoid_value))
                                                    #
                                                    # print("value1:",value1)
                                                    # print("value2",value2)
                                                    # print("value3",value3)
                                                    # print("value4",value4)

    J=(-1./m)*np.sum((y*(np.log(sigmoid(sigmoid_value))) + (1-y)*np.log( 1-sigmoid(sigmoid_value))   ))

    return J





def gradient_descent(X):


    grad=np.zeros((features+1,1),dtype=float)              #array of new_gradient generated thetas
    new_x=[0]*int(features+1)                                 #array for formatting X

    for i in range(features+1):                           #X formatted as 1*66 elements of each column changed to 66*1
        new_x[i]=np.array(X[:,i]).reshape(m,1)          #for simplifying multiplication
    #print((sigmoid(X.dot(grad))-y))
    #print(new_x[1])

    #theta_new=np.zeros((2501,1),dtype=float)
    theta_new=theta
    count=0

    for i in range(200000):
        for j in range(features+1):
            grad[j]=theta_new[j]-alpha*((1./m)*np.sum((sigmoid(X.dot(theta_new))-y)*new_x[j]))
        theta_new=grad
        #print(theta_new[1],theta_new[2],theta_new[3])
        count+=1
        #print(count)
        # if(i==10000):
        #     pl.plot(X.dot(theta_new))
        #     pl.show()
        # if(i==20000):
        #     pl.plot(X.dot(theta_new))
        #     pl.show()
        # if(i==30000):
        #     pl.plot(X.dot(theta_new))
        #     pl.show()
        # if(i==40000):
        #     pl.plot(X.dot(theta_new))
        #     pl.show()
            

    return grad


print("cost function")
J=cost(theta)
print(J)

print("gradient descent")
grad=gradient_descent(X)
print(grad)

print("cost function")
J=cost(grad)
print(J)


f=open("theta","wb")
pickle.dump(grad,f)
f.close()
print("successfull")


