# python-wkhtmltopdf

A simple python wrapper for the wkhtmltopdf lib (http://code.google.com/p/wkhtmltopdf/) with flash support.

## Requirements

### System:
    
    * wkhtmltopdf
    * flashplugin-nonfree

## Installation

### wkhtmltopdf - full installation

1. Install Xvfd:
    
    $ sudo apt-get install xvfb x11-xkb-utils xserver-xorg-core
    
2. Install Fonts:

    $ sudo apt-get install xfonts-100dpi xfonts-75dpi xfonts-scalable xfonts-cyrillic
    
3. Install wkhtmltopdf:
    
    $ sudo apt-get install openssl build-essential xorg libssl-dev libxrender-dev
    $ sudo apt-get install wkhtmltopdf

### python-wkhtmltopdf

1. From git:

    $ git clone git@github.com:qoda/python-wkhtmltopdf.git
    $ cd python-wkhtmltopdf
    $ python setup.py install

## Usage

1. Create and save a pdf from a URL:

    from wkhtmltopdf import WKHtmlToPdf
    
    wkhtmltopdf = WKHtmlToPdf(url='', output_file='')
    wkhtmltopdf.render(screen_resolution=[1024, 768], color=24flash_plugin=True, )
    create_pdf("http://www.google.com", 'google.com.pdf')        # throws CompilationError if the file is not created.
    