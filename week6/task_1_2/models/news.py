from datetime import datetime
from typing import Optional


class News:
    def __init__(self,
                 title: Optional[str] = None,
                 description: Optional[str] = None,
                 author: Optional[str] = None,
                 created_at: Optional[datetime] = None):
        self.title = title
        self.description = description
        self.author = author
        self.created_at = created_at
