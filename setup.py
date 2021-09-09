#!/usr/bin/python3

from setuptools import setup

with open('README.rst') as f:
    long_description = f.read()

setup(
    name='py-iir-filter',
    version='1.0.5',
    description="Fast realtime IIR filter",
    long_description=long_description,
    author='Bernd Porr',
    author_email='mail@berndporr.me.uk',
    py_modules=['iir_filter'],
    install_requires=['numpy'],
    zip_safe=False,
    url='https://github.com/berndporr/py-iir-filter',
    license='GPL 3.0',
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
    ],
)
