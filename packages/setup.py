# -*- coding: utf-8 -*-

# DO NOT EDIT THIS FILE!
# This file has been autogenerated by dephell <3
# https://github.com/dephell/dephell

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

readme = ''

setup(
    long_description=readme,
    name='name-that-hash',
    version='0.6.0',
    description='The Modern Hash Identifcation System',
    python_requires='==3.*,>=3.7.0',
    author='brandon',
    author_email='brandon@skerritt.blog',
    license='GPL-3.0-or-later',
    entry_points={
        "console_scripts": [
            "nth = name_that_hash.runner:main",
            "name-that-hash = name_that_hash.runner:main"
        ]
    },
    packages=['Name_That_Hash'],
    package_dir={"": "."},
    package_data={},
    install_requires=[
        'click==7.*,>=7.1.2', 'loguru==0.*,>=0.5.3', 'rich==9.*,>=9.9.0'
    ],
    extras_require={"dev": ["pytest==5.*,>=5.2.0"]},
)
