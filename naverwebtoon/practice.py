import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
scientists = pd.DataFrame(
    data = {
        'Occupation' : ['Chemist', 'Statistician', 'Chemist', 'Statistician'],
        'Born' : ['1920-07-25', '1876-06-13', '1995-07-22', '1995-07-22'],
        'Age' : [37, 61, 58, 47]
    },
    index = ['Rosaline Franklin', 'William Gosset', 'mingi', 'mingi2']
)
# print(scientists.iloc[0, :])
# print(scientists['Age'].isin([37]))
scientists = scientists.drop('mingi' , axis= 0) # index에 특정 이름을 정하면, drop method로도 삭제 가능 !
scientists.to_csv('scientists.csv')
scientists2 = pd.read_csv('scientists.csv', index_col= 'Unnamed: 0')