try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup
	
config = {

<<<<<<< HEAD
	'description': 'Exercise 47',
=======
	'description': 'LPTHW_Exercise_45',
>>>>>>> 6672cc2071eb418a5acc17af5705da4a1df3cbda
	'author': 'Philip Szalwinski',
	'download_url': 'Where to download it.',
	'author_email': 'pszalwinski@gmail.com',
	'version': '0.1',
	'install_requires': ['nose'],
<<<<<<< HEAD
	'packages': ['ex47'],
=======
	'packages': ['ex45', 'ex44b'],
>>>>>>> 6672cc2071eb418a5acc17af5705da4a1df3cbda
	'scripts': [],
	'name': 'projectname'
}

setup(**config)