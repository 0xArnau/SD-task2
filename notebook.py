import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

def database():

    #read the CSV
    df = pd.read_csv('data.csv')
    #connect to a database
    conn = sqlite3.connect("Any_Database_Name.db") #if the db does not exist, this creates a Any_Database_Name.db file in the current directory
    df.to_sql('table1', conn)
    date = pd.read_sql_query("SELECT date from table1", conn)['date'].to_string()
    sentiment_analysis = pd.read_sql_query("SELECT sentiment_analysis from table1", conn)['sentiment_analysis'].to_string()
    conn.close()

    date = date.split()
    data = []
    i = 0
    for x in date:
          if i % 2 == 0:
            next
          else:
            data.append(x)
          i += 1

    return data, sentiment_analysis


def create_plot():

    pass


if __name__ == "__main__":
    database()


