try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup
	
config =  {
	'description': 'My first py project',
	'author': 'Egor_P',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['FirstProject'],
	'scripts': '',
	'name': 'firstProject'
}

setup(**config)