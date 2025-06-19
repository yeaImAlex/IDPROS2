from setuptools import setup

package_name = 'object_following_ros2'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name, f'{package_name}/utils'],
    data_files=[
        ('share/ament_index/resource_index/packages',
         ['resource/' + package_name]),
         ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Alex Chan',
    maintainer_email='lolpokian92@gmail.com',
    description='object following robot with ROS 2',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'detection_node = object_following_ros2.detection_node:main',
            'command_listener = object_following_ros2.command_listener:main',
            'motor_node = object_following_ros2.motor_node:main',
            'mechanism_node = obejct_following_ros2.mechanism_node:main',
        ],
    },
)