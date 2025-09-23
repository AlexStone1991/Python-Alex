from dotenv import load_dotenv
import os
import base64
from settings import MISTRAL_APY_KEY, TELEGRAM_BOT_TOKEN
from mistralai import Mistral
from abc import ABC, abstractmethod
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, CallbackContext, filters
from mistralai import Mistral
from abc import ABC, abstractmethod

# Загрузка переменных окружения
load_dotenv()

class MistralAI(ABC):
    MODELS = {
        "text": [
            "mistral-small-latest",
            "mistral-large-latest",
        ],
        "image": [
            "pixtral-large-latest",
            "pixtral-12b-2409",
        ],
        "moderate": [
            "mistral-moderation-latest",
        ],
        "ocr": [
            "mistral-ocr-latest",
        ],
    }

    def __init__(self, api_key: str, model: str, type_request: str):
        self.api_key = api_key
        self.type_request = type_request
        self.__model = self.__validate_model(model)
        self.client = Mistral(api_key=self.api_key)

    def __validate_model(self, model: str):
        if model not in self.MODELS[self.type_request]:
            raise ValueError(
                f"Некорректная модель: {model}. Доступные модели: {self.MODELS[self.type_request]}"
            )
        return model

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model: str):
        self.__model = self.__validate_model(model)

    @abstractmethod
    def request(self, prompt: str, image_path: str | None = None) -> dict:
        pass

class MistralAIChat(MistralAI):
    def __init__(self, api_key: str, model: str, role: str):
        super().__init__(api_key, model, "text")
        self.role = role
        self.token_limit = 100_000
        self.messages = [
            {
                "role": "system",
                "content": role,
            }
        ]

    def __add_message(self, message: str, role: str, tokens: int):
        self.messages.append(
            {
                "role": role,
                "content": message,
            }
        )
        self.__check_token_limit(tokens)

    def __check_token_limit(self, tokens: int):
        if tokens > self.token_limit:
            self.messages.pop(1)

    def request(self, prompt: str, image_path: str | None = None) -> dict:
        self.__add_message(prompt, "user", 0)
        response = self.client.chat.complete(
            model=self.model,
            messages=self.messages,
        )
        result = {
            "response": response.choices[0].message.content,
            "total_tokens": response.usage.total_tokens,
        }
        self.__add_message(result["response"], "assistant", result["total_tokens"])
        return result

# Инициализация чата
chat = MistralAIChat(MISTRAL_APY_KEY, "mistral-large-latest", "Ты черный шар судьбы №8 из фильма 'трасса 60' и отвечаешь на вопросы в стиле этого фильма.")

# Функция обработки сообщений
async def handle_message(update: Update, context: CallbackContext) -> None:
    prompt = update.message.text
    if prompt.lower() == "стоп":
        await update.message.reply_text("Действие остановлено.", reply_markup=ReplyKeyboardMarkup([], resize_keyboard=True))
        return

    response = chat.request(prompt)
    await update.message.reply_text(response['response'], reply_markup=get_keyboard())

def get_keyboard():
    # Создаем клавиатуру с кнопкой "Стоп"
    keyboard = [[KeyboardButton("Стоп")]]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

# Основная функция
def main() -> None:
    application = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

    message_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message)
    application.add_handler(message_handler)

    application.run_polling()

if __name__ == '__main__':
    main()
