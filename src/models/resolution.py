from dataclasses import dataclass
from typing import List, Dict
from bson.objectid import ObjectId


@dataclass
class Reolution:
    """Resolution for the debate game"""

    id : ObjectId
    themes : List[str]
    title : str
    info_slide : str
    play_count : int
    opposition_wins : int
    proopposition_wins : int

    def to_document(self) -> Dict[str, any]:
        """Func that casts resolution model to mongodb document"""

        dict = {
            "discord_id": self.dicord_id,
            "themes": self.themes,
            "title": self.title,
            "info_slide": self.info_slide,
            "play_count": self.play_count,
            "opposition_wins": self.opposition_wins,
            "proopposition_wins": self.proopposition_wins
        }

        if self.id is not None:
            dict["_id"] = self.id

        return dict
