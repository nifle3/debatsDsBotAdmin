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

        return dict
    
    @staticmethod
    def from_document(doc : Dict[str, any]):
        """
        Creating model from mongodb document

        RETURNS:
            models.player.Player
        """

        return Player(
            id=doc["_id"],
            name=doc["name"],
            play_count=doc["play_count"],
            first_place_count=doc["first_place_count"],
            points=doc["first_place_count"],
            most_played_teammete=doc["most_played_teammete"]
        )


