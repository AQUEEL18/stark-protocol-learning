import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'my_first_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='aqueel18',
    maintainer_email='aqueel18@todo.todo',
    description='My first ROS 2 package',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'my_node = my_first_pkg.my_node:main',
            'subscriber_node = my_first_pkg.subscriber_node:main',
            'param_node = my_first_pkg.param_node:main',
            'add_server = my_first_pkg.add_server:main',
            'add_client = my_first_pkg.add_client:main',
        ],
    },
)