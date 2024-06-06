from os import getenv
from config.config import Config, TgConfig, MongoConfig


def init_config() -> Config:
    """
    function that parses environments to config dataclass
    environments:
        ENVIRONMENT - must be prod or debug
        ATLAS_URI - mongodb atlas connection string
        DB_NAME - mongodb database name 
        TOKEN_BOT - just token from botfather
        ADMINS - split with , (for example nifle3,nifle3)
    Returns:
        config.config.Config
    """

    env = getenv("ENVIRONMENT")
    atlas_uri = getenv('ATLAS_URI')
    db_name = getenv('DB_NAME')
    token_bot = getenv('TOKEN_BOT')
    admins_str = getenv('ADMINS')

    admins = admins_str.split(',')

    tg_config = TgConfig(token_bot, admins)
    mongo_config = MongoConfig(atlas_uri, db_name)

    return Config(env, mongo_config, tg_config)
