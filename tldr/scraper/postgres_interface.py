"""Provides an inteface for adding data to the article_object table."""
import psycopg2
conn = None


def connect():
    """Connect to article_database."""
    # Connect to the table containing article_objects in article_database
    try:
        conn = psycopg2.connect("dbname='article_database'\
                                user='samwasserman'\
                                host='localhost' password='#Dowhile97'")
        print("Connected")
    except:
        print "I am unable to connect to the database"


def insert(id, authors, url, content):
    """Insert data into column."""
    cur = conn.cursor()
    cur.execute("INSERT INTO \"article_objects\" \
                VALUES (" + str(id) + ",'" + authors + "','"
                + url + "','" + content + "');")
    conn.commit()
    print ("Records created successfully")
    conn.close()
