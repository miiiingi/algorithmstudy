import pandas as pd
# melting
pew = pd.read_csv('doit_pandas/data/pew.csv')
pew_long = pd.melt(pew, id_vars='religion', var_name='income', value_name='count')
billboard = pd.read_csv('doit_pandas/data/billboard.csv')
billboard_long = pd.melt(billboard, id_vars=['year', 'artist', 'track', 'time', 'date.entered'], var_name='week', value_name='rating')

ebola = pd.read_csv('doit_pandas/data/country_timeseries.csv') 
ebola_long = pd.melt(ebola, id_vars=['Date', 'Day'])
variable_split = ebola_long.variable.str.split('_')
cases = variable_split.str.get(0)
number = variable_split.str.get(1)
ebola_long['cases'] = cases
ebola_long['number'] = number 

weather  = pd.read_csv('doit_pandas/data/weather.csv') 
weather_long = pd.melt(weather, id_vars=['id', 'year', 'month', 'element'], var_name='day', value_name='temp')
weather_tidy = weather_long.pivot_table(
    index=['id', 'year', 'month','day'],
    columns= 'element',
    values='temp',
    dropna=False
)
print(weather)
print(weather_long)
print(weather_tidy)
print(weather_tidy.iloc[:15, :])
weather_tidy = weather_tidy.reset_index()
