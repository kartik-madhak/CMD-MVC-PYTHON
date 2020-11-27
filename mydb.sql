-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Nov 27, 2020 at 12:07 PM
-- Server version: 10.4.10-MariaDB
-- PHP Version: 7.3.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `mydb`
--

-- --------------------------------------------------------

--
-- Table structure for table `comments`
--

DROP TABLE IF EXISTS `comments`;
CREATE TABLE IF NOT EXISTS `comments` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `post_id` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `content` text DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `comments`
--

INSERT INTO `comments` (`id`, `post_id`, `user_id`, `content`, `created_at`, `updated_at`) VALUES
(6, 2, 1, '\nFUCK\nLATE', '2020-11-22 21:42:41', '2020-11-22 21:42:41'),
(5, 2, 1, '\nNice post\nReally liked it!', '2020-11-22 21:38:10', '2020-11-22 21:38:10');

-- --------------------------------------------------------

--
-- Table structure for table `notifications`
--

DROP TABLE IF EXISTS `notifications`;
CREATE TABLE IF NOT EXISTS `notifications` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `content` text DEFAULT NULL,
  `is_read` int(11) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `posts`
--

DROP TABLE IF EXISTS `posts`;
CREATE TABLE IF NOT EXISTS `posts` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `title` varchar(400) DEFAULT NULL,
  `content` text DEFAULT NULL,
  `allow_comments` int(11) DEFAULT NULL,
  `public_visibility` int(11) DEFAULT NULL,
  `tags` varchar(400) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `posts`
--

INSERT INTO `posts` (`id`, `user_id`, `title`, `content`, `allow_comments`, `public_visibility`, `tags`, `created_at`, `updated_at`) VALUES
(1, 1, 'New pOst', '\nnew post\nthis is my first [post\nhello world', 1, 1, 'new first', '2020-11-22 14:33:38', '2020-11-22 14:33:38'),
(2, 1, 'Second post', '\nThis post is much more organized than the previous one\nIt contains properly formatted content', 1, 1, 'second post', '2020-11-22 15:20:26', '2020-11-22 15:20:26'),
(3, 1, 'This is my third post', '\nThird post, much more organized, only for friends,\nno comments', 0, 0, 'friends private third', '2020-11-22 17:23:45', '2020-11-22 17:23:45'),
(4, 3, 'Post by arrow', '\nfdfg dskfhdsfh\nsfjdjskfh kds', 1, 1, 'post first', '2020-11-26 22:40:48', '2020-11-26 22:40:48');

-- --------------------------------------------------------

--
-- Table structure for table `post_likes`
--

DROP TABLE IF EXISTS `post_likes`;
CREATE TABLE IF NOT EXISTS `post_likes` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `post_id` varchar(400) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=29 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `post_likes`
--

INSERT INTO `post_likes` (`id`, `user_id`, `post_id`, `created_at`, `updated_at`) VALUES
(28, 3, '2', '2020-11-26 22:39:37', '2020-11-26 22:39:37'),
(25, 1, '2', '2020-11-22 21:20:00', '2020-11-22 21:20:00'),
(23, 1, '1', '2020-11-22 21:16:53', '2020-11-22 21:16:53');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
CREATE TABLE IF NOT EXISTS `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(400) DEFAULT NULL,
  `email` varchar(400) DEFAULT NULL,
  `description` text DEFAULT NULL,
  `passwordHash` varchar(400) DEFAULT NULL,
  `role` int(11) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `name`, `email`, `description`, `passwordHash`, `role`, `created_at`, `updated_at`) VALUES
(1, 'Kartik', 'kartikmadhak@gmail.com', '', 'ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f', 2, '2020-11-22 14:20:34', '2020-11-22 14:20:34'),
(2, 'arrow', 'arrow@gmail.com', '', 'ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f', 2, '2020-11-26 22:34:31', '2020-11-26 22:34:31'),
(3, 'arrow2', 'arrow@gmail.com', '', 'ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f', 2, '2020-11-26 22:36:26', '2020-11-26 22:36:26');

-- --------------------------------------------------------

--
-- Table structure for table `user_auths`
--

DROP TABLE IF EXISTS `user_auths`;
CREATE TABLE IF NOT EXISTS `user_auths` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `token` varchar(400) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=35 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `user_auths`
--

INSERT INTO `user_auths` (`id`, `user_id`, `token`, `created_at`, `updated_at`) VALUES
(1, 1, 'ad284400c18d299b8d38a831b10cd5f4', '2020-11-22 18:30:30', '2020-11-22 18:30:30'),
(2, 1, 'ad284400c18d299b8d38a831b10cd5f4', '2020-11-22 18:32:59', '2020-11-22 18:32:59'),
(3, 1, 'ad284400c18d299b8d38a831b10cd5f4', '2020-11-22 18:50:50', '2020-11-22 18:50:50'),
(4, 1, 'ad284400c18d299b8d38a831b10cd5f4', '2020-11-22 18:51:48', '2020-11-22 18:51:48'),
(5, 1, 'ad284400c18d299b8d38a831b10cd5f4', '2020-11-22 18:58:51', '2020-11-22 18:58:51'),
(6, 1, 'ad284400c18d299b8d38a831b10cd5f4', '2020-11-22 19:00:18', '2020-11-22 19:00:18'),
(7, 1, 'ad284400c18d299b8d38a831b10cd5f4', '2020-11-22 19:08:54', '2020-11-22 19:08:54'),
(8, 1, 'ad284400c18d299b8d38a831b10cd5f4', '2020-11-22 19:10:37', '2020-11-22 19:10:37'),
(9, 1, 'ad284400c18d299b8d38a831b10cd5f4', '2020-11-22 19:11:46', '2020-11-22 19:11:46'),
(10, 1, 'ad284400c18d299b8d38a831b10cd5f4', '2020-11-22 21:16:40', '2020-11-22 21:16:40'),
(11, 1, 'ad284400c18d299b8d38a831b10cd5f4', '2020-11-22 21:17:35', '2020-11-22 21:17:35'),
(12, 1, 'ad284400c18d299b8d38a831b10cd5f4', '2020-11-22 21:18:23', '2020-11-22 21:18:23'),
(13, 1, 'ad284400c18d299b8d38a831b10cd5f4', '2020-11-22 21:19:35', '2020-11-22 21:19:35'),
(14, 1, 'ad284400c18d299b8d38a831b10cd5f4', '2020-11-22 21:22:19', '2020-11-22 21:22:19'),
(15, 1, 'ad284400c18d299b8d38a831b10cd5f4', '2020-11-22 21:25:00', '2020-11-22 21:25:00'),
(16, 1, 'ad284400c18d299b8d38a831b10cd5f4', '2020-11-22 21:29:49', '2020-11-22 21:29:49'),
(17, 1, 'ad284400c18d299b8d38a831b10cd5f4', '2020-11-22 21:31:13', '2020-11-22 21:31:13'),
(18, 1, 'ad284400c18d299b8d38a831b10cd5f4', '2020-11-22 21:32:12', '2020-11-22 21:32:12'),
(19, 1, 'ad284400c18d299b8d38a831b10cd5f4', '2020-11-22 21:32:52', '2020-11-22 21:32:52'),
(20, 1, 'ad284400c18d299b8d38a831b10cd5f4', '2020-11-22 21:35:22', '2020-11-22 21:35:22'),
(21, 1, 'ad284400c18d299b8d38a831b10cd5f4', '2020-11-22 21:37:16', '2020-11-22 21:37:16'),
(22, 1, 'ad284400c18d299b8d38a831b10cd5f4', '2020-11-22 21:42:28', '2020-11-22 21:42:28'),
(23, 1, 'ad284400c18d299b8d38a831b10cd5f4', '2020-11-22 21:43:04', '2020-11-22 21:43:04'),
(24, 1, 'ad284400c18d299b8d38a831b10cd5f4', '2020-11-22 21:43:26', '2020-11-22 21:43:26'),
(25, 1, 'ad284400c18d299b8d38a831b10cd5f4', '2020-11-22 21:44:47', '2020-11-22 21:44:47'),
(26, 1, 'ad284400c18d299b8d38a831b10cd5f4', '2020-11-22 21:45:33', '2020-11-22 21:45:33'),
(27, 1, 'ad284400c18d299b8d38a831b10cd5f4', '2020-11-22 21:47:21', '2020-11-22 21:47:21'),
(28, 1, 'ad284400c18d299b8d38a831b10cd5f4', '2020-11-22 21:58:06', '2020-11-22 21:58:06'),
(29, 1, 'ad284400c18d299b8d38a831b10cd5f4', '2020-11-22 22:37:24', '2020-11-22 22:37:24'),
(30, 1, 'ad284400c18d299b8d38a831b10cd5f4', '2020-11-22 22:38:37', '2020-11-22 22:38:37'),
(31, 1, 'ad284400c18d299b8d38a831b10cd5f4', '2020-11-22 22:40:21', '2020-11-22 22:40:21'),
(32, 1, 'ad284400c18d299b8d38a831b10cd5f4', '2020-11-22 22:42:51', '2020-11-22 22:42:51'),
(33, 1, 'ad284400c18d299b8d38a831b10cd5f4', '2020-11-22 22:50:56', '2020-11-22 22:50:56'),
(34, 3, 'd6741db0d909396d389f69a58d4f9501', '2020-11-26 22:36:26', '2020-11-26 22:36:26');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
