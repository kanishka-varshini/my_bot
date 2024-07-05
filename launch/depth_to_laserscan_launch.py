from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='realsense2_camera',
            executable='rs_camera.launch.py',
            output='screen',
            parameters=[{'enable_depth': True}],
        ),
        Node(
            package='depthimage_to_laserscan',
            executable='depthimage_to_laserscan_node',
            name='depthimage_to_laserscan',
            output='screen',
            parameters=[{
                'range_min': 0.1,
                'range_max': 10.0,
                'scan_time': 0.1,
                'output_frame_id': 'camera_depth_frame',
                'scan_height': 10,
            }],
            remappings=[
                ('depth', '/camera/depth/image_rect_raw'),
                ('depth_camera_info', '/camera/depth/camera_info'),
                ('scan', '/scan'),
            ],
        ),
        Node(
            package='slam_toolbox',
            executable='sync_slam_toolbox_node',
            name='slam_toolbox',
            output='screen',
            parameters=[{
                'use_sim_time': False,
            }],
        )
    ])
