import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#find lowest m for all points
def fmin(k):
    return min([(ydata[i] - k) / (xdata[i] - min(xdata)) for i in range(len(xdata)) if xdata[i] - min(xdata) != 0])

#find greatest m for all points
def fmax(k):
    return max([(ydata[i] - k) / (xdata[i] - min(xdata)) for i in range(len(xdata)) if xdata[i] - min(xdata) != 0])

#plot mx+b given k, from min(xdata)
def lineplot(m, k):
    plt.plot([min(xdata),21],[k,m*(21-min(xdata)) + k])




df = pd.read_csv("every-20-rows-natality.csv", low_memory=False)

xdata = range(0,20)
ydata = [0] * 20

for i in range(df.shape[0]):
    ydata[int(df.DT_YEAR[i]) - 1969] += df.AM_BIRTHWEIGHT3[i] == 1
   

plt.scatter(xdata, ydata)
#for k in range(min(ydata)+1,max(ydata)):
#    mmin = fmin(k)
#    mmax = fmax(k)
#    print(mmin)
#    print(mmax)
#    lineplot(mmin, k)
#    lineplot(mmax, k)

    
plt.xlim(min(xdata),max(xdata))
plt.ylim(min(ydata),max(ydata))


#find the total error
def error(m, k):
    total_error = 0
    for i in range(len(xdata)):
        #print(str(m) + " " + str(k) + " " + str(total_error))
        total_error += (ydata[i] - (m * xdata[i] + k)) ** 2
    total_error / float(len(xdata) * len(ydata))
    return total_error

minerr = 999999999
minm = 0
mink = 0
for k in range(min(ydata) + 1, max(ydata)-5500):
    #print(k)
    #print(fmin(k))
    #print(fmax(k))
    for m in range(int(fmin(k)), int(fmax(k))):
        if(abs(error(m, k)) < minerr):
            minerr = error(m, k)
            minm = m
            mink = k
print(minerr)
print(minm)
print(mink)
lineplot(minm,mink)

#count = 0
#for i in df:
#    count += 1
#    if(count < 1000):
#        print(i)

#fig = plt.figure()
#ax = fig.gca()

#x = range(9)
#y = [0 for i in range (9)]
#for i in c: 
#    if(i[53:55]=='00'):
#        y[int(i[38])] += 1


#ax.scatter(x, y)

#colors = ('r', 'g', 'b', 'k')
#for c in colors:
#    x = np.random.sample(20)
#    y = np.random.sample(20)
#    ax.scatter(x, y, c=c)
