# TODO ООП Ч12. Паттерны проектирования. Ч3. Урок 34.
from abc import ABC, abstractmethod
from dataclasses import dataclass, field


"""
состояние музыкальный плеер

"""
class AbstractState(ABC):
    """
    Абстрактный класс состояния плеера
    """
    @abstractmethod
    def press_play(self):
        """
        метод для воспроизведения музыки
        """
        pass

    @abstractmethod
    def press_pause(self):
        """
        метод для паузы
        """
        pass
    @abstractmethod
    def press_stop(self):
        """"
        метод для остановки
        """
        pass

class PlayingState(AbstractState):
    """
    состояние воспроизведения
    """
    def __init__(self, player):
        self.player = player

    def press_play(self):
            print("Музыка уже воспроизводится")
    
    def press_pause(self):
        print("Воспроизведение приостановлено")
        self.player.set_state(PausedState(self.player))

    def press_stop(self):
        print("Воспроизведение остановлено")
        self.player.set_state(StoppedState(self.player))

class PausedState(AbstractState):
    """
    состояние паузы
    """
    def __init__(self, player):
        self.player = player

    def press_play(self):
        print("Воспроизведение возобновлено")
        self.player.set_state(PlayingState(self.player))

    def press_pause(self):
        print("Музыка уже на паузе")

    def press_stop(self):
        print("Воспроизведение остановлено")
        self.player.set_state(StoppedState(self.player))

class  StoppedState(AbstractState):
    """
    состояние остановки
    """
    def __init__(self, player):
        self.player = player

    def press_play(self):
        print("Воспроизведение возобновлено")
        self.player.set_state(PlayingState(self.player))
    
    def press_pause(self):
        print("Музыка уже на паузе")
    
    def press_stop(self):
        print("Музыка уже остановлена")

class MusicPlayer:
    """
    музыкальный плеер
    """
    def __init__(self):
        self.state = StoppedState(self)

    def set_state(self, state: AbstractState):
            self.state = state

    def press_play(self):
        self.state.press_play()
    
    def press_pause(self):
        self.state.press_pause()

    def press_stop(self):
        self.state.press_stop()

# if __name__ == "__main__":
#     player = MusicPlayer()
#     player.press_play()
#     player.press_pause()
#     player.press_play()
#     player.press_stop()
#     player.press_pause()
#     player.press_stop()
#     player.press_play()
#     player.press_stop()

from abc import ABC, abstractmethod

import email

class AbstractNotification(ABC):
    """
    Абстрактный класс уведомления.
    """

    @abstractmethod
    def notify(self, message: str) -> None:
        """
        Абстрактный метод для отправки уведомления.
        """
        pass

class EmailNotification(AbstractNotification):
    """
    Конкретная реализация уведомления по электронной почте.
    """

    def notify(self, message: str) -> None:
        """
        Отправка уведомления по электронной почте.
        """
        print(f"Отправлено уведомление по электронной почте: {message}")

class TelegramNotification(AbstractNotification):
    """
    Конкретная реализация уведомления в Telegram.
    """

    def notify(self, message: str) -> None:
        """
        Отправка уведомления в Telegram.
        """
        print(f"Отправлено уведомление в Telegram: {message}")

class Blog:
    """
    Класс блога, который уведомляет подписчиков о новых постах.
    """

    def __init__(self) -> None:
        self.subscribers: list[Any] = []

    def subscribe(self, subscriber: AbstractNotification) -> None:
        """
        Подписывает пользователя на уведомления.
        """
        self.subscribers.append(subscriber)

    def unsubscribe(self, subscriber: AbstractNotification) -> None:
        """
        Отписывает пользователя от уведомлений.
        """
        self.subscribers.remove(subscriber)

    def new_post(self, title: str) -> None:
        """
        Уведомляет подписчиков о новом посте.
        """
        message: str = f"Новый пост: {title}"
        for subscriber in self.subscribers:
            subscriber.notify(message)

# # Пример использования паттерна Наблюдатель
# blog = Blog()

# email_notification = EmailNotification()
# telegram_notification = TelegramNotification()

# # Подписываемся на уведомления
# blog.subscribe(email_notification)
# blog.subscribe(telegram_notification)

# # Создаем новый пост
# blog.new_post("Паттерны проектирования в Python")

# # Отписываемся от уведомлений
# blog.unsubscribe(email_notification)

# # Создаем новый пост
# blog.new_post("Наблюдатель в Python")
from abc import ABC, abstractmethod
from dataclasses import dataclass, field

@dataclass
class Post:
    """
    Класс поста в блоге.
    """
    title: str
    content: str
    hashtas: list = field(default_factory=list)
    history: list = field(default_factory=list)

    def __post_init__(self):
        self.add_history(f" пост {id(self)} создан")

    def add_history(self, state: str) -> None:
        self.history.append(state)

class AbstractPostHandler(ABC):
    """
    Абстрактный класс снимка.
    """
    @abstractmethod
    def handler(self, post: Post) -> None:
        pass

class TitleHandlerA(AbstractPostHandler):
    """
    Конкретная реализация снимка для заголовка поста.
    """
    def handler(self, post: Post) -> None:
        post.add_history(f" заголовок {post.title} изменен")

class TitleHandlerB(AbstractPostHandler):
    """
    Конкретная реализация снимка для заголовка поста.
    """
    def handler(self, post: Post) -> None:
        post.add_history(f" заголовок {post.title} изменен")

class ContentHandlerA(AbstractPostHandler):
    """
    Конкретная реализация снимка для контента поста.
    """
    def handler(self, post: Post) -> None:
        post.add_history(f" контент {post.content} изменен")

class ContentHandlerB(AbstractPostHandler):
    """
    Конкретная реализация снимка для контента поста.
    """
    def handler(self, post: Post) -> None:
        post.add_history(f" контент {post.content} изменен")

class BlogProcessor:

    def __init__(self):
        self.title_handlers = {
            "A": TitleHandlerA(),
            "B": TitleHandlerB()
        }

    def process_post_interactive(self, post: Post) -> Post:

        print("Доступные обработчики:") 
        for key in self.title_handlers.keys():
            print(f"{key}")

        title_choice = input("Выберите обработчик заголовка или нажмите Enter для продолжения: ")
        print("доступные обработчики:")
        for key in self.title_handlers.keys():
            print(f"{key}")
        
        content_choice = input("Выберите обработчик контента или нажмите Enter для продолжения: ")

        if title_choice and title_choice in self.title_handlers:
            post.add_history(f" обработчик заголовка {title_choice} выбран")
            self.title_handlers[title_choice].handler(post)
        
        if content_choice and content_choice in self.title_handlers:
            post.add_history(f" обработчик контента {content_choice} выбран")
            self.title_handlers[content_choice].handler(post)
        post.add_history("Обрааботка поста завершена")
        return post
    
    def process_post(self, post: Post, title_handler_key: str, content_handler_key: str = None) -> Post:
        
        if title_handler_key and title_handler_key in self.title_handlers:
            post.add_history(f" обработчик заголовка {title_handler_key} выбран")
            self.title_handlers[title_handler_key].handler(post)

        if content_handler_key and content_handler_key in self.title_handlers:
            post.add_history(f" обработчик контента {content_handler_key} выбран")
            self.title_handlers[content_handler_key].handler(post)
        post.add_history("Обрааботка поста завершена")
        return post
def main():
    proccessor = BlogProcessor()

    post = Post(title="Заголовок поста", content="Контент поста")
    processed_post = proccessor.process_post_interactive(post)

    print("\nРезультат обработки:")
    print(f"заголовок: {processed_post.title}")
    print(f"контент: {processed_post.content}")
    print("история:")
    for entry in processed_post.history:
        print(f"- {entry}")

if __name__ == "__main__":
    main()