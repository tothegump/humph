# -*- coding: utf-8 -*-
import re
from typing import Callable, Iterable

from humph.exceptions import HumphException
from humph.request import Request

_path_river = []


class Route:
    def __init__(self, path: str, handler: Callable):
        self.path = path
        self.handler = handler
        self.re = re.compile(path)

    def snap(self, path):
        return self.re.match(path)


def add_urls(urls: Iterable(str, Callable)):
    for path, handler in urls:
        _path_river.append(Route(path, handler))


def get_route(request: Request) -> Route:
    for route in _path_river:
        if route.snap(request.path):
            return route.handler
    raise HumphException('404')
