import pickle
fc=open('C:\\Users\\dipali\\OneDrive\\Documents\\pythonfile handle2.dat','rb')
ln=pickle.load(fc)
print(ln)
fc.close()

fc=open('C:\\Users\\dipali\\OneDrive\\Documents\\pythonfile handle3.dat','wb')
d={}
for nb in ln:
    d[nb]=int(input("enter marks"))
pickle.dump(d,fc)
fc.close()

