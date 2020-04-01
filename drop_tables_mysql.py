import mysql.connector


db_conn = mysql.connector.connect(host="localhost", user="shaunt",
                                  password="Passw0rd", database="events")
db_cursor = db_conn.cursor()

db_cursor.execute('''
                  DROP TABLE scan_in, body_info
                  ''')

db_conn.commit()
db_conn.close()