-- Import from a database and write a script that lists all genres from hbtn_0d_tvshows and displays

-- SELECT g.`id`, g.`name`, COUNT(s.`id`) AS `number_of_shows`
--   FROM `genres` AS g
-- 	   LEFT JOIN `shows` AS s
-- 	   ON g.`id` = s.`genre_id`
--  GROUP BY g.`id`, g.`name`
--  ORDER BY g.`id`;

SELECT g.`name` AS `genre`,
       COUNT(*) AS `number_of_shows`
  FROM `tv_genres` AS g
       INNER JOIN `tv_show_genres` AS t
       ON g.`id` = t.`genre_id`
 GROUP BY g.`name`
 ORDER BY `number_of_shows` DESC;