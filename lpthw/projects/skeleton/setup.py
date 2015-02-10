try:
	from setuptools import setuptools
except ImportError:
	from distutils.core import setuptools

config = {
	'description': 'My Project',
	'author': 'Jon Gore',
	'URL': 'URL to get in at.',
	'download_url': 'Where to download it',
	'author_email': 'jongore@outlook.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['NAME'],
	'scripts': [],
	'name': 'projectname'
}

setup(**config)

