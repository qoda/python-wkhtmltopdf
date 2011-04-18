# python-wkhtmltopdf

A simple python wrapper for the wkhtmltopdf lib (http://code.google.com/p/wkhtmltopdf/) with flash support.

## Requirements

### System:
    
    * Xvfd
    * wkhtmltopdf
    * flashplugin-nonfree
    * python 2.5+

## Installation

### wkhtmltopdf

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

### Simple Usage:

        from wkhtmltopdf import WKHtmlToPdf
        
        wkhtmltopdf = WKHtmlToPdf(
            url='http://www.google.com',
            output_file='google.pdf',
            
        )
        wkhtmltopdf.render()
        
### Required Arguments:

    * url - the url to convert to pdf
    * output_file - the pdf file that you want to create
        
### Optional Arguments:

    * screen_resolution (default: [1024, 768])
    * color_depth (default: 24 (bit))
    * flash_plugin (default: True)
    * disable_javascript (default: False)
    * delay (default: 0 (millisecs))
    * orientation (default: Portrait)
    * dpi (default: 100)
    * no_background (default: False)
    * grayscale (default: False)
    * http_username (default: None)
    * http_password (default: None)
    