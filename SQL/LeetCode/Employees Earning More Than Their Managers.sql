SELECT Employee.name AS Employee
FROM Employee
    INNER JOIN Employee AS Manager ON Employee.managerId = Manager.id
WHERE Employee.salary > Manager.salary