import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
data=pd.DataFrame(
        [[100,200],[200,300]],
        index=["sample1","sample2"],
        columns=["gene1","gene2"])
sns.heatmap( data=data)
plt.show()
