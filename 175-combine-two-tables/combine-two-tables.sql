# Write your MySQL query statement below
SELECT lastName,firstName,city,state
FROM Person AS p
LEFT JOIN Address AS a
ON p.personId=a.personId;
