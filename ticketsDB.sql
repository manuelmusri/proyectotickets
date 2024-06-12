-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Jun 12, 2024 at 04:55 PM
-- Server version: 8.0.30
-- PHP Version: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `tickets`
--

-- --------------------------------------------------------

--
-- Table structure for table `usuario`
--

CREATE TABLE `usuario` (
  `id_usuario` int NOT NULL,
  `pass_usuario` varchar(45) NOT NULL,
  `nombre_usuario` varchar(45) NOT NULL,
  `apellido_usuario` varchar(45) NOT NULL,
  `tel_usuario` int NOT NULL,
  `correo_usuario` varchar(45) NOT NULL,
  `id_tusuario` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `usuario`
--

INSERT INTO `usuario` (`id_usuario`, `pass_usuario`, `nombre_usuario`, `apellido_usuario`, `tel_usuario`, `correo_usuario`, `id_tusuario`) VALUES
(1, '81dc9bdb52d04dc20036dbd8313ed055', 'user1', 'apellido1', 998547426, 'correo@algo.com', 1),
(2, '1234', 'jefedemesa2', 'mesa', 998547426, 'correo@falso.com', 1),
(3, '81dc9bdb52d04dc20036dbd8313ed055', 'ejemesa1', 'aplee', 665821455, 'correo@algo.cl', 3),
(4, '81dc9bdb52d04dc20036dbd8313ed055', 'ejemesa2', 'aplee', 995631254, 'correo@falsisimo.cl', 3),
(5, '81dc9bdb52d04dc20036dbd8313ed055', 'ejemesa3', 'kasjs', 215747211, 'falso@correo.com', 3),
(6, '81dc9bdb52d04dc20036dbd8313ed055', 'ejearea1', 'apell', 457845241, 'nada@falso.cl', 2),
(7, '81dc9bdb52d04dc20036dbd8313ed055', 'ejearea2', 'lsksk', 1234587878, 'corr@ghas.cl', 2),
(8, '81dc9bdb52d04dc20036dbd8313ed055', 'ejearea4', 'kdjdjd', 122145454, 'sdsk@jkfjf.cl', 2),
(9, '81dc9bdb52d04dc20036dbd8313ed055', 'ejemesa232', 'dsds', 545784521, 'jsjd.@fgm.cl', 3),
(10, '81dc9bdb52d04dc20036dbd8313ed055', 'ejemesa87', 'dsss', 5468456, 'hjsd@lask.cl', 2),
(11, '81dc9bdb52d04dc20036dbd8313ed055', 'ejemesa232', 'ewewe', 125645521, 'isd@gjais.cl', 2),
(12, '81dc9bdb52d04dc20036dbd8313ed055', 'editadook', 'edi', 12354312, 'shjsas@ga.com', 3),
(13, '81dc9bdb52d04dc20036dbd8313ed055', 'elelelel', 'lelelele', 54621546, 'lelele@lele.cl', 2);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`id_usuario`),
  ADD UNIQUE KEY `id_usuario_UNIQUE` (`id_usuario`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `usuario`
--
ALTER TABLE `usuario`
  MODIFY `id_usuario` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
