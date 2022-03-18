from test_framework.exceptions import RouteIsNotExist, MethodNotAllowedException
from test_framework.parser import Request


class HandlerMethodInfo:
    def __init__(self, handler, methods: list):
        self.handler = handler
        self.methods = methods


class Router:
    routes = dict()

    def __init__(self, base_route: str = ""):
        self.base_route = base_route

    def add_route(self, route: str, handler, methods: list):
        route = self.base_route + route
        self.routes[route] = HandlerMethodInfo(handler=handler, methods=methods)

    async def navigate(self, request: Request):
        route = request.path
        try:
            handler_methods_info = self.routes[route]
        except KeyError:
            raise RouteIsNotExist(route)
        if request.method not in handler_methods_info.methods:
            raise MethodNotAllowedException(request.method)
        return await handler_methods_info.handler(request)
