#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import cherrypy
import threading
from launcher import Launcher

config = {
    'global' : {
        'server.socket_host' : '0.0.0.0',
        'server.socket_port' : 8080
    }
}

class RobotWeb(object):

    def __init__(self):
        self.laucher = Launcher()

    @cherrypy.expose
    def index(self):
        return "Hello! We are Virtuoso Robotics!"

    @cherrypy.expose
    def start_roscore(self):
        self.laucher.launch_roscore()
        return 'start roscore'

    @cherrypy.expose
    def kill_roscore(self):
        self.laucher.kill_roscore()
        return 'kill roscore'

    @cherrypy.expose
    def start_roslaunch(self):
        self.laucher.roslauncher()
        return 'start roslaunch'

    @cherrypy.expose
    def kill_roslaunch(self):
        self.laucher.kill_roslaunch()
        return 'kill roslaunch'

if __name__ == "__main__":
    cherrypy.quickstart(RobotWeb(), '/',config)


