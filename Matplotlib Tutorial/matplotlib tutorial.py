import matplotlib.pyplot as plt
#from random import randint as rdt
import csv
import numpy as np

import urllib
import matplotlib.dates as mdates

import sys
print(sys.version)


"""
x=[1,2,3]
y=[5,7,4]

x2=[1,2,3]
y2=[10,14,12]

plt.plot(x,y,label="First Line")
plt.plot(x2,y2,label="Second Line")
plt.xlabel("Plot Number")
plt.ylabel("Important var")
plt.title("Interesting graph\nCheck it out!")
plt.legend()
plt.show()



x=[2,4,6,8,10]
y=[6,7,8,9,10]

x2=[1,3,5,6,0]
y2=[6,3,8,3,10]

population_ages=[20+rdt(0,50) for i in range(20)]
ids=range(len(population_ages))

bins=[10*x for x in ids]


plt.bar(ids,population_ages)
plt.bar(x,y,label="Bars1",color="blue")
plt.bar(x2,y2,label="Bars2",color="c")
plt.hist(population_ages,bins,histtype="bar",rwidth=0.8)



x=[2,4,6,8,10]
y=[6,7,8,9,10]

days=[1,2,3,4,5]
sleeping=[7,6,6,11,7]
eating=[2,3,4,3,2]
working=[5,3,5,6,2]
playing=[6,4,7,3,9]

#plt.scatter(x,y,label="skitcat",color="k",marker="x",s=100)

plt.plot([],[],color="m",label="Sleeping")
plt.plot([],[],color="c",label="Eating")
plt.plot([],[],color="r",label="Working")
plt.plot([],[],color="k",label="Playing")

plt.stackplot(days,sleeping,eating,working,playing,colors=["m","c","r","k"])



slices=[7,4,2,13]
activities=["sleeping","eating","working","playing"]
cols=["c","m","r","k"]

plt.pie(slices,labels=activities,colors=cols,startangle=90,shadow=True,explode=[0,0,0.1,0],autopct="%1.1f%%")


#Part 1

x=[]
y=[]

with open("text.txt","r") as csvfile:
    plots=csv.reader(csvfile,delimiter=",")
    for row in plots:
        x.append(int(row[0]))
        y.append(int(row[1]))

plt.plot(x,y,label="loaded from file")


#Part 2

x,y=np.loadtxt("text.txt",delimiter=",",unpack=True)

plt.plot(x,y,label="loaded from file")
"""

def bytespdate2num(fmt,encoding="utf-8"):
    strconverter=mdates.strpdate2num(fmt)
    def bytesconverter(b):
        s=b.decode(encoding)
        return strconverter(s)
    return bytesconverter



def graph_data(stock):

    #fig=plt.figure()
    #ax1=plt.subplot2grid((1,1),(0,0))

    stock_price_url = 'https://pythonprogramming.net/yahoo_finance_replacement'

    source_code=urllib.request.urlopen(stock_price_url).read().decode()
    #print(source_code)
    stock_data=[]
    split_source=source_code.split('\n')

    for line in split_source:
        split_line=line.split(",")
        if len(split_line)==6:
            if 'values' not in line and 'labels' not in line:
                stock_data.append(line)

    date,closep,highp,lowp,openp,volume=np.loadtxt(stock_data,
                                             delimiter=",",
                                             unpack=True,
                                             #%Y=full year
                                             #%y=partial year
                                             #%m=number month
                                             #%d=day
                                             #%H=hours
                                             #%M=minutes
                                             #%S=seconds
                                             #%m-%d-%Y
                                             #converters={0: bytespdate2num('%Y%m%d')})
                                             converters={0: lambda s : mdates.date2num(datetime.strptime(s.decode("utf-8"),'%Y%m%d'))})

    plt.plot_date(date,closep,"-")



    plt.xlabel("date")
    plt.ylabel("price")
    plt.title("Interesting graph\nCheck it out!")
    plt.legend()
    plt.show()

graph_data("TSLA")
