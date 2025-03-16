# TODO ООП. Ч6. Наследование. Миксины. Практика. Урок 27.

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
            raise ValueError(f"Некорректная модель: {model}. Доступные модели: {self.MODELS[self.type_request]}"
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

        self.messages = [
            {
                "role": "system",
                "content": role,
            }
        ]
    def __add_message(self, message: str, role: str):
        self.messages.append(
            {
                "role": role,
                "content": message,
            }
        )
    def request(self, prompt, image_path: str | None = None)-> dict:
        self.__add_message(prompt, "user")
        response = self.client.chat.complete(
            model = self.model,
            messages = self.messages,
        )
        self.__add_message(response.choices[0].message.content, "assistant")

        result = {
            "response": response.choices[0].message.content,
            "total_tokens": response.usage.total_tokens,
        }

        return result
    
chat = MistralAIChat(MISTRAL_APY_KEY, "mistral-large-latest", "system")
while True:
    prompt = input("Твой вопрос: ")
    if prompt.lower() == "выход":
        break
    responce = chat.request(prompt)
    

