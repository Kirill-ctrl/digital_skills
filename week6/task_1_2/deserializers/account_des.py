import json

from zope.interface import implementer

from course.week6.task_1_2.deserializers.base_des import BaseDeserializer
from course.week6.task_1_2.formats import FORMAT_JSON, FORMAT_XML, FORMAT_HTML
from course.week6.task_1_2.models.account import Account


@implementer(BaseDeserializer)
class AccountDeserializer:

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
        return Account(
            id=json_obj.get('id') if json_obj.get('id') else None,
            name=json_obj.get('name') if json_obj.get('name') else None,
            surname=json_obj.get('surname') if json_obj.get('surname') else None,
            email=json_obj.get('email') if json_obj.get('email') else None,
        )

    @staticmethod
    def des_from_xml(xml_obj):
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(xml_obj, 'xml')
        for item in soup.main.find_all('account'):
            if item['attr'] == 'id':
                id = item.string
            elif item['attr'] == 'name':
                name = item.string
            elif item['attr'] == 'surname':
                surname = item.string
            elif item['attr'] == 'email':
                email = item.string
        return Account(
            id=id if id else None,
            name=name if name else None,
            surname=surname if surname else None,
            email=email if email else None,
        )

    @staticmethod
    def des_from_html(html_obj):
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(html_obj, 'html.parser')
        x = soup.body.find('div', attrs={'class': 'container'})
        for div in x.find_all('div'):
            if div['id'] == 'id':
                id = div.string
            elif div['id'] == 'name':
                name = div.string
            elif div['id'] == 'surname':
                surname = div.string
            elif div['id'] == 'email':
                email = div.string
        return Account(
            id=id if id else None,
            name=name if name else None,
            surname=surname if surname else None,
            email=email if email else None,
        )
