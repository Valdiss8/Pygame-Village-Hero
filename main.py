import pygame
from random import randint

pygame.init()
'''Interface'''

WIDTH, HEIGHT = 1280, 780
FPS = 60
TILE = 32

window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

"""Window Name"""
pygame.display.set_caption('Village Hero')

fontUI = pygame.font.Font(None, 30)

imgHero = [[[
    pygame.image.load('images/sprites/hero_level_1/forward_1.png'),
    pygame.image.load('images/sprites/hero_level_1/forward_2.png'),
    pygame.image.load('images/sprites/hero_level_1/forward_3.png')
],
    [
        pygame.image.load('images/sprites/hero_level_1/right_1.png'),
        pygame.image.load('images/sprites/hero_level_1/right_2.png'),
        pygame.image.load('images/sprites/hero_level_1/right_3.png')
    ],
    [
        pygame.image.load('images/sprites/hero_level_1/back_1.png'),
        pygame.image.load('images/sprites/hero_level_1/back_2.png'),
        pygame.image.load('images/sprites/hero_level_1/back_3.png'),
    ],
    [
        pygame.image.load('images/sprites/hero_level_1/left_1.png'),
        pygame.image.load('images/sprites/hero_level_1/left_2.png'),
        pygame.image.load('images/sprites/hero_level_1/left_3.png'),
    ]
]]

DIRECTS = [[0, -1], [1, 0], [0, 1], [-1, 0]]

MOVE_SPEED = [1, 2, 2, 1, 2, 3, 3, 2]
BULLET_SPEED = [4, 5, 6, 5, 5, 5, 6, 7]
BULLET_DAMAGE = [1, 1, 2, 3, 2, 2, 3, 4]
SHOT_DELAY = [60, 50, 30, 40, 30, 25, 25, 30]


class Hero:
    def __init__(self, hp, damage, px, py, direct, keyList):

        objects.append(self)
        self.type = 'hero'

        self.rect = pygame.Rect(px, py, TILE, TILE)
        self.direct = direct
        self.hp = hp
        self.moveSpeed = 2

        self.shotTimer = 0
        self.shotDelay = 60
        self.bulletSpeed = 5
        self.bulletDamage = damage

        self.keyLEFT = keyList[0]
        self.keyRIGHT = keyList[1]
        self.keyUP = keyList[2]
        self.keyDOWN = keyList[3]
        self.keySHOT = keyList[4]

        self.rank = 0
        self.image = imgHero[self.rank][0][0]
        self.rect = self.image.get_rect(center=self.rect.center)

        self.count = 0

    def update(self):
        self.image = imgHero[self.rank][0][0]
        self.rect = self.image.get_rect(center=self.rect.center)
        self.moveSpeed = MOVE_SPEED[self.rank]
        self.shotDelay = SHOT_DELAY[self.rank]
        self.bulletSpeed = BULLET_SPEED[self.rank]
        self.bulletDamage = BULLET_DAMAGE[self.rank]

        oldX, oldY = self.rect.topleft

        if keys[self.keyLEFT]:
            self.rect.x -= self.moveSpeed
            self.direct = 3
            self.image = imgHero[self.rank][self.direct][self.count]

        elif keys[self.keyRIGHT]:
            self.rect.x += self.moveSpeed
            self.direct = 1
            self.image = imgHero[self.rank][self.direct][self.count]

        elif keys[self.keyUP]:
            self.rect.y -= self.moveSpeed
            self.direct = 0
            self.image = imgHero[self.rank][self.direct][self.count]

        elif keys[self.keyDOWN]:
            self.rect.y += self.moveSpeed
            self.direct = 2
            self.image = imgHero[self.rank][self.direct][self.count]

    def draw(self):
        window.blit(self.image, self.rect)


objects = []
User = Hero(10, 1, 100, 275, 0, (pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s, pygame.K_SPACE))
animationTimer = 20 / MOVE_SPEED[User.rank]

play = True

while play:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

    keys = pygame.key.get_pressed()

    if animationTimer > 0:
        animationTimer -= 1

    else:
        animationTimer = 20 / MOVE_SPEED[User.rank]
        User.count += 1
        if User.count == 3:
            User.count = 0

    window.fill('black')
    for obj in objects:
        obj.update()
        obj.draw()

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
