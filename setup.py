from setuptools import setup, find_packages

package_name = 'arduino_interface'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='rechner2',
    maintainer_email='sth4124@thi.de',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        'arduino_command_node = arduino_interface.arduino_command_node:main',
        'command_publisher_node = arduino_interface.command_publisher:main', ],
    },
)
