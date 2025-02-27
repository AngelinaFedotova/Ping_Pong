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

ball = GameSprite('ball.png', 15, 250, 250, 60, 60)
racket1 = Player('racket.png', 15, 20, 100, 40, 80)
racket2 = Player('racket.png', 15, 540, 100, 40, 80)

init()
font.init()
font1 = font.Font(None, 35)
lose1 = font1.render('PLAYER 1 LOSE!', True, (180, 0, 0))
lose2 = font1.render('PLAYER 2 LOSE!', True, (180, 0, 0))

clock = time.Clock()
speed_x = 3
speed_y = 3
FPS = 30
run = True
finish = False
while run:
    window.fill((240, 230, 140))
    for e in event.get():
        if e.type == QUIT:
            run = False

        if finish != True:
            ball.rect.x += speed_x
            ball.rect.y += speed_y

        if ball.rect.y > height-50 or ball.rect.y < 0:
            speed_y *= -1

        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1

        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))
        if ball.rect.x > 600:
            finish = True
            window.blit(lose2, (200, 200))

    ball.update()
    ball.reset()
    racket1.update_l()
    racket1.reset()
    racket2.update_r()
    racket2.reset()
    display.update()

    clock.tick(FPS)