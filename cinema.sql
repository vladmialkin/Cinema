-- MySQL dump 10.13  Distrib 8.0.31, for Linux (x86_64)
--
-- Host: localhost    Database: intership
-- ------------------------------------------------------
-- Server version	8.0.31

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `film`
--

DROP TABLE IF EXISTS `film`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `film` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` text,
  `genre_id` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `film`
--

LOCK TABLES `film` WRITE;
/*!40000 ALTER TABLE `film` DISABLE KEYS */;
INSERT INTO `film` VALUES (1,'Главный герой',2),(2,'Крепкий орешек',2),(3,'Аватар',2);
/*!40000 ALTER TABLE `film` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `genre`
--

DROP TABLE IF EXISTS `genre`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `genre` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `genre`
--

LOCK TABLES `genre` WRITE;
/*!40000 ALTER TABLE `genre` DISABLE KEYS */;
INSERT INTO `genre` VALUES (1,'Все'),(2,'Детектив'),(3,'Драма'),(4,'Комедия');
/*!40000 ALTER TABLE `genre` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hall`
--

DROP TABLE IF EXISTS `hall`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `hall` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` text,
  `size_hall` int DEFAULT NULL,
  `count_row` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hall`
--

LOCK TABLES `hall` WRITE;
/*!40000 ALTER TABLE `hall` DISABLE KEYS */;
INSERT INTO `hall` VALUES (1,'Зал 1',40,5),(2,'Зал 2',40,6);
/*!40000 ALTER TABLE `hall` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `places`
--

DROP TABLE IF EXISTS `places`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `places` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_hall` int DEFAULT NULL,
  `employment` int DEFAULT NULL,
  `session_id` int DEFAULT NULL,
  `number` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=161 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `places`
--

LOCK TABLES `places` WRITE;
/*!40000 ALTER TABLE `places` DISABLE KEYS */;
INSERT INTO `places` VALUES (1,1,1,1,1),(2,1,1,1,2),(3,1,1,1,3),(4,1,1,1,4),(5,1,1,1,5),(6,1,1,1,6),(7,1,0,1,7),(8,1,0,1,8),(9,1,0,1,9),(10,1,0,1,10),(11,1,1,1,11),(12,1,1,1,12),(13,1,1,1,13),(14,1,1,1,14),(15,1,0,1,15),(16,1,0,1,16),(17,1,1,1,17),(18,1,1,1,18),(19,1,1,1,19),(20,1,1,1,20),(21,1,1,1,21),(22,1,1,1,22),(23,1,0,1,23),(24,1,0,1,24),(25,1,0,1,25),(26,1,0,1,26),(27,1,0,1,27),(28,1,0,1,28),(29,1,0,1,29),(30,1,1,1,30),(31,1,0,1,31),(32,1,0,1,32),(33,1,1,1,33),(34,1,1,1,34),(35,1,1,1,35),(36,1,1,1,36),(37,1,0,1,37),(38,1,1,1,38),(39,1,0,1,39),(40,1,0,1,40),(41,2,0,1,1),(42,2,1,1,2),(43,2,0,1,3),(44,2,0,1,4),(45,2,0,1,5),(46,2,0,1,6),(47,2,0,1,7),(48,2,1,1,8),(49,2,1,1,9),(50,2,1,1,10),(51,2,0,1,11),(52,2,0,1,12),(53,2,0,1,13),(54,2,0,1,14),(55,2,0,1,15),(56,2,0,1,16),(57,2,0,1,17),(58,2,0,1,18),(59,2,0,1,19),(60,2,0,1,20),(61,2,0,1,21),(62,2,0,1,22),(63,2,0,1,23),(64,2,0,1,24),(65,2,0,1,25),(66,2,0,1,26),(67,2,0,1,27),(68,2,0,1,28),(69,2,0,1,29),(70,2,0,1,30),(71,2,0,1,31),(72,2,0,1,32),(73,2,0,1,33),(74,2,0,1,34),(75,2,0,1,35),(76,2,0,1,36),(77,2,0,1,37),(78,2,0,1,38),(79,2,0,1,39),(80,2,0,1,40),(121,1,0,2,1),(122,1,1,2,2),(123,1,1,2,3),(124,1,1,2,4),(125,1,0,2,5),(126,1,1,2,6),(127,1,0,2,7),(128,1,0,2,8),(129,1,0,2,9),(130,1,1,2,10),(131,1,0,2,11),(132,1,0,2,12),(133,1,1,2,13),(134,1,0,2,14),(135,1,0,2,15),(136,1,0,2,16),(137,1,0,2,17),(138,1,1,2,18),(139,1,0,2,19),(140,1,0,2,20),(141,1,0,2,21),(142,1,0,2,22),(143,1,0,2,23),(144,1,0,2,24),(145,1,0,2,25),(146,1,0,2,26),(147,1,0,2,27),(148,1,0,2,28),(149,1,0,2,29),(150,1,0,2,30),(151,1,0,2,31),(152,1,0,2,32),(153,1,0,2,33),(154,1,0,2,34),(155,1,0,2,35),(156,1,0,2,36),(157,1,0,2,37),(158,1,0,2,38),(159,1,0,2,39),(160,1,0,2,40);
/*!40000 ALTER TABLE `places` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sale`
--

DROP TABLE IF EXISTS `sale`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sale` (
  `id` int NOT NULL AUTO_INCREMENT,
  `hall_id` int DEFAULT NULL,
  `place` int DEFAULT NULL,
  `session_id` int DEFAULT NULL,
  `film_id` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sale`
--

LOCK TABLES `sale` WRITE;
/*!40000 ALTER TABLE `sale` DISABLE KEYS */;
INSERT INTO `sale` VALUES (1,1,1,1,1),(2,1,1,1,1),(3,1,2,1,1),(4,1,3,1,1),(5,1,12,1,1),(6,1,13,1,1),(7,1,14,1,1),(8,1,19,1,1),(9,1,18,1,1),(10,1,17,1,1),(11,1,3,2,3),(12,1,4,2,3),(13,1,6,2,3),(14,1,33,1,1),(15,1,34,1,1),(16,1,35,1,1),(17,1,36,1,1),(18,2,2,1,1),(19,1,20,1,1),(20,1,21,1,1),(21,1,13,2,3),(22,2,8,1,1),(23,2,9,1,1),(24,2,10,1,1),(25,1,2,2,3),(26,1,10,2,3),(27,1,18,2,3),(28,1,11,1,1),(29,1,4,1,1),(30,1,38,1,1),(31,1,5,1,1),(32,1,6,1,1),(33,1,22,1,1);
/*!40000 ALTER TABLE `sale` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `session`
--

DROP TABLE IF EXISTS `session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `session` (
  `id` int NOT NULL AUTO_INCREMENT,
  `TIME` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `session`
--

LOCK TABLES `session` WRITE;
/*!40000 ALTER TABLE `session` DISABLE KEYS */;
INSERT INTO `session` VALUES (1,'10:00-13:00'),(2,'13:00-16:00'),(3,'16:00-19:00'),(4,'19:30-23:00');
/*!40000 ALTER TABLE `session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `session_information`
--

DROP TABLE IF EXISTS `session_information`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `session_information` (
  `id` int NOT NULL AUTO_INCREMENT,
  `session_id` int DEFAULT NULL,
  `hall_id` int DEFAULT NULL,
  `film_id` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `session_information`
--

LOCK TABLES `session_information` WRITE;
/*!40000 ALTER TABLE `session_information` DISABLE KEYS */;
INSERT INTO `session_information` VALUES (1,1,1,1),(2,1,2,1),(3,1,1,2),(4,2,1,3),(5,1,2,3);
/*!40000 ALTER TABLE `session_information` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-03-26 19:03:59
