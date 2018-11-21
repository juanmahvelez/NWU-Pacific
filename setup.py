#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

requirements = [
    'gensim',
    'nltk',
    'spacy',
    'pandas',
    'numpy',
    'MarkupSafe',
    'jsonschema',
    'webencodings',
    'configparser',
    'ipykernel',
    'jupyter',
    'azure',
    'tables',
    'scikit-learn',
    'xgboost>=0.80',
    'matplotlib==2.1.2',
    'seaborn'
]

extras_require = {
    'dev': ['pytest', 'flake8']
}

setup(
    name='NWU-Pacific',
    version='0.1.0',
    description='Machine Learning For Consumer Complaints',
    long_description=readme,
    author='Juan Hernandez, Jeff Jarrard, Dale Mitchell, Simon Wilson',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
    extras_require=extras_require,
    zip_safe=False,
    keywords='pacific',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],
)
