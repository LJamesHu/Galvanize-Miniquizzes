import pandas as pd

df = pd.read_csv('data1.tsv', '\t')

print df.describe()

#                custid         income health.ins  num.vehicles          age
# count     1000.000000    1000.000000       1000    944.000000  1000.000000
# mean    698499.702000   53504.771000      0.841      1.916314    51.699815
# std     413508.277399   65478.065729   0.365859      1.101618    18.863433
# min       2068.000000   -8700.000000      False      0.000000     0.000000
# 25%     345666.750000   14600.000000          1      1.000000    38.000000
# 50%     693403.000000   35000.000000          1      2.000000    50.000000
# 75%    1044606.250000   67000.000000          1      2.000000    64.000000
# max    1414286.000000  615000.000000       True      6.000000   146.680197

# num.vehicles is missing 56 entries.
# The max age being 146.68 is very unlikely. Min age being 0 is also unlikely.
# Min income being -8700 is possible, but unlikely.

print df.info()

# Many nulls in is.employed.
# 944 in housing.type, recent.move and num.vehicles (missing 56)

# Can probably ignore housing.type, recent.move, num.vehicles or set to 0.
# Have to reinterpret nulls in is.employed to not being employed. There are over 300 nulls for is.employed. They should be represented as 0s.

# The outliers in the age column are particularly relevant with an age of 0 and an age of 146.68, both clearly being wrong.

print df.sort('age')['age'].unique()

# After doing some deeper looking in, the ages over 100 have very specific decimal numbers which makes it look like there was possibly some mistake somewhere.

print df.sort('income')['income'].unique()

# As for income, only one is negative.