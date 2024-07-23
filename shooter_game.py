#Создай собственный Шутер!
from random import randint
from pygame import *
font.init()

mixer.init()
window = display.set_mode((700, 500))
display.set_caption('Sniper')
background = transform.scale(image.load("galaxy.jpg"), (700,500))
mixer.music.load('space.ogg')
mixer.music.play()
bullets = sprite.Group()
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, player_height, player_weight):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_height, player_weight))    
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y 
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
   def update(self):
       keys = key.get_pressed()
       if keys[K_LEFT] and self.rect.x > 5:
           self.rect.x -= self.speed
       if keys[K_RIGHT] and self.rect.x < 620:
           self.rect.x += self.speed
   def fire(self):
        bullet = Bullet('bullet.png', self.rect.centerx, self.rect.top, 15, 20, 15)
        bullets.add(bullet)
      
lost = 0 
class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > 500:
            self.rect.y = 0
            self.rect.x = randint(80,620)
            global lost
            lost = lost + 1
class Enemy_1(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > 500:
            self.rect.y = 0
            self.rect.x = randint(80,620)
monsters = sprite.Group()
asteroids = sprite.Group()
class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y > 500:
            self.kill 
bullets = sprite.Group()
for i in range(5):
    monster = Enemy('ufo.png', randint(65, 635), 0, randint(1, 2 ), 65, 65)
    monsters.add(monster)
for i in range(3):
    asteroid = Enemy_1('asteroid.png', randint(65, 635), 0,randint(1,3),65,65)
    asteroids.add(asteroid)
rocket = Player('rocket.png', 350, 400, 5, 60, 80)
font1 = font.SysFont('Arial', 36)

font = font.SysFont('Arial', 70)
win = font.render(
   'Победа', True, (255, 215, 0)
)
lose = font.render(
   'Вас захватили', True, (255, 215, 0)
)
 
point = 0
clock = time.Clock()
FPS = 60
run = True
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
        if e.type == KEYDOWN       :
            if e.key == K_SPACE:
                rocket.fire()
    death_list = sprite.groupcollide(
        monsters, bullets, True, True
    )
    sprites_list = sprite.spritecollide(
        rocket, monsters, False
    )
    asteroids_list = sprite.spritecollide(
        rocket, asteroids, False
    )
    for i in death_list:
        point+=1
        monster = Enemy('ufo.png', randint(65, 635), 0, randint(1, 5), 65, 65)
        monsters.add(monster)
    if sprites_list == 10:
        run = False
        window_blit(win,(200,200))
    if lost == 3:
        run = False
        window.blit(lose,(200,200))
    window.blit(background,(0, 0))
    monsters.draw(window)
    rocket.reset()
    rocket.update()
    monsters.update()
    asteroids.draw(window)
    asteroids.update()
    text_lose = font1.render(
        "Пропущено: " + str(lost), 1, (255, 255, 255)
    )
    window.blit(text_lose,(0,0))

    text_win = font1.render(
        "Счёт: " + str(point), 1, (255, 255, 255)
    )
    window.blit(text_win,(0,50))
   
    bullets.draw(window)
    bullets.update()
    display.update()
    clock.tick(FPS)
while lost == 3:
    window.blit(lose,(200,200))
    display.update()
    for e in event.get():
        if e.type == QUIT:
            lost= False
while asteroids_list == 3:
    window.blit(lose,(200,200))
    display.update()
    for e in event.get():
        if e.type == QUIT:
            asteroids_list = False