##############################################################################
#What part of the passengers managed to survive?                             #
#Calculate the percentage of surviving passengers, rounded to two characters.#
##############################################################################

import pandas

#get data from a file
data = pandas.read_csv('titanic.csv', index_col='PassengerId')

#calculate
amount_survived = data['Survived'].value_counts()[1]
amount_people = len(data['Survived'])
percentage_survived = amount_survived / amount_people * 100

#output result
print ("People survived: " + str(round(percentage_survived, 2)) + "%")