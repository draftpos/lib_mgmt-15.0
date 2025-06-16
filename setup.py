from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in lib_mgmt/__init__.py
from lib_mgmt import __version__ as version

setup(
	name="lib_mgmt",
	version=version,
	description="Library Management",
	author="Ketan Patel",
	author_email="contact@solufy.in",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
