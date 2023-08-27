-- create table
Create table If Not Exists MyNumbers (num int)
Truncate table MyNumbers
insert into MyNumbers (num) values ('8')
insert into MyNumbers (num) values ('8')
insert into MyNumbers (num) values ('3')
insert into MyNumbers (num) values ('3')
insert into MyNumbers (num) values ('1')
insert into MyNumbers (num) values ('4')
insert into MyNumbers (num) values ('5')
insert into MyNumbers (num) values ('6')


--- query
SELECT MAX(B.num) AS num
FROM (
  SELECT A.num, count(1) AS NBR
  FROM MyNumbers AS A
  GROUP BY A.num
  HAVING NBR = 1
) AS B