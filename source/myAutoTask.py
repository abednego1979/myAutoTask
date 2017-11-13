# -*- coding: utf-8 -*-

#Python 3.5.x

#V0.01

import os
import configparser


#add code to auto start task


#read config and get which task should be start
#start one or more sub-process to run
#    in the sub-process
#        start a new sub-process to run task, and this process used to demo.
#        in the demo, download code from github and check if there is some new change. if yes, restart the task process.
#        the demo also should check task process state to make sure the task run ok


cf = configparser.ConfigParser()
cf.read("base.conf")

cf.get('task01', "taskname")