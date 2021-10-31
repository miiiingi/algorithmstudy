from os import terminal_size
import pandas as pd
df1 = pd.read_csv('doit_pandas/data/concat_1.csv')
df2 = pd.read_csv('doit_pandas/data/concat_2.csv')
df3 = pd.read_csv('doit_pandas/data/concat_3.csv')
df3.columns = ['A', 'B', 'E', 'F']
row_concat = pd.concat([df1, df2], axis = 0)
row_new = pd.DataFrame(data = {
    'A' : ['n1'],
    'B' : ['n2'],
    'C' : ['n3'],
    'D' : ['n4']
})
row_concat = pd.concat([row_concat, row_new], ignore_index = False)
print(row_concat)