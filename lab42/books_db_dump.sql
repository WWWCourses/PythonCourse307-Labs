-- MySQL dump 10.19  Distrib 10.2.38-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: books_db
-- ------------------------------------------------------
-- Server version	10.2.38-MariaDB-10.2.38+maria~xenial-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `authors`
--

DROP TABLE IF EXISTS `authors`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `authors` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `fname` varchar(250) DEFAULT NULL,
  `lname` varchar(250) NOT NULL,
  `birth_year` smallint(4) DEFAULT NULL,
  `death_year` smallint(4) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `lname` (`lname`(10))
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `authors`
--

LOCK TABLES `authors` WRITE;
/*!40000 ALTER TABLE `authors` DISABLE KEYS */;
INSERT INTO `authors` VALUES (1,'Kurt','Vonnegut',1922,2007),(2,'Douglas','Adams',1952,2001),(3,'Charles','Dodgson',1832,1898);
/*!40000 ALTER TABLE `authors` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `books`
--

DROP TABLE IF EXISTS `books`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `books` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `author_id` int(10) unsigned NOT NULL,
  `book_name` varchar(250) NOT NULL,
  `pub_year` smallint(4) unsigned DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `book_name` (`book_name`(10)),
  KEY `author_id` (`author_id`),
  CONSTRAINT `books_ibfk_1` FOREIGN KEY (`author_id`) REFERENCES `authors` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `books`
--

LOCK TABLES `books` WRITE;
/*!40000 ALTER TABLE `books` DISABLE KEYS */;
INSERT INTO `books` VALUES (1,1,'The Sirens of Titan',1959),(2,1,'Mother Night',1961),(3,1,'Cat\'s Cradle',1963),(4,1,'God Bless You',1965),(5,1,'Slaughterhouse',1969),(6,1,'Breakfast of Champions',1973),(7,2,'The Hitchhiker\'s Guide to the Galaxy',1979),(8,2,'The Restaurant at the End of the Universe',1980),(9,2,'Life',1982),(10,2,'So Long',1984),(11,2,'Young Zaphod Plays It Safe',1986),(12,2,'Dirk Gently\'s Holistic Detective Agency',1987),(13,2,'The Long Dark Tea',1988),(14,2,'Last Chance to See',1990),(15,2,'Mostly Harmless',1992),(16,3,'Alice\'s Adventures in Wonderland',1865),(17,3,'Through the Looking-Glass, and What Alice Found There',1871),(18,3,'Rhyme? And Reason?',NULL),(19,3,'A Tangled Tale',NULL),(20,3,'Pillow Problems',NULL),(21,3,'La Guida di Bragia, a Ballad Opera for the Marionette Theatre',1950),(22,3,'Sylvie and Bruno',NULL),(23,3,'Sylvie and Bruno Concluded',NULL),(24,3,'Three Sunsets and Other Poems',1898),(25,3,'The Hunting of the Snark',1876),(26,3,'What the Tortoise Said to Achilles',1895),(27,3,'A Syllabus of Plane Algebraic Geometry',1860),(28,3,'The Fifth Book of Euclid Treated Algebraically',1858),(29,3,'An Elementary Treatise on Determinants, With Their Application to Simultaneous Linear Equations and Algebraic Equations',NULL),(30,3,'Euclid and his Modern Rivals',1879),(31,3,'Symbolic Logic Part I',NULL),(32,3,'Symbolic Logic Part II',NULL),(33,3,'The Alphabet Cipher',1868),(34,3,'The Game of Logic',1887),(35,3,'Curiosa Mathematica I',1888),(36,3,'Curiosa Mathematica II',1892);
/*!40000 ALTER TABLE `books` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-10-07 20:19:16
