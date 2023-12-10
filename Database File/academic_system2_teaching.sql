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
-- Table structure for table `teaching`
--

DROP TABLE IF EXISTS `teaching`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `teaching` (
  `CourseCode` varchar(10) NOT NULL,
  `TeacherID` varchar(10) NOT NULL,
  `CourseLeader` tinyint(1) DEFAULT NULL,
  KEY `TeacherID` (`TeacherID`),
  KEY `teaching_ibfk_1` (`CourseCode`),
  CONSTRAINT `teaching_ibfk_1` FOREIGN KEY (`CourseCode`) REFERENCES `course` (`CourseCode`),
  CONSTRAINT `teaching_ibfk_2` FOREIGN KEY (`TeacherID`) REFERENCES `teacher` (`TeacherID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `teaching`
--

LOCK TABLES `teaching` WRITE;
/*!40000 ALTER TABLE `teaching` DISABLE KEYS */;
INSERT INTO `teaching` VALUES ('COMPS333F','T001',1),('COMPS362F','T002',1),('COMPS381F','T003',1),('COMPS390F','T004',1),('COMPS413F','T005',1),('ELECS305F','T006',1),('ELECS363F','T001',0),('COMPS333F','T002',0),('COMPS362F','T003',0),('COMPS390F','T005',0),('ELECS363F','T004',0);
/*!40000 ALTER TABLE `teaching` ENABLE KEYS */;
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
