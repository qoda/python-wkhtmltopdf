#!/usr/bin/env python
import os
import optparse


class WKOption(object):
    """Build an option to be used throughout"""
    def __init__(self, name, shortcut, otype=str, action=None, dest=None,
            default=None, help=None, validate=None, validate_error=None):
        self.name = name
        self.shortcut = shortcut
        self.otype = bool if (default is True or default is False) else otype
        self.action = "store_true" if self.otype is bool else "store"
        self.dest = dest if dest else name.replace('-', '_')
        self.default = default
        self.help = help
        self._validate = validate
        self.validate_error = validate_error

        # we're going to want to get the values in here
        self.value = None

    def validate(self):
        if self.validate is None:
            return True

        # only try to validate if we have a function to do so
        if self.validate(self.value):
            return True
        else:
            return False, self.validate_error

    def long(self):
        return '--' + self.name.replace('_', '-')

    def to_cmd(self):
        """Return the str() of this command, bool is just --long, etc"""
        if self.otype is bool:
            if self.value:
                return self.long()
            else:
                return ""
        else:
            return " ".join([self.long(), str(self.value)
                            if self.value is not None else ""])


OPTIONS = [
    WKOption('enable-plugins', '-F',
                 default=True,
                 help="use flash and other plugins",
                 ),
    WKOption('disable-javascript', '-J',
                 default=False,
                 help="disable javascript",
                 ),
    WKOption('no-background', '-b',
                 default=False,
                 help="do not print background",
                 ),
    WKOption('grayscale', '-g',
                 default=False,
                 help="make greyscale",
                 ),
    WKOption('redirect-delay', '-d',
                 default=0,
                 help="page delay before conversion",
                 ),
    WKOption('orientation', '-O',
                 default="Portrait",
                 help="page orientation",
                 validate=lambda x: x in ['Portrait', 'Landscape'],
                 validate_error="Orientation argument must be either Portrait or Landscape"
                 ),
    WKOption('dpi', '-D',
                 default=100,
                 help="print dpi",
                 ),
    WKOption('username', '-U',
                 default="",
                 help="http username",
                 ),
    WKOption('password', '-P',
                 default="",
                 help="http password",
                 ),
    WKOption('margin-bottom', '-B',
                 default=10,
                 help="bottom page margin, default 10mm",
                 ),
    WKOption('margin-top', '-T',
                 default=10,
                 help="top page margin, default 10mm",
                 ),
    WKOption('margin-left', '-L',
                 default=10,
                 help="left page margin, default 10mm",
                 ),
    WKOption('margin-right', '-R',
                 default=10,
                 help="right page margin, default 10mm",
                 ),
    WKOption('disable-smart-shrinking', None,
                 default=False,
                 help="Disable the intelligent shrinking strategy used by WebKit that makes the pixel/dpi ratio none constant",
                 ),
]


class WKhtmlToPdf(object):
    """
    Convert an html page via its URL into a pdf.
    """
    def __init__(self, *args, **kwargs):
        self.url = None
        self.output_file = None

        # get the url and output_file options
        try:
            self.url, self.output_file = args[0], args[1]
        except IndexError:
            pass

        if not self.url or not self.output_file:
            raise Exception("Missing url and output file arguments")

        # save the file to /tmp if a full path is not specified
        output_path = os.path.split(self.output_file)[0]
        if not output_path:
            self.output_file = os.path.join('/tmp', self.output_file)

        # set the options per the kwargs coming in
        for o in OPTIONS:
            o.value = kwargs.get(o.dest)

        self.params = [o.to_cmd() for o in OPTIONS]
        self.screen_resolution = [1024, 768]
        self.color_depth = 24

    def render(self):
        """
        Render the URL into a pdf and setup the evironment if required.
        """

        # setup the environment if it isn't set up yet
        if not os.getenv('DISPLAY'):
            os.system("Xvfb :0 -screen 0 %sx%sx%s & " % (
                self.screen_resolution[0],
                self.screen_resolution[1],
                self.color_depth
            ))
            os.putenv("DISPLAY", '127.0.0.1:0')

        # execute the command
        command = 'wkhtmltopdf %s "%s" "%s" >> /tmp/wkhtp.log' % (
                        " ".join([cmd for cmd in self.params]),
                        self.url,
                        self.output_file
                  )
        sys_output = int(os.system(command))

        # return file if successful else return error code
        if not sys_output:
            return True, self.output_file
        return False, sys_output


def wkhtmltopdf(*args, **kwargs):
    wkhp = WKhtmlToPdf(*args, **kwargs)
    wkhp.render()


if __name__ == '__main__':

    # parse through the system argumants
    usage = "Usage: %prog [options] url output_file"
    parser = optparse.OptionParser()

    for o in OPTIONS:
        if o.shortcut:
            parser.add_option(o.shortcut, o.long(),
                              action=o.action,
                              dest=o.dest,
                              default=o.default,
                              help=o.help)
        else:
            parser.add_option(o.long(),
                              action=o.action,
                              dest=o.dest,
                              default=o.default,
                              help=o.help)

    options, args = parser.parse_args()

    # call the main method with parsed argumants
    wkhtmltopdf(*args, **options.__dict__)
