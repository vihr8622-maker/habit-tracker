Это так
import json
from datetime import date
import os

class Habit:
    def __init__(self, name: str):
        self.name = name
        self.done = False
        self.streak = 0
        self.created_at = date.today().isoformat()

    def mark_done(self):
        if not self.done:
            self.done = True
            self.streak += 1

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


if os.path.exists("habits.json"):
    with open("habits.json", "r", encoding="utf-8") as f:
        loaded = json.load(f)
    habits = []
    for item in loaded:
        h = Habit(item["name"])
        h.done = item["done"]
        h.streak = item["streak"]
        h.created_at = item["created_at"]
        habits.append(h)
    print("Привычки загружены из файла.")
else:
    habits = [
        Habit("Сон 7–8 часов"),
        Habit("Код 30 минут"),
        Habit("Прогулка 10 минут"),
    ]
    print("Файла нет. Создаю привычки заново.")

for h in habits:
    print(h.status())

print("\nЧто сделать?")
print("1. Отметить привычку выполненной")
print("2. Выход")
choice = input("Твой выбор: ").strip()

if choice == "1":
    for i, h in enumerate(habits, 1):
        print(f"{i}. {h.name}")
    num = input("Номер привычки: ").strip()
    if num.isdigit():
        idx = int(num) - 1
        if 0 <= idx < len(habits):
            habits[idx].mark_done()
            print(f"Отмечено: {habits[idx].status()}")
to_save = []
for h in habits:
   to_save.append({
        "name": h.name,
        "done": h.done,
        "streak": h.streak,
        "created_at": h.created_at,
    })

with open("habits.json", "w", encoding="utf-8") as f:
    json.dump(to_save, f, ensure_ascii=False, indent=2)

print("Сохранено в habits.json")
