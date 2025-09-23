# TODO Функции Ч2. Взаимодействие функций. Пакеты. модули. Импорт. if_name_. Урок 15.

# - Повторение типов аргументов в функциях
# - Варианты импортов модулей и модулей из пакетов
# - Корневая директория
# - Примеры импортов

# Функция которая принимает все типы аргументов
# позиционные параметры
# keyword аргументы
# Параметры по умолчанию
# Множесвтенные позиционные параметры
# Множесвтенные ключевые аргументы

def all_param_func(a, b, c=10, *args, **kwargs):
    print(f"{a=}")
    print(f"{b=}")
    print(f"{c=}")
    print(f"{args=}")
    print(f"{kwargs=}")

if __name__ == "__main__":
    all_param_func(1, 2, 3, 4, five=5)
    print("привет из модуля lesson_15.py")

name = __name__ # __main__
print(name)

# openai/gpt-4o-mini

from openai import OpenAI

client = OpenAI(
    api_key=, # ваш ключ в VseGPT после регистрации
    base_url="https://api.vsegpt.ru/v1",
)
"""
prompt = "Напиши анекдот про то как Python разработчик выбирает имя функции"

messages = [{"role": "user", "content": prompt}]


response_big = client.chat.completions.create(
    model="openai/gpt-4o-mini", # id модели из списка моделей - можно использовать OpenAI, Anthropic и пр. меняя только этот параметр
    messages=messages,
    temperature=0.9,
    max_tokens=100, # максимальное число ВЫХОДНЫХ токенов. Для большинства моделей не должно превышать 4096
    extra_headers={ "X-Title": "My App" }, # опционально - передача информация об источнике API-вызова
)

#print("Response BIG:",response_big)
response = response_big.choices[0].message.content
# print("Response:",response)
"""
#  PRACTICE
"""
функция get_openai_request
Принемает:
- Объект клиента OpenAI   client: OpenAI
- Cообщение пользователя prompt: str
- Модель  модели для генерации ответа model: str
- Максимальное число токенов ответа max_tokens: int
- Температура ответа temperature: float

Отдает ответ response: str
"""

def get_openai_request(
    client: OpenAI,
    prompt: str,
    max_tokens: int,
    model: str = "openai/gpt-4o-mini",
    temperature: float = 0.6,
) -> str:
    """
    Функция get_openai_request
    Принемает:
    - Объект клиента OpenAI   client: OpenAI
    - Cообщение пользователя prompt: str
    - Модель  модели для генерации ответа model: str
    - Максимальное число токенов ответа max_tokens: int
    - Температура ответа temperature: float
    Отдает ответ response: str
    """

    message = [{"role": "user", "content": prompt}]
    
    response_big = client.chat.completions.create(
        model=model,
        messages=message,
        temperature=temperature,
        max_tokens=max_tokens,
    )
    response = response_big.choices[0].message.content
    return response


# result = get_openai_request(
#     client=client,
#     prompt="Напиши андекдот про музыканта",
#     max_tokens=400,
#     model="anthropic/claude-3-5-haiku",
#     temperature=0.9,
# )

# print(result)

import base64

# Функция для кодирования изображения в base64
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

# Путь к вашему изображению
# image_path = r"C:\Users\ALEXSTONE\Downloads\Telegram Desktop\photo_2025-01-19_16-02-58.jpg"

# Получаем строку в формате base64
base64_image = encode_image(image_path)

response = client.chat.completions.create(
    model="gpt-4o-mini",
    temperature=0.5,
    max_tokens=200,
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Что изображено на этой картинке?",
                },
                {
                    "type": "image_url",
                    "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"},
                },
            ],
        }
    ],
)
# print(response.choices[0].message.content)

#  PRACTICE
"""
Функция для анализа изображения
Позволяет отправить картинку на анализ и получить ответ от GPT
 
 
 client: OpenAI,
    prompt: str,
    max_tokens: int,
    model: str = "openai/gpt-4o-mini",
    temperature: float = 0.6,
"""

def analyze_image(
    client: OpenAI,
    prompt: str,
    max_tokens: int,
    model: str = "openai/gpt-4o-mini",
    temperature: float = 0.6,
) -> str:
    """
    Функция для анализа изображения
    Позволяет отправить картинку на анализ и получить ответ от GPT
    """
    message = [{"role": "user", "content": prompt}]
    response_big = client.chat.completions.create(
        model=model,
        messages=message,
        temperature=temperature,
        max_tokens=max_tokens,
    )
    response = response_big.choices[0].message.content
    return response

# Путь к вашему изображению
image_path = r"C:\Users\ALEXSTONE\Downloads\Telegram Desktop\  photo_2025-01-19_16-02-58.jpg"

# Получаем строку в формате base64
base64_image = encode_image(image_path)
response = client.chat.completions.create(
    model="gpt-4o-mini",
    temperature=0.5,
    max_tokens=200,
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Что изображено на этой картинке?",
                },
                {
                    "type": "image_url",
                    "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"},
                },
            ],
        }
    ],
)
print(response.choices[0].message.content)

