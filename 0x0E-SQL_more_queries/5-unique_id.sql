-- A script that creates the table unique_id in the MYSQL server

CREATE TABLE IF NOT EXISTS `unique_id` (
	`id`   INT          AUTO_INCREMENT,
	`name` VARCHAR(256),
	PRIMARY KEY (`id`)
);