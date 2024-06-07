from collections.abc import Iterable
from typing import List
from bson.objectid import ObjectId
from motor.motor_asyncio import AsyncIOMotorDatabase
from bot.repository import AbstractResolutionRepository
from models.resolution import Resolution


class ResolutionRepository(AbstractResolutionRepository):
    """"""

    COLLECTION_NAME = "resolution"

    async def __init__(self, db : AsyncIOMotorDatabase):
        self.collection = db[self.COLLECTION_NAME]

    async def add(self, resolution : Resolution) -> bool:
        document = resolution.to_document()
        result = await self.collection.insert_one(document)

        return result.acknowledged

    async def update(self, resolution : Resolution) -> bool:
        document = resolution.to_document()
        result = await self.collection.update_one({"_id": resolution.id}, document)

        return result.acknowledged

    async def get_skip_limit(self, skip : int, limit : int) -> Iterable[Resolution]:
        result = list()
        cursor = self.collection.find().skip(skip).limit(limit)

        for document in await cursor.to_list():
            resolution = Resolution.from_document(document)
            result.append(resolution)

        return result

    async def get_by_theme_skip_limit(self, theme : List[str], skip : int, limit : int) -> Iterable[Resolution]:
        result = list()
        cursor = self.collection.find({"themes": {"$all": theme}}).skip(skip).limit(limit)

        for document in await cursor.to_list():
            resolution = Resolution.from_document(document)
            result.append(resolution)

        return result

    async def get_by_title(self, title : str) -> Iterable[Resolution]:
        raise NotImplementedError

    async def get_one(self, id : ObjectId) -> Resolution:
        result = await self.collection.find_one({"_id": id})

        return Resolution.from_document(result)

    async def delete(self, id : ObjectId) -> bool:
        result = await self.collection.delete_one({"_id": id})

        return result.acknowledged

    async def delete_theme(self, theme : str, id : ObjectId) -> bool:
        result = await self.collection.update_one({"_id": id}, {"$pull": {"themes": theme}})

        return result.acknowledged