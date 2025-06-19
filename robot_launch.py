#object_following_ros2/launch/robot_launch.py
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='object_following_ros2',
            executable='command_listener',
            name='command_listener',
            output='screen'
        ),
        Node(
            package='object_following_ros2',
            executable='motor_node',
            name='motor_node',
            output='screen'
        ),
        Node(
            package='object_following_ros2',
            executable='mechanism_node',
            name='mechanism_node',
            output='screen'
        )
    ])

"""
source ~/ros2_ws/install/setup.bash
export ROS_DOMAIN_ID=0
export ROS_LOCALHOST_ONLY=0
ros2 launch object_following_ros2 robot_launch.pys
"""