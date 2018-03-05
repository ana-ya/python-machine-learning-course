################################################
#How many men and women were traveling by ship?#
################################################

import pandas

#get data from a file
data = pandas.read_csv('titanic.csv', index_col='PassengerId')

#calculate
amount_sex = data['Sex'].value_counts()

#output result
print ("Men are " + str(amount_sex.male) + ", women are " + str(amount_sex.female))