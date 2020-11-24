SELECT max(Balance)
FROM Bank2
WHERE Country="USA"
GROUP BY Branch
HAVING max(Balance) > 25000
ORDER BY max(Balance) ASC
 
