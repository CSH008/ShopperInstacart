-- phpMyAdmin SQL Dump
-- version 4.9.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 22, 2019 at 09:05 AM
-- Server version: 10.4.6-MariaDB
-- PHP Version: 7.3.8

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `easyhour_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `id` int(11) NOT NULL,
  `name` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `phonenumber` varchar(50) NOT NULL,
  `password` varchar(155) NOT NULL,
  `remember_token` varchar(100) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`id`, `name`, `email`, `phonenumber`, `password`, `remember_token`, `created_at`, `updated_at`) VALUES
(1, 'Rabbit', '', '7868179221', '$2y$10$BUIpM/r.FHL6p8NDKCrIP.jlqLE0UZEiYgVf.Yw4zEEHFe103gAOm', NULL, '2019-11-16 08:49:12', '2019-11-16 07:54:58');

-- --------------------------------------------------------

--
-- Table structure for table `contactus`
--

CREATE TABLE `contactus` (
  `id` int(11) NOT NULL,
  `contact_email` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `contactus`
--

INSERT INTO `contactus` (`id`, `contact_email`) VALUES
(1, 'vpcflex@gmail.com');

-- --------------------------------------------------------

--
-- Table structure for table `failed_jobs`
--

CREATE TABLE `failed_jobs` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `connection` text COLLATE utf8mb4_unicode_ci NOT NULL,
  `queue` text COLLATE utf8mb4_unicode_ci NOT NULL,
  `payload` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `exception` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `failed_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `messages`
--

CREATE TABLE `messages` (
  `id` int(11) NOT NULL,
  `sms_to_newuser` text NOT NULL,
  `sms_to_allusers` text NOT NULL,
  `email_to_allusers` text NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `messages`
--

INSERT INTO `messages` (`id`, `sms_to_newuser`, `sms_to_allusers`, `email_to_allusers`, `created_at`, `updated_at`) VALUES
(1, 'Welcome New User', 'Hi, All Users Ok aaabcdefg', 'Hi, All Users Ok aaabcd', NULL, '2019-11-21 19:06:35');

-- --------------------------------------------------------

--
-- Table structure for table `migrations`
--

CREATE TABLE `migrations` (
  `id` int(10) UNSIGNED NOT NULL,
  `migration` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `batch` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `migrations`
--

INSERT INTO `migrations` (`id`, `migration`, `batch`) VALUES
(1, '2014_10_12_000000_create_users_table', 1),
(2, '2014_10_12_100000_create_password_resets_table', 1),
(3, '2019_08_19_000000_create_failed_jobs_table', 1),
(4, '2019_05_03_000001_create_customer_columns', 2),
(5, '2019_05_03_000002_create_subscriptions_table', 2);

-- --------------------------------------------------------

--
-- Table structure for table `password_resets`
--

CREATE TABLE `password_resets` (
  `email` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `token` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `principles`
--

CREATE TABLE `principles` (
  `id` int(11) NOT NULL,
  `content` text DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `principles`
--

INSERT INTO `principles` (`id`, `content`, `created_at`, `updated_at`) VALUES
(1, 'Dashboard Content 1', '2019-11-16 08:51:10', '2019-11-20 02:04:53'),
(2, 'Dashboard Content 2', '2019-11-17 08:51:10', '2019-11-17 08:51:10'),
(3, 'Dashboard Content 3', '2019-11-18 08:51:10', '2019-11-17 08:51:10'),
(4, 'Dashboard Content 4', '2019-11-19 08:51:10', '2019-11-16 08:51:10'),
(13, 'Dashboard Content 5', '2019-11-20 02:01:37', '2019-11-20 02:04:42'),
(14, 'Dashboard Content 6', '2019-11-20 02:05:10', '2019-11-20 02:05:10');

-- --------------------------------------------------------

--
-- Table structure for table `stripe_option`
--

CREATE TABLE `stripe_option` (
  `id` int(11) NOT NULL,
  `stripe_pub_key` text NOT NULL,
  `stripe_secret_key` text NOT NULL,
  `amount` int(11) NOT NULL,
  `currency` varchar(10) NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `stripe_option`
--

INSERT INTO `stripe_option` (`id`, `stripe_pub_key`, `stripe_secret_key`, `amount`, `currency`, `created_at`, `updated_at`) VALUES
(1, 'pk_live_KUq6p0AyXcWGPQHcXh4i6QLk', 'sk_live_Tpwv1DrXmx2gVJpSa2grD1Aa', 1999, 'USD', NULL, '2019-11-16 09:49:35');

-- --------------------------------------------------------

--
-- Table structure for table `subscriptions`
--

CREATE TABLE `subscriptions` (
  `id` int(11) NOT NULL,
  `userid` int(11) NOT NULL,
  `started_date` timestamp NULL DEFAULT NULL,
  `amount` int(11) NOT NULL,
  `currency` varchar(10) NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `name` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `phonenumber` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `email` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `password` varchar(155) COLLATE utf8mb4_unicode_ci NOT NULL,
  `location` varchar(155) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `remember_token` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `ip_address` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `extension` varchar(10) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `is_running` int(2) NOT NULL DEFAULT 0,
  `active` tinyint(1) NOT NULL DEFAULT 0,
  `subscription_expired` tinyint(1) NOT NULL DEFAULT 1,
  `subscription_started_date` timestamp NULL DEFAULT NULL,
  `subscription_end_date` timestamp NULL DEFAULT NULL,
  `paid_amount` int(11) NOT NULL DEFAULT 0,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `admin_id` int(11) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `name`, `phonenumber`, `email`, `password`, `location`, `remember_token`, `ip_address`, `extension`, `is_running`, `active`, `subscription_expired`, `subscription_started_date`, `subscription_end_date`, `paid_amount`, `created_at`, `updated_at`, `admin_id`) VALUES
(1, 'Rabbit', '7868179221', 'redhat2@gmail.com', '$2y$10$pASaH4ciDvJIT1haUpv4puTTfee3/SkKqA.WH4Gzx0k9SpW7oBZuO', '', '2q54DWqN3tFNcfX4Y3L2yqbyZwxyUXw5HBVQrsSUNAWgQ0XgbZ1CX9SgNLfC', 'localhost', 'exe', 0, 1, 1, '2019-11-09 16:00:00', '2019-11-16 16:00:00', 0, '2019-11-06 12:30:31', '2019-11-20 01:15:06', 0),
(4, 'suju', '1554224820', 'redhat4@gmail.com', '$2y$10$1q0/tfGSsMJl94Pey8EnGOarpwP1ze/ElksyXdgvcfKLR1vMMp1iC', '', NULL, '52.206.230.16 ', NULL, 0, 1, 1, NULL, NULL, 0, '2019-11-05 17:56:07', '2019-11-10 07:52:30', 0),
(5, 'zch', '1504007648', 'redhat3@gmail.com', '$2y$10$wLabZfY6cKcfSGJhQpMUvunvWXgnh3dciU5inLC6V6JwoFAmwmO1q', '', NULL, '52.206.230.16 ', NULL, 0, 0, 1, NULL, NULL, 0, '2019-11-06 08:38:54', '2019-11-15 23:53:48', 0),
(10, 'Rabbit', '4047236476', 'redhat1@gmail.com', '$2y$10$jwk10cG67Q.S0sum69mxdujcTvuz4KGFGxBhjbxsVzhmrVboDcm6a', NULL, NULL, '52.206.230.16 ', NULL, 0, 1, 1, NULL, NULL, 0, '2019-11-12 15:56:17', '2019-11-12 15:56:17', 0);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `phonenumber` (`phonenumber`);

--
-- Indexes for table `contactus`
--
ALTER TABLE `contactus`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `failed_jobs`
--
ALTER TABLE `failed_jobs`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `messages`
--
ALTER TABLE `messages`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `migrations`
--
ALTER TABLE `migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `password_resets`
--
ALTER TABLE `password_resets`
  ADD KEY `password_resets_email_index` (`email`);

--
-- Indexes for table `principles`
--
ALTER TABLE `principles`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `stripe_option`
--
ALTER TABLE `stripe_option`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `subscriptions`
--
ALTER TABLE `subscriptions`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `phonenumber_unique` (`phonenumber`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin`
--
ALTER TABLE `admin`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `contactus`
--
ALTER TABLE `contactus`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `failed_jobs`
--
ALTER TABLE `failed_jobs`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `messages`
--
ALTER TABLE `messages`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `migrations`
--
ALTER TABLE `migrations`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `principles`
--
ALTER TABLE `principles`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT for table `stripe_option`
--
ALTER TABLE `stripe_option`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `subscriptions`
--
ALTER TABLE `subscriptions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
