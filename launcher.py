import subprocess
import os,sys,time
import signal
import requests

class Launcher:

    def __init__(self):
        self.current_path = os.getcwd()
        # print self.current_path

    def launch_roscore(self):
        subprocess.Popen(['bash /home/pn60/robot_web_service/start_roscore.bash'],shell=True)

    def kill_roscore(self):
        subprocess.call(['pkill', '-f', 'roscore'])

    def launch_carto_3d(self):
        subprocess.Popen(['bash /home/pn60/robot_web_service/start_carto_3d.bash'],shell=True)

    def kill_carto_3d(self):
        subprocess.call(['pkill', '-f', 'slam_test.launch'])

    def launch_carto_3d_vo(self):
        subprocess.Popen(['bash /home/pn60/robot_web_service/start_carto_3d_vo.bash'],shell=True)
        time.sleep(1)
        s = requests.Session()
        r = s.get('http://192.168.31.160:8080/start_realsense')
        print r.text

    def kill_carto_3d_vo(self):
        subprocess.call(['pkill', '-f', 'carto3d_vo.launch'])
        time.sleep(1)
        s = requests.Session()
        r = s.get('http://192.168.31.160:8080/kill_realsense')
        print r.text


if __name__ == "__main__":
    laucher = Launcher()
    laucher.launch_carto_3d_vo()
    time.sleep(15)
    laucher.kill_carto_3d_vo()