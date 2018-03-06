##################################################################################
#How old were the passengers? Calculate the average and median age of passengers.#
##################################################################################

import pandas
import numpy as np

#get data from a file
data = pandas.read_csv('titanic.csv', index_col='PassengerId')

#calculate
average = np.mean(data['Age'])
median_age = np.median(data['Age'].dropna())

#output result
print("Average is " + str(round(average, 2)) + ", median age is " + str(round(median_age, 2)))
