NO LONGER MAINTAINED
====================



python-wkhtmltopdf
==================
A simple python wrapper for the wkhtmltopdf lib (https://github.com/wkhtmltopdf/wkhtmltopdf)

Requirements
------------

System:
~~~~~~~

- Linux 32/64 or OSX only (Windows is not supported at this stage)
- Xvfd
- wkhtmltopdf
- python 2.5+

Installation
------------

wkhtmltopdf (Linux)
~~~~~~~~~~~~~~~~~~~

1. Install Xvfd::

    $ sudo apt-get install xvfb

2. Install Fonts::

    $ sudo apt-get install xfonts-100dpi xfonts-75dpi xfonts-scalable xfonts-cyrillic

3. Install wkhtmltopdf::

    $ sudo apt-get install wkhtmltopdf

wkhtmltopdf (OSX)
~~~~~~~~~~~~~~~~~

1. Install wkhtmltopdf::

    $ brew install wkhtmltopdf

python-wkhtmltopdf (Any Platform)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Development::

    $ git clone git@github.com:qoda/python-wkhtmltopdf.git
    $ cd python-wkhtmltopdf
    $ virtualenv .
    $ pip install -r requirements.pip

2. PIP::

    $ pip install git+https://github.com/qoda/python-wkhtmltopdf.git

    or from pypi

    $ pip install python-wkhtmltopdf

Usage
-----

Simple Usage::
~~~~~~~~~~~~~~

1. Use from class::

    from wkhtmltopdf import WKHtmlToPdf

    wkhtmltopdf = WKHtmlToPdf(
        url='http://www.example.com',
        output_file='~/example.pdf',
    )
    wkhtmltopdf.render()

2. Use from method::

    from wkhtmltopdf import wkhtmltopdf

    wkhtmltopdf(url='example.com', output_file='~/example.pdf')

3. Use from commandline (installed)::

    $ python -m wkhtmltopdf.main example.com ~/example.pdf

4. Use the api (installed)::

    $ python -m wkhtmltopdf.api &
    $ wget http://localhost:8888/?url=example.com&output_file=example.pdf

Required Arguments:
~~~~~~~~~~~~~~~~~~~

- **url** - the url to convert to pdf
- **output_file** - the pdf file that you want to create

Optional Arguments:
~~~~~~~~~~~~~~~~~~~

- **enable-plugins** (default: True)
- **disable-javascript** (default: False)
- **no-background** (default: False)
- **grayscale** (default: False)
- **orientation** (default: Portrait)
- **dpi** (default: 100)
- **username** (default: None)
- **password** (default: None)
- **margin-bottom** (default: 10)
- **margin-top** (default: 10)
- **margin-left** (default: 10)
- **margin-right** (default: 10)
- **disable-smart-shrinking** (default: False)


