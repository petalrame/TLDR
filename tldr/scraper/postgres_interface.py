"""Provides an interface for adding data to the article_object table."""
import psycopg2
connection_str = "dbname='article_database'\
                        user='samwasserman'\
                        host='localhost' password='#Dowhile97'"
conn = psycopg2.connect(connection_str)


def insert(authors, url, content):
    """Insert data into column. PARAMETERS: (unique id for postgres, etc.)"""
    print("Inserting into DB")
    cur = conn.cursor()
    cur.execute("INSERT INTO article_objects VALUES(" + "\'" + authors + "','" + url + "','" + content + "')");
    conn.commit()
    print ("Records created successfully")
    conn.close()
