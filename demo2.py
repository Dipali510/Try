import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

gene1=[1,2,3,4,5]
gene2=[2,3,4,5,6]
plt.boxplot([gene1,gene2],labels=["gene1","gene2"])
plt.title("Boxplot of gene expression")
plt.ylabel("Expression level")
plt.show()