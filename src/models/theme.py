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

        return {
            "theme": self.theme
        }

    @staticmethod
    def from_document(doc : Dict[str, any]):
        """
        Creating model from mongodb document

        RETURNS:
            models.theme.Theme
        """

        return Theme(
            id=doc["_id"],
            theme=doc["theme"]
        )
