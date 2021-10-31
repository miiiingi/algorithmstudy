from numpy.core.fromnumeric import mean
import pandas as pd
import seaborn as sns
df = pd.read_csv('doit_pandas/data/gapminder.tsv', sep = '\t')
mean_global = df['lifeExp'].mean()
def standardize(col, mean_whole) : 
    return col.mean() - mean_whole

# print(df.groupby('year')['lifeExp'].agg(standardize, mean_whole = mean_global))
def print_max(col) : 
    return col.max()
tips = sns.load_dataset('tips')
print(tips.groupby('sex').apply(print_max))
exit()
print((tips.groupby('sex').apply(mean)))

