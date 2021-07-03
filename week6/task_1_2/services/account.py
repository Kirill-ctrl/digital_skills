import html
import json
import xml

from course.week6.task_1_2.deserializers.account_des import AccountDeserializer
from course.week6.task_1_2.formats import FORMAT_JSON, FORMAT_XML, FORMAT_HTML
from course.week6.task_1_2.models.account import Account
from course.week6.task_1_2.serializers.account_ser import AccountSerializer
from course.week6.task_1_2.services.base import BaseF


class AccountF(BaseF):

    def serialize_to_json(self, account: Account):
        return AccountSerializer.get_serialize(account, FORMAT_JSON)

    def serialize_to_xml(self, account: Account):
        return AccountSerializer.get_serialize(account, FORMAT_XML)

    def serialize_to_html(self, account: Account):
        return AccountSerializer.get_serialize(account, FORMAT_HTML)

    def deserialize_from_json(self, json_obj: json):
        return AccountDeserializer.get_deserialize(json_obj, FORMAT_JSON)

    def deserialize_from_xml(self, xml_obj: xml):
        return AccountDeserializer.get_deserialize(xml_obj, FORMAT_XML)

    def deserialize_from_html(self, html_obj: html):
        return AccountDeserializer.get_deserialize(html_obj, FORMAT_HTML)