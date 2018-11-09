import psycopg2

#1. What are the most popular three articles of all time?
#Example:

#  "Princess Shellfish Marries Prince Handsome" — 1201 views
#  "Baltimore Ravens Defeat Rhode Island Shoggoths" — 915 views
#  "Political Scandal Ends In Political Scandal" — 553 views


#2. Who are the most popular article authors of all time?
#Example:

#  Ursula La Multa — 2304 views
#  Rudolf von Treppenwitz — 1985 views
#  Markoff Chaney — 1723 views
#  Anonymous Contributor — 1023 views


#3. On which days did more than 1% of requests lead to errors?

#  July 29, 2016 — 2.5% errors

#NOTES:
#select select replace(log.path,'/article/','') as path
dbname = news

db = psycopg2.connect(database=dbname)
c = db.cursor()
c.execute("create view newlog as
select replace(log.path, '/article/','') as newpath, log.time, log.status,
from log;")
c.fetchall()
db.close()


"""
def get_posts():

  db = psycopg2.connect(database=DBNAME)
  c = db.cursor()
  c.execute("select content, time from posts order by time desc")
  posts = c.fetchall()
  db.close()
  return posts

def add_post(content):

  db = psycopg2.connect(database=DBNAME)
  c = db.cursor()
  c.execute("insert into posts values (%s)", (bleach.clean(content),))  # good
  db.commit()
  db.close()
"""
