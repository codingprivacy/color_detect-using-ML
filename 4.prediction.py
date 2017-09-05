__author__ = 'Harsh'
import numpy as np
import matplotlib.pyplot as pl
import pickle
f=open("theta","rb")
theta=pickle.load(f)
f=open("sample_data","rb")
X=pickle.load(f)
f=open("sample_output","rb")
y=pickle.load(f)
f.close()


def sigmoid(z):

    den = 1.0 + np.e ** (-1.0 * z)

    d = 1.0 / den
    #print(d)
    return d

X=X/1000.0
X=np.insert(X,0,[1],axis=1)

y_new=[]
p=sigmoid(X.dot(theta))
for i in p:
    if(i>=0.60):
        y_new.append([1])
    else:
        y_new.append([0])
print(y_new==y)   #checking if the predicted values match with the trained values.


def plot():
    X_plot=[]             #X_plot contains all the values for which y is 1
    Y_plot=[]
    for i in range(247):
        if(y_new[i]==[0]):
            Y_plot.append(X[i])
        if(y_new[i]==[1]):
            X_plot.append(X[i])
    X_plot=np.array(X_plot)
    Y_plot=np.array(Y_plot)
    print(X_plot.shape)

    print(theta)
    pl.plot(X_plot[:,2],X_plot[:,3],'ro')
    pl.axis([-.1,0.3,-.1,0.3])
    pl.plot(Y_plot[:,2],Y_plot[:,3],'bs')
    pl.show()

plot()
