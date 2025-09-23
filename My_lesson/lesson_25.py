"""
.env - Содержит секретные ключи. Обязательно добавлять в .gitignore и никогда не коммитить.
.env.example - Пример файла .env - обязательно идет на Github.
"""

from dotenv import load_dotenv

# pip install python-dotenv
import os
import base64

load_dotenv()

MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")

# Тут мы можем вылавливать из переменных окружения ключи к API

from mistralai import Mistral


# class MistralAIChat:

#     MODELS = [
#         "mistral-small-latest",
#         "mistral-large-latest",
#         "mistral-moderation-latest",
#         "pixtral-12b-2409",
#     ]

#     def __init__(self, api_key: str, model: str, system_role: str):
#         self.api_key = api_key
#         self.__model = self.__validate_model(model)
#         self.system_role = system_role
#         self.client = Mistral(api_key=self.api_key)

#         self.messages = [
#             {
#                 "role": "system",
#                 "content": self.system_role,
#             }
#         ]

#     def __validate_model(self, model: str):
#         if model not in self.MODELS:
#             raise ValueError(
#                 f"Некорректная модель: {model}. Доступные модели: {self.MODELS}"
#             )

#         return model

#     @property
#     def model(self):
#         return self.__model

#     @model.setter
#     def model(self, model: str):
#         self.__model = self.__validate_model(model)

#     def __add_message(self, message: str, role: str):
#         self.messages.append(
#             {
#                 "role": role,
#                 "content": message,
#             }
#         )

#     def text_completion(self, prompt: str):
#         self.__add_message(prompt, "user")

#         response = self.client.chat.complete(
#             model=self.model,
#             messages=self.messages,
#         )

#         self.__add_message(response.choices[0].message.content, "assistant")

#         return response.choices[0].message.content


# class MistralAiImageChat:
#     MODELS = [
#         "pixtral-12b-2409",
#     ]

#     def __init__(self, api_key: str, model: str, system_role: str):
#         self.api_key = api_key
#         self.__model = self.__validate_model(model)
#         self.system_role = system_role
#         self.client = Mistral(api_key=self.api_key)

#         self.messages = [
#             {
#                 "role": "system",
#                 "content": self.system_role,
#             }
#         ]

#     def __validate_model(self, model: str):
#         if model not in self.MODELS:
#             raise ValueError(
#                 f"Некорректная модель: {model}. Доступные модели: {self.MODELS}"
#             )

#         return model

#     @property
#     def model(self):
#         return self.__model

#     @model.setter
#     def model(self, model: str):
#         self.__model = self.__validate_model(model)

#     def __add_message(self, message: str, role: str):
#         self.messages.append(
#             {
#                 "role": role,
#                 "content": message,
#             }
#         )
#     def __add_image_message(self, message: str, image_base64: str | None = None):
#         new_message = [
#             {
#                 "role": "user",
#                 "content": [
#                     {"type": "text", "text": message},
#                 ]
#             }
#         ]

#         if image_base64:
#             new_message[0]["content"].append(
#                 {
#                     "type": "image_url",
#                     "image_url": f"data:image/jpeg;base64,{image_base64}",
#                 }
#             )

#         self.messages.extend(new_message)
#     def __encode_image(self, image_path: str) -> str | None:
#         """Метод кодирования изображений в Base64"""

#         try:
#             with open(image_path, "rb") as image_file:
#                 return base64.b64encode(image_file.read()).decode("utf-8")
#         except FileNotFoundError:
#             print(f"Ошибка: Файл {image_path} не найден.")
#             return None
#         except Exception as e:
#             print(f"Иная ошибка: {e}")
#             return None
        
#     def image_text_completion(self, prompt: str, image_path: str | None = None):
#         """
#         Метод для генерации текста по изображению.
#         :param prompt: Текст запроса.
#         :param image_path: Путь к изображению.
#         :return: Сгенерированный текст.
#         """
#         if image_path:
#             image_base64 = self.__encode_image(image_path)
#             if image_base64:
#                 self.__add_image_message(prompt, image_base64)
#             else:
#                 return "Ошибка при кодировании изображения"
#         else:
#             self.__add_message(prompt, "user")

#         response = self.client.chat.complete(
#             model=self.model,
#             messages=self.messages,
#         )

#         self.__add_message(response.choices[0].message.content, "assistant")

#         return response.choices[0].message.content


# # Тестовый запуск
# image = r"C:\Users\user\Pictures\2025-01-18_14-07-29.png"
# chat = MistralAiImageChat(api_key=MISTRAL_API_KEY, model="pixtral-12b-2409", system_role="Ты опытный разработчик")
# print(chat.image_text_completion("Дай детальную обратную связь по изображению. Там есть текст на русском языке", image))

# # Цикл дополнительных вопросов
# while True:
#     question = input("Задайте вопрос (или напишите 'выход' для завершения): ")
#     if question.lower() == "выход":
#         break
#     print(chat.image_text_completion(question))



class AiChat():
    message = "Мое послание"
    def __str__(self):
        return f"я есть {self.__class__.__name__}. {self.message}"
    
    def send_message(self, additional_message: str = ""):
        return f"Отправляю сообщение: {self.message} {additional_message}"
    
class ImageAiChat(AiChat):
    def send_message(self, additional_message = ""):
        result = AiChat.send_message(self, additional_message)
        return f"{result} и еще какой то текст"

class MistralAiChat(AiChat):
    pass

image_ai_chat = ImageAiChat()
print(image_ai_chat.send_message("Привет"))
