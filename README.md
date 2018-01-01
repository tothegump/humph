# Humph

How the camel got his hump.

The camel says, "Humph!"

This is a very small web framework. It does nothing but says "Humph!"

`(*^__^*)`

# Tutorial

## Quick Start
```Python
from humph.base import run_server
from humph.response import Response
from humph.router import add_urls


def hello(request):
    return Response('hello, world.')


def index(request):
    return Response('this is index.')


urls = [
    ('^/$', index),
    ('^/hello$', hello),
]


if __name__ == '__main__':
    add_urls(urls)
    run_server(port=3000)

```
