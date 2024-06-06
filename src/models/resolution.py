from dataclasses import dataclass
from typing import List
from bson.objectid import ObjectId


@dataclass
class Reolution:
    """Resolution for the debate game"""

    id : ObjectId
    name : str
    themes : List[str]
    title : str
    info_slide : str
    play_count : int

    def __dict__(self):
        dict = {
            "discord_id": self.dicord_id,
            "name": self.name,
            "play_count": self.play_count,
            "first_place_count": self.first_place_count,
            "points": self.points,
            "most_played_teammete": self.most_played_teammete,
        }

        if self.id is not None:
            dict["_id"] = self.id

        return dict
