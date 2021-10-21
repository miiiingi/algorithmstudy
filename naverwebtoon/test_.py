import pandas as pd
dataset = pd.read_csv('india-airquality.csv')
dataset = dataset.loc[dataset['pm2_5'].isnull() == False, :]
dataset.loc[(10 <= dataset['pm2_5'] ) & (dataset['pm2_5'] <= 20), 'rank'] = "나쁨"
dataset.loc[(20 < dataset['pm2_5'] ) & (dataset['pm2_5'] <= 40), 'rank'] = "개나쁨" 
dataset.loc[(40 < dataset['pm2_5'] ) & (dataset['pm2_5'] <= 80), 'rank'] = "매우나쁨" 
dataset.loc[(80 < dataset['pm2_5'] ), 'rank'] = "최악" 
result = pd.DataFrame({'예보등급' : ['나쁨', '개나쁨', '매우나쁨', '최악'], 'count' : [dataset['rank'].value_counts()[2], dataset['rank'].value_counts()[0], dataset['rank'].value_counts()[1], dataset['rank'].value_counts()[3]]})
result = result.set_index('예보등급')
print(result)
exit()