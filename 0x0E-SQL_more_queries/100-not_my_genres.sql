-- A script that uses the hbtn_0d_tvshows database to list all genres of the show Dexter

-- SELECT t.`title`
--   FROM `tv_shows` AS t
-- 	   INNER JOIN `tv_show_genres` AS s
-- 	   ON t.`id` = s.`show_id`

-- 	   INNER JOIN `tv_genres` AS g
-- 	   ON g.`id` = s.`genre_id`
-- 	   WHERE t.`title` != "Dexter"
--  ORDER BY t.`title`;

SELECT DISTINCT `name`
  FROM `tv_genres` AS g
       INNER JOIN `tv_show_genres` AS s
       ON g.`id` = s.`genre_id`

       INNER JOIN `tv_shows` AS t
       ON s.`show_id` = t.`id`
       WHERE g.`name` NOT IN
             (SELECT `name`
                FROM `tv_genres` AS g
	             INNER JOIN `tv_show_genres` AS s
		     ON g.`id` = s.`genre_id`

		     INNER JOIN `tv_shows` AS t
		     ON s.`show_id` = t.`id`
		     WHERE t.`title` = "Dexter")
 ORDER BY g.`name`;