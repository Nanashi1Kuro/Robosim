from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from launch.actions import SetEnvironmentVariable
import os
from ament_index_python import get_package_share_directory
import launch.actions
import launch_ros.actions

def generate_launch_description():
    os.environ["TURTLEBOT3_MODEL"] = "burger"

    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory('turtlebot3_gazebo'),
                'launch/turtlebot3_world.launch.py'))
    )
    cartographer = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory('turtlebot3_cartographer'),
                'launch/cartographer.launch.py'))
    )
    navigation = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory('like_a_rumba_robot'),
                'launch/nav2.py'))
    )    
    controller = Node(
            package='like_a_rumba_robot',
            executable='move',
            name='move_controller'
        )
    return LaunchDescription([
	gazebo,
	launch.actions.TimerAction(
            actions = [cartographer
                ], period = 10.0),
	launch.actions.TimerAction(
            actions = [navigation
                ], period = 20.0),
        launch.actions.TimerAction(
            actions = [controller
                ], period = 30.0),
    ])
