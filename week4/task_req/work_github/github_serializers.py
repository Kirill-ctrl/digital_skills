import json
from datetime import datetime


def ser_for_list_repo(data: json):
    return [
        {
            'id': item.get('id'),
            'language': item.get('language'),
            'name': item.get('name'),
            'url': item.get('html_url'),
            'visibility': {
                'private': item.get('private'),
            },
            'subscribers': {
                'watchers': item.get('watchers'),
                'watchers_count': item.get('watchers_count'),
            },
            'size': item.get('size')
        }
        for item in data
    ]


def ser_for_info_user(data: json):
    return {
        'id': data.get('login'),
        "login": data.get('login'),
        'url': data.get('url'),
        'repos_url': data.get('repos_url'),
        'public_repos': data.get('public_repos'),
        'followers': data.get('followers'),
        'following': data.get('following'),
        'created_at': str(datetime.strptime(data.get('created_at'), '%Y-%m-%dT%H:%M:%SZ'))
    }
