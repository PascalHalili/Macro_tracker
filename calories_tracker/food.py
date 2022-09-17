from dataclasses import dataclass


@dataclass
class Food:
    name: str
    calories: int
    protein: int
    fat: int
    carbs: int