import pandas as pd


# 0 Load
df = pd.read_csv("salary_data.csv")


# 1 Rename
df.columns = ['Name', 'Job', 'Department', 'Salary', 'Date']


# 2 Info and Apply
print df.info()
df['Salary'] = df['Salary'].str.strip('$').apply(float)
print df.info()


# 3 Top 5 Salaries
print df.groupby('Job').mean().sort_values('Salary', ascending=False).head()


# 4 Police
print len(df[df['Job'].str.contains('POLICE')])


# 5 What Percent of Police are Police Officers
print float(len(df[df['Job'] == 'POLICE OFFICER']))/len(df[df['Job'].str.contains('POLICE')])


# 6 People joined between 13th July, 2000 and 13th August, 2000
df['Date'] = pd.to_datetime(df['Date'])
date_df = df.set_index('Date').sort_index()
print date_df.ix['2000-07-13': '2000-08-13']
