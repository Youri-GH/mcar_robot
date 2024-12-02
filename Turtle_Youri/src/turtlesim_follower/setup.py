from setuptools import find_packages, setup

package_name = 'turtlesim_follower'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/turtles_follow_launch.py']),  # Ajout du fichier de lancement
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='insa',
    maintainer_email='youri.beideler@insa-strasbourg.fr',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'master = turtlesim_follower.master:main',
            'slave = turtlesim_follower.slave:main',
        ],
    },

)
