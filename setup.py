#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='pvl',
    version='1.0.0-alpha.7',
    description='Python implementation of PVL (Parameter Value Language)',
    long_description=readme + '\n\n' + history,
    author='The PlanetaryPy Developers',
    author_email='trevor@heytrevor.com',
    url='https://github.com/planetarypy/pvl',
    packages=[
        'pvl',
    ],
    package_dir={'pvl':
                 'pvl'},
    include_package_data=True,
    license="BSD",
    zip_safe=False,
    keywords='pvl',
    classifiers=[
        'Development Status :: Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    entry_points={"console_scripts": [
        "pvl_translate = pvl.pvl_translate:main",
        "pvl_validate= pvl.pvl_validate:main",
    ], }
)
