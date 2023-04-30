# Word of the day discord bot

### Requirements:
Discord.py
```
python3 -m pip install -U discord.py
```
Requests
```
python3 -m pip install -U requests
```

API Documentation:
* Discord.py - https://discordpy.readthedocs.io/en/stable/index.html
* Wordnik -  https://developer.wordnik.com/docs#!/words/getWordOfTheDay

### Setup:
1. Clone repo to directory of your choosing:
```
git clone https://github.com/blanec12/wordOfTheDayBot.git
```

2. Create .env file in root of project: **(ex: wordOfTheDayBot/.env)** 
```
cd wordOfTheDayBot
touch .env
```

3. Populate the .env file with the following details:
```
DISCORD_TOKEN="<YOURDISCORDTOKENHERE>"
CHANNEL_ID="<YOURCHANNELIDHERE>"
URL="https://api.wordnik.com/v4/words.json/wordOfTheDay?api_key=<YOURAPIKEYHERE>"
```

4. Schedule as cron job:
```
# open cron table for editing
crontab -e

# ex: schedule script to run at 8am every day.
0 8 * * * /usr/bin/python3 /home/user/wordOfTheDayBot/main.py
```

