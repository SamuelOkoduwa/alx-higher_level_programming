-- a script that lists all the cities in California that can be found in the database hbtn_0d_usa

-- SELECT cities.name	FROM cities
-- JOIN states ON cities.state_id = states.id
-- WHERE states.name = 'California';

SELECT `id`, `name`
  FROM `cities`
 WHERE `state_id` IN
       (SELECT `id`
	        FROM `states`
	       WHERE `name` = "California")
ORDER BY `id`;