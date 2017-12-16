# -*- coding: utf-8 -*-
from wsgiref.util import setup_testing_defaults
from wsgiref.validate import validator


from humph.base import request_handler


def run_wsgi_app(app, environ, buffered=False):
    result = {'code': 0, 'status': 'error', 'header': {}, 'body': b''}

    def _write(data):
        return data

    def start_response(status, headers, exc_info=None):
        """'start_response()' callable as specified by PEP 3333"""
        result['code'] = int(status.split()[0])
        result['status'] = status.split(None, 1)[-1]
        for name, value in headers:
            name = name.title()
            if name in result['header']:
                result['header'][name] += ', ' + value
            else:
                result['header'][name] = value
        assert len(status)>=4, "Status must be at least 4 characters"
        assert status[:3].isdigit(), "Status message must begin w/3-digit code"
        assert status[3]==" ", "Status message must have a space after code"
        return _write
    env = {}
    setup_testing_defaults(env)
    wsgi_app = validator(request_handler)
    response = wsgi_app(env, start_response)
    for part in response:
        try:
            result['body'] += part
        except TypeError:
            raise TypeError('WSGI app yielded non-byte object %s', type(part))
    if hasattr(response, 'close'):
        response.close()
        del response
    return result
