#HW3
#Worked with Federico Rivas,Gage Ferguson, Jillian W.,Caridad Coll, Francisco Mendez
import numpy as np
annual_avg=np.flip(np.loadtxt('annual_csv_average.csv',dtype='float',skiprows=1),axis=0)
annual=np.flip(np.loadtxt('annual_csv.csv',dtype='float',skiprows=1),axis=0)
avg_years=annual_avg[:,0]
avg_temp=annual_avg[:,1]
anl_years= annual[:,0]
anl_temp= annual[:,1]

def derive(anl_years): #defining and deriving the annual_csv.csv data
    first=[]
    h=1
    x=anl_years
    for i in range(0,len(x)):
        if i==0:
          y=(anl_years[i+h]-anl_years[i])/h
          first.append(y)
        elif i == len(anl_years)-1:
          y=(anl_years[i]-anl_years[i-h])/h
          first.append(y)
        else:
          y=(anl_years[i+h]-anl_years[i-h])/(2*h)
          first.append(y)
    print(first)
    return list(first)


d1=derive(anl_temp) #defining and deriving the annual_csv_average.csv data

def derive(avg_years):
    second=[]
    h=1
    for i in range(0,len(avg_years)):
        if i==0:
          y=(avg_years[i+h]-avg_years[i])/h
          second.append(y)
        elif i == len(avg_years)-1:
          y=(avg_years[i]-avg_years[i-h])/h
          second.append(y)
        else:
          y=(avg_years[i+h]-avg_years[i-h])/(2+h)
          second.append(y)
    print(second)
    return list(second)
d2=derive(avg_temp)

import matplotlib #plotting the derived data
matplotlib.use('Agg')
import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(anl_years,d1)
fig.savefig("Basha_hw3plot2.png",dpi=300)
