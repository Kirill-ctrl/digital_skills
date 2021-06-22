from task_req.main_app import MainApp


def app(environ, start_response):
    return MainApp(environ, start_response).route()
