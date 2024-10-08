import pygame
import random

# background
grass_surface = pygame.image.load('graphics/ground1.png')
sky_surface = pygame.image.load('graphics/sky.png')

# character
stationary = pygame.image.load('graphics/girl1.png')
stationaryl = pygame.image.load('graphics/girl1l.png')
left = [
    pygame.image.load('graphics/girlrunningleft/3.png'),
    pygame.image.load('graphics/girlrunningleft/4.png'),
    pygame.image.load('graphics/girlrunningleft/5.png'),
    pygame.image.load('graphics/girlrunningleft/6.png'),
    pygame.image.load('graphics/girlrunningleft/7.png'),
    pygame.image.load('graphics/girlrunningleft/8.png'),
    pygame.image.load('graphics/girlrunningleft/9.png'),
    pygame.image.load('graphics/girlrunningleft/10.png'),
    pygame.image.load('graphics/girlrunningleft/11.png'),
    pygame.image.load('graphics/girlrunningleft/12.png'),
    pygame.image.load('graphics/girlrunningleft/13.png'),
    pygame.image.load('graphics/girlrunningleft/14.png'),
    pygame.image.load('graphics/girlrunningleft/15.png'),
    pygame.image.load('graphics/girlrunningleft/16.png'),
    pygame.image.load('graphics/girlrunningleft/17.png'),
    pygame.image.load('graphics/girlrunningleft/18.png'),
    pygame.image.load('graphics/girlrunningleft/19.png'),
    pygame.image.load('graphics/girlrunningleft/20.png'),
    pygame.image.load('graphics/girlrunningleft/1.png'),
    pygame.image.load('graphics/girlrunningleft/2.png'),
    pygame.image.load('graphics/girl1l.png')
]
right = [
    pygame.image.load('graphics/girlrunningright/3.png'),
    pygame.image.load('graphics/girlrunningright/4.png'),
    pygame.image.load('graphics/girlrunningright/5.png'),
    pygame.image.load('graphics/girlrunningright/6.png'),
    pygame.image.load('graphics/girlrunningright/7.png'),
    pygame.image.load('graphics/girlrunningright/8.png'),
    pygame.image.load('graphics/girlrunningright/9.png'),
    pygame.image.load('graphics/girlrunningright/10.png'),
    pygame.image.load('graphics/girlrunningright/11.png'),
    pygame.image.load('graphics/girlrunningright/12.png'),
    pygame.image.load('graphics/girlrunningright/13.png'),
    pygame.image.load('graphics/girlrunningright/14.png'),
    pygame.image.load('graphics/girlrunningright/15.png'),
    pygame.image.load('graphics/girlrunningright/16.png'),
    pygame.image.load('graphics/girlrunningright/17.png'),
    pygame.image.load('graphics/girlrunningright/18.png'),
    pygame.image.load('graphics/girlrunningright/19.png'),
    pygame.image.load('graphics/girlrunningright/20.png'),
    pygame.image.load('graphics/girlrunningright/1.png'),
    pygame.image.load('graphics/girlrunningright/2.png'),
    pygame.image.load('graphics/girl1.png'),
]

# fruits
fruits = [
    pygame.image.load('graphics/fruits/apple.png'),
    pygame.image.load('graphics/fruits/bananas.png'),
    pygame.image.load('graphics/fruits/grapes.png'),
    pygame.image.load('graphics/fruits/peach.png'),
    pygame.image.load('graphics/fruits/pear.png')
]

bomb = pygame.image.load('graphics/bomb.png')
# hearts
hearts = [
    pygame.image.load('graphics/hearts/full_hearts.png'),
    pygame.image.load('graphics/hearts/two_hearts.png'),
    pygame.image.load('graphics/hearts/one_hearts.png'),
    pygame.image.load('graphics/hearts/zero_hearts.png')
]


class GameView:

    def __init__(self, window):
        self.window = Window()
        self.draw = Draw(self.window)  # Instantiate Draw class
        self.chosen = self.draw.choose_random()

    def get_window_data(self):
        return self.window.get_data()


class Window:
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))
        self.win_width = 800

    def get_data(self):
        return {
            "win_width": self.win_width,
            "screen": self.screen
        }

    def draw_game(self):
        self.screen.fill((0, 0, 0))  # Clear screen with black color
        self.screen.blit(sky_surface, (0, 0))
        self.screen.blit(grass_surface, (0, 335))


class Draw:
    def __init__(self, window):
        self.window = window
        self.font = pygame.font.Font('graphics/Pacifico.ttf', 30)
        self.font1 = pygame.font.Font('graphics/Pacifico.ttf', 20)
        self.font2 = pygame.font.Font('graphics/Pacifico.ttf', 15)
        self.random = random
        self.view = True
        self.new = True
        self.chosen = None
        self.parameter = None

    def draw_distance(self, x, y, distance):
        distance_surface = self.font1.render(f"Distance: {distance}", False, 'black')
        self.draw(x, y, distance_surface)

    # def draw_info(self, x, y, info):
    #     info_surface = self.font2.render(f"Current position of Anna: {info}", False, 'white')
    #     self.draw(x, y, info_surface)

    def draw_game_over(self, x, y):
        game_over_surface = self.font.render("GAME OVER", False, 'red')
        self.draw(x, y, game_over_surface)

    def draw_start(self, x, y):
        start_surface = self.font1.render("Catch all the fruits and watch out for the bombs!", False, 'black')
        self.draw(x, y, start_surface)

    def draw_hearts_left(self, x, y, hearts_number):
        hearts_number_surface = self.font1.render(f"The number of hearts left: {hearts_number}", False, 'black')
        self.draw(x, y, hearts_number_surface)

    def draw_anna(self, stepIndex, x, y, face_left, face_right):
        if stepIndex >= 21:
            stepIndex = 0
        if face_left:
            self.window.screen.blit(left[stepIndex], (x, y))
        elif face_right:
            self.window.screen.blit(right[stepIndex], (x, y))
        else:
            self.window.screen.blit(stationary, (x, y))

    def choose_random(self):
        self.chosen = random.choice(fruits)
        return self.chosen

    def draw(self, x, y, parameter):
        self.parameter = parameter
        self.window.screen.blit(parameter, (x, y))

    def draw_fruit(self, x, y, parameter=None):
        if parameter is None:
            parameter = self.chosen
        self.draw(x, y, parameter)

    def draw_score(self, x, y, points):
        score_surface = self.font1.render(f"Score: {points}", False, 'black')
        self.draw(x, y, score_surface)

    def draw_hearts(self, x, y, number):
        self.window.screen.blit(hearts[number], (x, y))

    def draw_bomb(self, x, y, parameter=None):
        if parameter is None:
            parameter = bomb
        self.draw(x, y, parameter)
