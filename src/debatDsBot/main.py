from dotenv import load_dotenv
from config import init

def main() -> None:
    load_dotenv(dotenv_path="./.env")

    cfg = init()
    log = logger()

    db = mongo(cfg)
    bot = tg()
    bot.start()


if __name__ == "__main__":
    main()