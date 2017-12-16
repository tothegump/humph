# -*- coding: utf-8 -*-
from tests.base import run_wsgi_app


def test_responder():
    def foo(environ, start_response):
        return list(b'Test')
    result = run_wsgi_app(foo, {})
    assert result['code'] == 200
    assert result['status'] == 'OK'
    assert result['body'] == b'Hello, tothegump. Welcome to this wonderland.'
