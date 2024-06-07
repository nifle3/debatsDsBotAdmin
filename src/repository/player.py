from collections.abc import Iterable
from motor.motor_asyncio import AsyncIOMotorDatabase
from bot.repository import AbstractPlayerRepository
from models.player import Player

class PlayerRepository(AbstractPlayerRepository):
    """Mongodb repository for player collection"""

    COLLECION_NAME = "player"

    async def __init__(self, db : AsyncIOMotorDatabase):
        self.collection = db[self.COLLECION_NAME]

    async def update(self, player: Player) -> bool:
        document = player.to_document()
        result = await self.collection.update_one({"_id" : player.id}, document)

        return result.acknowledged

    async def get(self) -> Iterable[Player]:
        cursor = self.collection.find()
        result = []

        for document in await cursor.to_list():
            player = Player.from_document(document)
            list.append(player )

        return result

    async def get_one(self, discord_id: str) -> Player:
        result = await self.collection.find_one({"dicord_id" : discord_id})

        return Player.from_document(result)

    async def delete(self, discord_id: str) -> bool:
        result = await self.collection.delete_one({"discord_id" : discord_id})
        
        return result.acknowledged
