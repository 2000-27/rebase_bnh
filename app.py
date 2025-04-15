import pandas as pd
from sqlalchemy import create_engine

# Load Excel
df = pd.read_excel('/home/python/Desktop/sudir code/Ayush_Regex.xlsx')

# DB config
engine = create_engine('postgresql+psycopg2://postgres:Java_123@localhost:5432/sukdeep')

# Write to DB
df.to_sql('ayush_regex', engine, if_exists='replace', index=False)

print("Data inserted successfully!")
print("new commit to dev b branch")