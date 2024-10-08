import pygame
from gameModel import GameModel
import gameView
import sys
import gc


class GameController:
    model = None
    view = None
    start = False

    def __init__(self):
        pygame.init()
        self.model = GameModel()
        self.window = gameView.Window()
        self.view = gameView.GameView(self.window)

        data = self.model.get_anna_data()
        print(data)

        data_fruit = self.model.get_fruit_data()
        print(data_fruit)

        data_view = self.view.get_window_data()
        print(data_view)

        data_score = self.model.get_score_data()
        print(data_score)

        data_bomb = self.model.get_bomb_data()
        print(data_bomb)

        self.data = data
        self.data_fruit = data_fruit
        self.data_view = data_view
        self.data_score = data_score
        self.data_bomb = data_bomb

        self.current_frame_index = 0

    def get_bomb_data(self):
        return self.data_bomb

    def get_anna_data(self):
        return self.data

    def get_fruit_data(self):
        return self.data_fruit

    def gain_distance(self):
        anna = self.model.anna
        anna.distance_value += anna.stepIndex

    def move_anna(self, userInput):
        anna = self.model.anna
        win = self.window
        self.gain_distance()

        if userInput[pygame.K_RIGHT] and anna.x <= win.win_width - 72:
            anna.x += anna.velx
            anna.face_right = True
            anna.face_left = False
            anna.stepIndex += 1
        elif userInput[pygame.K_LEFT] and anna.x >= -50:
            anna.x -= anna.velx
            anna.face_right = False
            anna.face_left = True
            anna.stepIndex += 1
        elif userInput[pygame.KEYUP]:
            anna.face_right = False
            anna.face_left = False
            anna.stepIndex = 0
        else:
            anna.stepIndex = 0
        anna.update_hitbox()

        if anna.stepIndex >= 20:
            anna.stepIndex = 0

    def hit(self):
        anna = self.model.anna
        fruit = self.model.fruit
        if anna.hitbox[0] < fruit.x + 50 < anna.hitbox[0] + anna.hitbox[2] and anna.hitbox[1] < fruit.y + 50 < anna.hitbox[1] + anna.hitbox[3]:
            return True
        else:
            return False

    def levels(self):
        score = self.model.score
        score.update_score(score.points)

        if score.points <= 5:
            return 0
        elif 5 < score.points <= 10:
            return 1
        elif 10 < score.points <= 20:
            return 2
        elif 20 < score.points <= 30:
            return 3
        elif 30 < score.points:
            return 4

    def accelerate(self):
        score = self.model.score
        fruit = self.model.fruit

        score.update_score(points=score.points)

        if score.levels() == 0:
            fruit.vely = 3
        elif score.levels() == 1:
            fruit.vely = 5
        elif score.levels() == 2:
            fruit.vely = 7
        elif score.levels() == 3:
            fruit.vely = 9
        elif score.levels() == 4:
            fruit.vely = 11

    def gaining(self):
        score = self.model.score
        score += 1
        score.update_score(points=score)

    def losing(self):
        life = self.model.life
        life.number = life.number + 1
        life.hearts_left.pop()
        print(f"You have {len(life)} number of hearts left!")
        if life.number >= 3:
            self.lose_the_game()

    def move(self):
        fruit = self.model.fruit

        self.accelerate()

        if self.hit():
            fruit.off_screen()
            self.gaining()
            self.view.draw.choose_random()

        if fruit.y >= 0:
            fruit.y += fruit.vely

        if fruit.y >= 480:
            fruit.off_screen()
            self.losing()
            self.view.draw.choose_random()

    def move_bomb(self):
        bomb = self.model.bomb

        if self.hit_bomb():
            bomb.off_screen()
            self.lose_the_game()

        if bomb.y >= 0:
            bomb.y += bomb.vely

        if bomb.y >= 480:
            bomb.off_screen()

    def hit_bomb(self):
        anna = self.model.anna
        bomb = self.model.bomb
        if anna.hitbox[0] < bomb.x + 50 < anna.hitbox[0] + anna.hitbox[2] and anna.hitbox[1] < bomb.y + 50 < anna.hitbox[1] + anna.hitbox[3]:
            return True
        else:
            return False

    def lose_the_game(self):
        self.view.draw.draw_game_over(x=300, y=250)
        pygame.display.update()
        pygame.time.delay(1000)
        pygame.quit()
        sys.exit()

    def start_the_game(self):
        if not self.start:
            self.view.draw.draw_start(x=170, y=270)
            pygame.display.update()
            pygame.time.delay(2500)
            self.start = True

    def drawing(self):

        anna = self.model.anna
        self.view.draw.draw_anna(stepIndex=anna.stepIndex, x=anna.x, y=anna.y, face_left=anna.face_left, face_right=anna.face_right)
        self.view.draw.draw_distance(x=610, y=50, distance=anna.distance_value)
        # self.view.draw.draw_info(x=30, y=570, info=anna)

        fruit = self.model.fruit
        self.view.draw.draw_fruit(x=fruit.x, y=fruit.y)

        score = self.model.score
        self.view.draw.draw_score(x=score.x, y=score.y, points=score.points)
        score.update_score(points=score.points)

        life = self.model.life
        self.view.draw.draw_hearts(x=life.x, y=life.y, number=life.number)
        self.view.draw.draw_hearts_left(x=30, y=23, hearts_number=len(life))

        bomb = self.model.bomb
        self.view.draw.draw_bomb(x=bomb.x, y=bomb.y)

    def draw_game(self):
        pygame.display.set_caption('Catch The Fruit!')
        pygame_icon = pygame.image.load('graphics/fruits/apple.png')
        self.window.draw_game()
        pygame.display.set_icon(pygame_icon)
        self.start_the_game()
        self.drawing()

    def __del__(self):
        self.model = None
        self.view = None
        print("Garbage collected.")
        gc.collect()
        print(f"Unreachable objects: {gc.garbage}.")

    def run_game(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            keys = pygame.key.get_pressed()
            self.move_anna(keys)
            self.accelerate()
            self.move()
            self.move_bomb()
            pygame.display.update()
            pygame.time.Clock().tick(45)
            self.draw_game()

        pygame.quit()
