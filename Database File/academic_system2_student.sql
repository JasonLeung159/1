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
-- Table structure for table `student`
--

DROP TABLE IF EXISTS `student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student` (
  `StudentID` char(10) NOT NULL,
  `StudentName` varchar(50) NOT NULL,
  `Year` int NOT NULL,
  `Age` int NOT NULL,
  `Gender` enum('M','F') NOT NULL,
  `PhoneNum` char(15) NOT NULL,
  `Email` varchar(50) NOT NULL,
  `login_password` varchar(50) NOT NULL,
  `SpLD` varchar(50) NOT NULL,
  `restudy` tinyint(1) NOT NULL,
  PRIMARY KEY (`StudentID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student`
--

LOCK TABLES `student` WRITE;
/*!40000 ALTER TABLE `student` DISABLE KEYS */;
INSERT INTO `student` VALUES ('01234567','Jacob Wilson',2,19,'M','90123456','01234567@stu.abcu.edu.hk','Jacob123','ADHD',1),('12345670','Kate Davis',3,20,'F','91234567','12345670@stu.abcu.edu.hk','Kate123','None',0),('12345678','Alice Johnson',1,18,'F','91234567','12345678@stu.abcu.edu.hk','Alice123','Dyslexia',0),('23456781','Liam Johnson',1,19,'M','92345678','23456781@stu.abcu.edu.hk','Liam123','None',0),('23456789','Bob Smith',2,19,'M','92345678','23456789@stu.abcu.edu.hk','Bob123','None',0),('34567890','Catherine Davis',1,19,'F','93456789','34567890@stu.abcu.edu.hk','Catherine123','Dyscalculia',0),('45678901','David Lee',3,19,'M','94567890','45678901@stu.abcu.edu.hk','David123','None',0),('56789012','Emily Wilson',2,19,'F','95678901','56789012@stu.abcu.edu.hk','Emily123','None',1),('67890123','Frank Johnson',1,18,'M','96789012','67890123@stu.abcu.edu.hk','Frank123','None',0),('78901234','Grace Taylor',2,20,'F','97890123','78901234@stu.abcu.edu.hk','Grace123','Dyslexia',1),('89012345','Henry Brown',3,19,'M','98901234','89012345@stu.abcu.edu.hk','Henry123','None',0),('90123456','Isabella Anderson',1,18,'F','99012345','90123456@stu.abcu.edu.hk','Isabella123','dyslexia',0);
/*!40000 ALTER TABLE `student` ENABLE KEYS */;
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
