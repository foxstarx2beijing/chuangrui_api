import os
import six
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

def get_config(name, default = None):
    """
    从settings里面获取配置信息
    """
    config = os.environ.get(name, getattr(settings, name, default))
    if config is not None:
        if isinstance(config, six.string_types):
            return config.strip()
        else:
            return config
    else:
        raise ImproperlyConfigured(
            "Can't find config for '%s' either in environment"
            "variable or in setting.py" % name)

ACCESSKEY = 'st8oQwZUVVTq4Ryz'
ACCESSSECRET = 'rlKra7f3V1tOQ2u2DjjYJBJdUjEybLWx'

class sms():
    def __init__(self):
        return

    def single_send(self):
        return

    def send(self):
        return

class Sign():
    def __init__(self):
        return

    def get(self):
        return

