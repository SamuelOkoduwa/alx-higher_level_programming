-- Import from a database and write a script that lists all genres from hbtn_0d_tvshows and displays

SELECT g.`id`, g.`name`, COUNT(s.`id`) AS `number_of_shows`
  FROM `genres` AS g
	   LEFT JOIN `shows` AS s
	   ON g.`id` = s.`genre_id`
 GROUP BY g.`id`, g.`name`
 ORDER BY g.`id`;