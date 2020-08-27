-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 19, 2020 at 07:09 AM
-- Server version: 10.4.13-MariaDB
-- PHP Version: 7.2.32

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `epm`
--

-- --------------------------------------------------------

--
-- Table structure for table `employee`
--

CREATE TABLE `employee` (
  `Idno` int(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `email` varchar(150) NOT NULL,
  `gender` varchar(100) NOT NULL,
  `contact` varchar(150) NOT NULL,
  `dob` varchar(150) NOT NULL,
  `address` varchar(200) NOT NULL,
  `department` varchar(100) NOT NULL,
  `status` varchar(100) NOT NULL,
  `payment` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `employee`
--

INSERT INTO `employee` (`Idno`, `name`, `email`, `gender`, `contact`, `dob`, `address`, `department`, `status`, `payment`) VALUES
(1, 'Bipin Adhikari', 'adhkadhkbipin@gmail.com', 'Male', '9841304294', '03/03//2001', 'Satdobato, Lalitpur-15\n\n', 'Admin', 'Present', 'Bank'),
(2, 'Hari', 'Dhungey_bagar@gmail.com', 'Male', '9869969696', '01/01/2000', 'Gotikhel\n\n', 'IT', 'Busy', 'Cash'),
(3, 'Madan Bahadur', 'bhungey_bagar@gmail.com', 'Male', '9869969696', '01/01/2000', 'Gotikhel\n\n\n', 'IT', 'Busy', 'Cheque'),
(5, 'Bipin ', 'adhkadhkbipin@gmail.com', 'Male', '9841304294', '03/03//2001', 'Satdobato, Lalitpur-15\n\n\n', 'Admin', 'Present', 'Bank'),
(7, 'Bhari', 'bhungey_bagar@gmail.com', 'Male', '9869969696', '01/01/2000', 'Gotikhel\n\n\n\n\n\n\n\n', 'Management', 'Busy', 'E-Sewa'),
(11, 'Ronaldododo', 'ronaldo@ronaldo.ronaldo.ronaldo', 'Male', '777777777', '07/07/7070', 'Ronaldo highway-77\n\n\n\n\n\n\n\n', 'Sales', 'Absent', 'Cheque');

-- --------------------------------------------------------

--
-- Table structure for table `total_payment`
--

CREATE TABLE `total_payment` (
  `Idno` int(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `contact` varchar(150) NOT NULL,
  `department` varchar(100) NOT NULL,
  `payment` varchar(150) NOT NULL,
  `amount` varchar(150) NOT NULL,
  `overtime` varchar(100) NOT NULL,
  `total` int(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `total_payment`
--

INSERT INTO `total_payment` (`Idno`, `name`, `contact`, `department`, `payment`, `amount`, `overtime`, `total`) VALUES
(2, 'Hari', '9869969696', 'IT', 'Cash', '40000', '5%', 42000),
(3, 'Madan Bahadur', '9869969696', 'IT', 'Cheque', '456346', '15%', 0),
(7, 'Bhari', '9869969696', 'Management', 'E-Sewa', '456', '5%', 0);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `employee`
--
ALTER TABLE `employee`
  ADD PRIMARY KEY (`Idno`);

--
-- Indexes for table `total_payment`
--
ALTER TABLE `total_payment`
  ADD PRIMARY KEY (`Idno`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
