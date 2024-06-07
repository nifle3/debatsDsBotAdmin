from collections.abc import Iterable
from motor.motor_asyncio import AsyncIOMotorDatabase
from bot.repository import AbstractThemeRepository
from models.theme import Theme


class ThemeRepository(AbstractThemeRepository):
    """Mongodb repository for theme collection"""

    COLLECTION_NAME="theme"

    def __init__(self, db : AsyncIOMotorDatabase):
        self.collection = db[self.COLLECTION_NAME]

    async def add(self, theme: Theme) -> bool:
        document = theme.to_document()
        result = await self.collection.insert_one(document)

        return result.acknowledged
    
    async def update(self, theme: Theme) -> bool:
        document = theme.to_document()
        result = await self.collection.update_one({"_id": theme.id}, document)
    
        return result.acknowledged
    
    async def get(self) -> Iterable[Theme]:
        result = list()
        cursor = self.collection.find()
    
        for document in await cursor.to_list():
            theme = Theme.from_document(document)
            result.append(theme)

        return result

    async def delete(self, id: str) -> bool:
        result = await self.collection.delete_one({"_id": id})

        return result.acknowledged
