#Создай собственный Шутер!
from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, images, x, y, size_x, size_y, speed):
        super().__init__()
        self.image = transform.scale(image.load(images), [size_x, size_y])
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def reset(self): 
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys_pressed = key.get_pressed()

        if keys_pressed[K_w] and self.rect.y > -35:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 290:
            self.rect.y += self.speed

    def update_r(self):
        keys_pressed = key.get_pressed()

        if keys_pressed[K_UP] and self.rect.y > -35:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 290:
            self.rect.y += self.speed


    

player = Player("tennis.png", 250, 200, 70, 70, 10)
racket1 = Player("rectangle.png", 0, 150, 30, 250, 10)
racket2 = Player("rectangle.png", 670, 150, 30, 250, 10)
#создай окно игры
window_size = [700, 500]
window = display.set_mode(window_size)
display.set_caption("Пинг Понг")
#задай фон сцены
background = transform.scale(image.load("fon.jpg"), window_size)

#фоновая музыка

#обработай событие «клик по кнопке "Закрыть окно"»

clock = time.Clock()
FPS = 60
game = True


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    racket1.update_l()
    racket2.update_r()

    window.blit(background, (0,0))
    player.reset()
    racket1.reset()
    racket2.reset()
    
    display.update()
    clock.tick(FPS)
