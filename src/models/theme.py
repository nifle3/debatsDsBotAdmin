from dataclasses import dataclass
from typing import Dict
from bson.objectid import ObjectId


@dataclass
class Theme:
    """Resolution's type"""

    id : ObjectId
    theme : str

    def to_document(self) -> Dict[str, any]:
        """Func that casts theme model to mongodb document"""
        
        dict = {
            "theme": self.theme
        }

        if self.id is not None:
            dict["_id"] = self.id

        return dict
