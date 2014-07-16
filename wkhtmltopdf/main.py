#!/usr/bin/env python
import os
import optparse

from subprocess import Popen
from subprocess import PIPE


class WKOption(object):
    """
    Build an option to be used throughout
    """
    def __init__(self, name, shortcut, otype=str, action=None, dest=None, default=None, help=None, validate=None, \
                 validate_error=None, value=None):
        self.name = name
        self.shortcut = shortcut
        self.otype = bool if (default is True or default is False) else otype
        self.action = "store_true" if self.otype is bool else "store"
        self.dest = dest if dest else name.replace('-', '_')
        self.default = default
        self.help = help
        self._validate = validate
        self.validate_error = validate_error

        # if there's a value passed to us use it, else use the default
        if value is not None:
            self.value = value
        else:
            self.value = default

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
        """
        Return the str of this command, bool is just --long, etc
        """
        if self.otype is bool:
            if self.value:
                return self.long()
            else:
                return ""
        else:
            return " ".join([self.long(), str(self.value) if self.value is not None else ""])


OPTIONS = [
    WKOption('enable-plugins', '-F', default=True, help="Use flash and other plugins."),
    WKOption('disable-javascript', '-J', default=False, help="Disable javascript."),
    WKOption('no-background', '-b', default=False, help="Do not print background."),
    WKOption('grayscale', '-g', default=False, help="Make greyscale."),
    WKOption(
        'orientation', '-O', default="Portrait", help="Set page orientation.",
        validate=lambda x: x in ['Portrait', 'Landscape'],
        validate_error="Orientation argument must be either Portrait or Landscape"
    ),
    WKOption(
        'page-size', '-s', default="A4", help="Set page size.",
        validate=lambda x: x in ['A4', 'Letter'],
        validate_error="Page size argument must be A4 or Letter"
    ),
    WKOption('print-media-type', '', default = False, help="Set print media type."),

    WKOption('dpi', '-D', default=100, help="Set DPI"),
    WKOption('username', '-U', default="", help="Set the HTTP username"),
    WKOption('password', '-P', default="", help="Set the HTTP password"),
    WKOption('margin-bottom', '-B', default=10, help="Bottom page margin."),
    WKOption('margin-top', '-T', default=10, help="Top page margin."),
    WKOption('margin-left', '-L', default=10, help="Left page margin."),
    WKOption('margin-right', '-R', default=10, help="Right page margin."),
    WKOption(
        'disable-smart-shrinking', None, default=False,
        help="Disable the intelligent shrinking strategy used by WebKit that makes the pixel/dpi ratio none constant",
    )
]


class WKHtmlToPdf(object):
    """
    Convert an html page via its URL into a pdf.
    """
    def __init__(self, *args, **kwargs):
        self.url = None
        self.output_file = None

        # get the url and output_file options
        try:
            self.url, self.output_file = kwargs['url'], kwargs['output_file']
        except KeyError:
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
        for option in OPTIONS:
            try:
                option.value = kwargs[option.dest]  # try to get the value for that kwarg passed to us.
            except KeyError:
                pass  # can't find? just ignore and move on

        self.params = [option.to_cmd() for option in OPTIONS]
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
        try:
            p = Popen(command, shell=True, stdout=PIPE, stderr=PIPE, close_fds=True)
            stdout, stderr = p.communicate()
            retcode = p.returncode

            if retcode == 0:
                # call was successful
                return
            elif retcode < 0:
                raise Exception("Terminated by signal: ", -retcode)
            else:
                raise Exception(stderr)

        except OSError, exc:
            raise exc


def wkhtmltopdf(*args, **kwargs):
    wkhp = WKHtmlToPdf(*args, **kwargs)
    wkhp.render()


if __name__ == '__main__':

    # parse through the system argumants
    usage = "Usage: %prog [options] url output_file"
    parser = optparse.OptionParser()

    for option in OPTIONS:
        if option.shortcut:
            parser.add_option(
                option.shortcut,
                option.long(),
                action=option.action,
                dest=option.dest,
                default=option.default,
                help=option.help
            )
        else:
            parser.add_option(
                option.long(),
                action=option.action,
                dest=option.dest,
                default=option.default,
                help=option.help
            )

    options, args = parser.parse_args()

    # call the main method with parsed argumants
    wkhtmltopdf(*args, **options.__dict__)
