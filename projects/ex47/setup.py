try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup
	
config =  {
	'description': 'My second py project',
	'author': 'Egor_P',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['ex47'],
	'scripts': '',
	'name': 'ex47'
}

setup(**config)