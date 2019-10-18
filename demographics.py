import numpy as np
import csv
import matplotlib.pyplot as plt


f = open('data/demographics.csv')
reader_demo = csv.DictReader(f)
features = []
flag = 0
#basically we are creating a matrix of 4*77
for row in reader_demo:
	if int(row['Community #']) > flag:
            features.append([row['Total_Population'], row['NHW_P'], row['NHB_P'], row['Poverty_P']])
            flag += 1
print(features)
#converting in to float 
features = np.asarray(features, dtype=np.float)

#prints the float matrix

#print(features)

f = open('data/demographics.csv')
reader_demo = csv.DictReader(f)
x = []  # x to store the communties
y = []  # y is crime rate vecctor
flag = 0
#basically we are creating a matrix of 1*77 only crime rate
for row in reader_demo:
	x.append(int(row['Community #']))
	if int(row['Community #']) > flag:
            y.append(row['crime_rate'])
            flag += 1
print(y)
y = np.asarray(y, dtype=np.float)
#prints the float matrix
new_y = np.round(y, decimals=3)
#print(y)

#now plot communties vs crime rate

plt.ylim(0,0.5)
plt.xlim(1,77)

plt.xlabel('Communities')
plt.ylabel('Rate')
plt.plot(x,y,"-o")
for i, txt in enumerate(new_y):
    plt.annotate(txt, (x[i],y[i]))
plt.show()

