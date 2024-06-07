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

        return dict
    
    @staticmethod
    def from_document(doc : Dict[str, any]):
        return Theme(
            id=doc["_id"],
            theme=doc["theme"]
        )
