-- Import from a database and write a script that uses the hbtn_0d_tvshows database to list all genres of the show Dexter

SELECT g.`name`
  FROM `tv_genres` AS g
	   INNER JOIN `tv_show_genres` AS t
	   ON g.`id` = t.`genre_id`
 WHERE t.`show_id` IN
	   (SELECT `id`
		  FROM `tv_shows`
		 WHERE `title` = "Dexter")
 ORDER BY g.`name`;			