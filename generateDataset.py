import codecs
import json
import image
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
    rows, columns = df.shape

    for i in range(11):
        if i not in counts:
            print('no cases of {} score {} out of {}'.format(column, i, rows))
        else:
            percent = float(counts[i])*100/rows
            print('{} people have a {} of {} out of {} which is {}%'.format(counts[i], column, i, rows, int(percent)))
    total = 0
    # for i in range(8,11):
    #     total += counts[i]

    # print()
    # print('{} total amount with 7 or greater {}'.format(total, column))

    # print('Worse case figures ',counts[0])



def getText(df):
    print()
    print('-------------------------------------')
    print('Text')
    print('-------------------------------------')
    print(df['Text'])


metrics = ['Satisfaction', 'NPS','Issue Resolution']
#df = pd.read_json('survey.json')
dates = pd.date_range('20130101', periods=9000)

data = {'Satisfaction': [10, 7, 5, 1], 
        'NPS': [8, 8, 5, 2],
        'Issue Resolution': [7, 8, 4, 3] ,
        'Text': ['some great text', 'some more great text', 'some ok text', 'some bad text']}

df = pd.DataFrame(data, index=['a', 'b','c','d'])
# {'points':90, 'time': '9:00', 'month': 'january'}, 
# {'points_h1':20, 'month': 'june'}


print(df)


#first graph summmary
ax = df.plot.line()
fig = ax.get_figure()
fig.savefig('test.png')

plt.show()


# print(df.head())

for i in metrics:
    getStats(df, i)

# #getting rows where value = 0 for metrics
#sat = df[df[metrics[0]]>=7 ][ df[metrics[1]]>=7]

#getting high scores
high = df[(df[metrics[0]]>=7) | (df[metrics[1]]>=7) | (df[metrics[2]]>=7)]

#getting medium scores for sat
med = df[(df[metrics[0]]>3) & (df[metrics[0]]<7)]


#getting low scores
low = df[(df[metrics[0]]<=3) | (df[metrics[1]]<=3) | (df[metrics[2]]<=3)]


nps = df[df[metrics[1]]==8]
issue = df[df[metrics[2]]==3]


# print(sat.head())
# print()
# print(nps.head())
# print()
# print(issue.head())

print('this is the high scores')
print(high)

# high.plot.bar()
# plt.show()

# high.plot.line()
# plt.show()

print()
print('this is the medium scores')
print(med)
print()
print('this is the low scores')
print(low)
#getText(sat)

# #get top satisfaction rows
# sat = df[df[metrics[0]].isin([7, 10])]
# print(sat.head())


# #get lower satisfaction rows
# sat = df[df[metrics[0]].isin([0, 3])]
# print(sat.head())

# print(df.index.values)
