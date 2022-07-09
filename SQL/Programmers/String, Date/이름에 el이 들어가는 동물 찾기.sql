--1차 풀이
SELECT ANIMAL_INS.ANIMAL_ID, ANIMAL_INS.NAME
FROM ANIMAL_INS
WHERE ANIMAL_INS.ANIMAL_TYPE = 'Dog' 
AND ANIMAL_INS.NAME LIKE '%EL' 
OR ANIMAL_INS.NAME LIKE 'EL%'
ORDER BY ANIMAL_INS.NAMES

-- 2차 풀이
SELECT ANIMAL_INS.ANIMAL_ID, ANIMAL_INS.NAME
FROM ANIMAL_INS
WHERE ANIMAL_INS.ANIMAL_TYPE = 'Dog' AND ANIMAL_INS.NAME LIKE '%EL%'
ORDER BY ANIMAL_INS.NAME