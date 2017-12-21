# -*- coding: utf-8 -*-
import http

from humph.exceptions import HumphException


def get_status_string(status: http.HTTPStatus):
    return '{} {}'.format(status.value, status.phrase)


class Response:
    """http response object with status, header, body"""

    def __init__(self, data, status_code=200, headers=None, charset=None):
        self._data = data
        self.status_code = status_code
        self.content_type = ('Content-Type', 'text/plain')
        self._charset = charset or 'UTF-8'
        self._headers = headers or [self.content_type]  # todo: make header class

    def body(self):
        if isinstance(self._data, str):
            return [self._data.encode(self._charset)]
        elif isinstance(self._data, bytes):
            return [self._data]
        else:
            raise HumphException('Unknown data type')

    @property
    def headers(self):
        return self._headers

    @property
    def status(self):
        status = http.HTTPStatus(self.status_code)
        return '{} {}'.format(status.value, status.phrase)

    @property
    def charset(self):
        if self._charset:
            return self._charset
        return 'UTF-8'

    @charset.setter
    def charset(self, value):
        self._charset = value
