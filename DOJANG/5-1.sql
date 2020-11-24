SELECT DocID, number FROM (SELECT DocID, count(*) as number FROM Documents GROUP BY DocID)
WHERE number >= 3