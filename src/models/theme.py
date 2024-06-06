from dataclasses import dataclass
from bson.objectid import ObjectId


@dataclass
class Theme:
    """Resolution's type"""
    
    id : ObjectId
    theme : str

    def __dict__(self):
        dict = {
            "theme": self.theme
        }

        if self.id is not None:
            dict["_id"] = self.id

        return dict
