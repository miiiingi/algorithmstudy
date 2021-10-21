import pandas as pd
person = pd.read_csv('doit_pandas/data/survey_person.csv')
site = pd.read_csv('doit_pandas/data/survey_site.csv')
survey = pd.read_csv('doit_pandas/data/survey_survey.csv')
visited = pd.read_csv('doit_pandas/data/survey_visited.csv')
visited_subset = visited.loc[[0, 2, 6], :]
o2o_merge = site.merge(visited_subset, left_on='name', right_on='site')
print(site)
print(visited)
print(o2o_merge)
