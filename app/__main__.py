from app.utils import initialize_plugins
from app import bot, main_loop



if __name__ == "__main__":   
    bot.start()
    main_loop.run_forever()

