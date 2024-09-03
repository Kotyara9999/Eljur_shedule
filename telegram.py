import telebot
from telebot.types import InputMediaPhoto, InputMediaDocument, InputMediaVideo
from config import teleGroupId, debug

class teleHandler:
    def __init__(self, tele_token: str):
        self.bot = telebot.TeleBot(tele_token)
        self.media = []

    def addDocument(self, file, caption: str = ""):
        """
        Добавляет файлы в сообщение.

        :param file: Файл.
        :param caption: Описание.
        :return: None.
        """

        self.media.append(InputMediaDocument(media=file,
                                             caption=caption,
                                             parse_mode='HTML'))

    def addPhoto(self, file, caption: str = ""):
        """
         Добавляет фото в сообщение.

        :param file: Фото.
        :param caption: Описание.
        :return: None.
        """
        self.media.append(InputMediaPhoto(media=file,
                                          caption=caption,
                                          parse_mode='HTML'))

    def clearMedia(self):
        """
        Очищает список медиа файлов.

        :return: None.
        """
        self.media = []

    def sendMsg(self, text, send_id=teleGroupId, thread_id=None):
        """
        Отправляет сообщение.

        :param thread_id: Id темы.
        :param send_id: В какой чат/канал отправляется сообщение.
        :param text: Текст сообщения.
        :return: None.
        """
        self.bot.send_message(send_id,
                              text,
                              message_thread_id=thread_id,
                              parse_mode='HTML')

    def sendMedia(self, send_id=teleGroupId, thread_id=None):
        """
        Отправляет сообщение с прикрепленными файлами.

        :param thread_id: Id темы.
        :param send_id: В какой чат/канал отправляется сообщение.
        :return: None
        """
        self.bot.send_media_group(send_id,
                                  self.media,
                                  message_thread_id=thread_id)
        self.clearMedia()