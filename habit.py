from datetime import date


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


h = Habit("Ручной код")
print(h.status())
h.mark_done()
print(h.status())
h.rename("Python руками")
print(h.status())
h.reset()
print(h.status())
