from dataclasses import dataclass
from typing import Dict
from bson.objectid import ObjectId


@dataclass
class Player:
    """Debater"""

    id : ObjectId | None
    dicord_id : str
    name : str
    play_count : int
    first_place_count : int
    points : int
    most_played_teammete : str

    def to_document(self) -> Dict[str, any]:
        """Func that casts player model to mongodb document"""

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
