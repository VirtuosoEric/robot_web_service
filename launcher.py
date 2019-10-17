import subprocess
import os,sys,time
import signal

class Launcher:

    def __init__(self):
        self.current_path = os.getcwd()
        # print self.current_path

    def launch_roscore(self):
        subprocess.Popen(['bash /home/nano/robot_web_service/start_roscore.bash'],shell=True)

    def kill_roscore(self):
        subprocess.call(['pkill', '-f', 'roscore'])

    def roslauncher(self):
        subprocess.Popen(['bash /home/nano/robot_web_service/start_roslauch.bash'],shell=True)

    def kill_roslaunch(self):
        subprocess.call(['pkill', '-f', 'sample_nodelet_all.launch'])

    def launch_realsense(self):
        subprocess.Popen(['bash /home/nano/robot_web_service/start_realsense.bash'],shell=True)

    def kill_realsense(self):
        subprocess.call(['pkill', '-f', 'rs_t265.launch'])


if __name__ == "__main__":
    laucher = Launcher()
    laucher.launch_realsense()
    time.sleep(5)
    laucher.kill_realsense()