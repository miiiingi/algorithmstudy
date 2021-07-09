import pandas as pd
import collections
df = pd.read_csv('austine-incidents.csv').sort_values(by=['timestamp'], axis = 0)
# for ind in range(df.shape[0]) : 
#     df.loc[ind == ind, 'new_timestamp'] = pd.to_datetime(df.iloc[ind, -1])
df['timestamp'] = pd.to_datetime(df.loc[:, 'timestamp'])
durationlist = collections.deque([])
durationlist_ = [] 
for ind in range(df.shape[0]) : 
    if ind == 0 :
        durationlist.append(0)
    else : 
        durationlist.append(df.iloc[ind, -1] - df.iloc[ind-1, -1])
for ind, d in enumerate(durationlist): 
    if ind == 0 :
        durationlist_.append(0)
        continue
    day = d.days
    seconds = d.seconds
    durationlist_.append(day * 24 * 60 + seconds // 60)
df['duration'] = durationlist_
# df['duration'] = durationlist
# days = df['duration'][0].seconds
# print(days)
# print(days, hours, minutes)
exit()
print(df.head())
exit()
print(df.iloc[1, -1] -df.iloc[0, -1])
exit()
df.loc['new_timestamp'] = pd.to_datetime(df.iloc[:, -1])
print(df.head())