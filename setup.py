#!/usr/bin/env python
# from distutils.core import setup
from setuptools import setup


setup(
    name='uz-api',
    version='1.1',
    description='Python UZ API',
    author='Anton Adamiv',
    author_email='detonavomek@gmail.com',
    url='https://github.com/1d20/uz-api',
    packages=['uz_api'],
    license='MIT',
    install_requires=['aiohttp==0.21.6', 'aiotg==0.7.1', 'datadog==0.11.0', 'dateutils==0.6.6'],
    python_requires='>=3',
)
