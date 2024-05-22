-- Importing data for table top_city and writing a script that displays the top 3 cities during july and august by average temperature (Fahrenheit) ordered by temperature (descending).

SELECT city, AVG(temperature) AS avg_temp
FROM temperatures
WHERE MONTH(date) IN (7, 8)
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;