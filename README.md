# Devii
Discord Moderation &amp; Utility Bot
# Discord Moderation & Utility Bot

A Discord bot built with **discord.py** that provides moderation tools, welcome messages, role assignment, avatar viewing, greeting commands, and a profanity filter.

## Features

### 🛡️ Moderation

* Automatic profanity detection and message deletion.
* Warning messages for users who use blocked words.
* Kick command for moderators.

### 👋 Welcome System

* Sends a direct message to new members.
* Posts a welcome message in the server's general chat channel.

### 🎭 Role Management

* Self-assign a secret role using a command.

### 📸 Utility Commands

* Display user avatars.
* Custom help menu.

### 💬 Fun & Greeting Commands

* Hello
* Namaste
* Yo
* Motivate
* Spanish greeting

---

## Requirements

* Python 3.10+
* Discord Bot Token
* Discord Server with appropriate bot permissions

### Python Packages

Install dependencies:

```bash
pip install discord.py python-dotenv
```

---

## Project Structure

```text
project/
│
├── devi.py
├── .env
├── discord.log
└── README.md
```

---

## Environment Variables

Create a `.env` file in the project root:

```env
DISCORD_TOKEN=YOUR_DISCORD_BOT_TOKEN
```

---

## Required Bot Permissions

Enable the following permissions in the Discord Developer Portal:

* Read Messages
* Send Messages
* Manage Messages
* Kick Members
* Manage Roles
* View Channels

Also enable these privileged intents:

* Message Content Intent
* Server Members Intent

---

## Commands

| Command             | Description                     |
| ------------------- | ------------------------------- |
| `hello`             | Sends a greeting                |
| `namaste`           | Sends a Hindi greeting          |
| `yo`                | Sends a casual greeting         |
| `motivate`          | Sends a motivational message    |
| `assign`            | Assigns the secret role         |
| `avatar`            | Displays a user's avatar        |
| `kick @user reason` | Kicks a member (Moderator only) |
| `helpp`             | Shows the help menu             |
| `vix`               | Mentions everyone               |

---

## Profanity Filter

The bot automatically monitors messages and removes messages containing words from the predefined profanity list.

Example:

```text
User: bad word
Bot: @User, don't use abusive language here.
```

---

## Welcome Messages

When a member joins:

1. The bot sends a private welcome message.
2. The bot posts a public welcome message in the configured channel.

---

## Running the Bot

Start the bot:

```bash
python devi.py
```

If the token is configured correctly, you should see:

```text
✅ We are ready to launch! Logged in as BotName
```

---

## Logging

Logs are stored in:

```text
discord.log
```

This helps with debugging and monitoring bot activity.

---

## Security Notice

⚠️ Never commit your Discord bot token to GitHub or share it publicly.

Store tokens only in a `.env` file and add the following to `.gitignore`:

```gitignore
.env
discord.log
```

If a token has been exposed, regenerate it immediately from the Discord Developer Portal.

---

## Future Improvements

* Ban command
* Mute command
* Slash commands
* Custom welcome channel configuration
* Database support
* Advanced moderation system
* Reaction roles
* Music features

---

## License

This project is open-source and can be modified for personal or educational use.


## Add Devi to your server

https://discord.com/oauth2/authorize?client_id=1513918178781040872&permissions=8&integration_type=0&scope=bot
