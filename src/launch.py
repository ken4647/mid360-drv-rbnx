from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='livox_ros_driver2',
            executable='livox_ros_driver2_node',
            name='livox_driver',
            parameters=[{
                'xfer_format': 0,
                'frame_id': 'livox_frame',
                # 'multi_topic': 0,
                'user_config_path': '/home/orin/.robonix/packages/mid360-drv-rbnx/src/livox_ros_driver2/config/MID360s_config.json',  # 如果有配置文件，填路径
            }],
            remappings=[
                ('/livox/lidar', '/scanner/cloud'),  # 话题重映射
                ('/livox/imu', '/scanner/imu'),   # IMU话题
            ]
        )
    ])