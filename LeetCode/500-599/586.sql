-- create table
Create table If Not Exists orders (order_number int, customer_number int)
Truncate table orders
insert into orders (order_number, customer_number) values ('1', '1')
insert into orders (order_number, customer_number) values ('2', '2')
insert into orders (order_number, customer_number) values ('3', '3')
insert into orders (order_number, customer_number) values ('4', '3')


--- query
SELECT customer_number
FROM (
    SELECT customer_number, count(1) AS order_cnt
    FROM Orders
    GROUP BY customer_number
) AS A
WHERE A.order_cnt = (
    SELECT MAX(B.order_cnt)
    FROM(
        SELECT customer_number, count(1) AS order_cnt
        FROM Orders
        GROUP BY customer_number
    ) AS B
)