import pandas as pd
import seaborn as sns
import numpy as np
df = pd.DataFrame({'a' : [20, 30, 40], 'b' : [100, 300, 500]})
def my_func(col) : 
    return (col[0] + col[1] + col[2]) / 3
titanic = sns.load_dataset('titanic')
def count_missing(col) : 
    null_vec = col.isnull()
    null_count = np.sum(null_vec)
    return null_count
def prop_missing(col) : 
    num = count_missing(col)
    return num / len(col)