import pandas as pd
import matplotlib.pyplot as plt
filename="C:\\Users\\dipali\\OneDrive\\Documents\\demo.csv"
data=pd.read_csv(filename)
rdata=[data['Marks']>90]
print(rdata)

