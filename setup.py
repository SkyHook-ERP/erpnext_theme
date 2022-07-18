from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in erpnext_theme/__init__.py
from erpnext_theme import __version__ as version

setup(
	name="erpnext_theme",
	version=version,
	description="Theme for Skyhook ERP",
	author="Pegas Technologies Solutions Ltd",
	author_email="admin@pegas.io",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
