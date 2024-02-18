-- create table
Create table If Not Exists Logs (id int, num int)
Truncate table Logs
insert into Logs (id, num) values ('1', '1')
insert into Logs (id, num) values ('2', '1')
insert into Logs (id, num) values ('3', '1')
insert into Logs (id, num) values ('4', '2')
insert into Logs (id, num) values ('5', '1')
insert into Logs (id, num) values ('6', '2')
insert into Logs (id, num) values ('7', '2')

--- query
WITH SOURCE AS (
    SELECT num,
    lead(num,1) over() num1,
    lead(num,2) over() num2
    FROM Logs
)

SELECT DISTINCT(num) AS ConsecutiveNums
FROM SOURCE
WHERE num=num1 AND num=num2
