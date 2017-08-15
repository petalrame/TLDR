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
        print ("Error: Not able to connect to the database")

def create_user_table():
    """Creates a Postgres table representing information about our users"""
    cur = conn.cursor()
    cur.execute('''CREATE TABLE Users
    (UserID INT PRIMARY KEY     NOT NULL,
    Username           TEXT    NOT NULL,
    Email            TEXT     NOT NULL,
    Taglist         TEXT[]);''')
    print("Table created successfully")
    conn.commit()
    conn.close()

def add_event(title, summary, tags):
    """Inserts a new event"""
    cur = conn.cursor()
    try:
        cur.execute("INSERT INTO" + table +
        "(TITLE,RANKING,SUMMARY,ARTICLES,TAGS )\
        VALUES (" + title + "," + null + "," + summary + "," + tags +")")
        print("Event added successfully")
    except:
        print("Error adding event to database")

def getRowById(id):
    """gets Row From database by ID"""
    cur = conn.cursor
    try:
        cur.execute("SELECT FROM" + "EventObjectList" + "WHERE ID =" + id)
    except:
        print("Error retreiving event id: " + id)

def getEventData(tag):
    cur = conn.cursor
    try:
        cur.execute("SELECT FROM" + "EventObjectList" + "WHERE TAG = " +tag)
    except:
        print("Error retrieving " + tag + " data")
