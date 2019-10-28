#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import cherrypy
import subprocess
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
        return open('web/home.html')

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
        return open('web/cartographer_3d.html')

    @cherrypy.expose
    def kill_carto_3d(self):
        self.laucher.kill_carto_3d()
        return open('web/home.html')

    @cherrypy.expose
    def start_carto_3d_vo(self):
        self.laucher.launch_carto_3d_vo()
        return open('web/cartogrpher_3d_vo.html')

    @cherrypy.expose
    def kill_carto_3d_vo(self):
        self.laucher.kill_carto_3d_vo()
        return open('web/home.html')

    @cherrypy.expose
    def start_gmapping_vo(self):
        self.laucher.launch_gmapping_vo()
        return open('web/gmapping_vo.html')

    @cherrypy.expose
    def kill_gmapping_vo(self):
        self.laucher.kill_gmapping_vo()
        return open('web/home.html')

    @cherrypy.expose
    def start_amcl_vo(self):
        self.laucher.launch_amcl_vo()
        return open('web/amcl_vo.html')

    @cherrypy.expose
    def kill_amcl_vo(self):
        self.laucher.kill_amcl_vo()
        return 'kill AMCL with VO'

    @cherrypy.expose
    def save_map(self,map_name):
        subprocess.Popen(['bash /home/pn60/robot_web_service/bash_script/save_map.bash ' + map_name],shell=True)
        return open('web/gmapping_vo.html')

if __name__ == "__main__":
    cherrypy.quickstart(RobotWeb(), '/',config)


