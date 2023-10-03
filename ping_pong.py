#Создай собственный Шутер!
from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, images, x, y, size_x, size_y, speed, speed_y):
        super().__init__()
        self.image = transform.scale(image.load(images), [size_x, size_y])
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.speed_y = speed_y

    def reset(self): 
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys_pressed = key.get_pressed()

        if keys_pressed[K_w] and self.rect.y > -35:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 490:
            self.rect.y += self.speed

    def update_r(self):
        keys_pressed = key.get_pressed()

        if keys_pressed[K_UP] and self.rect.y > -35:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 490:
            self.rect.y += self.speed

class Ball(GameSprite):
    def update(self):
        if self.rect.y < 0:
            self.speed_y = self.speed_y * -1

        if self.rect.y > 650:
            self.speed_y = self.speed_y * -1

        self.rect.x -= self.speed
        self.rect.y -= self.speed_y
        
    def speeds(self):
        self.speed = self.speed * -1

    def one(self):
        self.speed_y = 3

    def two(self):
        self.speed_y = -3

    def three(self):
        self.speed_y = 0



    

player = Ball("tennis.png", 250, 200, 70, 70, 10, 0)
racket1 = Player("rectangle.png", 0, 150, 30, 250, 10, 0)
racket2 = Player("rectangle.png", 670, 150, 30, 250, 10, 0)
#создай окно игры
window_size = [700, 700]
window = display.set_mode(window_size)
display.set_caption("Пинг Понг")
#задай фон сцены
background = transform.scale(image.load("fon.jpg"), window_size)

#фоновая музыка

#обработай событие «клик по кнопке "Закрыть окно"»

clock = time.Clock()
FPS = 60
game = True

font.init()
fontmy = font.SysFont("Arial", 70)

player1 = fontmy.render("PLAYER 1 WIN", True, (255, 215, 0))
player2 = fontmy.render("PLAYER 2 WIN", True, (255, 0, 0))

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    racket1.update_l()
    racket2.update_r()
    player.update()

    if sprite.collide_rect(player, racket1) or sprite.collide_rect(player, racket2) :
        player.speeds()
        if player.rect.y >= racket1.rect.y and player.rect.y <= racket1.rect.y + 45:
            player.one()
        elif player.rect.y >= racket1.rect.y + 151 and player.rect.y <= racket1.rect.y + 250:
            player.two()
        elif player.rect.y >= racket1.rect.y + 125 and player.rect.y <= racket1.rect.y + 150:
            player.three()



    window.blit(background, (0,0))
    if player.rect.x >= 700:
        window.blit(player1, (130,300))

    if player.rect.x <= 0:
        window.blit(player2, (130,300))

    player.reset()
    racket1.reset()
    racket2.reset()
    
    display.update()
    clock.tick(FPS)
