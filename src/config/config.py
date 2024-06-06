from dataclasses import dataclass
from collections.abc import Iterable


@dataclass
class MongoConfig:
    atlas_uri : str
    db_name : str

@dataclass
class TgConfig:
    token : str
    admins : Iterable[str]

@dataclass
class Config:
    environment : str
    mongo_config : MongoConfig
    tg_config : TgConfig
