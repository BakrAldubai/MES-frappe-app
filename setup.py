from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in mes/__init__.py
from mes import __version__ as version

setup(
	name="mes",
	version=version,
	description="this app is for monitoring and evaluating projects ",
	author="BakrAldubai",
	author_email="eng.bakraldubai@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
