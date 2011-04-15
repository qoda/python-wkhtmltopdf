python-wkhtmltopdf
==================
A simple python wrapper for the wkhtmltopdf lib (http://code.google.com/p/wkhtmltopdf/) with flash support.

Requirements
------------
System:
    * wkhtmltopdf
    * flashplugin-nonfree

Installation
------------
wkhtmltopdf:
    refer to http://code.google.com/p/wkhtmltopdf/wiki/compilation

$ git clone ????????

Simple Usage
------------
Create and save a pdf from a URL:

    from wkhtmltopdf import create_pdf
    
    url = "http://www.google.com"
    output_file = "google.com.pdf"
    create_pdf("http://www.google.com", google.com.pdf)        # throws CompilationError if the file is not created.
    