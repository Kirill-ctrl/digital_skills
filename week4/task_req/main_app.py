
class MainApp:

    def __init__(self,
                 environ,
                 start_response):
        self.environ = environ
        self.start_response = start_response
        self.path_req = {
            '/': self.success_response,
            '/hello': self.forbidden_response,
            '/documents': self.no_such_resource,
            '/hello_world': self.internal_server_err,
            '/path_info': self.redirect,
        }

    def route(self):
        try:
            return self.path_req[self.environ['PATH_INFO'].split('?')[0]]()
        except KeyError:
            return self.other()

    def success_response(self):
        self.start_response('200 OK', [('Content-Type', 'text/plain')])
        return [b'This is page with success response']

    def forbidden_response(self):
        self.start_response('403 Forbidden', [('Content-Type', 'text/html')])
        return [b'<html><body><h1>This is page with forbidden response</h1></body></html>']

    def no_such_resource(self):
        self.start_response('422 Unprocessable Entity', [('Content-Type', 'text/html')])
        return [b'<html><body><h1>This is page does not exist</h1></body></html>']

    def internal_server_err(self):
        self.start_response('500 Internal Server Error', [('Content-Type', 'text/plain'),
                                                          ('Content-Type', 'text/html')])
        return [b'This page returned internal server error,\n',
                b'<html><body><p>but this page comes up very often...</p></body></html>']

    def redirect(self):
        self.start_response('301 Redirect', [('Content-Type', 'text/plain')])
        return [b"All will be good, if only not 500"]

    def other(self):
        self.start_response('301 Redirect', [('Content-Type', 'text/plain')])
        return [b'No content, it is sure']
