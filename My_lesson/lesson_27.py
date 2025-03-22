# TODO ООП. Ч6. Наследование. Миксины. Практика. Урок 27.


from dotenv import load_dotenv

# pip install python-dotenv
import os
import base64

load_dotenv()
from settings import MISTRAL_APY_KEY
# MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")

# Тут мы можем вылавливать из переменных окружения ключи к API

from mistralai import Mistral
from abc import ABC, abstractmethod

class MistralAI(ABC):
    """
    Абстрактный класс для работы с API MistralAI.
    Наследники:
    - MistralAIChat
    - MistralAiImageChat
    - MistralAIModeration
    - MistralOCR

    :param api_key: Ключ API.
    :param model: Модель.
    :param type_request: Тип запроса.

    """
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


        # Messages - список словарей с сообщениями. Выносим в конкретные классы.
    
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
    def request(self, prompt: str, image_path: str | None = None)-> dict:
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
        """
        Метод добавления сообщения в список сообщений.
        :param message: Текст сообщения.
        :param role: Роль.
        :param tokens: Количество токенов.
        """
        self.messages.append(
            {
                "role": role,
                "content": message,
            }
        )

        self.__check_token_limit(tokens)

    def __check_token_limit(self, tokens: int):
        """
        Метод проверки лимита токенов.
        :param tokens: Количество токенов.
        """
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
    

# Тестовый запуск
chat = MistralAIChat(MISTRAL_APY_KEY, "mistral-large-latest", "Ты шутник юморист. Отвечаешь как робот Бендер из Футурамы")

while True:
    prompt = input("Введите текст: ")
    if prompt == "exit":
        break

    response = chat.request(prompt)
    print('Ответ:', response['response'])
    print('Токенов использовано:', response['total_tokens'])
    print("-" * 50)
    

