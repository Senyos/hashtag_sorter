import telebot

from config import settings
from hash_sorting import (
    remove_and_add_hashtag,
    join_tags,
    sort_tags
)
from appendix import (
    get_command_args,
    get_args,
    embrace_text
)


bot = telebot.TeleBot(settings['token'])

@bot.message_handler(commands=['help', 'помощь', 'пом', 'start'])
def start_message(message):
    """The help message to start with"""
    msg = """
Бот под MIT лицензией: https://github.com/Senyos/hashtag_sorter

Теги можно указывать и с и без символа "#":
```sh
#tag1 #tag2 #тег3 #тег4
```
и

```sh
tag1 tag2 тег3 тег4
```
будут обработаны идентично.

Для сортировки тегов введите их подряд через пробел:
    """
    bot.send_message(message.chat.id, msg, parse_mode="Markdown")

@bot.message_handler(func = lambda msg: msg.text is not None and '/' not in msg.text)
def get_tags(message):
    """Getting tags"""
    tags = get_args(message.text)
    tags = remove_and_add_hashtag(tags)
    tags = sort_tags(tags)
    tags_text = join_tags(tags)
    msg = embrace_text(tags_text)
    bot.send_message(message.chat.id, msg, parse_mode="Markdown")

bot.infinity_polling(logger_level=None)