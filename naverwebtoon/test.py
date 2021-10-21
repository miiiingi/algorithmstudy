import pandas as pd
df = pd.read_csv('india-airquality.csv')
df = df.loc[df['pm2_5'].isnull()==False, :]
df.loc[df['pm2_5']<16, 'rank'] = 1
df.loc[(df['pm2_5']>=16) & (df['pm2_5']<36), 'rank'] = 2
df.loc[(df['pm2_5']>=36) & (df['pm2_5']<76), 'rank'] = 3 
df.loc[df['pm2_5']>=76, 'rank'] = 4
result = pd.DataFrame({'예보등급' : ['매우나쁨', '나쁨', '보통', '좋음'], 'count' : [df['rank'].value_counts()[4], df['rank'].value_counts()[3],df['rank'].value_counts()[2] ,df['rank'].value_counts()[1]]})
result = result.set_index('예보등급')
result.to_csv('finedust_count.csv')