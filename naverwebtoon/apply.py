import pandas as pd
import seaborn as sns
import numpy as np
<<<<<<< HEAD
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
=======
def count_missing(col) : 
    null_vec = pd.isnull(col)
    null_sum = np.sum(null_vec)
    return null_sum
def prop_missing(col) : 
    null_sum = count_missing(col)
    return null_sum / len(col)
titanic = sns.load_dataset('titanic')
print(titanic.apply(prop_missing))
>>>>>>> 02d60132aee9e66b4f9b4cd32820848b2cf27e9c
