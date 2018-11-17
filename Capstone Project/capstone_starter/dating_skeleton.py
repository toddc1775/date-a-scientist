import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


#Create your df here:
df = pd.read_csv("profiles.csv")

df2 = df[['age','drugs']]

##### FORMUlATE THE QUESTION ####
#Can we predict which age group uses drugs often?

##### Explore the Data
#df2.head()
#print(df2.age)
#print(df2.drugs)
#print(df2.age.unique(), df2.drugs.unique())

##### Find the total number of missing values...NaN.
#null_counts = df2.isnull().sum()
#print("Number of null values in each column:\n{}".format(null_counts))

##### Remove the NaN from the drugs column.
#df2.dropna(subset = ['drugs']) for some reason this doesn't work.

### replace "NaN" with "Unknown" and then remove that data.
df2.drugs.fillna("UNKNOWN",inplace=True)

df2 = df2[(df2[['drugs']] !="UNKNOWN").all(axis=1)]
df2 = df2[(df2[['drugs']] !="never").all(axis=1)]
df2 = df2[(df2[['drugs']] !="sometimes").all(axis=1)]
#print(df2.drugs.unique())



df2['age'].hist(bins=[20,30,40,50,60,70])


plt.style.use('ggplot')

plt.bar(df2.age,df2.drugs, color='green')

plt.xlabel("Age Groups")
plt.ylabel("Uses Drugs Often")


plt.show()


##### transform drugs column into numerical data.
#drug_map = {"never": 0, "sometimes":1, "offten":2}




