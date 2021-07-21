from os.path import join, dirname
from setuptools import setup, find_packages

setup(
    name='week3',
    version='1.0',
    description='Work with iterator package',
    author='Kirill Pechurin',
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'README.md')).read()
)
