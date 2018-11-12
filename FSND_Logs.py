import psycopg2

#1. What are the most popular three articles of all time?
#Example:

#  Princess Shellfish Marries Prince Handsome" 1201 views
#  Baltimore Ravens Defeat Rhode Island Shoggoths 915 views
#  Political Scandal Ends In Political Scandal 553 views


#2. Who are the most popular article authors of all time?
#Example:

#  Ursula La Multa 2304 views
#  Rudolf von Treppenwitz 1985 views
#  Markoff Chaney  1723 views
#  Anonymous Contributor 1023 views


#3. On which days did more than 1% of requests lead to errors?

#  July 29, 2016 2.5% errors

dbname = "news"

db = psycopg2.connect(database=dbname)
c = db.cursor()
#Creating View that preps log table into joinable format and excludes extra data.
c.execute("create view newlog as select replace(path, '/article/','') as newpath, date(time) as newdate, status from log where path != '/' and status = '200 OK';")

#Queary that joins newlog view and articles table for Question 1 and stores in ans1
c.execute("Select articles.title, count(*) as num from newlog join articles on articles.slug = newlog.newpath group by articles.title order by num desc;")
ans1 = c.fetchall()


i = 0
print("1. Top Most Popular Articles of all time are:")
while i < 3:
    print("    {} -- {} views".format(ans1[i][0],ans1[i][1]))
    i += 1

c.execute("Select newauthor.name, count(*) as num from newlog join (select authors.name, articles.slug from authors join articles on authors.id = articles.author) as newauthor on newauthor.slug = newlog.newpath group by newauthor.name order by num desc;")
ans2 = c.fetchall()
print(ans2)

db.close()


