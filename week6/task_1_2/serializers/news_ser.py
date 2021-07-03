import json

from zope.interface import implementer

from course.week6.task_1_2.formats import FORMAT_JSON, FORMAT_HTML, FORMAT_XML
from course.week6.task_1_2.models.news import News
from course.week6.task_1_2.serializers.base_ser import BaseSerializer


@implementer(BaseSerializer)
class NewsSerializer:

    @classmethod
    def get_serialize(cls, news_obj, format_ser: str):
        if format_ser == FORMAT_JSON:
            return cls.ser_to_json(news=news_obj)
        elif format_ser == FORMAT_XML:
            return cls.ser_to_xml(news=news_obj)
        elif format_ser == FORMAT_HTML:
            return cls.ser_to_html(news=news_obj)
        else:
            raise NotImplementedError

    @staticmethod
    def ser_to_json(news: News):
        return json.dumps({
            "title": news.title,
            "description": news.description,
            "author": news.author,
            "created_at": news.created_at,
        })

    @staticmethod
    def ser_to_xml(news: News):
        return f"""
<main>
    <news attr="title">{news.title}</news>
    <news attr="description">{news.description}</news>
    <news attr="author">{news.author}</news>
    <news attr="created_at">{news.created_at}</news>
</main>
"""

    @staticmethod
    def ser_to_html(news: News):
        return f"""
<html>
<head>Heading</head>
<body>
    <div class='container'>
        <div id='title'>{news.title}</div>
        <div id='description'>{news.description}</div>
        <div id='author'>{news.author}</div>
        <div id='created_at'>{news.created_at}</div>
    </div>
</body>
</html>
"""
