
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Frekans is network protocol definition library',
    'author': 'Mahmut Bulut',
    'url': 'http://mahmutbulut.com/frekans',
    'download_url': 'http://mahmutbulut.com/frekans/download',
    'author_email': 'mahmutbulut0@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['frekans'],
    'scripts': [],
    'name': 'frekans'
}

setup(**config)
