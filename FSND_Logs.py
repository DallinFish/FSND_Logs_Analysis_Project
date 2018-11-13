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

#****************************************************************

#Initializes db connection
dbname = "news"
db = psycopg2.connect(database=dbname)
c = db.cursor()

#Creates View that preps log table into joinable format and excludes extra data.
c.execute("create view newlog as select replace(path, '/article/','') as newpath, date(time) as newdate, status from log where path != '/' and status = '200 OK';")

#Query that joins newLog view & articles table for Q1 & stores in ans1
c.execute("Select articles.title, count(*) as num from newlog join articles on articles.slug = newlog.newpath group by articles.title order by num desc;")
ans1 = c.fetchall()
num_of_records = 3
topic = "Articles"

#Output of Results for Q1
i = 0
print("Top Most Popular {} of all time are:".format(topic))
while i < num_of_records:
    print("    {} -- {} views".format(ans1[i][0],ans1[i][1]))
    i += 1

#Query that joins newLog, articles, & authors tables for Q2 & stores in ans2
c.execute("Select newauthor.name, count(*) as num from newlog join (select authors.name, articles.slug from authors join articles on authors.id = articles.author) as newauthor on newauthor.slug = newlog.newpath group by newauthor.name order by num desc;")
ans2 = c.fetchall()
num_of_records = 4
topic = "Authors"

#Output of Results for Q2
i = 0
print("Top Most Popular {} of all time are:".format(topic))
while i < num_of_records:
    print("    {} -- {} views".format(ans2[i][0],ans1[i][1]))
    i += 1


c.execute("Create view Total_Count as select count(*) as num, date(time) as newdate from log group by newdate;")
c.execute("Create view Error_Count as select count(*) as num, date(time), as newdate from log where status != '200 OK' group by newdate;")
c.execute("Select Error_Count.num/Total_Count.num as Err_Percent, Total_count.newdate from Error_Count join Total_Count on Error_Count.newdate = Total_Count.newdate order by Err_Percent")

Print(c.fetchall())


db.close()
