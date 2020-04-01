import sqlite3

conn = sqlite3.connect('records.sqlite')

c = conn.cursor()
c.execute('''
          CREATE TABLE scan_in
          (id INTEGER PRIMARY KEY ASC, 
           member_id VARCHAR(250) NOT NULL,
           store_id VARCHAR(250) NOT NULL,
           timestamp VARCHAR(100) NOT NULL,
           date_created VARCHAR(100) NOT NULL)
          ''')

c.execute('''
          CREATE TABLE body_info
          (id INTEGER PRIMARY KEY ASC, 
           member_id VARCHAR(250) NOT NULL,
           store_id VARCHAR(250) NOT NULL,
           weight INTEGER NOT NULL,
           body_fat INTEGER NOT NULL,
           timestamp VARCHAR(100) NOT NULL,
           date_created VARCHAR(100) NOT NULL)
          ''')

conn.commit()
conn.close()