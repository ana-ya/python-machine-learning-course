######################################################################
#What percentage of first class passengers were among all passengers?#
######################################################################

import pandas

#get data from a file
data = pandas.read_csv('titanic.csv', index_col='PassengerId')

#calculate
amount_first_class = data['Pclass'].value_counts()[1]
amount_people = len(data['Survived'])
percentage = amount_first_class / amount_people * 100

#output result
print ("People from 1st class: " + str(round(percentage, 2)) + "%")