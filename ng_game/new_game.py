from pygame import *
from random import *


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, rect_x, rect_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (100, 90))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = rect_x
        self.rect.y = rect_y
    
    def reset(self):
        win.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):

    def update(self):
        
        keys = key.get_pressed()
        if self.rect.y < 710:
            self.rect.y += 8

        if keys[K_d] and self.rect.x < 1200:
            self.rect.x += self.speed
        
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed



    def jump(self):
        
        keys = key.get_pressed()
        if self.rect.y == 710:
            if keys[K_SPACE]:
                for i in range(100):
                    self.rect.y -= 2


class Enemy(GameSprite):
    def update(self):
        self.rect.y += 7
        if self.rect.y > 750:
            self.rect.y = randint(-120, 50)
            self.rect.x = randint(20, 950)
    

class Platform(GameSprite):
    def update(self):
        pass
        

# окно
win = display.set_mode((1300, 800))
display.set_caption('Новогодния игра')
fon = transform.scale(image.load("bg_lvl1.png"), (1300, 800))
win.blit(fon, (0, 0))


#игрок
main_hero = Player('main_hero.png', 600, 710, 10)

#платформа
platform_1 = Platform('New Piskel (14).png', 300, 600, 10)

#враги
meteors = sprite.Group()
for i in range(15):
    meteor = Enemy('meteor.png', randint(-120, 50), randint(20, 850), 4)
    meteors.add(meteor)

#игра
fps = 60
clock = time.Clock()
game = True

while game:
    win.blit(fon, (0, 0))
    for e in event.get():
        if e.type == QUIT:
            game = False
    a = sprite.spritecollide(platform_1, meteors, True, False)
    if a:
        for meteor in a:
            meteors.add(Enemy('meteor.png', randint(-120, 50), randint(20, 850), 4))
            meteor.kill()

        
    
    main_hero.update()
    main_hero.reset()
    main_hero.jump()

    meteors.update()
    meteors.draw(win)

    platform_1.update()
    platform_1.reset()

    clock.tick(fps)
    display.update()
