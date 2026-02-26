import glob
from setuptools import setup

package_name = 'turtlebot3_dqn'

setup(
    name=package_name,
    version='1.0.3',
    packages=['turtlebot3_dqn'],  # inner folder is the Python module
    data_files=[
        # Required for ROS 2 package registration
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # Include launch files if you have any
        ('share/' + package_name + '/launch', glob.glob('launch/*.py')),
        # Include resources folder
        ('share/' + package_name + '/resources', glob.glob('resources/*')),
        # Include saved_model folder
        ('share/' + package_name + '/saved_model', glob.glob('saved_model/*')),
    ],
    install_requires=[
        'setuptools',
        'launch',
        'tensorflow==2.19.0',
        'numpy==1.26.4',
        'scipy==1.10.1',
        'keras==3.9.2',
    ],
    zip_safe=True,
    author='Gilbert, Ryan Shim, ChanHyeong Lee, Hyungyu Kim',
    author_email='kkjong@robotis.com, N/A, dddoggi1207@gmail.com, kimhg@robotis.com',
    maintainer='Pyo',
    maintainer_email='pyo@robotis.com',
    description='ROS 2 packages for TurtleBot3 machine learning',
    license='Apache 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'action_graph = turtlebot3_dqn.action_graph:main',
            'dqn_agent = turtlebot3_dqn.dqn_agent:main',
            'dqn_environment = turtlebot3_dqn.dqn_environment:main',
            'dqn_gazebo = turtlebot3_dqn.dqn_gazebo:main',
            'dqn_test = turtlebot3_dqn.dqn_test:main',
            'result_graph = turtlebot3_dqn.result_graph:main',
            'cube_goals = turtlebot3_dqn.random_goals:main',
        ],
    },
)
