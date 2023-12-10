-- MySQL dump 10.13  Distrib 8.0.26, for Win64 (x86_64)
--
-- Host: localhost    Database: academic_system2
-- ------------------------------------------------------
-- Server version	8.0.26

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `coursescore`
--

DROP TABLE IF EXISTS `coursescore`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `coursescore` (
  `CourseCode` varchar(10) NOT NULL,
  `StudentID` char(10) NOT NULL,
  `Score` double NOT NULL,
  `Type` varchar(10) NOT NULL,
  `ScorePercent` int DEFAULT NULL,
  `Final_score` double DEFAULT NULL,
  PRIMARY KEY (`CourseCode`,`StudentID`,`Type`),
  KEY `StudentID` (`StudentID`),
  CONSTRAINT `coursescore_ibfk_1` FOREIGN KEY (`CourseCode`) REFERENCES `course` (`CourseCode`),
  CONSTRAINT `coursescore_ibfk_2` FOREIGN KEY (`StudentID`) REFERENCES `student` (`StudentID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `coursescore`
--

LOCK TABLES `coursescore` WRITE;
/*!40000 ALTER TABLE `coursescore` DISABLE KEYS */;
INSERT INTO `coursescore` VALUES ('ELECS305F','01234567',76,'Exam',50,38),('ELECS305F','01234567',80,'Homework',20,16),('ELECS305F','01234567',67,'Test',30,20.1),('ELECS305F','12345678',64,'Exam',50,32),('ELECS305F','12345678',67,'Homework',20,13.4),('ELECS305F','12345678',80,'Test',30,24);
/*!40000 ALTER TABLE `coursescore` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-12-10 13:08:52
