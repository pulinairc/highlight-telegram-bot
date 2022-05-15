## Telegram bot for matterbridge Telegram channel highlights

The gateway bot [matterbridge](https://github.com/42wim/matterbridge) doesn't know how to map users with Telegram nicks so the highlights don't work on Telegram side. This bot aims to fix that.

### Requirements 

* Python 3.8
* pipenv
* Linux/WSL
* [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)

### Installation

1. Create your bot via [BotFather](https://t.me/botfather)
2. Set up at least with `/newbot`, `/setdescription`, `/setname` and `/setuserpic`.
3. Set up command options with `/setcommands`:
4. Disable privacy mode with `/setprivacy`, if this is not set the bot cannot reply to a channel
5. Add your personal bot `TOKEN` to .env file
6. Run `pipenv install -r requirements.txt` (sudo might be needef or WSL)
7. Run `pipenv run python bot.py`
