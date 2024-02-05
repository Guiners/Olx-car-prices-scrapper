import sqlite3

conn = sqlite3.connect('database.sqlite')
cur = conn.cursor()

conn.execute('''CREATE TABLE RobE36
                (DATE BOLD,
                AVERAGE  REAL,
                MIN REAL,
                MAX REAL,
                AUCTIONS REAL     
                );''')
conn.commit()

conn.close()