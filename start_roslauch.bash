#!/bin/bash

source /opt/ros/kinetic/setup.bash
source /home/eric/catkin_ws/devel/setup.bash

export ROS_IP=$(ip route get 1.2.3.4 | awk '{print $7}')
export ROS_MASTER_URI=http://$ROS_IP:11311/ 
echo y|rosclean purge
roslaunch sample_nodelet sample_nodelet_all.launch