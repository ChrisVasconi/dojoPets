from unicodedata import east_asian_width
from winsound import PlaySound


class Ninja:
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.fist_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    def walk(self, walk, play):
        self.walk = walk
        self.play = play

    def feed(self, feed, eat):
        self.feed = feed
        self.eat = eat

    def bathe(self, bathe, noise):
        self.bathe = bathe
        self.noise = noise


class Pet:
    def __init__(self, name, type, tricks):
        self.name = name
        self.type = type
        self.tricks = tricks

    def sleep(self, sleep, energy):
        self.sleep = energy = + 5

    def eat(self, eat, energy, health):
        self.eat = energy = + 5
        self.eat = health = + 10
        print(f"Pet: {self.name}, Ate Milk bone")

    def play(self, play, health):
        self.play = health = + 5

    def noise(self, noise):
        self.noise = noise
        print("Woof")


Molly = Pet("ms.molly roo", 'Dog', 'Lay down')

Molly.eat("dog treat", 'energy', 'health')
Molly.sleep("energy", "health")
Molly.play("health", "play")
Molly.noise("noise")
