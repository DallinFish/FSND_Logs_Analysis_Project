# FSND_Logs_Analysis_Project


This is a reporting program for the Full-Stack-Nanodegree Course. It answers The following three Questions in the format seen below in the examples. You will need to have your environment setup per the course instructions.

### Questions from the course

  1. What are the most popular three articles of all time? Which articles have been accessed the most? Present this information as a sorted list with the most popular article at the top.

  Example:

    * "Princess Shellfish Marries Prince Handsome" — 1201 views
    * "Baltimore Ravens Defeat Rhode Island Shoggoths" — 915 views
    * "Political Scandal Ends In Political Scandal" — 553 views

  2. Who are the most popular article authors of all time? That is, when you sum up all of the articles each author has written, which authors get the most page views? Present this as a sorted list with the most popular author at the top.

  Example:

    * Ursula La Multa — 2304 views
    * Rudolf von Treppenwitz — 1985 views
    * Markoff Chaney — 1723 views
    * Anonymous Contributor — 1023 views

  3. On which days did more than 1% of requests lead to errors? The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser. (Refer to this lesson for more information about the idea of HTTP status codes.)

  Example:

    * July 29, 2016 — 2.5% errors

## Quickstart

Assuming you have pulled down the files from the repo and are in the environment per the course, run the following command from the terminal:

```python
python FSND_Logs.py
```

This will display the results to the three questions.


## Structure & Design

### Questions 1 & 2

For Questions 1 and 2, I needed to join both the articles & log tables. In the log table the column path was similar to the slug used in the articles table but also contained the entire path of the article. I created a view that removed the /article/ portion of the path so that then articles table would then be able to join the log table. I also removed extra entries to the home page and 404 errors that weren't needed to answer the questions.

'''
"Create view newlog as "
  "Select replace(path, '/article/','') as newpath, "
  "date(time) as newdate, "
  "status "
  "from log "
  "where path != '/' and status = '200 OK';"
'''

### Question 3

For Question 3 I needed to be able to know the total count of errors and total count of requests for a given day. To make things easy to keep track of I created two views and then joined the two views for a final query.

**Total Count**
'''
"Create view Total_Count as "
  "Select count(status) as num, "
  "date(time) as newdate "
  "from log "
  "group by newdate;
'''

**Error Count**
'''
  "Create view Error_Count as "
    "Select count(status) as num, "
    "date(time) as newdate "
    "from log "
    "where status != '200 OK' group by newdate;"
'''

## License

The content of this repository is licensed under a [MIT License](https://choosealicense.com/licenses/mit/)
