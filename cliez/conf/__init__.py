# -*- coding: utf-8 -*-

import importlib

PACKAGE_ROOT = None


def settings():
    """
    a wrapper for Settings._wrapped
    :return:
    """
    return Settings._wrapped


class Settings(object):
    _path = None
    _wrapped = None

    @staticmethod
    def bind(mod_path):

        try:
            mod = importlib.import_module(mod_path)
        except ImportError:
            raise

        settings = Settings()

        for v in dir(mod):
            if v[0] == '_' or type(getattr(mod, v)).__name__ == 'module':
                continue
            setattr(settings, v, getattr(mod, v))
            pass

        Settings._path = mod_path
        Settings._wrapped = settings

        return settings

    pass