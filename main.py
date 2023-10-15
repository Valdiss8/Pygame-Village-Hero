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
pygame.display.set_icon(pygame.image.load('images/sprites/hero_level_1/back_1.png'))
fontUI = pygame.font.Font(None, 30)

"""Surface"""
#surf = pygame.Surface((2000, 2000))
#surf.fill('red')
#window.blit(surf, (50, 50))
pygame.display.update()

"""Images"""
imgBangs = [
    pygame.image.load('images/bang/bang1.png'),
    pygame.image.load('images/bang/bang1.png'),
    pygame.image.load('images/bang/bang1.png')
]

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
"""Sounds"""
sound_dest = pygame.mixer.Sound('sounds/destroy.wav')
sound_shot = pygame.mixer.Sound('sounds/shot.wav')

DIRECTS = [[0, -1], [1, 0], [0, 1], [-1, 0]]

MOVE_SPEED = [1, 2, 2, 1, 2, 3, 3, 2]
BULLET_SPEED = [4, 5, 6, 5, 5, 5, 6, 7]
BULLET_DAMAGE = [1, 1, 2, 3, 2, 2, 3, 4]
BULLET_DISTANCE = [50, 60, 70, 80, 90, 100, 110, 120]
SHOT_DELAY = [60, 50, 30, 40, 30, 25, 25, 30]



class Hero:
    def __init__(self, hp, damage, px, py, direct, keyList):

        objects.append(self)
        self.type = 'hero'
        self.rank = 0

        self.rect = pygame.Rect(px, py, TILE, TILE)
        self.direct = direct
        self.hp = hp
        self.moveSpeed = 2

        self.shotTimer = 0
        self.shotDelay = 60
        self.bulletSpeed = 5
        self.bulletDamage = BULLET_DAMAGE[self.rank]
        self.bulletDistance = BULLET_DISTANCE[self.rank]

        self.keyLEFT = keyList[0]
        self.keyRIGHT = keyList[1]
        self.keyUP = keyList[2]
        self.keyDOWN = keyList[3]
        self.keySHOT = keyList[4]


        self.image = imgHero[self.rank][0][0]
        self.rect = self.image.get_rect(center=self.rect.center)

        self.count = 0

    def update(self):
        self.image = imgHero[self.rank][self.direct][0]
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

        if keys[self.keySHOT] and self.shotTimer == 0:
            dx = DIRECTS[self.direct][0] * self.bulletSpeed
            dy = DIRECTS[self.direct][1] * self.bulletSpeed
            Bullet(self, self.rect.centerx, self.rect.centery, dx, dy, self.bulletDamage, self.bulletDistance)
            self.shotTimer = self.shotDelay
            sound_shot.play()
        for obj in objects:
            if obj != self and obj.type != 'bang' and obj.type != 'bonus' and self.rect.colliderect(obj.rect):
                self.rect.topleft = oldX, oldY



        if self.shotTimer > 0: self.shotTimer -= 1

    def draw(self):
        window.blit(self.image, self.rect)


class Bullet:
    def __init__(self, parent, px, py, dx, dy, damage, distance):
        bullets.append(self)
        self.parent = parent
        self.px, self.py = px, py
        self.dx, self.dy = dx, dy
        self.damage = damage
        self.distance = distance

    def update(self):
        self.px += self.dx
        self.py += self.dy

        if self.px < 0 or self.px > WIDTH or self.py < 0 or self.py > HEIGHT:
            bullets.remove(self)
        else:
            for obj in objects:
                if obj != self.parent and obj.type !='bang' and obj.type != 'bonus' and obj.rect.collidepoint(self.px, self.py):
                    obj.damage(self.damage)
                    bullets.remove(self)
                    Bang(self.px, self.py)
                    sound_dest.play()
                    break

    def draw(self):
        pygame.draw.circle(window, 'yellow', (self.px, self.py), 2)




class Bang:
    def __init__(self, px, py):
        objects.append(self)
        self.type = 'bang'

        self.px, self.py = px, py
        self.frame = 0

    def update(self):
        self.frame += 0.3
        if self.frame >= 3: objects.remove(self)

    def draw(self):
        image = imgBangs[int(self.frame)]
        rect = image.get_rect(center=(self.px, self.py))
        window.blit(image, rect)




bullets = []
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
    for bullet in bullets:
        bullet.update()
        bullet.draw()
    for obj in objects:
        obj.update()
        obj.draw()



    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
