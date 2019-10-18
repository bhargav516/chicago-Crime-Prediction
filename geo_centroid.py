import csv

f = open('data/taxiTripsPart.csv')
reader = csv.DictReader(f)

res = [] #matrix to store centroid of community
flag = 0
for row in reader:
    if int(row['Pickup Community Area']) > flag:
        res.append([row['Pickup Community Area'], row['Pickup Centroid Latitude'], row['Pickup Centroid Longitude']])
        flag += 1

# as usual 
outfile = open('data/centroid_community.csv','w')
writer = csv.writer(outfile, delimiter=';', quotechar='"')
writer.writerows(res)
outfile.close()
