# Write your MySQL query statement below
SELECT e.name AS Employee
FROM Employee e
JOIN Employee p
ON e.managerId=p.id
WHERE e.salary>p.salary;