from dataclasses import dataclass
from typing import List, Dict
from bson.objectid import ObjectId


@dataclass
class Resolution:
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

        return {
            "discord_id": self.dicord_id,
            "themes": self.themes,
            "title": self.title,
            "info_slide": self.info_slide,
            "play_count": self.play_count,
            "opposition_wins": self.opposition_wins,
            "proopposition_wins": self.proopposition_wins
        }
    
    @staticmethod
    def from_document(doc : Dict[str, any]):
        return Resolution(
            id=doc["_id"],
            themes=doc["themes"],
            title=doc["title"],
            info_slide=doc["info_slide"],
            play_count=doc["play_count"],
            opposition_wins=doc["opposition_wins"],
            proopposition_wins=doc["proopposition_wins"]
        )
