import pygame
from pygame.draw import *


def draw_angry_smiley():
    pygame.init()

    #настройки экрана 
    width, height = 400, 400
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Злой смайлик - Задание 1")


    #Цвета
    YELLOW = (255, 255, 0)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    WHITE = (255, 255, 255)

    #заливаем фон белым
    screen.fill(WHITE)

    # 1. рисуем голову (желтый круг)
    circle(screen, YELLOW, (width//2, height//2), 150)

      # 2. Рисуем глаза
    # Левый глаз
    circle(screen, RED, (width//2 - 50, height//2 - 30), 25)
    circle(screen, BLACK, (width//2 - 50, height//2 - 30), 10)
    # Правый глаз
    circle(screen, RED, (width//2 + 50, height//2 - 30), 25)
    circle(screen, BLACK, (width//2 + 50, height//2 - 30), 10)
    
    # 3. Рисуем злой рот (прямоугольник)
    rect(screen, BLACK, (width//2 - 60, height//2 + 40, 120, 20))
    
    # 4. Рисуем брови (злые треугольники)
    # Левая бровь
    polygon(screen, BLACK, [(width//2 - 80, height//2 - 50), 
                          (width//2 - 30, height//2 - 70),
                          (width//2 - 20, height//2 - 60)])
    # Правая бровь
    polygon(screen, BLACK, [(width//2 + 80, height//2 - 50), 
                          (width//2 + 30, height//2 - 70),
                          (width//2 + 20, height//2 - 60)])
    
    pygame.display.update()

    running = True
    while running:
        for even in pygame.event.get():
            if even.type == pygame.QUIT:
                running = False
        pygame.time.delay(30)

    pygame.quit()

if __name__ == "__main__":
    draw_angry_smiley()