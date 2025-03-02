# TODO ООП Ч3. Инкапсуляция. Приватные методы и атрибуты. Урок 24

# _ это protected - доступно при наследовании
# __ это private - доаступно только внутри класса

# собественные getters и  setters
# @property
# @speed.setter
# @speed.deleter

# https://pypi.org/project/tabulate/

import os
from mistralai import Mistral
from settings import APY_KEY

api_key = APY_KEY
model = "mistral-large-latest"

# client = Mistral(api_key=api_key)

# chat_response = client.chat.complete(
#     model= model,
#     messages = [
#         {
#             "role": "user",
#             "content": "Напиши веселый текст для песни",
#         },
#     ]
# )
# print(chat_response.choices[0].message.content)

class MistralAIchat:
    def __init__(self, api_key: str, model: str, system_role: str):
        self.api_key = api_key
        self.__model = model
        self.system_role = system_role
        self.client = Mistral(api_key=api_key)

    def __validate_model(self, model: str):
        if model not in self.MODELS:
            raise ValueError(f"некореткая модель: {model}. доступная модель {self.MODELS}")
        return model
    @property
    def model(self):
        return self.__model
    @model.setter
    def model(self, model: str):
        self.__model = self.__validate_model(model)

    def text_coplection(self, prompt: str):
        response = self.client.chat.complete(
            model = self.model,
            messages = [
                {
                    "role": "user",
                    "content": prompt,
                }
            ]
        )
        return response.choices[0].message.content  
    
chat = MistralAIchat(api_key=api_key, model="mistral-small-latest", system_role="Ты банан")
print(chat.text_coplection("Напиши обычный анекдот"))