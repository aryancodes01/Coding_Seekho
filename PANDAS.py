"""
Pandas is a Python library used for:

📊 Data analysis
🧹 Data cleaning
🔍 Data exploration
📁 Reading/writing CSV, Excel, JSON, etc.
🔄 Data transformation
📈 Preparing data for Machine Learning

The main objects in Pandas are:

Series → 1-dimensional data
DataFrame → 2-dimensional table

Think of a DataFrame like an Excel spreadsheet



"""
import pandas as pd
import numpy as np 
s=pd.Series([[1,2],[3,5]])
print(s)
data= {"Name":["aryan","ashish"],
       "Age":["23","33"],
       "Marks":["90","40"]
         
         
         }
df=pd.DataFrame(data)
print(df)