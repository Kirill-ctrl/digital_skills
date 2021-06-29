import html
import json
import xml

from course.week6.task_1_2.deserializers.news_des import NewsDeserializer
from course.week6.task_1_2.formats import FORMAT_JSON, FORMAT_XML, FORMAT_HTML

from course.week6.task_1_2.models.news import News
from course.week6.task_1_2.serializers.news_ser import NewsSerializer
from course.week6.task_1_2.services.base import BaseF


class NewsF(BaseF):

    def serialize_to_json(self, news: News):
        return NewsSerializer.get_serialize(news, FORMAT_JSON)

    def serialize_to_xml(self, news: News):
        return NewsSerializer.get_serialize(news, FORMAT_XML)

    def serialize_to_html(self, news: News):
        return NewsSerializer.get_serialize(news, FORMAT_HTML)

    def deserialize_from_json(self, json_obj: json):
        return NewsDeserializer.get_deserialize(json_obj, FORMAT_JSON)

    def deserialize_from_xml(self, xml_obj: xml):
        return NewsDeserializer.get_deserialize(xml_obj, FORMAT_XML)

    def deserialize_from_html(self, html_obj: html):
        return NewsDeserializer.get_deserialize(html_obj, FORMAT_HTML)
