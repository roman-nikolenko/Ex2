import random
import pygame

SIZE = W, H = 500, 500
clock = pygame.time.Clock()
FPS = 60
x = random.randint(1, 350)
y = random.randint(1, 350)
timer = 180

pygame.init()
win = pygame.display.set_mode((SIZE))

list_circles = []

class Circle:

    def __init__(self, x, y, rad, col):
        self.x = x
        self.y = y
        self.rad = rad
        self.col = col
        list_circles.append(self) #Добавление шаров в список

    def spawn(self):
            pygame.draw.circle(win, self.col, (self.x, self.y), self.rad)

    def update(self):
        if self.x == self.x:
            self.x += 0.1
            if self.x > W:
                self.x -= 0.1
        if self.y == self.y:
            self.y += 0.1
            if self.y > H:
                self.y -= 0.1
        else:
            self.y += 1
            if self.y < 0:
                self.y -= 0

circle = Circle(x, y, 50, 0)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            quit()
    win.fill((225, 225, 225))

    if timer > 0:
        timer -= 1
    if timer == 0:                      #По истечение времени шары из списка спавнятся
        for circle in list_circles:
            circle.spawn()
            circle.update()
    pygame.display.flip()
    pygame.display.update()