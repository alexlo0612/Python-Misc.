import numpy as np
import numpy.random as rnd
import matplotlib.pyplot as plt
import md5



####Calculate the MD5 Hash Value of the Following String
##m = md5.new()
##m.update("12lsdfahlwfhiqwefuqwguifhsfgjksagf2qiuofwqieurihfiasfhdqpweiqoweyiqoryquiwdfg3")
##m1= m .hexdigest()
##  


##Simple Non-Secure Numerical Only RSA Function

def resarsaencfunc():
    try:
            m = int(input('Input Some Random Number')) #5
            e = int(input('Input Some Random Number')) #5321
            n = int(input('Input Some Random Number')) #15 # n =10545437.0
            func_value= m**e%n
            return func_value
    except:
        print "Input is Not a Valid Number"





r2 = 1 ## r^2 (radius squared)
#n = int(1e5) ## number of elements
n = 10545437.0



## seed PRNG (for debugging)
#print resarsaencfunc()
k = 5
#resarsaencfunc()
#429496729
rnd.seed(k)

## generate random numbers

Xr = rnd.rand(n)

Yr = rnd.rand(n)

Len = rnd.rand(n)

m = 0.

pi = 0. 

#print Xr

#print Yr


## calculate whether or not your x, y values are in the circle

for i in range (0,len(Len)):

    if Xr[i]**2 + Yr[i]**2 < r2:
      m = m+1
      pi = 4*(m/n)
    

## print your approximation of pi

print pi 

## optional task: create a scatter plot of the points inside the circle vs the
## points outside of the circle;
## need to use np.where() for this to get the indices
## use plt.scatter() to plot
