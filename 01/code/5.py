################################################################################################
#Do the number of brothers / sisters / spouses correlate with the number of parents / children?#
#Calculate the Pearson correlation between the SibSp and Parch attributes.                     #
################################################################################################

import pandas
from scipy.stats.stats import pearsonr

#get data from a file
data = pandas.read_csv('titanic.csv', index_col='PassengerId')

#calculate
pearson_corr = pearsonr(data['SibSp'], data['Parch'])
#OR
pearson_corr = data['SibSp'].corr(data['Parch'])

#output result
print ("Pearson correlation is",  round(pearson_corr, 2))
