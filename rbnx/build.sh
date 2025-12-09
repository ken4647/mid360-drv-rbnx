#!/bin/bash
git submodule update --init

cd src/livox_ros_driver2
git apply ../livox_ros_driver2.patch

# build.sh
source /opt/ros/humble/setup.sh
./build.sh humble