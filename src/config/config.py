from dataclasses import dataclass
from collections.abc import Iterable


@dataclass
class MongoConfig:
    """Data class with config for mongodb access"""

    atlas_uri : str
    db_name : str

@dataclass
class TgConfig:
    """data class with config for tg bot"""

    token : str
    admins : Iterable[str]

@dataclass
class Config:
    """data class with app config"""

    environment : str
    mongo_config : MongoConfig
    tg_config : TgConfig
