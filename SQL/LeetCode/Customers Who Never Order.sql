SELECT Customers.name AS Customers
FROM Customers
LEFT JOIN Orders on Customers.id = Orders.CustomerId
WHERE Orders.id IS Null