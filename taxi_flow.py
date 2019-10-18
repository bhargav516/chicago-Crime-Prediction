import csv
import numpy as np
leaveOut =-1
#taking trips data set initial
f = open('data/taxiTripsPart.csv')   # This file is too large, so plz download i have just added part of it.
reader = csv.DictReader(f)
matrix_count = np.zeros((77,77)) # 77 * 77 matrix or array 2d
for row in reader:
	if not row['Dropoff Community Area']: # checking for emptiness of drop location
		print("")
	else:
		if int(row['Dropoff Community Area'])>1 and int(row['Dropoff Community Area'])<77 : #checking for range
			matrix_count[int(row['Pickup Community Area'])-1, int(row['Dropoff Community Area'])-1] += 1 #entering in intermediate matrix
#new file to copy the intermediate matrix for future use 
outfile = open('data/taxi_flow_count.csv', 'w')
writer = csv.writer(outfile, delimiter=';', quotechar='"')
writer.writerows(matrix_count)
outfile.close()

#---------------------------------------------------------------------------------------------------------------------------------------------

#this part will just make the  actual matix for taxi flow 
f = open('data/taxi_flow_count.csv')
reader = csv.reader(f, delimiter = ';')
matrixTF = np.zeros((77,77))  #creating the intermediate matrix
rowNum = 0
for row in reader:
        matrixTF[rowNum] = row #copying complete row
        matrixTF[rowNum][rowNum] = 0 #except example : 77 to 77 there wont be any trips
        rowNum += 1
#new file to copy the intermediate matrix for future use 
outfile = open('data/taxi_flow_matrix.csv', 'w')
writer = csv.writer(outfile, delimiter=';', quotechar='"')
writer.writerows(matrixTF)
outfile.close()

#---------------------------------------------------------------------------------------------------------------------------------------------

#loading csv file back to matrix
f_matrix = np.loadtxt('data/taxi_flow_matrix.csv', delimiter=';')
n = f_matrix.shape
#print(n)
if leaveOut > 0:
        f_matrix = np.delete(f_matrix, leaveOut - 1, 0)
        f_matrix = np.delete(f_matrix, leaveOut - 1, 1)
n = f_matrix.shape
#print(n)

#---------------------------------------------------------------------------------------------------------------------------------------------

#normalizing the matrix for taxi flow please refer the research paper for further details to have indepth knowledge (6.3.2)

# normalizing can be done with destination or source (6.3.2)

#for an instance we need to choose only one so : by destination 

tf_matrix = f_matrix #copying matrix from above

n = tf_matrix.shape[0] #number of row

tf_matrix = tf_matrix.astype(float) #converting int matrix to float

tf_matrix = np.transpose(tf_matrix) #transpose the matrix
#print(tf_matrix)

#https://docs.scipy.org/doc/numpy-1.10.0/reference/generated/numpy.sum.html

fsum = np.sum(tf_matrix, axis=1, keepdims=True)

fsum[fsum == 0] = 1 #if sum is zero makes it '1'
#print(fsum)
#print(fsum.shape)

#https://stackoverflow.com/questions/5142418/what-is-the-use-of-assert-in-python

assert fsum.shape == (n, 1)

tf_matrix = tf_matrix / fsum # 2d matrix / 1d matrix

#print(tf_matrix)

#https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.testing.assert_array_almost_equal.html
#add for testing when we get the complete data sets

#np.testing.assert_almost_equal(tf_matrix.sum(), n)
#np.testing.assert_almost_equal(tf_matrix.sum(axis=1)[n - 1], 1)

#bysource we will execute if by destination wont work

#fsum = np.sum(tf_matrix, axis=1, keepdims=True)
 #       fsum[fsum == 0] = 1
  #      tf_matrix = tf_matrix / fsum
   #     assert fsum.shape == (n, 1)
    #    np.testing.assert_almost_equal(tf_matrix.sum(axis=1)[n - 1], 1)
#both are working already checked
print(tf_matrix)


