1. Sök ur Metri fram en lista som innehåller pubID samt instanceID. Listan ska se ut som följer:
165748; 1, 2, 1, 1, 2
196423; 2, 1, 0
201569; 1, 1, 1

Detta kan göras med hjälp av följande algoritm:

SELECT c.pubid, array_to_string(array_agg(di.instanceid), ’, ')
FROM uplmain AS c
INNER JOIN person_publ AS pp ON c.dbid = pp.dbid
INNER JOIN dept_pers_publ AS dpp ON pp.pd_id = dpp.pd_id
INNER JOIN departments AS d ON dpp.deptid = d.deptid
INNER JOIN dept_instance AS di ON d.deptid = di.deptid
WHERE c.pubyear BETWEEN 2012 and 2014 --Ändra här mellan vilka år du vill ha data
GROUP BY c.pubid

2. Spara filen med namn pubids_input.txt och kör Pythonscriptet getPubID. Öppna den nya filen, döpt till pubids.txt och ta bort sista kommatecknet i filen.

3. Kör följande algoritm i PostSQL:

SELECT c.pubid, d.sv_name
FROM uplmain AS c
INNER JOIN person_publ AS pp ON c.dbid = pp.dbid
INNER JOIN dept_pers_publ AS dpp ON pp.pd_id = dpp.pd_id
INNER JOIN departments AS d ON dpp.deptid = d.deptid
WHERE c.pubid IN (--pubID här)

Klistra in pubID från pubids.txt på anvisad plats i koden. Spara resultatet i en .txt-fil.

4. Kör pythonscriptet createNetworkFile. En fil vid namn network.net skapas. Öppna denna med exempelvis Gephi.