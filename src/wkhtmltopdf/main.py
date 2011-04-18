import os
import sys

class WKhtmlToPdf(object):
    """
    Convert an html page via its URL into a pdf.
    """
    def __init__(self, *args, **kwargs):
        self.defaults = {
            'url': kwargs.get('url', None),
            'output_file': kwargs.get('output_file', None),
            'screen_resolution': kwargs.get('screen_resolution', [1024, 768]),
            'color_depth': kwargs.get('color_depth', 24),
            'flash_plugin': kwargs.get('flash_plugin', True),
            'disable_javascript': kwargs.get('disable_javascript', False),
            'delay': kwargs.get('delay', 0),
            'orientation': kwargs.get('orientation', 'Portrait'),
            'dpi': kwargs.get('dpi', 100),
            'no_background': kwargs.get('no_background', False),
            'grayscale': kwargs.get('grayscale', False),
            'http_username': kwargs.get('http_username', None),
            'http_password': kwargs.get('http_password', None),
        }
        
        for k, v in self.defaults.items():
            setattr(self, k, v)
        
        if not self.url or not self.output_file:
            raise Exception("URL and Output File Parmas are required.")
            
    def _create_option_list(self):
        """
        Add command option according to the default settings.
        """
        option_list = []
        if self.flash_plugin:
            option_list.append("--enable-plugins")
        if self.disable_javascript:
            option_list.append("--disable-javascript")
        if self.no_background:
            option_list.append("--no-background")
        if self.grayscale:
            option_list.append("--grayscale")
        if self.delay:
            option_list.append("--redirect-delay %s" % self.delay)
        if self.http_username:
            option_list.append("--username %s" % self.http_username)
        if self.http_password:
            option_list.append("--password %s" % self.http_password)
        option_list.append("--orientation %s" % self.orientation)
        option_list.append("--dpi %s" % self.dpi)
        
        return option_list
        
    def render(self):
        """
        Render the URL into a pdf and setup the evironment if required.
        """
        # setup the environment if it isn't set up yet
        display_env_var = os.system("echo $DISPLAY")
        if not display_env_var:
            os.system("Xvfb :0 -screen 0 %sx%sx%s & DISPLAY=127.0.0.1:0" % (
                self.screen_resolution[0],
                self.screen_resolution[1],
                self.color_depth
            ))
            os.system("export DISPLAY")
        
        # execute the command
        os.system("wkhtmltopdf %s %s %s" % (
            " ".join(self._create_option_list()),
            self.url,
            self.output_file
        ))