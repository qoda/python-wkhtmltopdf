from setuptools import setup, find_packages

setup(
    name='wkhtmltopdf',
    version='0.1',
    description='Simple python wrapper for wkhtmltopdf',
    long_description = open('README.rst', 'r').read() + open('AUTHORS.rst', 'r').read() + open('CHANGELOG.rst', 'r').read(),
    author='Jonathan Bydendyk',
    author_email='jpbydendyk@gmail.com',
    license='BSD',
    url='http://github.com/qoda/python-wkhtmltopdf',
    packages = find_packages('src'),
    dependency_links = [],
    install_requires = [],
    include_package_data=True,
    classifiers = [
        "Programming Language :: Python",
        "License :: OSI Approved :: BSD License",
        "Development Status :: 4 - Beta",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
)