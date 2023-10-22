import pandas as pd
import sqlite3
import os

# Define the folder path
folder_path = 'academy'

# Read CSV data
csv_file = os.path.join(folder_path, 'salary.csv')
db_file = os.path.join(folder_path, 'salary.db')

# Read CSV data
data = pd.read_csv(csv_file)

# Create an SQLite database connection
conn = sqlite3.connect(db_file)

# Write data to the SQLite database
data.to_sql('salary', conn, if_exists='replace', index=False)

# Commit and close the database connection
conn.commit()
conn.close()
