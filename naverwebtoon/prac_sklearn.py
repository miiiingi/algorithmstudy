from numpy.core.numeric import cross
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, VotingClassifier
from sklearn.metrics import roc_auc_score, f1_score
from sklearn.model_selection import cross_val_score
import pandas as pd
titanic = sns.load_dataset('titanic')
titanic = titanic.loc[titanic['age'].isnull() == False, :]
titanic_train = titanic.iloc[:500, :]
titanic_test = titanic.iloc[500:, :]
def count_missing(col) : 
    return sum(col.isnull())
y_tr = titanic_train['alive']
X_tr = titanic_train.drop('alive', axis = 1)
X_tr = pd.get_dummies(X_tr)
y_te = titanic_test['alive']
X_te = titanic_test.drop('alive', axis = 1)
X_te = pd.get_dummies(X_te)
print(X_tr)
print(y_tr)

rf = RandomForestClassifier()
ada = AdaBoostClassifier()
vot = VotingClassifier(estimators=[('rf' , rf), ('ada', ada)], voting = 'soft')
vot.fit(X_tr, y_tr)
predict = vot.predict_proba(X_te)[:, 1]
print(roc_auc_score(y_te, predict))

# print(cross_val_score(vot, X, y, cv = 5))