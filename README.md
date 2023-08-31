# About

This is a lightweight python discord bot to harass my friends with facts about the great state of
Michigan. The bot returns facts about the state whenever the word "Michigan" is mentioned in a given
server.

# Quick start

You'll need to set up an app and get a bot token in your personal discord account first. You can then use
the token generated in your account as an environmental variable (in your `.env` if you're running locally, for example).

To run the bot locally:

1. Set up virtual environment (optional but recommended)
```console

python3 -m venv venv
source venv/bin/activate

```

2. Install dependencies

```console

pip3 install -r requirements.txt

```

3. Run

```console

python3 bot.py

```