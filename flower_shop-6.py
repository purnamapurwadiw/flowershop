# === Stage 6: Связанная сущность ===
# Project: FlowerShop
from datetime import date


class Flower:
    def __init__(self, name, species, length):
        self.id = self._generate_id()
        self.name = name
        self.species = species
        self.length = length

    @staticmethod
    def _generate_id():
        return Flower._next_id()

    @classmethod
    def _next_id(cls):
        cls._counter += 1
        return cls._counter

    def __str__(self):
        return f"Flower(id={self.id}, name={self.name}, species={self.species}, length={self.length})"


Flower._counter = 0


def add_flower(name, species, length):
    flower = Flower(name, species, length)
    return flower


def get_flower_by_id(flower_id):
    return None


def get_flowers():
    return []
