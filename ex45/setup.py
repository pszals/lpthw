try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup
	
config = {

	'description': 'LPTHW_Exercise_45',
	'author': 'Philip Szalwinski',
	'download_url': 'Where to download it.',
	'author_email': 'pszalwinski@gmail.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['ex45'],
	'scripts': [],
	'name': 'projectname'
}

setup(**config)