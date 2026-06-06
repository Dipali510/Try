import csv
with open('C:\\Users\\dipali\\OneDrive\\Documents\\Book1.csv','r') as f:
  ro=csv.reader(f,delimiter=',')
  for row in ro:
    print(row)
