import os
from commands.goose import GooseCommand
from signalbot import SignalBot, Command, Context
import logging

logging.getLogger().setLevel(logging.INFO)
logging.getLogger("apscheduler").setLevel(logging.WARNING)


from commands.friday import FridayCommand

def main():
    # Load environment variables
    from dotenv import load_dotenv
    load_dotenv()

    signal_service = os.environ["SIGNAL_SERVICE"]
    signal_id = os.environ["SIGNAL_ID"]
    group_id = os.environ["GROUP_ID"]
    internal_id = os.environ["GROUP_INTERNAL_ID"]

    config = {
        "signal_service": signal_service,
        "phone_number": signal_id,
        "storage": None,
    }
    bot = SignalBot(config)

    bot.listen(group_id, internal_id)

    bot.register(FridayCommand())
    bot.register(GooseCommand())
    print("Signalbot started. Listening for 'friday' command...")
    bot.start()

if __name__ == "__main__":
    main()
