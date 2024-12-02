from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='turtlesim',
            executable='turtlesim_node',
            name='turtlesim'
        ),
        Node(
            package='turtlesim_follower',
            executable='master',
            name='master'
        ),
        Node(
            package='turtlesim_follower',
            executable='slave',
            name='slave'
        ),
    ])
