import json

from lxml import objectify
from zope.interface import implementer

from course.week6.task_1_2.deserializers.account_des import AccountDeserializer
from course.week6.task_1_2.deserializers.base_des import BaseDeserializer
from course.week6.task_1_2.formats import FORMAT_JSON, FORMAT_XML, FORMAT_HTML
from course.week6.task_1_2.models.news import News


@implementer(BaseDeserializer)
class NewsDeserializer:

    @classmethod
    def get_deserialize(cls, data, format_des: str):
        if format_des == FORMAT_JSON:
            return cls.des_from_json(json_obj=data)
        elif format_des == FORMAT_XML:
            return cls.des_from_xml(xml_obj=data)
        elif format_des == FORMAT_HTML:
            return cls.des_from_html(html_obj=data)
        else:
            raise NotImplementedError

    @staticmethod
    def des_from_json(json_obj):
        json_obj = json.loads(json_obj)
        return News(
            title=json_obj.get('title') if json_obj.get('title') else None,
            description=json_obj.get('description') if json_obj.get('description') else None,
            author=json_obj.get('author') if json_obj.get('author') else None,
            created_at=json_obj.get('created_at') if json_obj.get('created_at') else None
        )

    @staticmethod
    def des_from_xml(xml_obj):
        title = description = author = created_at = None
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(xml_obj, 'xml')
        for item in soup.main.find_all('news'):
            print(item['attr'])
            if item['attr'] == 'title':
                title = item.string
            elif item['attr'] == 'description':
                description = item.string
            elif item['attr'] == 'author':
                author = item.string
            elif item['attr'] == 'created_at':
                created_at = item.string
        return News(
            title=title,
            description=description,
            author=author,
            created_at=created_at,
        )

    @staticmethod
    def des_from_html(html_obj):
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(html_obj, 'html.parser')
        x = soup.body.find('div', attrs={'class': 'container'})
        for div in x.find_all('div'):
            if div['id'] == 'title':
                title = div.string
            elif div['id'] == 'description':
                description = div.string
            elif div['id'] == 'author':
                author = div.string
            elif div['id'] == 'created_at':
                created_at = div.string
        return News(
                title=title,
                description=description,
                author=author,
                created_at=created_at,
            )
