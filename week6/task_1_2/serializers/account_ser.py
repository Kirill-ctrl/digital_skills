from zope.interface import implementer

from course.week6.task_1_2.formats import FORMAT_JSON, FORMAT_XML, FORMAT_HTML
from course.week6.task_1_2.models.account import Account
from course.week6.task_1_2.serializers.base_ser import BaseSerializer


@implementer(BaseSerializer)
class AccountSerializer:

    @classmethod
    def get_serialize(cls, account_obj, format_ser: str):
        if format_ser == FORMAT_JSON:
            return cls.ser_to_json(account=account_obj)
        elif format_ser == FORMAT_XML:
            return cls.ser_to_xml(account=account_obj)
        elif format_ser == FORMAT_HTML:
            return cls.ser_to_html(account=account_obj)
        else:
            raise NotImplementedError

    @staticmethod
    def ser_to_json(account: Account):
        return {
            "id": account.id if account.id else None,
            "name": account.name if account.name else None,
            "surname": account.surname if account.surname else None,
            "email": account.email if account.email else None,
        }

    @staticmethod
    def ser_to_xml(account: Account):
        return f"""
<main>
    <news1 attr="id">{account.id}</object1>
    <news1 attr="name">{account.name}</object1>
    <news1 attr="surname">{account.surname}</object1>
    <news1 attr="email">{account.email}</object1>
</main>
"""

    @staticmethod
    def ser_to_html(account: Account):
        return f"""
<html>
<head>Heading</head>
<body>
    <div class='container'>
        <div id='id'>{account.id}</div>
        <div id='name'>{account.name}</div>
        <div id='surname'>{account.surname}</div>
        <div id='email'>{account.email}</div>
    </div>
</body>
</html>
"""
