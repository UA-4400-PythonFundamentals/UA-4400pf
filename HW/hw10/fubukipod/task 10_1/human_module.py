import random
from typing import ClassVar

class Human:
    
    _population_count: ClassVar[int] = 0

    def __init__(self, name: str):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Ім'я має бути непорожнім рядком.")
        self.name = name.strip()
        Human._population_count += 1

    def greet(self) -> None:
        print(f"Привіт, {self.name}! Радий(а) бачити тебе в цьому чудовому світі 😊")

    @classmethod
    def species_info(cls) -> str:
        return f"Вид: Homo sapiens. Створено екземплярів класу Human: {cls._population_count}"

    @staticmethod
    def random_message() -> str:
        messages = [
            "Підтримуй свою допитливість кожного дня!",
            "Цікавий факт: мед ніколи не псується.",
            "Посміхнись! Це покращує настрій не тільки тобі, а й оточуючим.",
            "Знаєш, Ейфелева вежа може вирости на 15 см влітку через нагрівання металу."
        ]
        return random.choice(messages)