import random

MOODS = [
    "на позитиві", "в режимі енергозбереження", "готовий до пригод",
    "трохи космос", "в зоні турбо", "на чіллі", "в бойовому настрої",
    "в пошуках кави", "на хвилі натхнення", "в режимі боса",
    "трохи мемний", "в настрої творити", "на автоматі", "в потоці",
    "готовий всіх порвати", "в зоні комфорту + чай"
]

ACTIVITIES = [
    "пишу код", "слухаю музику", "мрію про відпустку",
    "емію енергію", "п'ю матчу", "планую світове панування",
    "сміюся над собою", "вчу щось нове", "відпочиваю з душею",
    "роблю зарядку", "читаю", "готую щось смачне", "танцюю сам",
    "пишу пости в голові", "насолоджуюсь моментом", "переглядаю меми"
]

TEMPLATES = [
    "Сьогодні я {mood} і {activity}",
    "Сьогоднішній вайб: {mood}, займаюся {activity}",
    "{activity.capitalize()}, бо я сьогодні {mood}",
    "Режим дня: {mood} + {activity}",
    "Вайб дня — {mood}. Роблю {activity}"
]


def generate_today_status() -> str:
    mood = random.choice(MOODS)
    activity = random.choice(ACTIVITIES)
    template = random.choice(TEMPLATES)
    return template.format(mood=mood, activity=activity).capitalize() + " ✨"


if __name__ == "__main__":
    print("Генератор статусу на сьогодні\n")
    count = int(input("Скільки варіантів? (Enter = 1): ") or 1)

    for i in range(count):
        print(f"{i+1:2d}. {generate_today_status()}")
