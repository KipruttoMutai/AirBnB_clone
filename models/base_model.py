#!/usr/bin/python3
"""

"""

import uuid
from datetime import datetime

class BaseModel:
    def init(self, id, created_at, updated_at):
        id = str(uuid.uuid4())
        self.created_at = time.localtime()
        self.updated_at = time.localtime()

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        updated_at = time.localtime()

    def to_dict(self):

