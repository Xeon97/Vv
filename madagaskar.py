# -*- coding: utf-8 -*-
# Hikka Userbot Module: Random Word Bot
from .. import loader, utils
import random

@loader.tds
class RandomWordBotMod(loader.Module):
    """Модуль для случайного выбора слова"""

    strings = {"name": "RandomWordBot"}
    
    def __init__(self):
        self.config = loader.ModuleConfig(
            "WORDS", ["Баку", "Тру", "Комбат", "Былины", "Mafioso"], "Список слов для случайного выбора"
        )
        self.active_chats = []

    async def client_ready(self, client, db):
        self.client = client

    @loader.command()
    async def activbot(self, message):
        """Включает функцию случайного выбора слов в текущем чате"""
        chat_id = utils.get_chat_id(message)
        if chat_id not in self.active_chats:
            self.active_chats.append(chat_id)
            await message.edit(f"Функция активирована в чате с ID: {chat_id}")
        else:
            await message.edit("Функция уже активирована в этом чате.")

    @loader.command()
    async def bot(self, message):
        """Выдаёт случайное слово из списка, отвечая на сообщение пользователя"""
        chat_id = utils.get_chat_id(message)
        if chat_id in self.active_chats:
            random_word = random.choice(self.config["WORDS"])
            await message.respond(f"Случайное слово: {random_word}", reply_to=message.id)
        else:
            await message.edit("Функция не активирована в этом чате. Используйте %activbot.")
