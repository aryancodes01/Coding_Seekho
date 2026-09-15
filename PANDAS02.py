import pandas as pd
import numpy as np

data = {
    "Name": ["Aryan", "Rahul", "Priya", "Aman", "Neha", "Riya", "Karan", "Sneha", "Vikas", None],
    "Age": [20, 21, np.nan, 22, 20, None, 23, 21, 22, 24],
    "Marks": [85, 90, 78, np.nan, 88, 92, None, 76, 95, 89],
    "City": ["Lucknow", "Delhi", None, "Kanpur", "Agra", "Lucknow", "Delhi", "Agra", None, "Kanpur"]
}

df = pd.DataFrame(data)
print(df.dropna(subset=['Name']))# this is most important
print(df['Name'].fillna('LUND'))
