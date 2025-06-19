#object_following_ros2/launch/laptop_launch.py
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='object_following_ros2',
            executable='detection_node',
            name='detection_node',
            output='screen'
        )
    ])


"""
source ~/ros2_ws/install/setup.bash
export ROS_DOMAIN_ID=0
export ROS_LOCALHOST_ONLY=0
ros2 launch object_following_ros2 laptop_launch.py
"""