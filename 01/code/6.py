#####################################################################################################
#What is the most popular female name on the ship? Extract from the full name                       #
# of the passenger (column Name) his personal name (First Name).                                    #
# This task is a typical example of what a data analysis specialist faces.                          #
# The data is very heterogeneous and noisy, but they need to extract the necessary information.     #
# Try to manually parse several values of the Name column and work out a rule for extracting names, #
# as well as dividing them into female and male names.                                              #
#####################################################################################################

import pandas
import re
from collections import Counter

#get data from a file
data = pandas.read_csv('titanic.csv', index_col='PassengerId')


def getNames(names):
    women = []
    for name in names:
        match = re.search('.*, (.*)', name)
        if match:
            name = match.group(1)

        match = re.search('\((.*)\)', name)
        if match:
            name = match.group(1)

        name = re.sub('(Miss\. |Mrs\. |Ms\.)', '', name)

        name = name.split(' ')[0].replace('"', '')

        if len(name) > 0:
            women.append(name)

    return women

name_counts = getNames(data[data['Sex'] == 'female']['Name'])

print(Counter(name_counts).most_common(1))