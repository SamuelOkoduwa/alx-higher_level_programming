-- Importing in htbn_0c_0 database and writing a script that displays max temperature of each state (orderd by state name).


SELECT state, MAX(temperature) AS max_temp
FROM temperatures
GROUP BY state
ORDER BY state;
