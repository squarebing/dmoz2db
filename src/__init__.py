# -*- coding: UTF-8 -*-



import logging

class NullHandler(logging.Handler):
    def emit(self, record):
        pass

_log = logging.getLogger(__name__)
_log.setLevel(logging.DEBUG)
_log.addHandler(NullHandler())

from . import lib
