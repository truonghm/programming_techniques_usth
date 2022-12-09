# mystats.py : the module with the personal stats functions
import numpy as np
import matplotlib.pyplot as plt

#mean(x): returns the mean of the one-dimensional array x
def mean(x) :
    total = 0
    count = 0
    for i in x:
        total += i
        count += 1

    return total/count

#variance(x): returns the variance of the one-dimensional array x
def variance(x) :
    mean_x = mean(x)
    total = 0
    count = 0
    for i in x:
        total += (i - mean_x)**2
        count += 1
    
    return total/count

#covariance(x,y): returns the covariance of the one-dimensional array x and y
def covariance(x,y) :
    if len(x) != len(y):
        raise ValueError("Lengths of x and y have to be the same")
    mean_x = mean(x)
    mean_y = mean(y)
    total = 0
    count = 0
    for i,j in zip(x, y):
        total += (i-mean_x)*(j-mean_y)
        count += 1

    return total/count

# median(x): returns the median of the one-dimensional array x
def median(x) :
    def __qsort(inlist):
        if inlist == []: 
            return []
        else:
            pivot = inlist[0]
            lesser = __qsort([x for x in inlist[1:] if x < pivot])
            greater = __qsort([x for x in inlist[1:] if x >= pivot])
            return lesser + [pivot] + greater
    x = __qsort(x)
    count = 0
    for i in x:
        count += 1
    if count % 2 == 1:
        return x[count // 2]
    else:
        mid = int(count/2)
        return 0.5 * (x[mid - 1] + x[mid])

# regression(x,y): returns a list [a,b] where y=ax+b is the linear regression of y on x
def regression(x,y) :
    n = np.size(x)

    mean_x = mean(x)
    mean_y = mean(y)

    ss_xy = np.sum(y*x) - n*mean_y*mean_x
    ss_xx = np.sum(x*x) - n*mean_x*mean_x

    a = ss_xy / ss_xx
    b = mean_y - a*mean_x

    return [a,b]

if __name__ == "__main__":

    #Tests
    w=np.asarray([0.0,12.0,13.0,99.0])
    print("Median = "+str(median(w)))
    x=np.asarray([2.0,6.0,10])
    print("Mean = "+str(mean(x)))
    print("Variance = "+str(variance(x)))
    print("Median = "+str(median(x)))
    y=np.asarray([1.0,20.0,15.0])
    print("Covariance of "+str(x)+" and "+str(y)+" ="+str(covariance(x,y)))
    [a,b]=regression(x,y)
    print("The regression line of "+str(y)+"on "+str(x)+"has the equation :\n","y="+str(a)+"*x+"+str(b))

    #Test to a random numpy array
    x=np.random.random_sample(15)
    print(x)
    print("Mean = "+str(mean(x)))
    print("Variance = "+str(variance(x)))
    print("Median = "+str(median(x)))
    y=np.random.random_sample(15)
    print(y)
    print("Covariance of "+str(x)+" and "+str(y)+" = "+str(covariance(x,y)))
    [a,b]=regression(x,y)
    print("The regression line of"+str(y)+"on"+str(x)+"has the equation :\n","y="+str(a)+"*x+"+str(b))