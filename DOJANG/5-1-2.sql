SELECT count(*) FROM (SELECT DocID, count(*) FROM Documents WHERE Term="data" or Term="base" GROUP by DocID HAVING count(*)=2)