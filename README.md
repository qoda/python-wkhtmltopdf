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
    
4. Install flashplugin:

        $ sudo apt-get install flashplugin-nonfree

### python-wkhtmltopdf

1. From git:

        $ git clone git@github.com:qoda/python-wkhtmltopdf.git
        $ cd python-wkhtmltopdf
        $ python setup.py install

## Usage

1. Create and save a pdf from a URL:

        from wkhtmltopdf import WKHtmlToPdf
    
        wkhtmltopdf = WKHtmlToPdf(url='http://www.google.com', output_file='google.pdf')
        wkhtmltopdf.render(screen_resolution=[1024, 768], color_depth=24, flash_plugin=True, delay=0)
    