# -*- coding: utf-8 -*-


class Request:
    """request object base on environ """
    def __init__(self, environ):
        self.environ = environ
        self._host = None
        self._scheme = None

    @property
    def host(self):
        if not self._host:
            self._host = self.environ.get('HTTP_X_FORWARDED_PROTO') or self.environ.get('HTTP_HOST')
            if not self._host:
                server_name = self.environ['SERVER_NAME', '127.0.0.1']
                default_port = 80 if self.scheme == 'http' else 443
                server_port = self.environ.get('SERVER_PORT', default_port)
                self._host = '{}:{}'.format(server_name, server_port)
        return self._host

    @property
    def scheme(self):
        if not self._scheme:
            # scheme = self.environ['']
            self._scheme = 'http'
        return self._scheme

    def header(self):
        pass

    def method(self):
        pass

    def cookies(self):
        pass

    def files(self):
        pass

    @property
    def content_type(self):
        return self.environ.get('CONTENT_TYPE', '').lower()

    @property
    def query_string(self):
        return self.environ.get('QUERY_STRING', '')

    @property
    def path(self):
        return '/' + self.environ.get('PATH_INFO', '').lstrip('/')

    @property
    def body(self):
        pass
