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


-- 導出 mybook 的資料庫結構
CREATE DATABASE IF NOT EXISTS `mybook` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `mybook`;

-- 導出  表 mybook.book 結構
CREATE TABLE IF NOT EXISTS `book` (
  `id` char(5) NOT NULL,
  `title` varchar(30) DEFAULT NULL,
  `author` varchar(15) DEFAULT NULL,
  `price` decimal(10,0) DEFAULT NULL,
  `category` varchar(30) DEFAULT NULL,
  `pubdate` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- 正在導出表  mybook.book 的資料：6 rows
/*!40000 ALTER TABLE `book` DISABLE KEYS */;
INSERT INTO `book` (`id`, `title`, `author`, `price`, `category`, `pubdate`) VALUES
	('D0001', 'Access入門與實作', '陳會安', 450, '資料庫', '2016-06-01'),
	('P0001', '資料結構 - 使用C語言', '陳會安', 520, '資料結構', '2016-04-01'),
	('P0002', 'Java程式設計入門與實作', '陳會安', 550, '程式設計', '2017-07-01'),
	('P0003', 'Scratch+fChart程式邏輯訓練', '陳會安', 350, '程式設計', '2017-04-01'),
	('W0001', 'PHP與MySQL入門與實作', '陳會安', 550, '網頁設計', '2016-09-01'),
	('W0002', 'jQuery Mobile與Bootstrap網頁設計', '陳會安', 500, '網頁設計', '2017-10-01');
/*!40000 ALTER TABLE `book` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
