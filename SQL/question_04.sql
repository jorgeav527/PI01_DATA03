SELECT result.driverId, driver.name_forename, driver.name_surname, SUM(points) AS total, constructor.name, constructor.nationality FROM result 
INNER JOIN constructor on result.constructorId=constructor.constructorId
INNER JOIN driver on result.driverId=driver.driverId
WHERE constructor.nationality = "American" OR constructor.nationality = "British" 
GROUP BY result.driverId ORDER BY total DESC LIMIT 1;