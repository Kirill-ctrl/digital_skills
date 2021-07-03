from typing import Optional


class Account:
    def __init__(self,
                 id: Optional[int] = None,
                 name: Optional[str] = None,
                 surname: Optional[str] = None,
                 email: Optional[str] = None):
        self.id = id
        self.name = name
        self.surname = surname
        self.email = email
