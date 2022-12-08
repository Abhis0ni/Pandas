#Introduction
#Pandas is an open-source library that is made mainly for working with relational or labeled data both easily and intuitively.
#It provides various data structures and operations for manipulating numerical data and time series. Pandas is fast and it has high performance & productivity for users.

#Advantages
#1) Fast and efficient for manipulating and analyzing data.
#2) Data from different file objects can be loaded.
#3) Easy handling of missing data (represented as NaN) in floating point as well as non-floating point data
#4) Size mutability: columns can be inserted and deleted from DataFrame and higher dimensional objects
#5) Data set merging and joining.
#6) Flexible reshaping and pivoting of data sets
#7) Provides time-series functionality.
#8) Powerful group by functionality for performing split-apply-combine operations on data sets.

# installing pandas
# write code in terminal --> pip install pandas/!pip install pandas(in case of Jupyter)

import pandas as pd   # importing pandas

#Pandas as two major datatypes:
#1)Series
#2)Dataframe

L = [100,200,300,400]
L1 = [[1,2,3],['A','B','C']]
Ser = pd.Series(L)        
Ser1 = pd.Series(L1)
print(Ser)
print(Ser1)
print(type(Ser1))         # Series


Df = pd.DataFrame(L)      
Df1 = pd.DataFrame(L1)
print(Df)
print(Df1)
print(type(Df1))          # Dataframe


# Reading data from pandas
p = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")
print(p)

# select top rows
print(p.head())    # top 5 rows
print(p.head(10))  # top 10 rows

# select last rows
print(p.tail())     # last 5 rows
print(p.tail(10))   # last 10 rows

# checking column datatypes
print(p.dtypes)

# getting insights of datatype
print(p.describe())

# shape of dataframe
print(p.shape)

# selecting column from dataframe
print(p.Name)
print(p['Name'])
print(p[['Name','Age','Sex']])

# selecting unique values from column
print(p['Pclass'].unique())

# selecting row using index (both returns same rows)
print(p.loc[100])
print(p.iloc[100])

# change index to PassengerId
p.set_index('PassengerId',inplace = True)  # to make changes on original dataset use inplace
print(p)
print(p.loc[100])   #using new index
print(p.iloc[100])  #using earlier default index (both returns different rows)

#checking missing values
print(p.isnull())

# checking the total number of missing values
print(p.isnull().sum())

#creating new column
p['New']=p['Survived']+p['Pclass']
print(p)


#Droping new column
#p.drop('New')   # will give error need to pass axis=1
p.drop('New',axis=1)
print(p)
p.drop('New',axis=1,inplace=True)
print(p)




data1 = {'Name':['Jai', 'Anuj', 'Jai', 'Princi',
                 'Gaurav', 'Anuj', 'Princi', 'Abhi'],
        'Age':[27, 24, 22, 32,
               33, 36, 27, 32],
        'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj',
                   'Jaunpur', 'Kanpur', 'Allahabad', 'Aligarh'],
        'Qualification':['Msc', 'MA', 'MCA', 'Phd',
                         'B.Tech', 'B.com', 'Msc', 'MA']}

print(data1)
df = pd.DataFrame(data1)
print(df)

# GroupBy 
g = df.groupby('Name')
# similarly for multiple groupby columns
#g = df.groupby(['Name','Qualification'])

print(g.groups) 
for i in g:
    print(i)


print(g.first())  # print first set of records in groupby
print(g.last())   # print last set of records in groupby

print(g.sum())


# Merging two dataframes
data1 = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'], 
        'Age':[27, 24, 22, 32], 
        'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'], 
        'Qualification':['Msc', 'MA', 'MCA', 'Phd']} 

 
data2 = {'Name':['Abhi', 'Ayushi', 'Dhiraj', 'Hitesh'], 
        'Age':[17, 14, 12, 52], 
        'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'], 
        'Qualification':['Btech', 'B.A', 'Bcom', 'B.hons']} 

# Convert the dictionary into DataFrame  
df = pd.DataFrame(data1,index=[0, 1, 2, 3])
df1 = pd.DataFrame(data2,index=[4,5,6,7])
print(df)
print(df1)

#concatenating 
Frames = [df,df1]
Concate = pd.concat(Frames)
print(Concate)
