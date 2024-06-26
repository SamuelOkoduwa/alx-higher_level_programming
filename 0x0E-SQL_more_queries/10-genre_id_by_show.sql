-- Import from a database and write a script that shows the genre_id by shows contained in the database hbtn_0d_tvshows that can be found in the database hbtn_0d_tvshows

-- CREATE DATABASE
-- 	IF NOT EXISTS `hbtn_0d_tvshows`;
-- USE `hbtn_0d_tvshows`;
-- SELECT
-- 	`shows`.`title`,
-- 	`genres`.`name`
--   FROM `shows`
--   JOIN `genres` ON `shows`.`genre_id` = `genres`.`id`	
-- ORDER BY `shows`.`id`;

SELECT s.`title`, g.`genre_id`
  FROM `tv_shows` AS s
        INNER JOIN `tv_show_genres` AS g
	ON s.`id` = g.`show_id`
 ORDER BY s.`title`, g.`genre_id`;