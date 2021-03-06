from setuptools import setup, find_packages
from os import path
from io import open
here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='LeetCode',  # Required
    version='1.0.0',  # Required
    description='pratice code',  # Optional
    long_description=long_description,  # Optional
    long_description_content_type='text/markdown',  # Optional (see note above)
    author='yenchen',  # Optional
    author_email='yenchen0416@gmail.com',  # Optional
    classifiers=[  # Optional
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='leetcode, python',  # Optional
    packages=find_packages(exclude=['importlib']),
)
