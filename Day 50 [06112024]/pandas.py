# -*- coding: utf-8 -*-
"""Pandas.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1znM0Qp3D2M6Z1CbKdA234wsouSlS6esN
"""

pip install pandas

import pandas as pd
import numpy as np

#Remove warnings

import warnings
warnings.filterwarnings('ignore')

"""## Pandas Series"""

info = np.array(['A','B','C','D','E','F'])
a = pd.Series(info)
print(a)

info = {'x':0,'y':1,'z':2}
a = pd.Series(info)
print(a)

arr = [1,2,3,4]
index = ['a','b','c','d']
x = pd.Series(arr,index)
print(x)

print(x[3])
print(x.index)
print(x.values)
print(x.dtype)
print(x.size)
print(x.shape)
print(len(x))

a = pd.Series(data = [1,2,3,np.nan], index = [0,1,2,3])
print(a)
print(a.hasnans)

"""## DataFrame"""

df = pd.DataFrame()
print(df)

x = ['Python','Pandas']

df = pd.DataFrame(x)
df

info = {'ID':[101,102,103,104,105],'Department':['MEC','CEC','MPC','BIPC',np.nan]}

df = pd.DataFrame(info)
df

emp = ['Parker','John','Smith','William']
id = [102,107,109,111]

emp_series = pd.Series(emp)
id_series = pd.Series(id)

a = {'Emp':emp_series, 'ID':id_series}
df = pd.DataFrame(a)
df

info = {'One':pd.Series([1,2,3,4,5,6,7], index=['a','b','c','d','e','f','g']),
       'Two': pd.Series([1,2,3,4,5,6,7,8],index = ['a','b','c','d','e','f','g','h'])}

df = pd.DataFrame(info)
df

df['Two']

df['Three'] = df['One'] + df['Two']
df

del df['One']
df

"""# loc and iloc"""

data = pd.Series(['a','b','c','d'], index = [1,3,5,7])
print(data)
print(data.loc[1])
print(data.iloc[1])

data = pd.Series(['a','b','c','d'], index = [1,3,5,7])
print(data)
print('**************************************')

print('loc values') # it will take manually generated index values
print(data.loc[1])
print(data.loc[3])
print(data.loc[5])
print(data.loc[7])
print('**************************************')

print('iloc values') # it will take original index values
print(data.iloc[0])
print(data.iloc[1])
print(data.iloc[2])
print(data.iloc[3])
print('**************************************')
print(data.loc[1:7])
print(data.iloc[0:3])

data = {"Name":['A','B','C','D'],'Age':['25','21','62','41']}
df = pd.DataFrame(data)
print(df.dtypes)
df

#astype --> convert one datatype into another datatype

df['Age'] = df['Age'].astype(int)
print(df.dtypes)
df

df.describe()

data = {'Name':['A','B',np.nan,'D'], 'Age':[25,np.nan,62,41]}
df = pd.DataFrame(data)
df

df.describe()

df1 = df.dropna()
df1

df1 = df.fillna(0)
df1

data = {"Name":['A','B','C','D'],'Age':[25,21,62,41]}
df = pd.DataFrame(data)
df
df['Age'].replace(25,30, inplace=True)
df

"""#   Wroking with CSV files
    #open empty Excel file
    #Click on file -> Save as -> (Choose the location of the current .py file)
    #Create a file name & choose the type as CSV (comma delimited)
    #Enter some values in the file
"""

df = pd.read_csv('Book1.csv')
df

df.head() #generates first 5 rows

df.tail() #generates lsat five rows

df

df.iloc[2]

df.describe(include = 'all')

df.SALARY.value_counts()

df

df.apply(np.max)

df.apply(np.min)

df

df.set_index('SALARY')

df

df.sort_values(by = 'AGE')

# unique

df['SALARY'].unique()

df[1:4]

new_df = df[['NAME','AGE']]
new_df

df

df.loc[df.SALARY == 20000]

df

df.loc[(df.AGE > 22) & (df.SALARY > 10000),["NAME","AGE"]]