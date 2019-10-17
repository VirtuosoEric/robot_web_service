#!/bin/bash

source /opt/ros/melodic/setup.bash
source /home/nano/catkin_ws/devel/setup.bash

export ROS_IP=$(ip route get 1.2.3.4 | awk '{print $7}')
export ROS_MASTER_URI=http://192.168.31.100:11311/ 
echo y|rosclean purge

roslaunch realsense2_camera rs_t265.launch