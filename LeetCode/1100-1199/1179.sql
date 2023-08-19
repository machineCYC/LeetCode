-- create table
Create table If Not Exists Department (id int, revenue int, month varchar(5))
Truncate table Department
insert into Department (id, revenue, month) values ('1', '8000', 'Jan')
insert into Department (id, revenue, month) values ('2', '9000', 'Jan')
insert into Department (id, revenue, month) values ('3', '10000', 'Feb')
insert into Department (id, revenue, month) values ('1', '7000', 'Feb')
insert into Department (id, revenue, month) values ('1', '6000', 'Mar')


--- query
SELECT A.id AS id,
    SUM(CASE WHEN A.month="Jan" THEN revenue ELSE NULL END) AS Jan_Revenue,
    SUM(CASE WHEN A.month="Feb" THEN revenue ELSE NULL END) AS Feb_Revenue,
    SUM(CASE WHEN A.month="Mar" THEN revenue ELSE NULL END) AS Mar_Revenue,
    SUM(CASE WHEN A.month="Apr" THEN revenue ELSE NULL END) AS Apr_Revenue,
    SUM(CASE WHEN A.month="May" THEN revenue ELSE NULL END) AS May_Revenue,
    SUM(CASE WHEN A.month="Jun" THEN revenue ELSE NULL END) AS Jun_Revenue,
    SUM(CASE WHEN A.month="Jul" THEN revenue ELSE NULL END) AS Jul_Revenue,
    SUM(CASE WHEN A.month="Aug" THEN revenue ELSE NULL END) AS Aug_Revenue,
    SUM(CASE WHEN A.month="Sep" THEN revenue ELSE NULL END) AS Sep_Revenue,
    SUM(CASE WHEN A.month="Oct" THEN revenue ELSE NULL END) AS Oct_Revenue,
    SUM(CASE WHEN A.month="Nov" THEN revenue ELSE NULL END) AS Nov_Revenue,
    SUM(CASE WHEN A.month="Dec" THEN revenue ELSE NULL END) AS Dec_Revenue
FROM Department AS A
GROUP BY A.id