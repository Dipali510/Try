import matplotlib.pyplot as plt
from matplotlib_venn import venn2
items=[80,43,6]
labels=['set1','set2']    
venn2(subsets=items, set_labels=labels,set_colors=['red','blue'])  
plt.title("Venn Diagram")
plt.savefig("C:/Users/dipali/Downloads/venn_diagram.png")
plt.show()