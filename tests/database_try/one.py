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

# data structure
# date, BLOB. The value is a blob of data, stored exactly as it was input.
# average, REAL. The value is a floating point value, stored as an 8-byte IEEE floating point number.
# min, REAL. The value is a floating point value, stored as an 8-byte IEEE floating point number.
# max, REAL. The value is a floating point value, stored as an 8-byte IEEE floating point number.
# auctions INTEGER. The value is a signed integer, stored in 1, 2, 3, 4, 6, or 8 bytes depending on the magnitude of the value.
