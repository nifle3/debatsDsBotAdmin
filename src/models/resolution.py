from dataclasses import dataclass
from typing import List
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

    def __dict__(self):
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