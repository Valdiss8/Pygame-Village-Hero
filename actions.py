import pygame


from objects import objects
WIDTH, HEIGHT = 1280, 780

bullets = []
objects_part1 = []
window = pygame.display.set_mode((WIDTH, HEIGHT))

"""sounds"""


class Bullet:
    """Attacking magic"""

    def __init__(self, parent, px, py, dx, dy, damage):
        bullets.append(self)
        self.parent = parent
        self.px, self.py = px, py
        self.dx, self.dy = dx, dy
        self.damage = damage

    def update(self):
        self.px += self.dx
        self.py += self.dy

        if self.px - self.dx > abs(500) or self.py - self.dy > abs(500):
            bullets.remove(self)
        else:
            for obj in objects:
                if obj != self.parent and obj.type == 'hero' or obj.type == 'mob':
                    obj.damage(self.damage)
                    bullets.remove(self)
                    Bang(self.px, self.py)
                    #sound_dest.play()
                    break

    def draw(self):
        pygame.draw.circle(window, 'yellow', (self.px, self.py), 2)


imgBangs = [
    pygame.image.load('images/bang/bang1.png'),
    pygame.image.load('images/bang/bang1.png'),
    pygame.image.load('images/bang/bang1.png')
]


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
