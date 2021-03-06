--1st try
SELECT P,
CASE P
WHEN 2 THEN 'Leaf'
WHEN 8 THEN 'Leaf'
WHEN 'null' THEN 'Root'
WHEN 5 THEN 'Inner'
END
FROM BST
ORDER BY P

--2nd try
SELECT  N, 
CASE 
WHEN P IS NULL THEN 'Root' 
WHEN N NOT IN (SElECT Distinct P FROM bst WHERE P IS NOT NULL) THEN 'Leaf'
ELSE 'Inner' END
FROM BST
ORDER BY N