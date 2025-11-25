class Animal:
    alive = []

    def __init__(self, name: str,
                 health: int = 100,
                 hidden: bool = False) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}")

    def __str__(self) -> str:
        return ", ".join([str(animal) for animal in Animal.alive])


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, herbivore: Herbivore) -> None:
        if not isinstance(herbivore, Herbivore):
            return
        if not herbivore.hidden:
            herbivore.health -= 50
        if herbivore.health <= 0:
            herbivore.health = 0
        if herbivore.health == 0:
            herbivore.alive = False
            Animal.alive.remove(herbivore)
