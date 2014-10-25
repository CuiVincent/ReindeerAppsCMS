__author__ = 'CuiVincent'
# encoding:utf-8

import base64
import uuid
from os import path

app_settings = {
    'debug': False,
    'cookie_secret': base64.b64encode(uuid.uuid4().bytes + uuid.uuid4().bytes),
    'login_url': r'/login',
    'xsrf_cookies': True,
    'static_path': path.join(path.dirname(__file__), 'res/static'),
    'template_path': path.join(path.dirname(__file__), 'res/templates')
}

