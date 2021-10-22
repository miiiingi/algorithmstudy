import pandas as pd
import seaborn as sns
import numpy as np
def count_missing(col) : 
    null_vec = pd.isnull(col)
    null_sum = np.sum(null_vec)
    return null_sum
def prop_missing(col) : 
    null_sum = count_missing(col)
    return null_sum / len(col)
titanic = sns.load_dataset('titanic')
print(titanic.apply(prop_missing))