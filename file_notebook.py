fa=open('C:\\Users\\dipali\\OneDrive\\Documents\\pythonfile handle.txt','r')

fb=open('C:\\Users\\dipali\\OneDrive\\Documents\\pythonfile handle1.txt','w')
data=fa.read()
ls=data.split(' ')
fb.write(str(len(ls)))
fa.close()
fb.close()