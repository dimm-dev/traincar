import os
import setuptools

setuptools.setup(
    name = 'traincar',
    version = '0.1',
    author = "dimm",
    author_email = "none",
    description = "Reinforcement learning research project",
    long_description = open('README.md').read(),
    long_description_content_type = "text/markdown",
    url = "https://github.com/dimm-dev/traincar",
    packages = setuptools.find_packages(),
    package_dir = {'traincar' : 'traincar'},
    package_data = {'' : ['assets/*']},
    classifiers = [
	"Programming Language :: Python :: 3",
	"License :: OSI Approved :: MIT License",
	"Operating System :: OS Independent"
    ],
    entry_points = {
	    "console_scripts": [
	        "traincar=traincar.start:script_run"
        ]
    },
    requires = ['keras', 'pygame', 'setuptools'],
    install_requires=['keras', 'pygame'],
    data_files = [
	('share/applications/', ['traincar/assets/traincar.desktop']),
	('share/pixmaps/', ['traincar/assets/train-car.png']),
    ],
)
