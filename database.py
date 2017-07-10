import psycopg2
#TODO(Sam) Insert correct values in all these methods
global conn
def init():
    conn = psycopg2.connect(database="testdb", user = "postgres", password = "pass123", host = "127.0.0.1", port = "5432")
def create_table():
    cur = conn.cursor()
    cur.execute('''CREATE TABLE COMPANY
      (ID INT PRIMARY KEY     NOT NULL,
      NAME           TEXT    NOT NULL,
      AGE            INT     NOT NULL,
      ADDRESS        CHAR(50),
      SALARY         REAL);''')
      print ("Table created successfully")
      conn.commit()
      conn.close()

def insert():
    cur = conn.cursor()
    cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (1, 'Paul', 32, 'California', 20000.00 )");
def delete():
    cur.execute("DELETE from COMPANY where ID=2;")
    conn.commit
