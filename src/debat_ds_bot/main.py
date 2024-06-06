from dotenv import load_dotenv
from config.init import init_config
from logger.init import init_log


def main() -> None:
    """function that starts the app"""
    
    load_dotenv(dotenv_path="./.env")

    cfg = init_config()
    log = init_log(cfg.environment)

    db = mongo(cfg)
    bot = tg()
    bot.start()


if __name__ == "__main__":
    main()
