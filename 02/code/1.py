import pandas
import numpy as np
from sklearn.tree import DecisionTreeClassifier


#get data from a file
data = pandas.read_csv('titanic.csv', index_col='PassengerId')

name_cols = ['Pclass', 'Fare', 'Age', 'Sex']
# select columns by names
filtered_data = data.filter(items=name_cols)

def convert_sex(x):
     return 1 if x == 'male' else 0

#convert Sex to boolean
filtered_data['Sex'] = list(map(convert_sex, filtered_data['Sex']))

main_audience = data['Survived']

#remove empty data
data_without_nan = filtered_data.dropna()
main_audience = main_audience[data_without_nan.index.values]

#build Decision tree
clf = DecisionTreeClassifier(random_state=241)
classifier_data = clf.fit(data_without_nan, main_audience)
signs = classifier_data.feature_importances_

#get signs with max value
dictionary = dict(zip(name_cols, signs))
print (sorted(dictionary, key=dictionary.get, reverse=True)[:2])