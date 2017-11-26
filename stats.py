import codecs

import json

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def getStats(df, column):
    print()
    print('-------------------------------------')
    print('{} stats'.format(column))
    print('-------------------------------------')
    average = df[column].mean()
    print ('The average is {}'.format(average))
    print()
    counts = df[column].value_counts()
    print('im counts', len(counts))
    rows, columns = df.shape

    for i in range(11):
        if i not in counts:
            print('no cases of {} score {} out of {}'.format(column, i, rows))
        else:
            percent = float(counts[i])*100/rows
            print('{} people have a {} of {} out of {} which is {}%'.format(counts[i], column, i, rows, int(percent)))
    total = 0
    for i in range(7,11):
        total += counts[i]

    print()
    print('{} total amount with 7 or greater {}'.format(total, column))

    print('Worse case figures ',counts[0])

metrics = ['Satisfaction', 'NPS','Issue Resolution']
#df = pd.read_json('survey.json')
dates = pd.date_range('20130101', periods=9000)
df = pd.DataFrame(np.random.random_integers(0, 10,size=(9000,3)), index=dates, columns=metrics)
 

print(df.head())

# for i in metrics:
#     getStats(df, i)

df.plot.bar()
plt.show()

#getting rows where value = 0 for metrics
sat = df[df[metrics[0]]==0]
nps = df[df[metrics[1]]==0]
issue = df[df[metrics[2]]==0]


print(sat.head())
print(nps.head())
print(issue.head())


#get top satisfaction rows
sat = df[df[metrics[0]].isin([7, 10])]
print(sat.head())


#get lower satisfaction rows
sat = df[df[metrics[0]].isin([0, 3])]
print(sat.head())

print(df.index.values)
