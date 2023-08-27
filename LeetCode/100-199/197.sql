-- create table
Create table If Not Exists Weather (id int, recordDate date, temperature int)
Truncate table Weather
insert into Weather (id, recordDate, temperature) values ('1', '2015-01-01', '10')
insert into Weather (id, recordDate, temperature) values ('2', '2015-01-02', '25')
insert into Weather (id, recordDate, temperature) values ('3', '2015-01-03', '20')
insert into Weather (id, recordDate, temperature) values ('4', '2015-01-04', '30')


--- query
SELECT A.id AS id
FROM Weather AS A
LEFT JOIN (
    SELECT DATE_ADD(recordDate, INTERVAL 1 DAY) AS recordDate,
        temperature
    FROM Weather
) AS B
ON A.recordDate=B.recordDate
WHERE A.temperature>B.temperature