from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in vitalpbx/__init__.py
from vitalpbx import __version__ as version

setup(
	name='vitalpbx',
	version=version,
	description='Something',
	author='Someone',
	author_email='someone@somewhere.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
