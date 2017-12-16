import http


def request_handler(environ, start_response):
    """
    callable one that accept tow args: environ, start_response
    start_response accept two required positional args: status and response_header, and one optional arg: exec_info
    """
    start_response(
        '{} {}'.format(http.HTTPStatus.OK.value, http.HTTPStatus.OK.name),
        [('Content-type', 'text/plain')]
    )
    yield b'Hello, tothegump. Welcome to this wonderland.'


def run_server(host='localhost', port=8080):
    try:
        print('start up... {}:{}'.format(host, port))
        from wsgiref.simple_server import make_server
        server = make_server(host=host, port=port, app=request_handler)
        server.serve_forever()
    except KeyboardInterrupt:
        print('shutting down')
        import sys
        sys.exit()


if __name__ == '__main__':
    run_server()
