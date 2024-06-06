def main() -> None:
    cfg = config.init()
    log = logger()

    db = mongo(cfg)
    bot = tg()
    bot.start()


if __name__ = "__main__":
    main()