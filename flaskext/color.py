# -*- coding: utf-8 -*-
"""
    flaskext.color
    ~~~~~~~~~~~~~~

    Colors the requests in debugging mode

    :copyright: (c) 2014 by Frozenball.
    :license: MIT, see LICENSE for more details.
"""
import time
import re

class TerminalColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    GRAY = '\033[1;30m'
    LITTLEGRAY = '\033[1;30m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

        
def init_app(app):
    if not (
        app.config['DEBUG'] or
        app.config.get('COLOR_ALWAYS_ON', False)
    ):
        return
    import werkzeug.serving

    staticPattern = app.config.get(
        'COLOR_PATTERN_GRAY',
        r'^/(static|assets|img|js|css)/(.*)|favicon\.ico|(.*)\.(png|jpeg|jpg|gif|css)$'
    )
    hidePattern = app.config.get('COLOR_PATTERN_HIDE', r'/^$/')
    WSGIRequestHandler = werkzeug.serving.WSGIRequestHandler
    
    def log_request(self, code='-', size='-'):
        url = self.requestline.split(" ")[1]
        method = self.requestline.split(" ")[0]
        
        if code == 200:
            statusColor = TerminalColors.OKGREEN
        elif str(code)[0] in ['4', '5']:
            statusColor = TerminalColors.FAIL
        else:
            statusColor = TerminalColors.GRAY

        if re.search(hidePattern, url):
            return

        print("{statusColor}{status}{colorEnd} {methodColor}{method}{colorEnd} {urlColor}{url}{colorEnd}".format(
            status=code,
            method=method,
            url=url,
            statusColor=statusColor,
            colorEnd=TerminalColors.ENDC,
            methodColor=TerminalColors.GRAY if method == 'GET' else TerminalColors.ENDC,
            urlColor=TerminalColors.LITTLEGRAY if re.search(staticPattern, url) else TerminalColors.ENDC
        ))

    WSGIRequestHandler.log_request = log_request
    werkzeug.serving.WSGIRequestHandler = WSGIRequestHandler
