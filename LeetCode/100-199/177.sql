-- create table
Create table If Not Exists Employee (Id int, Salary int)
Truncate table Employee
insert into Employee (id, salary) values ('1', '100')
insert into Employee (id, salary) values ('2', '200')
insert into Employee (id, salary) values ('3', '300')

--- query
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
    SET N=N-1;
  RETURN (
      # Write your MySQL query statement below.
       SELECT DISTINCT(Salary) FROM Employee ORDER BY salary DESC LIMIT 1 OFFSET N
  );
END