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
            
