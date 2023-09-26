import setuptools
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name = 'invoiceTW',
    version = '0.1.0',
    author = 'jeng',
    author_email = 'tsjeng45@yahoo.com.tw',
    description = 'Taiwan invoice number',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url = 'https://github.com/tsjeng45/invoiceTW',
    packages=setuptools.find_packages(),
    keywords = ['invoice'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)
