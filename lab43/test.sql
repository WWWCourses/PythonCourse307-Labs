CREATE TABLE `customers` (
  `id` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(45) NOT NULL,
  `last_name` varchar(45) NOT NULL,
  `email` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) DEFAULT CHARSET=utf8;

# define the Child Table
CREATE TABLE `orders` (
  `id` int NOT NULL AUTO_INCREMENT,
  `customer_id` int NOT NULL,
  `order_date` datetime NOT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`customer_id`) REFERENCES `customers` (`id`)
) DEFAULT CHARSET=utf8;

INSERT INTO customers VALUES (1,'Ivan','Ivanov','ivan@abv.bg');
INSERT INTO customers VALUES (2,'Asen','Asenov', 'asen@abv.bg');

INSERT INTO orders (order_date)
VALUES ( "2021-03-03 12:00:00")

CREATE TABLE artist (
  artist_id SMALLINT(5) NOT NULL AUTO_INCREMENT KEY,
  fname VARCHAR(20) DEFAULT NULL,
  lname VARCHAR(20) NOT NULL
);