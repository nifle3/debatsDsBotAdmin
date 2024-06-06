from dotenv import load_dotenv

def main() -> None:
    load_dotenv(dotenv_path="./.env")

    cfg = config.init()
    log = logger()

    db = mongo(cfg)
    bot = tg()
    bot.start()


if __name__ == "__main__":
    main()