from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.progressbar import ProgressBar
import json
import os

SAVE_FILE = "progress.json"
MAX_LEVEL = 50
XP_PER_LEVEL = 100
MAX_ENERGY = 100

def load_progress():
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"level": 1, "xp": 0, "energy": MAX_ENERGY, "prestige": 0}

def save_progress(data):
    with open(SAVE_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

class FitnessRPG(App):
    def build(self):
        self.player = load_progress()

        self.layout = BoxLayout(orientation="vertical", padding=10, spacing=10)

        self.info_label = Label(text=self.get_info(), font_size=18)
        self.layout.add_widget(self.info_label)

        self.xp_bar = ProgressBar(max=XP_PER_LEVEL, value=self.player["xp"])
        self.layout.add_widget(self.xp_bar)

        self.energy_bar = ProgressBar(max=MAX_ENERGY, value=self.player["energy"])
        self.layout.add_widget(self.energy_bar)

        self.layout.add_widget(Button(text="🏋️ Тренировка (+30 XP, -20 Энергии)", on_press=self.train))
        self.layout.add_widget(Button(text="🥤 Вода (+10 XP)", on_press=self.drink))
        self.layout.add_widget(Button(text="🚶 Шаги (+20 XP, -10 Энергии)", on_press=self.walk))
        self.layout.add_widget(Button(text="😌 Отдых (+30 Энергии)", on_press=self.rest))

        return self.layout

    def get_info(self):
        return f"Престиж: {self.player['prestige']} | Уровень: {self.player['level']} | Энергия: {self.player['energy']}"

    def update_ui(self):
        self.info_label.text = self.get_info()
        self.xp_bar.value = self.player["xp"]
        self.energy_bar.value = self.player["energy"]
        save_progress(self.player)

    def level_up(self):
        while self.player["xp"] >= XP_PER_LEVEL:
            self.player["xp"] -= XP_PER_LEVEL
            self.player["level"] += 1
            if self.player["level"] > MAX_LEVEL:
                self.player["prestige"] += 1
                self.player["level"] = 1

    def train(self, instance):
        if self.player["energy"] >= 20:
            self.player["xp"] += 30
            self.player["energy"] -= 20
            self.level_up()
        self.update_ui()

    def drink(self, instance):
        self.player["xp"] += 10
        self.level_up()
        self.update_ui()

    def walk(self, instance):
        if self.player["energy"] >= 10:
            self.player["xp"] += 20
            self.player["energy"] -= 10
            self.level_up()
        self.update_ui()

    def rest(self, instance):
        self.player["energy"] = min(MAX_ENERGY, self.player["energy"] + 30)
        self.update_ui()

if __name__ == "__main__":
    FitnessRPG().run()
