import pygame

pygame.init()
dis = pygame.display.set_mode((400, 300))
pygame.display.update()
pygame.display.set_caption('The Great Snake Game')
game_over = False
crashed = False

clock = pygame.time.Clock()

snakeHead = pygame.image.load('')
snakeBody = pygame.image.load('')
def snake(x,y):
    dis.blit(snakeHead, (x,y))
    x = (400 * 0.45)
    y = (300 * 0.8)

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True


while not game_over:
    for event in pygame.event.get():
        print(event)  # prints out all the actions that take place on the screen

pygame.quit()
quit()
#https://www.edureka.co/blog/snake-game-with-pygame/#screen
#https://pythonprogramming.net/displaying-images-pygame/