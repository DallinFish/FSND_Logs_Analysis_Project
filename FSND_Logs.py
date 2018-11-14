import psycopg2

# Initializes db connection
dbname = "news"
db = psycopg2.connect(database=dbname)
c = db.cursor()


# Creates joinable view for the log table & excludes extra data
c.execute(
    "Create view newlog as "
    "Select replace(path, '/article/','') as newpath, "
    "date(time) as newdate, "
    "status "
    "from log "
    "where path != '/' and status = '200 OK';")

# Query that joins newLog view & articles table for Q1 & stores in ans1
c.execute(
    "Select articles.title, "
    "count(*) as num "
    "from newlog "
    "join articles on articles.slug = newlog.newpath "
    "group by articles.title "
    "order by num desc;")
ans1 = c.fetchall()

# Output of Results for Q1
num_of_records = 3
topic = "Articles"
i = 0
print("Top Most Popular {} of all time are:".format(topic))
while i < num_of_records:
    print("    {} -- {} views".format(ans1[i][0], ans1[i][1]))
    i += 1


# Query that joins newLog, articles, & authors tables for Q2 & stores in ans2
c.execute(
    "Select newauthor.name, "
    "count(*) as num "
    "from newlog "
    "join "
        "(select authors.name, "
        "articles.slug "
        "from authors "
        "join articles "
        "on authors.id = articles.author) "
        "as newauthor "
    "on newauthor.slug = newlog.newpath "
    "group by newauthor.name "
    "order by num desc;")
ans2 = c.fetchall()

# Output of Results for Q2
num_of_records = 4
topic = "Authors"
i = 0
print("Top Most Popular {} of all time are:".format(topic))
while i < num_of_records:
    print("    {} -- {} views".format(ans2[i][0], ans2[i][1]))
    i += 1


# Creates Views for Total Errors & Requests & Queries for day over 1.1% Errors
c.execute(
    "Create view Total_Count as "
    "Select count(status) as num, "
    "date(time) as newdate "
    "from log "
    "group by newdate;")
c.execute(
    "Create view Error_Count as "
    "Select count(status) as num, "
    "date(time) as newdate "
    "from log "
    "where status != '200 OK' group by newdate;")
c.execute(
    "Select Total_count.newdate, "
    "round(Error_Count.num * 1.0 / Total_Count.num * 100.0, 2) as Err_Percent "
    "from Error_Count "
    "join Total_Count "
    "on Error_Count.newdate = Total_Count.newdate "
    "where (Error_Count.num * 1.0 / Total_Count.num * 100.0) > 1.1 "
    "order by Err_Percent desc")
ans3 = c.fetchall()

# Output of Results for Q3
num_of_records = 1
i = 0
print("The Day with the Most Errors was:".format(topic))
while i < num_of_records:
    print("    {} -- {} % Errors".format(ans3[i][0], ans3[i][1]))
    i += 1

db.close()
