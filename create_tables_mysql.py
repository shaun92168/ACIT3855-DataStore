import mysql.connector


db_conn = mysql.connector.connect(host="acit3855-shaun.westus2.cloudapp.azure.com", user="shaun",
                                  password="shaun", database="events", port="3306")
db_cursor = db_conn.cursor()

db_cursor.execute('''
    CREATE TABLE scan_in
    (id INT NOT NULL AUTO_INCREMENT,
     member_id VARCHAR(250) NOT NULL,
     store_id VARCHAR(250) NOT NULL,
     timestamp VARCHAR(100) NOT NULL,
     date_created VARCHAR(100) NOT NULL,
     CONSTRAINT scan_in_pk PRIMARY KEY (id))''')

db_cursor.execute('''
    CREATE TABLE body_info
    (id INT NOT NULL AUTO_INCREMENT,
     member_id VARCHAR(250) NOT NULL,
     store_id VARCHAR(250) NOT NULL,
     weight INTEGER NOT NULL,
     body_fat INTEGER NOT NULL,
     timestamp VARCHAR(100) NOT NULL,
     date_created VARCHAR(100) NOT NULL,
     CONSTRAINT body_info_pk PRIMARY KEY (id))''')

db_conn.commit()
db_conn.close()