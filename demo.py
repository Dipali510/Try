import pandas as pd
import matplotlib.pyplot as plt
filename="C:\\Users\\dipali\\OneDrive\\Documents\\demo.csv"
data=pd.read_csv(filename)
print(data['Marks'].plot(kind='bar'))
plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Marks of Students")
plt.savefig("C:\\Users\\dipali\\OneDrive\\Documents\\marks_bar_chart.png")
plt.show()