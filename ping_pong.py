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
        if keys_pressed[K_s] and self.rect.y < 300:
            self.rect.y += self.speed

    def update_r(self):
        keys_pressed = key.get_pressed()

        if keys_pressed[K_UP] and self.rect.y > -35:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 300:
            self.rect.y += self.speed

class Ball(GameSprite):
    def update(self):
        if self.rect.y < 0:
            self.speed_y = self.speed_y * -1

        if self.rect.y > 450:
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
window_size = [700, 500]
window = display.set_mode(window_size)
display.set_caption("Пинг Понг")
#задай фон сцены
background = transform.scale(image.load("fon.jpg"), window_size)

#фоновая музыка

#обработай событие «клик по кнопке "Закрыть окно"»
def correct_dir(racket_check):
    player.speeds()
    if player.rect.y >= racket_check.rect.y and player.rect.y <= racket_check.rect.y + 45:
        player.one()
    elif player.rect.y >= racket_check.rect.y + 125 and player.rect.y <= racket_check.rect.y + 250:
        player.two()
    elif player.rect.y >= racket_check.rect.y + 75 and player.rect.y <= racket_check.rect.y + 110:
        player.three()

clock = time.Clock()
FPS = 60
game = True
notGame = True

font.init()
fontmy = font.SysFont("Arial", 70)

player1 = fontmy.render("PLAYER 1 WIN", True, (255, 215, 0))
player2 = fontmy.render("PLAYER 2 WIN", True, (255, 0, 0))

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
            

    if sprite.collide_rect(player, racket1):
        correct_dir(racket1)

    if sprite.collide_rect(player, racket2):
        correct_dir(racket2)
    
    if notGame:
        racket1.update_l()
        racket2.update_r()
        player.update()

        window.blit(background, (0,0))
        player.reset()
        racket1.reset()
        racket2.reset()



    if player.rect.x >= 700:
        window.blit(player1, (130,150))
        notGamse = False

    if player.rect.x <= -40:
        window.blit(player2, (130,150))
        notGame = False


    display.update()
    clock.tick(FPS)
