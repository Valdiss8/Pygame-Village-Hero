import json
import pickle
import sys

import mixer as mixer
import pygame
from random import randint

from pygame.mixer import music

pygame.init()
'''Interface'''

WIDTH, HEIGHT = 1200, 780
FPS = 60
TILE = 40

window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

"""Window Name"""
pygame.display.set_caption('Village Hero')
pygame.display.set_icon(pygame.image.load('images/sprites/hero_level_1/back_1.png'))
fontUI = pygame.font.Font(None, 30)
font_dialog = pygame.font.Font(None, 20)
font_UI = pygame.font.Font(None, 30)
font_MOB_life = pygame.font.Font(None, 19)
font_MENU = pygame.font.Font(None, 60)

"""Surface"""
# surf = pygame.Surface((2000, 2000))
# surf.fill('red')
# window.blit(surf, (50, 50))
pygame.display.update()

"""Images"""

back_map = [pygame.image.load('images/map/menu/back_1.png').convert(),
            pygame.image.load('images/map/map_level_1/back_1.jpg').convert(),
            pygame.image.load('images/map/map_level_2/back_1.jpg').convert(),
            pygame.image.load('images/map/map_level_boss/back_1.jpg').convert(),
            pygame.image.load('images/map/map_level_boss/back_1.jpg').convert()
            ]
img_message = pygame.image.load('images/message_2.png')

imgBangs = [
    pygame.image.load('images/bang/bang1.png'),
    pygame.image.load('images/bang/bang2.png'),
    pygame.image.load('images/bang/bang3.png')
]
imgPrincess = [[[
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
],
    [[
        pygame.image.load('images/sprites/mob/level_1/front_1.png'),
        pygame.image.load('images/sprites/mob/level_1/front_2.png'),
        pygame.image.load('images/sprites/mob/level_1/front_3.png')
    ],
        [
            pygame.image.load('images/sprites/mob/level_1/right_1.png'),
            pygame.image.load('images/sprites/mob/level_1/right_2.png'),
            pygame.image.load('images/sprites/mob/level_1/right_3.png')
        ],
        [
            pygame.image.load('images/sprites/mob/level_1/back_1.png'),
            pygame.image.load('images/sprites/mob/level_1/back_2.png'),
            pygame.image.load('images/sprites/mob/level_1/back_3.png'),

        ],
        [
            pygame.image.load('images/sprites/mob/level_1/left_1.png'),
            pygame.image.load('images/sprites/mob/level_1/left_2.png'),
            pygame.image.load('images/sprites/mob/level_1/left_3.png'),
        ]
    ],
    [[
        pygame.image.load('images/sprites/mob/level_2/front_1.png'),
        pygame.image.load('images/sprites/mob/level_2/front_2.png'),
        pygame.image.load('images/sprites/mob/level_2/front_3.png')
    ],
        [
            pygame.image.load('images/sprites/mob/level_2/right_1.png'),
            pygame.image.load('images/sprites/mob/level_2/right_2.png'),
            pygame.image.load('images/sprites/mob/level_2/right_3.png')
        ],
        [
            pygame.image.load('images/sprites/mob/level_2/back_1.png'),
            pygame.image.load('images/sprites/mob/level_2/back_2.png'),
            pygame.image.load('images/sprites/mob/level_2/back_3.png'),

        ],
        [
            pygame.image.load('images/sprites/mob/level_2/left_1.png'),
            pygame.image.load('images/sprites/mob/level_2/left_2.png'),
            pygame.image.load('images/sprites/mob/level_2/left_3.png'),
        ]
    ],
    [[
        pygame.image.load('images/sprites/mob/level_3/front_1.png'),
        pygame.image.load('images/sprites/mob/level_3/front_2.png'),
        pygame.image.load('images/sprites/mob/level_3/front_3.png')
    ],
        [
            pygame.image.load('images/sprites/mob/level_3/right_1.png'),
            pygame.image.load('images/sprites/mob/level_3/right_2.png'),
            pygame.image.load('images/sprites/mob/level_3/right_3.png')
        ],
        [
            pygame.image.load('images/sprites/mob/level_3/back_1.png'),
            pygame.image.load('images/sprites/mob/level_3/back_2.png'),
            pygame.image.load('images/sprites/mob/level_3/back_3.png'),

        ],
        [
            pygame.image.load('images/sprites/mob/level_3/left_1.png'),
            pygame.image.load('images/sprites/mob/level_3/left_2.png'),
            pygame.image.load('images/sprites/mob/level_3/left_3.png'),
        ]
    ],
    [[
        pygame.image.load('images/sprites/mob/level_4/front_1.png'),
        pygame.image.load('images/sprites/mob/level_4/front_2.png'),
        pygame.image.load('images/sprites/mob/level_4/front_3.png')
    ],
        [
            pygame.image.load('images/sprites/mob/level_4/right_1.png'),
            pygame.image.load('images/sprites/mob/level_4/right_2.png'),
            pygame.image.load('images/sprites/mob/level_4/right_3.png')
        ],
        [
            pygame.image.load('images/sprites/mob/level_4/back_1.png'),
            pygame.image.load('images/sprites/mob/level_4/back_2.png'),
            pygame.image.load('images/sprites/mob/level_4/back_3.png'),

        ],
        [
            pygame.image.load('images/sprites/mob/level_4/left_1.png'),
            pygame.image.load('images/sprites/mob/level_4/left_2.png'),
            pygame.image.load('images/sprites/mob/level_4/left_3.png'),
        ]
    ],
    [[
        pygame.image.load('images/sprites/mob/level_5/front_1.png'),
        pygame.image.load('images/sprites/mob/level_5/front_2.png'),
        pygame.image.load('images/sprites/mob/level_5/front_3.png')
    ],
        [
            pygame.image.load('images/sprites/mob/level_5/right_1.png'),
            pygame.image.load('images/sprites/mob/level_5/right_2.png'),
            pygame.image.load('images/sprites/mob/level_5/right_3.png')
        ],
        [
            pygame.image.load('images/sprites/mob/level_5/back_1.png'),
            pygame.image.load('images/sprites/mob/level_5/back_2.png'),
            pygame.image.load('images/sprites/mob/level_5/back_3.png'),

        ],
        [
            pygame.image.load('images/sprites/mob/level_5/left_1.png'),
            pygame.image.load('images/sprites/mob/level_5/left_2.png'),
            pygame.image.load('images/sprites/mob/level_5/left_3.png'),
        ]
    ],
    [[
        pygame.image.load('images/sprites/mob/level_5/front_1.png'),
        pygame.image.load('images/sprites/mob/level_5/front_2.png'),
        pygame.image.load('images/sprites/mob/level_5/front_3.png')
    ],
        [
            pygame.image.load('images/sprites/mob/level_5/right_1.png'),
            pygame.image.load('images/sprites/mob/level_5/right_2.png'),
            pygame.image.load('images/sprites/mob/level_5/right_3.png')
        ],
        [
            pygame.image.load('images/sprites/mob/level_5/back_1.png'),
            pygame.image.load('images/sprites/mob/level_5/back_2.png'),
            pygame.image.load('images/sprites/mob/level_5/back_3.png'),

        ],
        [
            pygame.image.load('images/sprites/mob/level_5/left_1.png'),
            pygame.image.load('images/sprites/mob/level_5/left_2.png'),
            pygame.image.load('images/sprites/mob/level_5/left_3.png'),
        ]
    ],
    [[
        pygame.image.load('images/sprites/mob/boss/front_1.png'),
        pygame.image.load('images/sprites/mob/boss/front_2.png'),
        pygame.image.load('images/sprites/mob/boss/front_3.png')
    ],
        [
            pygame.image.load('images/sprites/mob/boss/right_1.png'),
            pygame.image.load('images/sprites/mob/boss/right_2.png'),
            pygame.image.load('images/sprites/mob/boss/right_3.png')
        ],
        [
            pygame.image.load('images/sprites/mob/boss/back_1.png'),
            pygame.image.load('images/sprites/mob/boss/back_2.png'),
            pygame.image.load('images/sprites/mob/boss/back_3.png'),

        ],
        [
            pygame.image.load('images/sprites/mob/boss/left_1.png'),
            pygame.image.load('images/sprites/mob/boss/left_2.png'),
            pygame.image.load('images/sprites/mob/boss/left_3.png'),
        ]
    ],
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
    ]],
    [[
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
    ],
    [[
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
    ],
    [[
        pygame.image.load('images/sprites/hero_level_4/forward_1.png'),
        pygame.image.load('images/sprites/hero_level_4/forward_2.png'),
        pygame.image.load('images/sprites/hero_level_4/forward_3.png')
    ],
        [
            pygame.image.load('images/sprites/hero_level_4/right_1.png'),
            pygame.image.load('images/sprites/hero_level_4/right_2.png'),
            pygame.image.load('images/sprites/hero_level_4/right_3.png')
        ],
        [
            pygame.image.load('images/sprites/hero_level_4/back_1.png'),
            pygame.image.load('images/sprites/hero_level_4/back_2.png'),
            pygame.image.load('images/sprites/hero_level_4/back_3.png'),
        ],
        [
            pygame.image.load('images/sprites/hero_level_4/left_1.png'),
            pygame.image.load('images/sprites/hero_level_4/left_2.png'),
            pygame.image.load('images/sprites/hero_level_4/left_3.png'),
        ]
    ],
    [[
        pygame.image.load('images/sprites/hero_level_4/forward_1.png'),
        pygame.image.load('images/sprites/hero_level_4/forward_2.png'),
        pygame.image.load('images/sprites/hero_level_4/forward_3.png')
    ],
        [
            pygame.image.load('images/sprites/hero_level_4/right_1.png'),
            pygame.image.load('images/sprites/hero_level_4/right_2.png'),
            pygame.image.load('images/sprites/hero_level_4/right_3.png')
        ],
        [
            pygame.image.load('images/sprites/hero_level_4/back_1.png'),
            pygame.image.load('images/sprites/hero_level_4/back_2.png'),
            pygame.image.load('images/sprites/hero_level_4/back_3.png'),
        ],
        [
            pygame.image.load('images/sprites/hero_level_4/left_1.png'),
            pygame.image.load('images/sprites/hero_level_4/left_2.png'),
            pygame.image.load('images/sprites/hero_level_4/left_3.png'),
        ]
    ],
    [[
        pygame.image.load('images/sprites/hero_level_6/forward_1.png'),
        pygame.image.load('images/sprites/hero_level_6/forward_2.png'),
        pygame.image.load('images/sprites/hero_level_6/forward_3.png')
    ],
        [
            pygame.image.load('images/sprites/hero_level_6/right_1.png'),
            pygame.image.load('images/sprites/hero_level_6/right_2.png'),
            pygame.image.load('images/sprites/hero_level_6/right_3.png')
        ],
        [
            pygame.image.load('images/sprites/hero_level_6/back_1.png'),
            pygame.image.load('images/sprites/hero_level_6/back_2.png'),
            pygame.image.load('images/sprites/hero_level_6/back_3.png'),
        ],
        [
            pygame.image.load('images/sprites/hero_level_6/left_1.png'),
            pygame.image.load('images/sprites/hero_level_6/left_2.png'),
            pygame.image.load('images/sprites/hero_level_6/left_3.png'),
        ]
    ],
    [[
        pygame.image.load('images/sprites/hero_level_6/forward_1.png'),
        pygame.image.load('images/sprites/hero_level_6/forward_2.png'),
        pygame.image.load('images/sprites/hero_level_6/forward_3.png')
    ],
        [
            pygame.image.load('images/sprites/hero_level_6/right_1.png'),
            pygame.image.load('images/sprites/hero_level_6/right_2.png'),
            pygame.image.load('images/sprites/hero_level_6/right_3.png')
        ],
        [
            pygame.image.load('images/sprites/hero_level_6/back_1.png'),
            pygame.image.load('images/sprites/hero_level_6/back_2.png'),
            pygame.image.load('images/sprites/hero_level_6/back_3.png'),
        ],
        [
            pygame.image.load('images/sprites/hero_level_6/left_1.png'),
            pygame.image.load('images/sprites/hero_level_6/left_2.png'),
            pygame.image.load('images/sprites/hero_level_6/left_3.png'),
        ]
    ],
    [[
        pygame.image.load('images/sprites/hero_level_6/forward_1.png'),
        pygame.image.load('images/sprites/hero_level_6/forward_2.png'),
        pygame.image.load('images/sprites/hero_level_6/forward_3.png')
    ],
        [
            pygame.image.load('images/sprites/hero_level_6/right_1.png'),
            pygame.image.load('images/sprites/hero_level_6/right_2.png'),
            pygame.image.load('images/sprites/hero_level_6/right_3.png')
        ],
        [
            pygame.image.load('images/sprites/hero_level_6/back_1.png'),
            pygame.image.load('images/sprites/hero_level_6/back_2.png'),
            pygame.image.load('images/sprites/hero_level_6/back_3.png'),
        ],
        [
            pygame.image.load('images/sprites/hero_level_6/left_1.png'),
            pygame.image.load('images/sprites/hero_level_6/left_2.png'),
            pygame.image.load('images/sprites/hero_level_6/left_3.png'),
        ]
    ],

]
imgExit = pygame.image.load('images/map/exit.png')
imgBrick = pygame.image.load('images/map/tile.jpg')

imgBonuses = [pygame.image.load('images/bonus/magic_scroll.png'),
              pygame.image.load('images/bonus/healing.png')]

"""Sounds"""


sound_dest = pygame.mixer.Sound('sounds/destroy.wav')
sound_shot = pygame.mixer.Sound('sounds/shot.mp3')
sound_heavy_attack = pygame.mixer.Sound('sounds/heavy_attack.mp3')

sound_super_attack = pygame.mixer.Sound('sounds/super_ball.mp3')
sound_shield = pygame.mixer.Sound('sounds/shield.wav')
sound_finish = pygame.mixer.Sound('sounds/dead_hero.mp3')
sound_mob_death = pygame.mixer.Sound('sounds/mob_death.mp3')
sound_mob_shot = pygame.mixer.Sound('sounds/mob_shot_1.mp3')
sound_danger = pygame.mixer.Sound('sounds/danger.mp3')
sound_pickup_magic_scroll = pygame.mixer.Sound('sounds/pick_up_scroll.mp3')
sound_pickup_healing = pygame.mixer.Sound('sounds/pick_up_healing.mp3')
sound_level_up = pygame.mixer.Sound('sounds/level_up2.mp3')
sound_map_level_1_happy = pygame.mixer.Sound('sounds/map_level1_happy.mp3')
sound_map_level_upset = pygame.mixer.Sound('sounds/map_level_upset.mp3')
sound_map_next = pygame.mixer.Sound('sounds/map_next_level.mp3')
#sound_menu = pygame.mixer.Sound('sounds/menu_sound.mp3')
sound_menu_click = pygame.mixer.Sound('sounds/menu_switch.mp3')
sound_menu_select = pygame.mixer.Sound('sounds/menu_select.mp3')


MOVE_SPEED_MENU = [1, 1, 2, 2, 3, 3, 4, 4]
BULLET_DAMAGE_MENU = [1, 1, 2, 2, 2, 3, 3, 3]
HP_MENU = [5, 6, 7, 8, 9, 10, 11, 15]
CONSTANT_MOVE_SPEED = [1, 1, 2, 2, 3, 3, 4, 4]
CONSTANT_BULLET_DAMAGE = [1, 1, 2, 2, 2, 3, 3, 3]
CONSTANT_HP = [5, 6, 7, 8, 9, 10, 11, 15]

DIRECTS = [[0, -1], [1, 0], [0, 1], [-1, 0]]
EXPERIENCE = [7, 14, 30, 50, 80, 100, 150, 200]
MOVE_SPEED = [1, 1, 2, 2, 3, 3, 4, 4]
BULLET_SPEED = [4, 5, 6, 7, 8, 9, 10, 11]
BULLET_DAMAGE = [1, 1, 2, 2, 2, 3, 3, 3]
BULLET_DISTANCE = [90, 100, 110, 120, 130, 140, 150, 160]
BULLET_SIZE = [2, 3, 4, 4, 5, 5, 6, 7]
SHOT_DELAY = [60, 50, 40, 30, 25, 25, 25, 20]
SHIELD_LIMIT = [60, 60, 60, 70, 70, 70, 80, 80]

HP = [5, 6, 7, 8, 9, 10, 11, 15]
MOB_HP = [2, 4, 7, 10, 15, 25, 35, 100]
MOB_BULLET_DISTANCE = [60, 70, 80, 90, 100, 110, 120, 150]
MOB_BULLET_DAMAGE = [1, 1, 1, 2, 1, 2, 1, 3]
MOB_SHOT_DELAY = [30, 30, 30, 30, 20, 20, 20, 20]
MOB_BULLET_SIZE = [1, 1, 1, 2, 2, 3, 3, 4]
SCROLLS_LIMIT = [10, 10, 11, 11, 12, 13, 13, 14]


class UI:
    def __init__(self):
        pass

    def update(self):
        pass

    def draw(self):
        for obj in objects[scene_play]:
            # Hero life and scrolls
            if obj.type == 'hero':
                # life
                window.blit(imgBonuses[1], (5, 5, 32, 32))
                text_hp = fontUI.render(str(obj.hp), 0, 'red')
                rect_hp = text_hp.get_rect(center=(37, 16))
                window.blit(text_hp, rect_hp)
                # scrolls
                window.blit(imgBonuses[0], (50, 5, 32, 32))
                text_scrolls = fontUI.render(str(obj.scrolls), 0, 'blue')
                rect_scrolls = text_scrolls.get_rect(center=(92, 16))
                window.blit(text_scrolls, rect_scrolls)
                # level
                text_lvl = fontUI.render(str(obj.rank), 0, 'blue')
                text_level = fontUI.render('LEVEL', 0, 'red')
                rect_lvl = text_scrolls.get_rect(center=(190, 14))
                window.blit(text_level, (110, 5, 32, 32))
                window.blit(text_lvl, rect_lvl)

            # Mob life
            if obj.type == 'mob':
                text_hp = font_MOB_life.render(str(obj.hp), 0, 'red')
                rect = text_hp.get_rect(center=(obj.rect.center[0], obj.rect.center[1] - obj.rect.height // 2))
                window.blit(text_hp, rect)


class Hero:
    """Main character"""

    def __init__(self, px, py, direct, keyList):

        # objects[scene_play].append(self)

        self.type = 'hero'
        self.rank = 0
        self.count = 0
        self.bulletSize_count = 0
        self.rect = pygame.Rect(px, py, TILE, TILE)
        self.direct = direct
        self.hp = HP[self.rank]
        self.scrolls = 0
        self.xp = 0
        self.shield = False
        self.moveSpeed = MOVE_SPEED[self.rank]
        self.animationTimer = 20 / MOVE_SPEED[self.rank]
        self.shotTimer = 0
        self.shotDelay = SHOT_DELAY[self.rank]
        self.bulletSpeed = BULLET_SPEED[self.rank]
        self.bulletDamage = BULLET_DAMAGE[self.rank]
        self.bulletDistance = BULLET_DISTANCE[self.rank]
        self.bulletSize = BULLET_SIZE[self.bulletSize_count]
        self.shieldTimer = 0
        self.shieldDelay = SHIELD_LIMIT[self.rank]
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
        self.image = pygame.transform.scale(self.image, (self.image.get_width() - 5, self.image.get_height() - 5))

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
        for obj in objects[scene_play]:
            if obj != self and obj.type != 'bang' and obj.type != 'message' and obj.type != 'bonus' and self.rect.colliderect(
                    obj.rect):
                self.rect.topleft = oldX, oldY

        # map edge
        if self.rect.left < 0 or self.rect.right > WIDTH or self.rect.top < 0 or self.rect.bottom > HEIGHT:
            self.rect.topleft = oldX, oldY

        # Regular attack
        if keys[self.keySHOT] and self.shotTimer == 0:
            dx = DIRECTS[self.direct][0] * self.bulletSpeed
            dy = DIRECTS[self.direct][1] * self.bulletSpeed
            Bullet(self, self.rect.centerx, self.rect.centery, dx, dy, self.bulletDamage, self.bulletDistance,
                   self.bulletSize, 'blue')
            self.shotTimer = self.shotDelay
            sound_shot.play()

        # Heavy attack
        if keys[self.keySHIELD] and keys[self.keySHOT] and self.shieldDelay - 5 > self.shotTimer > self.shotDelay - 10:
            dx = DIRECTS[self.direct][0] * self.bulletSpeed
            dy = DIRECTS[self.direct][1] * self.bulletSpeed
            Bullet(self, self.rect.centerx, self.rect.centery, dx, dy, self.bulletDamage * 2, self.bulletDistance,
                   self.bulletSize * 3, 'yellow')
            self.shotTimer = self.shotDelay * 3
            sound_heavy_attack.play()

        if keys[self.keySHIELD] and self.shotTimer == 0:
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

        # Super ball
        if keys[self.keySUPER] and self.shotTimer == 0 and self.scrolls:
            dx = DIRECTS[self.direct][0] * self.bulletSpeed
            dy = DIRECTS[self.direct][1] * self.bulletSpeed
            Bullet(self, self.rect.centerx, self.rect.centery, dx, dy, self.bulletDamage * 3, self.bulletDistance * 3,
                   self.bulletSize * 3, 'red')
            self.shotTimer = self.shotDelay
            sound_super_attack.play()
            self.scrolls -= 1

        # Timers

        if self.shotTimer > 0:
            self.shotTimer -= 1

        if self.shieldTimer > 0:
            self.shieldTimer -= 1

        if self.animationTimer > 0:
            self.animationTimer -= 1

        else:
            self.animationTimer = 20 / MOVE_SPEED[User.rank]
            self.count += 1
            if User.count == 3:
                User.count = 0

    def draw(self):
        window.blit(self.image, self.rect)

    def damage(self, value):
        if self.shield == False:
            self.hp -= value
            if self.hp <= 0:
                sound_finish.play()
                switch_scene(menu(objects))
                objects[scene_play].remove(self)




class Bullet:
    def __init__(self, parent, px, py, dx, dy, damage, distance, size, collor='black'):
        bullets[scene_play].append(self)
        self.parent = parent
        self.px, self.py = px, py
        self.dx, self.dy = dx, dy
        self.damage = damage
        self.distance = distance
        self.size = size
        self.color = collor

    def update(self):
        self.px += self.dx
        self.py += self.dy

        if abs(self.px - self.parent.rect.x) > self.distance or abs(
                self.py - self.parent.rect.y) > self.distance:
            bullets[scene_play].remove(self)
        else:
            for obj in objects[scene_play]:
                if obj != self.parent and obj.type != self.parent.type and obj.type != 'princess' and obj.type != 'bang' and obj.type != 'bonus' and obj.type != 'message' and obj.rect.collidepoint(
                        self.px,
                        self.py):
                    obj.damage(self.damage)
                    bullets[scene_play].remove(self)
                    Bang(self.px, self.py)
                    sound_dest.play()
                    break

    def draw(self):
        pygame.draw.circle(window, self.color, (self.px, self.py), self.size)


class Bang:
    def __init__(self, px, py):
        objects[scene_play].append(self)
        self.type = 'bang'
        self.px, self.py = px, py
        self.frame = 0

    def update(self):
        self.frame += 0.3
        if self.frame >= 2:
            objects[scene_play].remove(self)

    def draw(self):
        image = imgBangs[int(self.frame)]
        rect = image.get_rect(center=(self.px, self.py))
        window.blit(image, rect)


class Bonus:
    def __init__(self, parent, bonusNum):
        objects[scene_play].append(self)
        self.type = 'bonus'
        self.bonusNum = bonusNum
        self.image = imgBonuses[self.bonusNum]
        self.rect = self.image.get_rect(center=parent.rect.center)
        self.timer = 600

    def update(self):
        if self.timer > 0:
            self.timer -= 1
        else:
            objects[scene_play].remove(self)
        for obj in objects[scene_play]:
            if obj.type == 'hero' and self.rect.colliderect(obj.rect):
                if self.bonusNum == 0:
                    if obj.scrolls < SCROLLS_LIMIT[obj.rank]:
                        obj.scrolls += 1
                    objects[scene_play].remove(self)
                    sound_pickup_magic_scroll.play()
                    break
                elif self.bonusNum == 1:
                    if obj.hp < HP[obj.rank]:
                        obj.hp += 1
                    objects[scene_play].remove(self)
                    sound_pickup_healing.play()
                    break

    def draw(self):
        if self.timer % 30 < 15:
            window.blit(self.image, self.rect)


class Block:
    def __init__(self, px, py, size):
        # objects.append(self)
        self.type = 'block'
        self.rect = pygame.Rect(px, py, size, size)
        self.hp = 35

    def update(self):
        pass

    def draw(self):
        window.blit(imgBrick, self.rect)

    def damage(self, value):
        self.hp -= value
        if self.hp <= 0:
            objects[scene_play].remove(self)


class Message:
    def __init__(self, parent, word, color='black'):
        objects[scene_play].append(self)
        self.type = 'message'
        self.bottom_right = parent.rect.topright
        self.timer = 0
        self.message_count = 0
        self.textlist = word
        self.color = color
        self.text = font_dialog.render(self.textlist[self.message_count], 1, self.color)
        self.image = img_message
        self.rect = self.image.get_rect(bottomright=self.bottom_right)

    def update(self):
        self.timer += 1

        if self.timer >= 30:
            self.message_count += 1
            self.timer = 0
        if self.message_count < len(self.textlist):
            self.text = font_dialog.render(self.textlist, 1, self.color)
        else:
            objects[scene_play].remove(self)

    def draw(self):
        self.rect = self.image.get_rect(bottomright=self.bottom_right)
        window.blit(self.text, (self.rect.x + 28, self.rect.y + 28))


class Princess:
    def __init__(self, px, py, direct, words, rank):
        # objects[scene_play].append(self)
        self.type = 'princess'
        self.count = 0
        self.rank = rank
        self.rect = pygame.Rect(px, py, TILE, TILE)
        self.direct = direct
        self.moveSpeed = 1
        self.words = words
        self.bonus_probability = randint(0, 2)
        self.image = imgPrincess[self.rank][self.direct][0]
        self.rect = self.image.get_rect(center=self.rect.center)
        self.activities = 0
        self.activity_timer = 30
        self.animationTimer = 20 / self.moveSpeed
        self.shield = True
        self.hp = 2
        self.message_time_counter = 0
        self.message_group_counter = 0
        self.activity_speed = 4 - self.rank // 2

    def update(self):
        self.image = pygame.transform.scale(self.image, (self.image.get_width() - 5, self.image.get_height() - 5))
        self.image = imgPrincess[self.rank][self.direct][0]
        self.rect = self.image.get_rect(center=self.rect.center)
        oldX, oldY = self.rect.topleft

        # Activities
        if self.activities == 0 and self.activity_timer < 100:
            if self.activity_timer % self.activity_speed == 0:
                self.rect.x -= self.moveSpeed
            self.direct = 3
            self.image = imgPrincess[self.rank][self.direct][self.count]

        if self.activities == 1 and self.activity_timer < 100:
            self.image = imgPrincess[self.rank][self.direct][0]

        if self.activities == 2 and self.activity_timer < 100:
            if self.activity_timer % self.activity_speed == 0:
                self.rect.y += self.moveSpeed
            self.direct = 2
            self.image = imgPrincess[self.rank][self.direct][self.count]

        if self.activities == 3 and self.activity_timer < 100:
            if self.activity_timer % self.activity_speed == 0:
                self.rect.x += self.moveSpeed
            self.direct = 1
            self.image = imgPrincess[self.rank][self.direct][self.count]

        if self.activities == 4 and self.activity_timer < 100:
            self.image = imgPrincess[self.rank][self.direct][0]

        if self.activities == 5 and self.activity_timer < 100:
            if self.activity_timer % self.activity_speed == 0:
                self.rect.y -= self.moveSpeed
            self.direct = 0
            self.image = imgPrincess[self.rank][self.direct][self.count]
        if self.activities == 6 and self.activity_timer < 100:
            self.image = imgPrincess[self.rank][self.direct][self.count]

        # Collision
        for obj in objects[scene_play]:
            if obj != self and obj.type != 'bang' and obj.type != 'message' and obj.type != 'bonus' and self.rect.colliderect(
                    obj.rect):
                self.rect.topleft = oldX, oldY
        # map edge
        if self.rect.left < 0 or self.rect.right > WIDTH or self.rect.top < 0 or self.rect.bottom > HEIGHT:
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

            if self.message_time_counter == len(self.words[self.message_group_counter]) - 1:
                self.message_group_counter += 1
                self.message_time_counter = 0
                if self.message_group_counter == 2:
                    sound_danger.play()
                    objects[1].append(
                        Mob(self.rect.center[0] + 30, self.rect.center[1], 0, [['', 'SHE', 'BELONGS', 'TO US', ]], 2))
                    objects[1].append(
                        Mob(self.rect.center[0] - 30, self.rect.center[1], 0, [['', 'OUR BOSS', 'GRR', 'THE BEST', ]],
                            2))
                if self.message_group_counter == len(self.words):
                    objects[scene_play].remove(self)
                    for i in range(6):
                        sound_map_level_upset.play()
                    Message(self, 'Help me!', 'red')
                    Message(User, 'I need to help', 'red')

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
                objects[scene_play].remove(self)
                if self.bonus_probability < 2:
                    Bonus(self, self.bonus_probability)
                if User.rank < len(EXPERIENCE) - 1:
                    User.xp += self.rank
                    print(EXPERIENCE[User.rank])
                    if User.xp >= EXPERIENCE[User.rank]:
                        print(EXPERIENCE[User.rank])
                        User.rank += 1
                        sound_level_up.play()
                sound_mob_death.play()


class Mob(Princess):
    def __init__(self, px, py, direct, words, rank):
        super().__init__(px, py, direct, words, rank)
        self.rank = rank
        self.type = 'mob'
        self.rect = pygame.Rect(px, py, 17, 42)
        self.moveSpeed = 1
        self.shield = False
        self.hp = MOB_HP[self.rank]
        self.bulletSpeed = 2
        self.bulletSize = MOB_BULLET_SIZE[self.rank]
        self.bulletDistance = MOB_BULLET_DISTANCE[self.rank]
        self.shotDelay = MOB_SHOT_DELAY[self.rank]
        self.bulletDamage = MOB_BULLET_DAMAGE[self.rank]
        self.shotTimer = 0

    def update(self):
        # Making sure that mobs message not end, and they will not disappear
        self.message_group_counter = -1
        super().update()

        if abs(abs(User.rect.center[0]) - abs(self.rect.center[0])) < self.bulletDistance and abs(
                abs(User.rect.center[1]) - abs(self.rect.center[1])) < self.bulletDistance and self.shotTimer == 0:
            dx = DIRECTS[self.direct][0] * self.bulletSpeed
            dy = DIRECTS[self.direct][1] * self.bulletSpeed

            if self.activity_timer % self.shotDelay == 0:
                Bullet(self, self.rect.centerx, self.rect.centery, dx, dy, self.bulletDamage, self.bulletDistance,
                       self.bulletSize)
                sound_mob_shot.play()


class Boss(Mob):
    def update(self):
        super().update()
        if abs(abs(User.rect.center[0]) - abs(self.rect.center[0])) < self.bulletDistance and abs(
                abs(User.rect.center[1]) - abs(self.rect.center[1])) < self.bulletDistance and self.shotTimer == 0:
            dx = DIRECTS[self.direct][0] * self.bulletSpeed
            dy = DIRECTS[self.direct][1] * self.bulletSpeed

            if self.activity_timer % self.shotDelay == 0:
                Bullet(self, self.rect.centerx, self.rect.centery, dx, dy, self.bulletDamage, self.bulletDistance,
                       self.bulletSize)
                Bullet(self, self.rect.centerx, self.rect.centery, -1, -1, self.bulletDamage, self.bulletDistance,
                       self.bulletSize)
                Bullet(self, self.rect.centerx, self.rect.centery, -1, 0, self.bulletDamage, self.bulletDistance,
                       self.bulletSize)
                Bullet(self, self.rect.centerx, self.rect.centery, -1, 1, self.bulletDamage, self.bulletDistance,
                       self.bulletSize)
                Bullet(self, self.rect.centerx, self.rect.centery, 0, -1, self.bulletDamage, self.bulletDistance,
                       self.bulletSize)
                Bullet(self, self.rect.centerx, self.rect.centery, 0, 1, self.bulletDamage, self.bulletDistance,
                       self.bulletSize)
                sound_mob_shot.play()
    def damage(self, value):
        if self.shield == False:
            self.hp -= value
            if self.hp <= 0:
                objects[scene_play].remove(self)
                if self.bonus_probability < 2:
                    Bonus(self, self.bonus_probability)
                if User.rank < len(EXPERIENCE) - 1:
                    User.xp += self.rank
                    if User.xp >= EXPERIENCE[User.rank]:
                        User.rank += 1

                sound_map_level_1_happy.play()


# Menu
class Menu:
    def __init__(self):  # option_surfaces, callbacks,
        self.option_surfaces = [[], [], [], []]
        self.callbacks = [[], [], [], []]
        self.current_group = 0
        self.current_option_index = 0

    def append_option(self, option, callback, group):
        self.option_surfaces[group].append(font_MENU.render(option, 0, 'red'))
        self.callbacks[group].append(callback)

    def switch(self, vertical_direction, horisontal_direction):
        sound_menu_click.play()
        self.current_group = max(0, min(self.current_group + vertical_direction, len(self.option_surfaces) - 1))
        self.current_option_index = max(0, min(self.current_option_index + horisontal_direction,
                                               len(self.option_surfaces[self.current_group]) - 1))

    def select(self):
        sound_menu_select.play()
        return self.callbacks[self.current_group][self.current_option_index]()

    def draw(self, surface, x, y, option_group_padding, options_surfaces_padding):
        for i, group in enumerate(self.option_surfaces):
            for j, option in enumerate(self.option_surfaces[i]):
                option_rect = option.get_rect()
                option_rect.topleft = (x + i * option_group_padding, y + j * options_surfaces_padding)
                if i == self.current_group and j == self.current_option_index:
                    pygame.draw.rect(surface, (0, 100, 0), option_rect)
                surface.blit(option, option_rect)


# Objects in different scenes
ui = UI()
User = Hero(100, 680, 0,
            (pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s, pygame.K_LEFT, pygame.K_DOWN, pygame.K_RIGHT))
princess = Princess(50, 680, 0, [['', 'Good day', 'Sun', 'Flowers'], ['', 'Good day', 'Sun', 'Flowers'],
                                 ['', 'O,no!', 'Help', 'Please!', 'Help!!!']], 0)

princess_words = [['', 'O,no!', 'Please!', 'Help!!!', 'You can win', 'You can do it', 'Please!!!'],
                  ['', 'O,no!', 'Please!', 'Help!!!', 'You can win', 'You can do it', 'Please!!!']] * 300
princess_end = Princess(1150, 350, 0, princess_words, 0)
boss = Boss(1100, 340, 0, [['', 'She', 'is', 'mine']], 7)
objects = [[], [User, princess], [User, ], [User, boss, princess_end]]
bullets = [[], [], [], []]

# Scene 1 objects
for _ in range(25):
    while True:
        x = randint(0, WIDTH // TILE - 1) * TILE
        y = randint(1, HEIGHT // TILE - 1) * TILE
        rect = pygame.Rect(x, y, TILE, TILE)
        fined = False
        for obj in objects[1]:
            if rect.colliderect(obj.rect):
                fined = True
        if not fined:
            break
    objects[1].append(Mob(x, y, 0, [['', 'GRR', 'RRR', 'Buga-ga']], 1))

for _ in range(18):
    while True:
        x = randint(0, WIDTH // TILE - 1) * (TILE + 7)
        y = randint(1, HEIGHT // TILE - 1) * (TILE + 7)
        rect = pygame.Rect(x, y, TILE + 7, TILE + 7)
        fined = False
        for obj in objects[1]:
            if rect.colliderect(obj.rect):
                fined = True
        if not fined:
            break
    objects[1].append(Mob(x, y, 0, [['', 'Uuuu', 'Shshsh', 'Aaaaa']], 2))

for _ in range(150):
    while True:
        x = randint(0, WIDTH // TILE - 1) * TILE
        y = randint(1, HEIGHT // TILE - 1) * TILE
        rect = pygame.Rect(x, y, TILE, TILE)
        fined = False
        for obj in objects[1]:
            if rect.colliderect(obj.rect):
                fined = True
        if not fined:
            break
    block = Block(x, y, TILE)
    objects[1].append(block)

# Scene 2 objects

for _ in range(25):
    while True:
        x = randint(0, WIDTH // TILE - 1) * TILE
        y = randint(1, HEIGHT // TILE - 1) * TILE
        rect = pygame.Rect(x, y, TILE, TILE)
        fined = False
        for obj in objects[2]:
            if rect.colliderect(obj.rect):
                fined = True
        if not fined:
            break
    objects[2].append(Mob(x, y, 0, [['', 'AAAA', 'SHshSH', 'Buga-ga']], 3))

for _ in range(18):
    while True:
        x = randint(0, WIDTH // TILE - 1) * (TILE + 7)
        y = randint(1, HEIGHT // TILE - 1) * (TILE + 7)
        rect = pygame.Rect(x, y, TILE + 7, TILE + 7)
        fined = False
        for obj in objects[2]:
            if rect.colliderect(obj.rect):
                fined = True
        if not fined:
            break
    objects[2].append(Mob(x, y, 0, [['', 'Catch him', 'AAAAA', 'Advance']], 4))

for _ in range(150):
    while True:
        x = randint(0, WIDTH // TILE - 1) * TILE
        y = randint(1, HEIGHT // TILE - 1) * TILE
        rect = pygame.Rect(x, y, TILE, TILE)
        fined = False
        for obj in objects[2]:
            if rect.colliderect(obj.rect):
                fined = True
        if not fined:
            break
    block = Block(x, y, TILE)
    objects[2].append(block)

# Scene Boss
for _ in range(10):
    while True:
        x = randint(0, WIDTH // TILE - 1) * TILE
        y = randint(1, HEIGHT // TILE - 1) * TILE
        rect = pygame.Rect(x, y, TILE, TILE)
        fined = False
        for obj in objects[3]:
            if rect.colliderect(obj.rect):
                fined = True
        if not fined:
            break
    objects[3].append(Mob(x, y, 0, [['', 'We will', 'destroy', 'you']], 5))

for _ in range(10):
    while True:
        x = randint(0, WIDTH // TILE - 1) * (TILE + 7)
        y = randint(1, HEIGHT // TILE - 1) * (TILE + 7)
        rect = pygame.Rect(x, y, TILE + 7, TILE + 7)
        fined = False
        for obj in objects[3]:
            if rect.colliderect(obj.rect):
                fined = True
        if not fined:
            break
    objects[3].append(Mob(x, y, 0, [['', 'Attack', 'Catch him', 'Food']], 4))

for _ in range(50):
    while True:
        x = randint(0, WIDTH // TILE - 1) * TILE
        y = randint(1, HEIGHT // TILE - 1) * TILE
        rect = pygame.Rect(x, y, TILE, TILE)
        fined = False
        for obj in objects[3]:
            if rect.colliderect(obj.rect):
                fined = True
        if not fined:
            break
    block = Block(x, y, TILE)
    objects[3].append(block)

SCENE_SAVED = 1
SCENE_NAME = 'scene1'


# MENU funtions
def menu_choose_easy_mode():
    global HP_MENU, CONSTANT_HP
    HP_MENU = CONSTANT_HP
    HP_MENU = [i + 3 for i in HP_MENU]



def menu_choose_medium_mode():
    global HP_MENU, CONSTANT_HP
    HP_MENU = CONSTANT_HP



def menu_choose_hard_mode():
    global HP_MENU, CONSTANT_HP
    HP_MENU = CONSTANT_HP
    HP_MENU = [i - 2 for i in HP_MENU]


def menu_choose_fast():
    global BULLET_DAMAGE_MENU, MOVE_SPEED_MENU, CONSTANT_BULLET_DAMAGE , CONSTANT_MOVE_SPEED
    BULLET_DAMAGE_MENU = CONSTANT_BULLET_DAMAGE
    MOVE_SPEED_MENU = CONSTANT_MOVE_SPEED
    BULLET_DAMAGE_MENU = [i - 1 if i > 1 else i for i in BULLET_DAMAGE_MENU]
    MOVE_SPEED_MENU = [i + 1 for i in MOVE_SPEED_MENU]


def menu_choose_balanced():
    global BULLET_DAMAGE_MENU, MOVE_SPEED_MENU, CONSTANT_BULLET_DAMAGE, CONSTANT_MOVE_SPEED
    BULLET_DAMAGE_MENU = CONSTANT_BULLET_DAMAGE
    MOVE_SPEED_MENU = CONSTANT_MOVE_SPEED


def menu_choose_strong():
    global BULLET_DAMAGE_MENU, MOVE_SPEED_MENU, CONSTANT_BULLET_DAMAGE, CONSTANT_MOVE_SPEED
    BULLET_DAMAGE_MENU = CONSTANT_BULLET_DAMAGE
    MOVE_SPEED_MENU = CONSTANT_MOVE_SPEED
    MOVE_SPEED_MENU = [i - 1 if i > 1 else i for i in MOVE_SPEED_MENU]
    BULLET_DAMAGE_MENU = [i + 1 for i in BULLET_DAMAGE_MENU]


def exit():
    sys.exit()


def start():
    global BULLET_DAMAGE_MENU, MOVE_SPEED_MENU, HP_MENU, BULLET_DAMAGE, MOVE_SPEED, HP
    BULLET_DAMAGE = BULLET_DAMAGE_MENU
    MOVE_SPEED = MOVE_SPEED_MENU
    HP = HP_MENU
    # If deleted not change hp as selected. Otherwise doesn't load hp
    User.hp = HP[User.rank]
    return True


def save():
    global objects, User, SCENE_SAVED, SCENE_NAME, HP, MOVE_SPEED, BULLET_DAMAGE
    # Create a dictionary to store game data

    game_data = {"scene_play": SCENE_SAVED,
                 "scene_name": SCENE_NAME,
                 "User": {
                     "rank": User.rank,
                     "rect_x_y": (User.rect.x, User.rect.y),
                     "hp": User.hp,
                     "scrolls": User.scrolls,
                     "xp": User.xp,
                     "HP": HP,
                     "MOVE_SPEED": MOVE_SPEED ,
                     "BULLET_DAMAGE": BULLET_DAMAGE
                 },
                 "princess": {
                     "rect_x_y": (princess.rect.x, princess.rect.y),
                     "words": princess.words,
                 },
                 "mobs": []}
    for obj in objects:
        for item in obj:
            if isinstance(item, Mob) and item.rank == 7:
                mob_data = {
                    "rank": item.rank,
                    "rect_x_y": (item.rect.x, item.rect.y),
                    "hp": item.hp,
                    "words": item.words
                }
                game_data["mobs"].append(mob_data)
    with open('savings.json', 'w') as file:
        json.dump(game_data, file)


def load():
    global objects, User, princess, boss, SCENE_SAVED, SCENE_NAME, BULLET_DAMAGE, MOVE_SPEED, HP
    with open('savings.json', 'r') as file:
        game_data = json.load(file)

    # Access and use the loaded game data as needed
    scene_play = game_data["scene_play"]
    scene_name = game_data["scene_name"]
    User.rank = game_data["User"]["rank"]
    User.rect.x, User.rect.y = game_data["User"]["rect_x_y"]

    #Detection collision
    for obj in objects[scene_play]:
        if obj.type != User.type and obj.type != 'bang' and obj.type != 'bonus' and obj.type != 'message' and obj.rect.colliderect(User.rect):
            objects[scene_play].remove(obj)


    User.hp = game_data["User"]["hp"]
    User.scrolls = game_data["User"]["scrolls"]
    User.xp = game_data["User"]["xp"]
    HP = game_data["User"]["HP"]
    MOVE_SPEED = game_data["User"]["MOVE_SPEED"]
    BULLET_DAMAGE = game_data["User"]["BULLET_DAMAGE"]

    for mob in game_data["mobs"]:
        if mob["rank"] == 7:
            boss.hp = mob["hp"]

    SCENE_NAME = scene_name
    return True


menu_game = Menu()
menu_game.append_option('EASY', menu_choose_easy_mode, 0)
menu_game.append_option('MEDIUM', menu_choose_medium_mode, 0)
menu_game.append_option('HARD', menu_choose_hard_mode, 0)
menu_game.append_option('FAST', menu_choose_fast, 1)
menu_game.append_option('BALANCED', menu_choose_balanced, 1)
menu_game.append_option('STRONG', menu_choose_strong, 1)
menu_game.append_option('LOAD', load, 2)
menu_game.append_option('SAVE', save, 2)
menu_game.append_option('START', start, 2)
menu_game.append_option('EXIT', exit, 3)

animationTimer = 40 / MOVE_SPEED[User.rank]

current_scene = None


# Main proces with scenes
def switch_scene(scene):
    global current_scene
    current_scene = scene

def menu(objects):
    global scene_play
    scene_play = 0
    play = True
    while play:
        select_count = 0
        global BULLET_DAMAGE_MENU, HP_MENU, MOVE_SPEED_MENU, BULLET_DAMAGE, HP, MOVE_SPEED, SCENE_NAME

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play = False
                switch_scene(None)
            elif event.type == pygame.KEYDOWN:


                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    global SCENE_SAVED
                    if SCENE_SAVED == 1:
                        switch_scene(scene1)
                    if SCENE_SAVED == 2:
                        switch_scene(scene2)
                    if SCENE_SAVED == 3:
                        switch_scene(scene_boss)
                    play = False
                if event.key == pygame.K_UP:
                    menu_game.switch(0, -1)
                if event.key == pygame.K_DOWN:
                    menu_game.switch(0, +1)
                if event.key == pygame.K_LEFT:
                    menu_game.switch(-1, 0)
                if event.key == pygame.K_RIGHT:
                    menu_game.switch(+1, 0)
                elif event.key == pygame.K_SPACE:
                    if select_count == 0:
                        menu_game.select()
                        select_count += 1
                    if menu_game.select() == True:
                        function_to_call = globals()[SCENE_NAME]
                        function_to_call(objects)
                        play = False
        #sound_menu.play()
        window.blit(back_map[scene_play], (0, 0))
        menu_game.draw(window, 150, 150, 300, 200)
        pygame.display.update()
        clock.tick(FPS)


def scene1(objects):
    global scene_play, SCENE_NAME
    scene_play = 1
    SCENE_NAME = 'scene1'
    play = True
    print(HP, HP_MENU, User.hp)
    while play:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play = False
                switch_scene(None)


            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                global SCENE_SAVED
                SCENE_SAVED = scene_play
                switch_scene(menu)
                play = False
        global keys
        keys = pygame.key.get_pressed()
        window.blit(back_map[scene_play], (0, 0))

        for bullet in bullets[scene_play]:
            bullet.update()
            bullet.draw()

        for obj in objects[scene_play]:
            obj.update()
            obj.draw()
        ui.update()
        ui.draw()
        if User.rect.x >= 1160 and abs(User.rect.y - 350) <= 20:
            SCENE_SAVED = scene_play + 1
            User.rect.x = 30
            User.rect.y = 350
            for obj in objects[scene_play+1]:
                if obj.type != User.type and obj.type != 'bang' and obj.type != 'bonus' and obj.type != 'message' and obj.rect.colliderect(
                        User.rect):
                    objects[scene_play+1].remove(obj)
            switch_scene(scene2)
            sound_danger.play()
            play = False

        window.blit(imgExit, (1160, 350))

        pygame.display.update()
        clock.tick(FPS)


def scene2(objects):
    global scene_play, SCENE_NAME
    scene_play = 2
    SCENE_NAME = 'scene2'
    play = True
    while play:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play = False
                switch_scene(None)

            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                global SCENE_SAVED
                SCENE_SAVED = scene_play
                switch_scene(menu)
                play = False

        window.blit(back_map[scene_play], (0, 0))
        global keys
        keys = pygame.key.get_pressed()

        for bullet in bullets[scene_play]:
            bullet.update()
            bullet.draw()

        for obj in objects[scene_play]:
            obj.update()
            obj.draw()
        # jump to a new scene
        if User.rect.x >= 1160 and abs(User.rect.y - 350) <= 20:
            SCENE_SAVED = scene_play + 1
            User.rect.x = 70
            User.rect.y = 680
            sound_danger.play()
            # Collision detection
            for obj in objects[scene_play+1]:
                if obj.type != User.type and obj.type != 'bang' and obj.type != 'bonus' and obj.type != 'message' and obj.rect.colliderect(
                        User.rect):
                    objects[scene_play+1].remove(obj)
            switch_scene(scene_boss)
            play = False
        window.blit(imgExit, (1160, 350))
        ui.update()
        ui.draw()
        pygame.display.update()
        clock.tick(FPS)


def scene_boss(objects):
    global scene_play, SCENE_NAME
    scene_play = 3
    SCENE_NAME = 'scene_boss'
    play = True
    while play:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play = False
                switch_scene(None)

            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                global SCENE_SAVED
                SCENE_SAVED = scene_play
                switch_scene(menu)
                play = False

        window.blit(back_map[scene_play], (0, 0))
        global keys
        keys = pygame.key.get_pressed()

        for bullet in bullets[scene_play]:
            bullet.update()
            bullet.draw()

        for obj in objects[scene_play]:
            obj.update()
            obj.draw()
        ui.update()
        ui.draw()

        pygame.display.update()
        clock.tick(FPS)


# Switch scenes
switch_scene(menu)

# Play scene
while current_scene is not None:
    current_scene(objects)

pygame.quit()
