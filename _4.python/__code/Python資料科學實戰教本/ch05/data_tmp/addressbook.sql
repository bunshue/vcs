-- --------------------------------------------------------
-- 主機:                           127.0.0.1
-- 服務器版本:                        5.1.40 - Source distribution
-- 服務器操作系統:                      Win32
-- HeidiSQL 版本:                  9.4.0.5125
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- 導出 addressbook 的資料庫結構
CREATE DATABASE IF NOT EXISTS `addressbook` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `addressbook`;

-- 導出  表 addressbook.address 結構
CREATE TABLE IF NOT EXISTS `address` (
  `id` int(4) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) DEFAULT NULL,
  `phone` varchar(30) DEFAULT NULL,
  `email` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

-- 正在導出表  addressbook.address 的資料：4 rows
/*!40000 ALTER TABLE `address` DISABLE KEYS */;
INSERT INTO `address` (`id`, `name`, `phone`, `email`) VALUES
	(1, 'Laika Clay', '430-555-2252', 'laika@doggie.com'),
	(2, 'Tiger Clay', '658-555-5985', 'tiger@kittie.us'),
	(4, 'A Clay', '555-777-0000', 'clay@php.com'),
	(5, 'Santa Clause', '888-888-7777', 'santa@np.net');
/*!40000 ALTER TABLE `address` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
