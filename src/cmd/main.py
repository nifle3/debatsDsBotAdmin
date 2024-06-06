from dotenv import load_dotenv
from config.init import init_config
from logger.init import init_log
from db.base_db import Db


def main() -> None:
    """function that starts the app"""

    load_dotenv(dotenv_path="./.env")

    cfg = init_config()
    init_log(cfg.environment)

    with Db(cfg.mongo_config.atlas_uri, cfg.mongo_config.db_name) as db:
        db.client
        None


if __name__ == "__main__":
    main()
