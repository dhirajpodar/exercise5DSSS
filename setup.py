from distutils.core import setup
from setuptools import find_packages

setup(
    name='snowflake',
    version='0.1',
    author='Dhiraj Poddar',
    author_email='dhiraj.poddar@fau.de',
    packages=find_packages(),
    install_requires=['numpy', 'turtles'],
)