-- MySQL dump 10.13  Distrib 8.0.28, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: prueba_bd
-- ------------------------------------------------------
-- Server version	8.0.28

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
-- Table structure for table `citas`
--

DROP TABLE IF EXISTS `citas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `citas` (
  `idcitas` int NOT NULL AUTO_INCREMENT,
  `usuario` varchar(45) NOT NULL,
  `fecha` datetime(1) NOT NULL,
  `motivo` varchar(50) NOT NULL,
  `c_mascotas` int NOT NULL,
  PRIMARY KEY (`idcitas`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `citas`
--

LOCK TABLES `citas` WRITE;
/*!40000 ALTER TABLE `citas` DISABLE KEYS */;
/*!40000 ALTER TABLE `citas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `citas_atendidas`
--

DROP TABLE IF EXISTS `citas_atendidas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `citas_atendidas` (
  `idcitas_atendidas` int NOT NULL AUTO_INCREMENT,
  `usuario` varchar(45) NOT NULL,
  `doctor` varchar(45) NOT NULL,
  `diagnostico` varchar(50) NOT NULL,
  `receta` varchar(100) NOT NULL,
  `fecha` datetime(1) NOT NULL,
  PRIMARY KEY (`idcitas_atendidas`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `citas_atendidas`
--

LOCK TABLES `citas_atendidas` WRITE;
/*!40000 ALTER TABLE `citas_atendidas` DISABLE KEYS */;
/*!40000 ALTER TABLE `citas_atendidas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ingresos_egresos`
--

DROP TABLE IF EXISTS `ingresos_egresos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ingresos_egresos` (
  `idingresos_egresos` int NOT NULL AUTO_INCREMENT,
  `ingreso` double NOT NULL,
  `egreso` double NOT NULL,
  `concepto` varchar(45) NOT NULL,
  `total` double NOT NULL,
  `fecha` date NOT NULL,
  PRIMARY KEY (`idingresos_egresos`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ingresos_egresos`
--

LOCK TABLES `ingresos_egresos` WRITE;
/*!40000 ALTER TABLE `ingresos_egresos` DISABLE KEYS */;
/*!40000 ALTER TABLE `ingresos_egresos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pagos`
--

DROP TABLE IF EXISTS `pagos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pagos` (
  `idpagos` int NOT NULL AUTO_INCREMENT,
  `usuario` varchar(45) NOT NULL,
  `doctor` varchar(45) NOT NULL,
  `concepto` varchar(45) NOT NULL,
  `cambio` double NOT NULL,
  `fecha` date NOT NULL,
  `metodo_pago` varchar(45) NOT NULL,
  `total` double NOT NULL,
  PRIMARY KEY (`idpagos`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pagos`
--

LOCK TABLES `pagos` WRITE;
/*!40000 ALTER TABLE `pagos` DISABLE KEYS */;
/*!40000 ALTER TABLE `pagos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t_usuarios`
--

DROP TABLE IF EXISTS `t_usuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `t_usuarios` (
  `ida_usuarios` int NOT NULL AUTO_INCREMENT,
  `nombre_completo` varchar(45) NOT NULL,
  `user_name` varchar(45) NOT NULL,
  `password` varchar(100) NOT NULL,
  `roll` varchar(45) NOT NULL,
  PRIMARY KEY (`ida_usuarios`),
  UNIQUE KEY `password_UNIQUE` (`password`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_usuarios`
--

LOCK TABLES `t_usuarios` WRITE;
/*!40000 ALTER TABLE `t_usuarios` DISABLE KEYS */;
/*!40000 ALTER TABLE `t_usuarios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuarios`
--

DROP TABLE IF EXISTS `usuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuarios` (
  `idusuarios` int NOT NULL AUTO_INCREMENT,
  `nombre_completo` varchar(45) NOT NULL,
  `user_name` varchar(45) NOT NULL,
  `password` varchar(100) NOT NULL,
  `direccion` varchar(45) NOT NULL,
  `celular` int NOT NULL,
  PRIMARY KEY (`idusuarios`),
  UNIQUE KEY `password_UNIQUE` (`password`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuarios`
--

LOCK TABLES `usuarios` WRITE;
/*!40000 ALTER TABLE `usuarios` DISABLE KEYS */;
INSERT INTO `usuarios` VALUES (1,'Patata','Pizza','$5$rounds=535000$NT9UJ03rNzzgP4ic$X6/O.0F7IBLeXI7BfJw81onJ8zQLeFmXLndkKZ5RLl/','potato\'s',39089),(2,'Potaos','Perro','$5$rounds=535000$M15XJAEHACXbBrJm$4tfVlVrix/RdSb6p5uGbeqciheIB2M5dSb3IL.j3IYB','potato\'s',39089);
/*!40000 ALTER TABLE `usuarios` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-04-25 16:30:24
