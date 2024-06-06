from config import Config, TgConfig, MongoConfig
from os import getenv


def init() -> Config:
    atlas_uri = getenv('ATLAS_URI')
    db_name = getenv('DB_NAME')
    token_bot = getenv('TOKEN_BOT')
    admins_str = getenv('ADMINS')

    admins = admins_str.split(',')

    tg_config = TgConfig(token_bot, admins)
    mongo_config = MongoConfig(atlas_uri, db_name)

    return Config(mongo_config, tg_config)