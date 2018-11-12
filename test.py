import psycopg2

dbname = "news"

db = psycopg2.connect(database=dbname)
c = db.cursor()
c.execute("Select * from articles;")
print (c.fetchall())
db.close()

