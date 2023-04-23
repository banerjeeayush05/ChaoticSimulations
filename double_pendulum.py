import pygame
import math

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

g = 1

r1 = 125
r2 = 125

m1 = 10
m2 = 10

a1 = math.pi / 2
a2 = math.pi / 2
a1_v = 0
a2_v = 0
a1_a = 0
a2_a = 0

CENTER_X = SCREEN_WIDTH / 2
CENTER_Y = 200

GAME_WINDOW = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Double Pendulum')
GAME_CLOCK = pygame.time.Clock()

end_coords = []

running = True
while running:
    GAME_WINDOW.fill(BLACK)

    x1 = CENTER_X + r1 * math.sin(a1)
    y1 = CENTER_Y + r1 * math.cos(a1)
    x2 = x1 + r2 * math.sin(a2)
    y2 = y1 + r2 * math.cos(a2)

    pygame.draw.line(GAME_WINDOW, GREEN, (CENTER_X, CENTER_Y), (x1, y1), width = 3)
    pygame.draw.circle(GAME_WINDOW, RED, (x1, y1), m1)

    pygame.draw.line(GAME_WINDOW, GREEN, (x1, y1), (x2, y2), width = 3)
    pygame.draw.circle(GAME_WINDOW, RED, (x2, y2), m2)

    if(len(end_coords) >= 2):
        pygame.draw.lines(GAME_WINDOW, WHITE, False, end_coords, width = 3)

    a1_v += a1_a
    a2_v += a2_a
    a1 += a1_v
    a2 += a2_v

    num1 = -g * (2 * m1 + m2) * math.sin(a1)
    num2 = -m2 * g * math.sin(a1 - 2 * a2)
    num3 = -2 * math.sin(a1 - a2) * m2
    num4 = a2_v * a2_v * r2 + a1_v * a1_v * r1 * math.cos(a1 - a2)
    den = r1 * (2 * m1 + m2 - m2 * math.cos(2 * a1 - 2 * a2))
    a1_a = (num1 + num2 + num3 * num4) / den

    num1 = 2 * math.sin(a1 - a2)
    num2 = (a1_v * a1_v * r1 * (m1 + m2))
    num3 = g * (m1 + m2) * math.cos(a1)
    num4 = a2_v * a2_v * r2 * m2 * math.cos(a1 - a2)
    den = r2 * (2 * m1 + m2 - m2 * math.cos(2 * a1 - 2 * a2))
    a2_a = (num1 * (num2 + num3 + num4)) / den

    end_coords.append((x2, y2))

    for event in pygame.event.get():
	    if event.type == pygame.QUIT:
		    running = False
	
    pygame.display.update()
    GAME_CLOCK.tick(20)