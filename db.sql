CREATE TABLE `onlineStats` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `status` text,
  `from_id` text,
  `resource` text,
  `timestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `type` text,
  `getShow` text,
  UNIQUE KEY `id` (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=latin1
