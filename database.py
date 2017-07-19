import psycopg2
global conn

def initialize_postgres():
    """ Connects to Postgres Database which contains all of the tables"""
    try:
        conn = psycopg2.connect(
            database="tldr",
            user = "tldrviewer",
            password = "Ram965",
            host = "localhost")
        except:
            print "Error: Not able to connect to the database"

def create_user_table():
    """Creates a Postgres table representing information about our users"""
    cur = conn.cursor()
    cur.execute('''CREATE TABLE Users
      (UserID INT PRIMARY KEY     NOT NULL,
      Username           TEXT    NOT NULL,
      Email            TEXT     NOT NULL,
      Taglist         TEXT[]);''')
      print ("Table created successfully")
      conn.commit()
      conn.close()

def create_aricle_list_table():
    """Creates a Postgres table representing our agregated list of articles"""

def create_event_object_list_table():
    """Creates a Postgres table representing event objects"""

def insert_into_table(table):
    """Inserts data into a table in the database"""
    cur = conn.cursor()
    cur.execute("INSERT INTO" + table +  "(ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (1, 'Paul', 32, 'California', 20000.00 )");

def delete():
    """Deletes from the database"""
    cur = conn.cursor()
    cur.execute("DELETE from Users where ID=2;")
    conn.commit
