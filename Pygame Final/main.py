from random import randint, choice
import pygame
import random

lanes = [18, 38, 58, 78, 98, 118, 138, 158, 178, 198, 218, 238, 258, 278, 298, 318, 338, 358, 378, 398, 418, 438, 458, 478, 498, 518, 538, 558, 578, 598, 618, 638, 658, 678, 698, 718, 738, 758, 778, 798, 818, 838, 858, 878, 898, 918, 938]
lanes_2 = lanes = [38, 58, 78, 98, 118, 138, 158, 178, 198, 218, 238, 258, 278, 298, 318, 338, 358, 378, 398, 418, 438, 458, 478, 498, 518, 538, 558, 578, 598, 618, 638, 658, 678, 698, 718, 738, 758, 778, 798, 818, 838, 858, 878, 898, 918, 938]
pygame.init()
pygame.mixer.init()

# Load Sounds
lives_lost = pygame.mixer.Sound('lives_lost.mp3')
gain_points = pygame.mixer.Sound('gain_points.wav')
game_win = pygame.mixer.Sound('game_win.mp3')
game_lost = pygame.mixer.Sound('game_lost.mp3')

# Setting The Width and Height
WIDTH, HEIGHT = 950, 950
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Setting The Frame Rate
clock = pygame.time.Clock()

# Setting The Font
main_font = pygame.font.SysFont("comicsans", 50)

 # Loading The Background Image
BG = pygame.image.load("background.png")

# Load Ice Cream Images
GREEN_ICE_CREAM = pygame.image.load("green_ice_cream.png")
RED_ICE_CREAM = pygame.image.load("red_ice_cream.png")
PINK_ICE_CREAM = pygame.image.load("pink_ice_cream.png")
PURPLE_ICE_CREAM = pygame.image.load("purple_ice_cream.png")
YELLOW_ICE_CREAM = pygame.image.load("yellow_ice_cream.png")
ORANGE_ICE_CREAM = pygame.image.load("orange_ice_cream.png")
BLACK_ICE_CREAM = pygame.image.load("black_ice_cream.png")
GRAY_ICE_CREAM = pygame.image.load("gray_ice_cream.png")
PEACH_ICE_CREAM = pygame.image.load("peach_ice_cream.png")

# Load Enemy Image
BEAR = pygame.image.load("herbert_bear.png")

class GameObject(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super(GameObject, self).__init__()
        self.surf = pygame.image.load(image)
        self.x = x
        self.y = y
        self.rect = self.surf.get_rect()

    def render(self, screen):
        self.rect.x = self.x
        self.rect.y = self.y
        screen.blit(self.surf, (self.x, self.y))

class Ice_Cream(GameObject):
    def __init__(self):
        super(Ice_Cream, self).__init__(0, 0, 'blue_ice_cream.png')
        self.dx = 0
        self.dy = (randint(0, 425) / 100) + 1
        self.reset()

    def move(self):
        self.x += self.dx
        self.y += self.dy
        if self.y > 950:
            self.reset()

    def reset(self):
        self.x = choice(lanes)
        self.y = random.choice([-64, 64])

class Enemy(GameObject):
    def __init__(self):
        super(Enemy, self).__init__(0, 0, 'tusk.png')
        self.dx = 0
        self.dy = (randint(0, 425) / 100) + 1
        self.reset()

    def move(self):
        self.x += self.dx
        self.y += self.dy
        if self.y > 950:
            self.reset()

    def reset(self):
        self.x = choice(lanes)
        self.y = random.choice([-64, 64])

class Player(GameObject):
    def __init__(self):
        super(Player, self).__init__(300, 630, 'penguin.png')
        self.dx = 0
        self.dy = 0
        self.pos_x = 1
        self.pos_y = 1
        self.reset()

    def left(self):
        if self.pos_x > 0:
            self.pos_x -= 1
            self.update_dx_dy()
    
    def right(self):
        if self.pos_x < len(lanes) - 1:
            self.pos_x += 1
            self.update_dx_dy()

    def up(self):
        if self.pos_y > 0:
            self.pos_y -= 1
            self.update_dx_dy()

    def down(self):
        if self.pos_y < len(lanes) - 1:
            self.pos_y += 1
            self.update_dx_dy()

    def move(self):
        self.x -= (self.x - self.dx) * 0.95
        self.y -= (self.y - self.dy) * 0.95
        if self.y > HEIGHT:
            self.pos_x = 1
            self.pos_y = 1

    def reset(self):
        self.x = lanes[self.pos_x]
        self.y = lanes[self.pos_y]
        self.dx = self.x
        self.dy = self.y

    def update_dx_dy(self):
        self.dx = lanes[self.pos_x]
        self.dy = lanes[self.pos_y]

class Bomb(GameObject):
    def __init__(self):
        super(Bomb, self).__init__(0, 0, 'bomb.png')
        self.dx = (randint(0, 425) / 100) + 1
        self.dy = 0
        self.reset()
    
    def move(self):
        self.x += self.dx
        self.y += self.dy
        if self.x > 950:
            self.reset()
    
    def reset(self):
        self.x = random.choice([-64, 64])
        self.y = choice(lanes_2)

# A Function That Contains The While Loop That Creates And Startes The Game

# Instances
player = Player()
ice_cream = Ice_Cream()
GREEN_ICE_CREAM = Ice_Cream()
RED_ICE_CREAM = Bomb()
PINK_ICE_CREAM = Bomb()
PURPLE_ICE_CREAM = Ice_Cream()
YELLOW_ICE_CREAM = Ice_Cream()
ORANGE_ICE_CREAM = Ice_Cream()
BLACK_ICE_CREAM = Ice_Cream()
GRAY_ICE_CREAM = Ice_Cream()
PEACH_ICE_CREAM = Ice_Cream()
enemy = Enemy()
BEAR = Enemy()
bomb = Bomb()

# All sprites Group
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(ice_cream)
all_sprites.add(enemy)
all_sprites.add(bomb)
all_sprites.add(GREEN_ICE_CREAM)
all_sprites.add(RED_ICE_CREAM)
all_sprites.add(PINK_ICE_CREAM)
all_sprites.add(PURPLE_ICE_CREAM)
all_sprites.add(YELLOW_ICE_CREAM)
all_sprites.add(ORANGE_ICE_CREAM)
all_sprites.add(BLACK_ICE_CREAM)
all_sprites.add(GRAY_ICE_CREAM)
all_sprites.add(PEACH_ICE_CREAM)
all_sprites.add(BEAR)

# Creating a Creams Group
creams = pygame.sprite.Group()
creams.add(ice_cream)
creams.add(GREEN_ICE_CREAM)

creams.add(YELLOW_ICE_CREAM)
creams.add(ORANGE_ICE_CREAM)
creams.add(BLACK_ICE_CREAM)
creams.add(GRAY_ICE_CREAM)
creams.add(PEACH_ICE_CREAM)
creams.add(PURPLE_ICE_CREAM)

# Creating an Ememies Group
enemies = pygame.sprite.Group()
enemies.add(enemy)
enemies.add(BEAR)

# Creating a Bomb Group
bombs = pygame.sprite.Group()
bombs.add(bomb)
bombs.add(RED_ICE_CREAM)
bombs.add(PINK_ICE_CREAM)

def game_function():
    running = True
    lives = 5
    points = 0
    level = 1
    lost = False
    while running:
        # Iterating Over A Pygame Evenet To Check If An event Type Has Occured
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_LEFT:
                    player.left()
                elif event.key == pygame.K_RIGHT:
                    player.right()
                elif event.key == pygame.K_UP:
                    player.up()
                elif event.key == pygame.K_DOWN:
                    player.down()

        # Copying The Background Image And Displaying It To The Screen
        screen.blit(BG, (0, 0))

        # Label That Tracks How Many Lives The User Has, Which Can Increase or Decrease Depending On The Collisions
        lives_label = main_font.render(f"Lives: {lives}", 1, (255, 255, 255))

        # Label That Tracks What Level The User Is On, Which Can Increase Depending On The Collisions
        level_label = main_font.render(f"Level: {level}", 1, (255, 255, 255))

        # Label That Tracks How Many Points The User Has, Which Can Increase Depending On The Collisions
        points_label = main_font.render(f"Points: {points}", 1, (255, 255, 255))

        # Copying The F String And Displaying It To The Screen, And Positioning It Using X and Y Values
        screen.blit(lives_label, (10, 10))

        # Copying The F String And Displaying It To The Screen, And Positioning It Using X and Y Values
        screen.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))

        # Copying The F String And Displaying It To The Screen, And Positioning It Using X and Y Values
        screen.blit(points_label, (WIDTH - points_label.get_width() - 415, 10))

        for entity in all_sprites:
            entity.move()
            entity.render(screen)

        enemy_collide = pygame.sprite.spritecollideany(player, enemies)
        if enemy_collide:
            lives -= 1
            pygame.mixer.Sound.play(lives_lost)
            enemy_collide.reset()
            if lives <= 0:
                main_label = main_font.render("You Lost", 1, (255, 255, 255))
                screen.blit(main_label, (WIDTH/2 - main_label.get_width()/2, 350))

        ice_cream_collide = pygame.sprite.spritecollideany(player, creams)
        if ice_cream_collide:
            points += 1
            pygame.mixer.Sound.play(gain_points)
            ice_cream_collide.reset()

        bomb_collide = pygame.sprite.spritecollideany(player, bombs)
        if bomb_collide:
            main_label = main_font.render("You Lost", 1, (255, 255, 255))
            screen.blit(main_label, (WIDTH/2 - main_label.get_width()/2, 350))
            pygame.mixer.Sound.play(game_lost)
            running = False
            bomb_collide.reset()

        # If Lost Is True, A Label Is Created That Is Copied And Displayed To The Screen Letting The User Know They Lost
        if lost:
            main_label = main_font.render("You Lost", 1, (255, 255, 255))
            screen.blit(main_label, (WIDTH/2 - main_label.get_width()/2, 350))

        if lives <= 0:
            lost = True
            running = False

        if points == 20:
            level += 1
        elif points == 40:
            level += 1
        elif points == 60:
            level += 1
        elif points == 80:
            level += 1
        elif points == 100:
            level += 1

        # If Level Equals 6, A Label Will Be Created, Copied, and Displayed To The Screen Showing The User They Won
        if level == 6:
            pygame.mixer.Sound.play(game_win)
            main_label = main_font.render("You Win", 1, (255, 255, 255))
            screen.blit(main_label, (WIDTH/2 - main_label.get_width()/2, 350))

        GREEN_ICE_CREAM.move()
        RED_ICE_CREAM.move()
        PINK_ICE_CREAM.move()
        PURPLE_ICE_CREAM.move()
        BEAR.move()
        GREEN_ICE_CREAM.render(screen)
        RED_ICE_CREAM.render(screen)
        PINK_ICE_CREAM.render(screen)
        BEAR.render(screen)

        pygame.display.flip()

        # FPS = Frames Per Second (60 Frames Per Second)
        clock.tick(60)

def home_page():
    running = True
    while running:
        screen.blit(BG, (0, 0))
        main_label = main_font.render("Press the mouse to begin", 1, (255, 255, 255))
        screen.blit(main_label, (WIDTH/2 - main_label.get_width()/2, 350))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                game_function()
    pygame.quit()

home_page()
