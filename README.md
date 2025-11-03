# Hashtag sorter bot

This bot sorts the tags in alphabetical order.

- [Launching the bot](#launching-the-bot)
- [Usage](#usage)
- [Example](#example)

## Launching the bot

The bot is waiting for a separate file `config.py` with the following contents:

```python
settings = {
    'token': 'bot_token',
    'bot': 'bot_username',
    'prefix': 'command_prefix',
}
```

It imports these settings into `main.py` to communicate with the bot in the telegram.

Next, the launch takes place through the launch of the file `main.py`.

## Usage

The bot has only one command, `start`, which has several synonyms: `help`, `помощь`, `пом`. Entering this command brings up a help menu on how to use the bot.

The bot treats messages without a command as a set of tags. It separates the message into tags by space and then sorts them, displaying the result.

Tags can be specified with or without the "#" symbol:

```sh
#tag1 #tag2 #тег3 #тег4
```

and

```sh
tag1 tag2 тег3 тег4
```

they will be processed identically.

## Example

User input:

```sh
tag1 #tag3 #tag2 tag4 watermelon art magic магия арт небо белый след
```

Bot output:

```sh
#art #magic #tag1 #tag2 #tag3 #tag4 #watermelon #арт #белый #магия #небо #след
```
