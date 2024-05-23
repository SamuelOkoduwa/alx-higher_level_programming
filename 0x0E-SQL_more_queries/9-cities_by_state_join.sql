-- A script that lists all cities contained in the database hbtn_0d_usa

-- SELECT cities.name, states.name
--   FROM cities
--   JOIN states ON cities.state_id = states.id
--  ORDER BY cities.id;

SELECT c.`id`, c.`name`, s.`name`
  FROM `cities` AS c
       INNER JOIN `states` AS s
       ON c.`state_id` = s.`id`
 ORDER BY c.`id`;