import os
from glob import glob
from setuptools import setup

package_name = 'like_a_rumba_robot'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
         (os.path.join('share', package_name, 'launch'), 
         glob(os.path.join('launch', '*'))),
        
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='droppedout',
    maintainer_email='droppedout@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'move = like_a_rumba_robot.move:main'
        ],
    },
)
