import json

import requests

from task_req.work_github.github_serializers import ser_for_info_user, ser_for_list_repo
from task_req.work_github.config import API_TOKEN, NAME


def set_session_by_name_and_token():
    session_name = requests.session()
    session_name.auth = (NAME, API_TOKEN)
    return session_name


def set_session_by_headers():
    session_headers = requests.session()
    session_headers.headers.update({"Authorization": f"token {API_TOKEN}"})
    return session_headers


class GithubApi:
    URL_SELF_REPOS = 'https://api.github.com/user/repos'
    URL_SELF_USER = 'https://api.github.com/user'
    URL_PHILOSOPHY = 'https://api.github.com/zen'
    URL_OTHER_USER = 'https://api.github.com/users/'

    def __init__(self,
                 environ):
        self.environ = environ
        self.session_by_headers = set_session_by_headers()
        self.session_by_name = set_session_by_name_and_token()

    def route(self):
        if '/user' in self.environ['PATH_INFO']:
            obj_req = self.get_info_self
        elif '/repos' in self.environ['PATH_INFO']:
            obj_req = self.get_info_repos
        else:
            raise KeyError

        resp, ser_resp = obj_req()

        with open('log.txt', 'a') as f:
            f.write("Request:\n" + resp.url + " Method: GET\nResponse:\n")
            json.dump(ser_resp, f, separators=(',\n', ':'))
            f.write('\n-------------------------------------\n')

        return resp, json.dumps(ser_resp)

    def get_info_self(self):
        if self.environ['QUERY_STRING']:
            item = ''
            for query in self.environ['QUERY_STRING'].split('&'):
                if 'name' in query:
                    item = query.split('=')[-1]
                    break
            url = self.URL_OTHER_USER + (item or None)
        else:
            url = self.URL_SELF_USER

        response = self.session_by_headers.get(url)
        ser_resp = ser_for_info_user(response.json())
        return response, ser_resp

    def get_info_repos(self):
        if self.environ['QUERY_STRING']:
            item = ''
            for query in self.environ['QUERY_STRING'].split('&'):
                if 'name' in query:
                    item = query.split('=')[-1]
                    break
            url = self.URL_OTHER_USER + item + '/' + 'repos'
        else:
            url = self.URL_SELF_REPOS

        response = self.session_by_name.get(url)
        ser_resp = ser_for_list_repo(response.json())
        return response, ser_resp
