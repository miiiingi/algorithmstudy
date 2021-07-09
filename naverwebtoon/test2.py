import pandas as pd
df = pd.read_csv('india-airquality.csv')
df = df.loc[df['pm2_5'].isnull() == False, :]
df.loc[df['pm2_5'] >= 76, 'rank'] = 'very bad' 
df.loc[(df['pm2_5'] >= 36) & (df['pm2_5'] < 76), 'rank'] = 'bad' 
df.loc[(df['pm2_5'] >= 16) & (df['pm2_5'] < 36), 'rank'] = 'usual' 
df.loc[df['pm2_5'] < 16, 'rank'] = 'good' 
counts = df['rank'].value_counts()
new_df = pd.DataFrame({'매우 나쁨' : [counts['very bad']], '나쁨' : [counts['bad']], '보통' : [counts['usual']],  '좋음' : [counts['good']]})
new_df = new_df.transpose()
new_df.columns = ['counts']
new_df.index.name = '예보 등급'
new_df.to_csv('finedust_count.csv', encoding='utf-8')
print(new_df)
# print(new_df)
# new_df = new_df.sort_values(by = new_df.index, axis = 1 )
# print(new_df)
# print(df.head())