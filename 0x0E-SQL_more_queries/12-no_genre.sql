-- Import from a database and write a script that lists all shows contained in the database hbtn_0d_tvshows without a genre linked

SELECT s.`title`
  FROM `tv_shows` AS s
	   LEFT JOIN `tv_show_genres` AS g
	   ON s.`id` = g.`show_id`
 WHERE g.`genre_id` IS NULL
 ORDER BY s.`title`;