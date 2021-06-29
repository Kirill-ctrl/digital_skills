from datetime import datetime
from typing import Optional

from course.week6.task_1_2.models.account import Account


class News:
    def __init__(self,
                 title: Optional[str] = None,
                 description: Optional[str] = None,
                 author: Optional[Account] = None,
                 created_at: Optional[datetime] = None):
        self.title = title
        self.description = description
        self.author = author
        self.created_at = created_at
