-- A script that lists all genres in the database hbtn_0d_tvshows rate by their rating

SELECT `name`, SUM(`rate`) AS `rating`
  FROM `tv_genres` AS g
	   INNER JOIN `tv_show_genres` AS s
	   ON g.`id` = s.`genre_id`
 
	   INNER JOIN `tv_shows` AS t
	   ON s.`show_id` = t.`id`
 
	   INNER JOIN `tv_show_ratings` AS r
	   ON t.`id` = r.`show_id`
 GROUP BY `name`
 ORDER BY `rating` DESC, `name` ASC;