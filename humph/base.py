from humph.request import Request
from humph.router import get_route


def request_handler(environ, start_response):
    """
    callable one that accept tow args: environ, start_response
    start_response accept two required positional args: status and response_header, and one optional arg: exec_info
    """
    request = Request(environ)
    handle = get_route(request)
    response = handle(request)
    start_response(
        response.status,
        response.headers
    )
    return response.body()


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
