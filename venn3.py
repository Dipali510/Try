import matplotlib.pyplot as plt
from matplotlib_venn import venn3, venn3_unweighted
items=[80,43,6,20,10,5,2]
labels=['set1','set2','set3']
venn3(subsets=items, set_labels=labels,set_colors=['red','blue','green'],alpha=0.5  )
plt.title("Venn Diagram")
plt.savefig("C:/Users/dipali/Downloads/venn_diagram.png")
plt.show()