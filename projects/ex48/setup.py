try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Input scanner project',
    'author': 'Egor_P',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['InputScanner'],
    'scripts': '',
    'name': 'inputScanner'
}

setup(**config)
