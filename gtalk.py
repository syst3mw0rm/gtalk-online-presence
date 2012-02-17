#!/usr/bin/python
# -*- coding: utf-8 -*-

import tornado
import json
import MySQLdb
import logging
import os
import sys
import time

from django.utils.encoding import smart_str
from tornado.options import define, options
from PyGtalkRobot import GtalkRobot

define("config")
define("port", type=int)
define("mysql_hostname")
define("mysql_user")
define("mysql_password")
define("mysql_database")
define("gtalk_username")
define("gtalk_password")

path = os.path.join(os.path.dirname(__file__), "settings.py")
tornado.options.parse_config_file(path)

connMySQL = MySQLdb.connect(options.mysql_hostname, options.mysql_user, options.mysql_password, options.mysql_database, charset = "utf8", use_unicode = True)
############################################################################################################################

class SampleBot(GtalkRobot):
   
    def command_100_default(self, user, message, args):
        '''.*?(?s)(?m)'''
        self.replyMessage(user, time.strftime("%Y-%m-%d %a %H:%M:%S", time.gmtime()))

    def enterIntoDB(self, presence):
	query = """INSERT INTO onlineStats (status , from_id, resource ,type, getShow) values (  '%s' , '%s', '%s', '%s', '%s')""" % (presence.getStatus(), presence.getFrom().getStripped() , presence.getFrom().getResource(), presence.getType(), presence.getShow() );
	self.cur = connMySQL.cursor()
	try:
		self.cur.execute(query)
	except:
		print "Error inserting into database"
		print query	

############################################################################################################################
if __name__ == "__main__":
    bot = SampleBot()
    bot.setState('available', "Simple Gtalk Robot")
    bot.start(options.gtalk_username, options.gtalk_password)
