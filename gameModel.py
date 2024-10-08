import pygame
import random
from abc import ABC, abstractmethod


class GameModel:
    def __init__(self):
        self.anna = Anna()
        self.anna.x = 250
        self.anna.y = 370
        self.fruit = Fruit(y=0)
        self.score = Points(x=611, y=23)
        self.life = Hearts(x=25, y=50)
        self.bomb = Bomb(y=0)

    def get_bomb_data(self):
        return self.bomb.get_data()

    def get_anna_data(self):
        return self.anna.get_data_anna()

    def get_fruit_data(self):
        return self.fruit.get_data()

    def get_score_data(self):
        return self.score.get_data_score()

    def get_hearts_data(self):
        return self.life.get_data_hearts()


class Anna:
    def __init__(self):
        self.__x = 0
        self.__y = 0
        self.velx = 10
        self.face_right = False
        self.face_left = False
        self.stepIndex = 0
        self.hitbox = 0
        self.distance_value = 0
        self.dx = 0
        self.font = pygame.font.Font('graphics/Pacifico.ttf', 30)
        self.distance = self.font.render(f"SCORE: {self.distance_value}", False, 'slateblue4')

    def __str__(self):
        return f"{self.__x+60}"

    def update_distance(self, distance):
        self.distance = distance
        self.distance = self.font.render(f"SCORE: {distance}", False, 'slateblue4')

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value
        self.update_hitbox()

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
        self.update_hitbox()

    def get_data_anna(self):
        return {
            "x": self.__x,
            "y": self.__y,
            "velx": self.velx,
            "face_right": self.face_right,
            "face_left": self.face_left,
            "stepIndex": self.stepIndex,
            "hitbox": self.hitbox,
            "distance_value": self.distance_value
        }

    def update_hitbox(self):
        self.hitbox = (self.__x + 20, self.__y + 20, 90, 130)

    def direction(self):
        if self.face_right:
            return 1
        if self.face_left:
            return -1


class FallingObject(ABC):
    def __init__(self, x, y, vely):
        self.x = x
        self.y = y
        self.vely = vely
        self.hitbox = (self.x, self.y, 100, 100)

    @abstractmethod
    def off_screen(self):
        self.x = random.randint(20, 670)
        self.y = 0


class Bomb(FallingObject):
    def __init__(self, y):
        x = random.randint(50, 600)
        super().__init__(x, y, vely=7)

    def get_data(self):
        data = {
            "x": self.x,
            "y": self.y,
            "hitbox": self.hitbox,
            "vely": self.vely
        }
        return data

    def off_screen(self):
        FallingObject.off_screen(self)
        print("Be careful! Another bomb!")


class Fruit(FallingObject):
    def __init__(self, y):
        x = random.randint(50, 600)
        super().__init__(x, y, vely=5)
        self.random = random

    def get_data(self):
        data = {
            "x": self.x,
            "y": self.y,
            "hitbox": self.hitbox,
            "vely": self.vely,
            "random": self.random
        }
        return data

    def off_screen(self):
        FallingObject.off_screen(self)
        print("Another fruit is about to fall!")


class Points:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.points = 0
        self.score = 0
        self.font = pygame.font.Font('graphics/Pacifico.ttf', 30)

    def __add__(self, other):
        if isinstance(other, int):
            self.points += other
            return self

    def get_data_score(self):
        return {
            "x": self.x,
            "y": self.y,
            "points": self.points,
            "score": self.score,
            "font": self.font
        }

    def update_score(self, points):
        self.score = points
        self.score = self.font.render(f"SCORE: {points}", False, 'slateblue4')

    def levels(self):

        if self.points <= 5:
            return 0
        elif 5 < self.points <= 10:
            return 1
        elif 10 < self.points <= 20:
            return 2
        elif 20 < self.points <= 30:
            return 3
        elif 30 < self.points:
            return 4


class Hearts:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.number = 0
        self.hearts_left = [1, 2, 3]

    def get_data_hearts(self):
        return {
            "x": self.x,
            "y": self.y,
            "number": self.number,
            "hearts_left": self.hearts_left
        }

    def __len__(self):
        return len(self.hearts_left)
