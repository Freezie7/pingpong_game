#Создай собственный Шутер!
from pygame import *

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

    window.blit(background, (0,0))
    
    display.update()
    clock.tick(FPS)
