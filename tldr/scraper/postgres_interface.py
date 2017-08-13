"""Provides an inteface for adding data to the article_object table."""
import psycopg2

# Connect to the table containing article_objects in article_database
conn = psycopg2.connect(database="article_database", user = "samwasserman",
                        password = "#Dowhile97")
