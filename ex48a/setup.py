try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup
	
config = {

	'description': 'Exercise 48',
	'description': 'LPTHW_Exercise_48',
	'author': 'Philip Szalwinski',
	'download_url': 'Where to download it.',
	'author_email': 'pszalwinski@gmail.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['ex48'],
	'scripts': [],
	'name': 'projectname'
}

setup(**config)