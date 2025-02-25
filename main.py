from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, image1, speed, x, y, size_x, size_y):
        super().__init__()
        self.image = transform.scale(image.load(image1), (size_x, size_y))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update_r(self):
        keys_pressed = key.get_pressed()

        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= 5
        if keys_pressed[K_DOWN] and self.rect.y < 500-80:
            self.rect.y += 5

    def update_l(self):
        keys_pressed = key.get_pressed()

        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= 5
        if keys_pressed[K_s] and self.rect.y < 500-80:
            self.rect.y += 5
            
widht = 600
height = 500
window = display.set_mode((widht, height))
window.fill((240, 230, 140))

ball = GameSprite('ball.png', 4, 250, 250, 60, 60)
racket1 = Player('racket.png', 3, 20, 100, 40, 80)
racket2 = Player('racket.png', 3, 540, 100, 40, 80)

clock = time.Clock()
FPS = 60
run = True
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    ball.update()
    ball.reset()
    racket1.update()
    racket1.update_l()
    racket1.reset()
    racket2.update()
    racket2.update_r()
    racket2.reset()
    display.update()

    clock.tick(FPS)