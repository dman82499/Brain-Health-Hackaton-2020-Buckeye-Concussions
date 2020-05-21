#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 10:21:09 2020

@author: ta2909
"""
import pandas as pd
import sqlite3

path='./data/'
#con = sqlite3.connect(path+'chinook.db')

# Read sqlite query results into a pandas DataFrame
con = sqlite3.connect(path+"portal_mammals.sqlite",timeout=1)
cur = con.cursor() # The cursor

# The result of a "cursor.execute" can be iterated over by row
for row in cur.execute('SELECT * FROM species;'):
    print(row)
    
# Return all results of query
cur.execute('SELECT plot_id FROM plots WHERE plot_type="Control"')
cur.fetchall()

# Return first result of query
cur.execute('SELECT species FROM species WHERE taxa="Bird"')
cur.fetchone()
    
#Read as pandas df
surveys_df = pd.read_sql_query("SELECT * from surveys", con)

# Verify that result of SQL query is stored in the dataframe
print(surveys_df.head())

# Select only data for 2002
surveys2002 = surveys_df[surveys_df.year == 2002]

# Write the new DataFrame to a new SQLite table
surveys2002.to_sql("surveys2002", con, if_exists="replace")

con.close()
