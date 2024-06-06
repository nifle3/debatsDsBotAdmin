from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from loguru import logger

class Db:
    """Class that provides db connection"""

    def __init__(self, conn_string : str, db_name : str):
        self.client = AsyncIOMotorClient(conn_string)
        self.db_name = db_name
        logger.info("db client initialize")

    def __enter__(self) -> AsyncIOMotorDatabase:
        db = self.client.get_database(self.db_name)
        logger.info("db initialize")

        return db

    def __exit__(self, reason, val, expection):
        self.client.close()
        logger.info("db client closed")
