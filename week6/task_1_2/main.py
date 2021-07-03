import json

from course.week6.task_1_2.services.account import AccountF
from course.week6.task_1_2.services.news import NewsF


HTML_OBJECT_NEWS = """
<html>
<head>Heading</head>
<body>
    <div class='container'>
        <div id='title'>1</div>
        <div id='description'>Something description</div>
        <div id='author'>name author</div>
        <div id='created_at'>2020-05-20</div>
    </div>
</body>
</html>
"""
XML_OBJECT_NEWS = """
<main>
    <news attr="title">title news</news>
    <news attr="description">description news</news>
    <news attr="author">author news</news>
    <news attr="created_at">2021-05-12</news>
</main>
"""
JSON_OBJECT_NEWS = json.dumps(
    {
        "title": "title_news",
        "description": "description news",
        "author": "author news",
        "created_at": "2021-05-12",
    }
)

HTML_OBJECT_ACCOUNT = """
<html>
<head>Heading</head>
<body>
    <div class='container'>
        <div id='id'>1</div>
        <div id='name'>kirill</div>
        <div id='surname'>Pechurin</div>
        <div id='email'>k.pech@mail.ru</div>
    </div>
</body>
</html>
"""
XML_OBJECT_ACCOUNT = """
<main>
<account attr="id">1</account>
<account attr="name">kirill</account>
<account attr="surname">Pechurin</account>
<account attr="email">k.pech@mail.ru</account>
</main>
"""
JSON_OBJECT_ACCOUNT = json.dumps(
    {
        "id": "1",
        "name": "kirill",
        "surname": "Pechurin",
        "email": "k.pech@mail.ru",
    }
)
if __name__ == '__main__':
    news_from_html = NewsF().deserialize_from_html(HTML_OBJECT_NEWS)
    news_from_xml = NewsF().deserialize_from_xml(XML_OBJECT_NEWS)
    news_from_json = NewsF().deserialize_from_json(JSON_OBJECT_NEWS)
    print(news_from_html)
    print(news_from_xml)
    print(news_from_json)

    news_to_html = NewsF().serialize_to_html(news_from_html)
    news_to_xml = NewsF().serialize_to_xml(news_from_xml)
    news_to_json = NewsF().serialize_to_json(news_from_json)

    assert news_to_html == HTML_OBJECT_NEWS
    assert news_to_xml == XML_OBJECT_NEWS
    print(news_to_json, JSON_OBJECT_NEWS)
    assert news_to_json == JSON_OBJECT_NEWS

    account_from_html = AccountF().deserialize_from_html(HTML_OBJECT_ACCOUNT)
    account_from_xml = AccountF().deserialize_from_xml(XML_OBJECT_ACCOUNT)
    account_from_json = AccountF().deserialize_from_json(JSON_OBJECT_NEWS)
    print(account_from_html)
    print(account_from_xml)
    print(account_from_json)

    account_to_html = AccountF().serialize_to_html(account_from_html)
    account_to_xml = AccountF().serialize_to_xml(account_from_xml)
    account_to_json = AccountF().serialize_to_json(account_from_json)

    assert account_to_html == HTML_OBJECT_ACCOUNT
    assert account_to_xml == XML_OBJECT_ACCOUNT
    assert account_to_json == JSON_OBJECT_ACCOUNT
