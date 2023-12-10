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
-- Table structure for table `class_arrangements`
--

DROP TABLE IF EXISTS `class_arrangements`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `class_arrangements` (
  `CourseCode` varchar(10) NOT NULL,
  `Course_Group` varchar(10) DEFAULT NULL,
  `Date` date NOT NULL,
  `Time_Start` time NOT NULL,
  `Time_End` time DEFAULT NULL,
  `Venue` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`CourseCode`,`Date`,`Time_Start`),
  CONSTRAINT `class_arrangements_ibfk_1` FOREIGN KEY (`CourseCode`) REFERENCES `course` (`CourseCode`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `class_arrangements`
--

LOCK TABLES `class_arrangements` WRITE;
/*!40000 ALTER TABLE `class_arrangements` DISABLE KEYS */;
INSERT INTO `class_arrangements` VALUES ('COMPS333F','Lecture','2023-11-20','09:00:00','11:00:00','Lecture Hall A'),('COMPS333F','Laboratory','2023-11-21','14:00:00','16:00:00','Lab 101'),('COMPS333F','Lecture','2023-11-27','09:00:00','11:00:00','Lecture Hall A'),('COMPS333F','Laboratory','2023-11-28','14:00:00','16:00:00','Lab 101'),('COMPS333F','testing','2023-12-08','14:30:00','16:30:00','test'),('COMPS362F','Lecture','2023-11-22','10:30:00','12:30:00','Lecture Hall D'),('COMPS362F','Laboratory','2023-11-23','16:00:00','18:00:00','Lab 102'),('COMPS362F','Lecture','2023-11-29','10:30:00','12:30:00','Lecture Hall D'),('COMPS362F','Laboratory','2023-11-30','16:00:00','18:00:00','Lab 102'),('COMPS381F','Lecture','2023-11-21','10:00:00','12:00:00','Lecture Hall C'),('COMPS381F','Laboratory','2023-11-23','09:00:00','11:00:00','Lab 103'),('COMPS381F','Lecture','2023-11-28','10:00:00','12:00:00','Lecture Hall C'),('COMPS381F','Laboratory','2023-11-30','09:00:00','11:00:00','Lab 103'),('COMPS390F','Lecture','2023-11-20','13:00:00','15:00:00','Lecture Hall D'),('COMPS390F','Laboratory','2023-11-24','11:00:00','13:00:00','Lab 104'),('COMPS390F','Lecture','2023-11-27','13:00:00','15:00:00','Lecture Hall D'),('COMPS390F','Laboratory','2023-12-01','11:00:00','13:00:00','Lab 104'),('COMPS413F','Lecture','2023-11-21','16:00:00','18:00:00','Lecture Hall A'),('COMPS413F','Laboratory','2023-11-22','14:30:00','16:30:00','Lab 101'),('COMPS413F','Lecture','2023-11-28','16:00:00','18:00:00','Lecture Hall A'),('COMPS413F','Laboratory','2023-11-29','14:30:00','16:30:00','Lab 101'),('ELECS305F','Lecture','2023-11-22','08:30:00','10:30:00','Lecture Hall B'),('ELECS305F','Laboratory','2023-11-23','14:00:00','16:00:00','Lab 102'),('ELECS305F','Lecture','2023-11-29','08:30:00','10:30:00','Lecture Hall B'),('ELECS305F','Laboratory','2023-11-30','14:00:00','16:00:00','Lab 102'),('ELECS305F','Laboratory','2023-12-06','17:00:00','19:00:00','Lab 102'),('ELECS363F','Lecture','2023-11-23','11:00:00','13:00:00','Lecture Hall C'),('ELECS363F','Laboratory','2023-11-24','14:30:00','16:30:00','Lab 102'),('ELECS363F','Lecture','2023-11-30','11:00:00','13:00:00','Lecture Hall C'),('ELECS363F','Laboratory','2023-12-01','14:30:00','16:30:00','Lab 102');
/*!40000 ALTER TABLE `class_arrangements` ENABLE KEYS */;
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
