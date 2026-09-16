import pandas as pd
import numpy as np

data = {
    "Name": ["Aryan", "rahul", "priya", "Aman", "Neha"],
    "Age": [20, 21, 21, 22, 24],
    "Marks": [85, 90, 78, 88, 92]
}

df = pd.DataFrame(data)
df['Name']=df['Name'].apply(str.title)#first letter capital me badal de rha tha 
print(df)
