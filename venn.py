import matplotlib.pyplot as plt
from matplotlib_venn import venn2,venn2_unweighted
items=[80,43,6]
labels=['set1','set2']    
venn2(subsets=items, set_labels=labels,set_colors=['red','blue'],alpha=0.5  ) 
plt.title("Venn Diagram")
plt.savefig("C:/Users/dipali/Downloads/venn_diagram.png")
plt.show()
venn2_unweighted(subsets=items, set_labels=labels,set_colors=['red','blue'],alpha=0.5  )
plt.title("Venn Diagram")
plt.savefig("C:/Users/dipali/Downloads/venn_diagram_unweighted.png")
plt.show()