import json
import os
from datetime import date, timedelta


class Habit:
    def __init__(self, name: str):
        self.name = name
        self.done = False
        self.streak = 0
        self.created_at = date.today().isoformat()
        self.last_done = None

    def mark_done(self):
        today = date.today().isoformat()
        yesterday = (date.today() - timedelta(days=1)).isoformat()

        if self.last_done == today:
            print("Уже выполнено сегодня.")
            return

        if self.last_done == yesterday:
            self.streak += 1
        else:
            self.streak = 1

        self.done = True
        self.last_done = today

    def rename(self, new_name: str):
        if not new_name:
            return
        self.name = new_name

    def reset(self):
        self.done = False
        self.streak = 0

    def status(self):
        if self.done:
            return f"{self.name}: выполнено, серия {self.streak} (с {self.created_at})"
        return f"{self.name}: не выполнено, серия {self.streak} (с {self.created_at})"


def load_habits():
    if os.path.exists("habits.json"):
        with open("habits.json", "r", encoding="utf-8") as f:
            loaded = json.load(f)
        habits = []
        for item in loaded:
            h = Habit(item["name"])
            h.done = item["done"]
            h.streak = item["streak"]
            h.created_at = item["created_at"]
            h.last_done = item.get("last_done")
            habits.append(h)  # <--- ИСПРАВЛЕНО: Добавляем в список
        print("Привычки загружены из файла.")
    else:
        habits = [
            Habit("Сон 7–8 часов"),
            Habit("Код 30 минут"),
            Habit("Прогулка 10 минут"),
        ]
        print("Файла нет. Создаю привычки заново.")
    return habits


def save_habits(habits):
    to_save = []
    for h in habits:
        to_save.append({
            "name": h.name,
            "done": h.done,
            "streak": h.streak,
            "created_at": h.created_at,
            "last_done": h.last_done,  # <--- ИСПРАВЛЕНО: Сохраняем дату
        })
    with open("habits.json", "w", encoding="utf-8") as f:
        json.dump(to_save, f, ensure_ascii=False, indent=2)
    print("Сохранено в habits.json")


def show_habits(habits):
    for h in habits:
        print(h.status())


def mark_habit(habits):
    for i, h in enumerate(habits, 1):
        print(f"{i}. {h.name}")
    num = input("Номер привычки: ").strip()
    if num.isdigit():
        idx = int(num) - 1
        if 0 <= idx < len(habits):
            habits[idx].mark_done()
            print(f"Отмечено: {habits[idx].status()}")


habits = load_habits()

while True:
    show_habits(habits)
    print("\nЧто сделать?")
    print("1. Отметить привычку выполненной")
    print("2. Выход")
    choice = input("Твой выбор: ").strip()

    if choice == "1":
        mark_habit(habits)
    elif choice == "2":
        save_habits(habits)
        print("Пока.")
        break
    else:
        print("Не понял. Введи 1 или 2.")
