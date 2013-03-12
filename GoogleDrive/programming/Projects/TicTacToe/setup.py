try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup
	
config = {

	'description': 'Unbeatable Tic Tac Toe',
	'author': 'Philip Szalwinski',
	'download_url': 'Where to download it.',
	'author_email': 'pszalwinski@gmail.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['NAME'],
	'scripts': [],
	'name': 'tictactoe'
}

setup(**config)