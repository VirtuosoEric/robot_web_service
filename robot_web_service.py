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
        return open('home.html')
    @cherrypy.expose
    def start_roscore(self):
        self.laucher.launch_roscore()
        return 'start roscore'

    @cherrypy.expose
    def kill_roscore(self):
        self.laucher.kill_roscore()
        return 'kill roscore'

    @cherrypy.expose
    def start_carto_3d(self):
        self.laucher.launch_carto_3d()
        return 'start catographer 3D SLAM'

    @cherrypy.expose
    def kill_carto_3d(self):
        self.laucher.kill_carto_3d()
        return 'kill catographer 3D SLAM'

    @cherrypy.expose
    def start_carto_3d_vo(self):
        self.laucher.launch_carto_3d_vo()
        return 'start catographer 3D SLAM with VO'

    @cherrypy.expose
    def kill_carto_3d_vo(self):
        self.laucher.kill_carto_3d_vo()
        return 'kill catographer 3D SLAM with VO'

if __name__ == "__main__":
    cherrypy.quickstart(RobotWeb(), '/',config)


