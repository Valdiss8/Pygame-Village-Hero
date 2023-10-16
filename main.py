import pygame
from random import randint

pygame.init()
'''Interface'''

WIDTH, HEIGHT = 1200, 780
FPS = 60
TILE = 32

window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

"""Window Name"""
pygame.display.set_caption('Village Hero')
pygame.display.set_icon(pygame.image.load('images/sprites/hero_level_1/back_1.png'))
fontUI = pygame.font.Font(None, 30)
font_dialog = pygame.font.SysFont('microsofttaile', 15)

"""Surface"""
# surf = pygame.Surface((2000, 2000))
# surf.fill('red')
# window.blit(surf, (50, 50))
pygame.display.update()

"""Images"""
back_map = [pygame.image.load('images/map/map_level_1/back_1.jpg').convert()]
img_message = pygame.image.load('images/message_2.png')

imgBangs = [
    pygame.image.load('images/bang/bang1.png'),
    pygame.image.load('images/bang/bang2.png'),
    pygame.image.load('images/bang/bang3.png')
]
imgPrincess = [[
    pygame.image.load('images/sprites/princess/front_1.png'),
    pygame.image.load('images/sprites/princess/front_2.png'),
    pygame.image.load('images/sprites/princess/front_3.png')
],
    [
        pygame.image.load('images/sprites/princess/right_1.png'),
        pygame.image.load('images/sprites/princess/right_2.png'),
        pygame.image.load('images/sprites/princess/right_3.png')
    ],
    [
        pygame.image.load('images/sprites/princess/back_1.png'),
        pygame.image.load('images/sprites/princess/back_3.png'),
        pygame.image.load('images/sprites/princess/back_6.png'),

    ],
    [
        pygame.image.load('images/sprites/princess/left_1.png'),
        pygame.image.load('images/sprites/princess/left_2.png'),
        pygame.image.load('images/sprites/princess/left_3.png'),
    ]
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
imgBrick = pygame.image.load('images/block_brick.png')

"""Sounds"""
sound_dest = pygame.mixer.Sound('sounds/destroy.wav')
sound_shot = pygame.mixer.Sound('sounds/shot.wav')
sound_shield = pygame.mixer.Sound('sounds/shield.wav')
sound_finish = pygame.mixer.Sound('sounds/dead_hero.mp3')

DIRECTS = [[0, -1], [1, 0], [0, 1], [-1, 0]]

MOVE_SPEED = [1, 2, 2, 3, 3, 4, 4, 5]
BULLET_SPEED = [4, 5, 6, 7, 8, 9, 10, 11]
BULLET_DAMAGE = [1, 1, 2, 3, 2, 2, 3, 4]
BULLET_DISTANCE = [90, 100, 110, 120, 130, 140, 150, 160]
BULLET_SIZE = [2, 3, 4, 4, 5, 5, 6, 7]
SHOT_DELAY = [60, 50, 40, 30, 25, 25, 25, 20]
SHIELD_LIMIT = [60, 100, 150, 200, 250, 300, 350, 400]
HP = [5, 6, 7, 8, 9, 10, 11, 12]
MOB_HP = [1, 2, 3, 4, 5, 6, 7, 8]


class Hero:
    """Main character"""

    def __init__(self, hp, damage, px, py, direct, keyList):

        objects.append(self)
        self.type = 'hero'
        self.rank = 0
        if self.rank >= 7:
            self.rank = 7
        self.count = 0
        self.bulletSize_count = 0
        self.rect = pygame.Rect(px, py, TILE, TILE)
        self.direct = direct
        self.hp = HP[self.rank]
        self.shield = False
        self.moveSpeed = 2
        self.animationTimer = 20 / MOVE_SPEED[self.rank]
        self.shotTimer = 0
        self.shotDelay = 60
        self.bulletSpeed = 5
        self.bulletDamage = BULLET_DAMAGE[self.rank]
        self.bulletDistance = BULLET_DISTANCE[self.rank]
        self.bulletSize = BULLET_SIZE[self.bulletSize_count]
        self.shieldTimer = 0
        self.shieldDelay = 60
        self.keyLEFT = keyList[0]
        self.keyRIGHT = keyList[1]
        self.keyUP = keyList[2]
        self.keyDOWN = keyList[3]
        self.keySHOT = keyList[4]
        self.keySHIELD = keyList[5]
        self.keySUPER = keyList[6]
        self.image = imgHero[self.rank][self.direct][0]
        self.image = pygame.transform.scale(self.image, (
            self.image.get_width() + (self.rank * 1), self.image.get_height() + (self.rank * 1)))
        self.rect = self.image.get_rect(center=self.rect.center)

    def update(self):
        self.image = imgHero[self.rank][self.direct][0]
        self.rect = self.image.get_rect(center=self.rect.center)
        self.moveSpeed = MOVE_SPEED[self.rank]
        self.shotDelay = SHOT_DELAY[self.rank]
        self.shieldDelay = SHIELD_LIMIT[self.rank]
        self.bulletSpeed = BULLET_SPEED[self.rank]
        self.bulletDamage = BULLET_DAMAGE[self.rank]
        self.bulletSize = BULLET_SIZE[self.rank]
        oldX, oldY = self.rect.topleft
        # keys and play activity
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
        # collision
        for obj in objects:
            if obj != self and obj.type != 'bang' and obj.type != 'message' and obj.type != 'bonus' and self.rect.colliderect(
                    obj.rect):
                self.rect.topleft = oldX, oldY

        # map edge
        if self.rect.left < 0 or self.rect.right > WIDTH or self.rect.top < 0 or self.rect.bottom > HEIGHT:
            print(self.rect.bottom, self.rect.top)
            self.rect.topleft = oldX, oldY

        if keys[self.keySHOT] and self.shotTimer == 0:
            dx = DIRECTS[self.direct][0] * self.bulletSpeed
            dy = DIRECTS[self.direct][1] * self.bulletSpeed
            Bullet(self, self.rect.centerx, self.rect.centery, dx, dy, self.bulletDamage, self.bulletDistance,
                   self.bulletSize)
            self.shotTimer = self.shotDelay
            sound_shot.play()

        elif keys[self.keySHIELD] and self.shotTimer == 0:
            self.shieldTimer = self.shieldDelay
            self.shotTimer = self.shotDelay + self.shieldDelay

        if self.shieldTimer > 0:
            self.image = pygame.transform.scale(self.image, (
                self.image.get_width() + (self.rank * 1) + 3, self.image.get_height() + (self.rank * 1) + 3))
            self.shield = True
            sound_shield.play()
        else:
            self.shield = False
            sound_shield.stop()

        if self.shotTimer > 0:
            self.shotTimer -= 1

        if self.shieldTimer > 0:
            self.shieldTimer -= 1

        if self.animationTimer > 0:
            self.animationTimer -= 1

        else:
            self.animationTimer = 20 / MOVE_SPEED[User.rank]
            User.count += 1
            User.bulletSize_count += 1
            if User.count == 3:
                User.count = 0
            if User.bulletSize_count == 8:
                User.bulletSize_count = 8

    def draw(self):
        window.blit(self.image, self.rect)

    def damage(self, value):
        if self.shield == False:
            self.hp -= value
            if self.hp <= 0:
                objects.remove(self)
                sound_finish.play()


class Bullet:
    def __init__(self, parent, px, py, dx, dy, damage, distance, size):
        bullets.append(self)
        self.parent = parent
        self.px, self.py = px, py
        self.dx, self.dy = dx, dy
        self.damage = damage
        self.distance = distance
        self.size = size

    def update(self):
        self.px += self.dx
        self.py += self.dy

        if abs(self.px - self.parent.rect.x) > self.parent.bulletDistance or abs(
                self.py - self.parent.rect.y) > self.parent.bulletDistance:
            bullets.remove(self)
        else:
            for obj in objects:
                if obj != self.parent and obj.type != 'bang' and obj.type != 'bonus' and obj.type != 'message' and obj.rect.collidepoint(
                        self.px,
                        self.py):
                    obj.damage(self.damage)
                    bullets.remove(self)
                    Bang(self.px, self.py)
                    sound_dest.play()
                    break

    def draw(self):
        pygame.draw.circle(window, 'yellow', (self.px, self.py), self.size)


class Bang:
    def __init__(self, px, py):
        objects.append(self)
        self.type = 'bang'

        self.px, self.py = px, py
        self.frame = 0

    def update(self):
        self.frame += 0.3
        if self.frame >= 2:
            objects.remove(self)

    def draw(self):
        image = imgBangs[int(self.frame)]
        rect = image.get_rect(center=(self.px, self.py))
        window.blit(image, rect)


class Block:
    def __init__(self, px, py, size):
        objects.append(self)
        self.type = 'block'
        self.rect = pygame.Rect(px, py, size, size)
        self.hp = 1

    def update(self):
        pass

    def draw(self):
        window.blit(imgBrick, self.rect)

    def damage(self, value):
        self.hp -= value
        if self.hp <= 0:
            objects.remove(self)


class Message:
    def __init__(self, parent, word):
        objects.append(self)
        self.type = 'message'
        self.bottom_right = parent.rect.topright
        self.timer = 0
        self.message_count = 0
        self.textlist = word
        self.text = font_dialog.render(self.textlist[self.message_count], 1, 'black')
        self.image = img_message
        self.rect = self.image.get_rect(bottomright=self.bottom_right)

    def update(self):
        self.timer += 1

        if self.timer >= 30:
            self.message_count += 1
            self.timer = 0
        if self.message_count < len(self.textlist):
            self.text = font_dialog.render(self.textlist, 1, 'black')
        else:
            objects.remove(self)

    def draw(self):
        self.rect = self.image.get_rect(bottomright=self.bottom_right)
        window.blit(self.text, (self.rect.x + 28, self.rect.y + 28))


class Princess:
    def __init__(self, px, py, direct, words):
        objects.append(self)
        self.type = 'princess'
        self.count = 0
        self.rect = pygame.Rect(px, py, TILE, TILE)
        self.direct = direct
        self.moveSpeed = 1
        self.words = words
        self.image = imgPrincess[self.direct][0]

        self.rect = self.image.get_rect(center=self.rect.center)
        self.activities = 0
        self.activity_timer = 30
        self.animationTimer = 20 / self.moveSpeed
        self.shield = True
        self.hp = 2
        self.message_time_counter = 0
        self.message_group_counter = 0

    def update(self):
        self.image = imgPrincess[self.direct][0]
        self.rect = self.image.get_rect(center=self.rect.center)

        oldX, oldY = self.rect.topleft

        # Activities
        if self.activities == 0 and self.activity_timer < 101:
            self.rect.x -= self.moveSpeed
            self.direct = 3
            self.image = imgPrincess[self.direct][self.count]

        if self.activities == 1 and self.activity_timer < 100:
            self.image = imgPrincess[self.direct][0]

        if self.activities == 2 and self.activity_timer < 100:
            self.rect.y += self.moveSpeed
            self.direct = 2
            self.image = imgPrincess[self.direct][self.count]

        if self.activities == 3 and self.activity_timer < 100:
            self.rect.x += self.moveSpeed
            self.direct = 1
            self.image = imgPrincess[self.direct][self.count]

        if self.activities == 4 and self.activity_timer < 100:
            self.image = imgPrincess[self.direct][0]

        if self.activities == 5 and self.activity_timer < 100:
            self.rect.y -= self.moveSpeed
            self.direct = 0
            self.image = imgPrincess[self.direct][self.count]
        if self.activities == 6 and self.activity_timer < 100:
            self.image = imgPrincess[self.direct][self.count]

        # Collision
        for obj in objects:
            if obj != self and obj.type != 'bang' and obj.type != 'message' and obj.type != 'bonus' and self.rect.colliderect(
                    obj.rect):
                self.rect.topleft = oldX, oldY
        # map edge
        if self.rect.left < 0 or self.rect.right > WIDTH or self.rect.top < 0 or self.rect.bottom > HEIGHT:
            print(self.rect.bottom, self.rect.top)
            self.rect.topleft = oldX, oldY
        # Timers
        if self.activity_timer > 0:
            self.activity_timer -= 1
        else:
            self.activity_timer = 30
            self.activities += 1
            if self.activities == 7:
                self.activities = 0
                self.message_time_counter += 1
                Message(self, self.words[self.message_group_counter][self.message_time_counter])
            if self.message_time_counter >= len(self.words[self.message_group_counter]) - 1:
                self.message_time_counter = 0


        if self.animationTimer > 0:
            self.animationTimer -= 1
        else:
            self.animationTimer = 20 / MOVE_SPEED[0] / 2
            self.count += 1

            if self.count == 3:
                self.count = 0

    def draw(self):
        window.blit(self.image, self.rect)

    def damage(self, value):
        if self.shield == False:
            self.hp -= value
            if self.hp <= 0:
                objects.remove(self)
                sound_finish.play()

class Mob(Princess):
    def __init__(self, px, py, direct, words, rank):
        super().__init__(px, py, direct, words)
        self.rank = 0
        objects.append(self)
        self.type = 'mob'
        self.rect = pygame.Rect(px, py, TILE, TILE)
        self.moveSpeed = MOVE_SPEED[self.rank] / 2
        self.image = imgPrincess[self.direct][0]
        self.rect = self.image.get_rect(center=self.rect.center)
        self.activities = 0
        self.activity_timer = 50
        self.animationTimer = 20 / self.moveSpeed
        self.shield = False
        self.hp = MOB_HP[self.rank]
        self.message_time_counter = 0
        self.message_group_counter = 0









bullets = []
objects = []
User = Hero(10, 1, 100, 275, 0,
            (pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s, pygame.K_LEFT, pygame.K_DOWN, pygame.K_RIGHT))
animationTimer = 40 / MOVE_SPEED[User.rank]
Princess = Princess(200, 500, 0, [['', 'Good day', 'Sun', 'Flowers'], ['', 'O,no!', 'Help', 'Please!', 'Help!!!']])
Mob(500, 500, 0, [['', 'Good day', 'Sun', 'Flowers'], ['', 'O,no!', 'Help', 'Please!', 'Help!!!']], 0)

#for _ in range(150):
#    while True:
#        x = randint(0, WIDTH // TILE - 1) * TILE
#        y = randint(1, HEIGHT // TILE - 1) * TILE
#        rect = pygame.Rect(x, y, TILE, TILE)
#        fined = False
#        for obj in objects:
#            if rect.colliderect(obj.rect):
#                fined = True
#
#        if not fined:
#            break
#    Block(x, y, TILE)

play = True

while play:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

    window.blit(back_map[0], (0, 0))
    keys = pygame.key.get_pressed()

    for bullet in bullets:
        bullet.update()
        bullet.draw()
    for obj in objects:
        obj.update()
        obj.draw()

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
