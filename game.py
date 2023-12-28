from pygame import *

init()

window = display.set_mode((700, 500))
window_news = display.set_mode((700, 500))
display.set_caption('Labirint')

background_image = transform.scale(image.load('algo.py\губка.jpg'), (700,500))

class GameSprite(sprite.Sprite):
    def __init__(self, sprite_image, x, y, size_x, size_y):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(sprite_image), (size_x, size_y))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    
    

class Player(GameSprite):
    def __init__(self, sprite_image, x, y, size_x, size_y, speed_x, speed_y):
        GameSprite.__init__(self, sprite_image, x, y, size_x, size_y)
        self.speed_x = speed_x
        self.speed_y = speed_y

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

    def fire(self):
        bullet = Bullet('algo.py\пуля.jpg', self.rect.right, self.rect.centery, 20,10, 15)
        bullets.add(bullet)
    def fire1(self):
        bullet = Bullet('algo.py\пуля.jpg', self.rect.left, self.rect.centery, 20,10, -15)
        bullets.add(bullet)

class Enemy(GameSprite):
    side = 'left'
    def __init__(self, sprite_image, x, y, size_x, size_y, enemy_speed):
        GameSprite.__init__(self, sprite_image, x, y, size_x, size_y)
        self.speed = enemy_speed
        self.side = 'left'
    def update(self):
        if self.rect.x >= 650:
            self.side = 'left'
        if self.rect.x <= 320:
            self.side = 'right'
        if self.side == 'right':
            self.rect.x += self.speed
        if self.side == 'left':
            self.rect.x -= self.speed


class Bullet(GameSprite):
    def __init__(self, sprite_image, x, y, size_x, size_y, bullet_speed):
        GameSprite.__init__(self, sprite_image, x, y, size_x, size_y)
        self.speed = bullet_speed
    def update(self):
         self.rect.x += self.speed
         if self.rect.x > 700:
             self.kill()


class Chest(GameSprite):
    def __init__(self, sprite_image, x, y, size_x, size_y):
        GameSprite.__init__(self, sprite_image, x, y, size_x, size_y)
    
    def open(self):
        new_window = display.set_mode((500, 350))
        new_window.fill((255, 255, 255))
        display.set_caption('New Window')
        display.update()

monster1 = Enemy('algo.py\сквидват.png', 640, 30, 60, 60, 5 )
monster2 = Enemy('algo.py\сквидват.png', 640, 130, 60, 60, 5 )
monster3 = Enemy('algo.py\сквидват.png', 640, 230, 60, 60, 5 )
monsters = sprite.Group()
monsters.add(monster1)
monsters.add(monster2)
monsters.add(monster3)

wall1 = GameSprite('algo.py\мега стена.png',100, 100, 20, 400)
wall2 = GameSprite('algo.py\мега стена.png',200, 0, 20, 400)
wall3 = GameSprite('algo.py\мега стена.png',300, 100, 20, 400)
wall4 = GameSprite('algo.py\мега стена.png',400, 100, 400,20)
wall5 = GameSprite('algo.py\мега стена.png',320, 200, 300,20)
wall6 = GameSprite('algo.py\мега стена.png',400, 300, 400,20)
wall7 = GameSprite('algo.py\мега стена.png',320, 400, 300,20)


player = Player('algo.py\патрик.jpg', 10, 425, 50, 50, 0, 0)
chest = Chest('algo.py\пуля.jpg' , 350, 425, 50, 50)
run = True
finish = False

walls = sprite.Group()

walls.add(wall1)
walls.add(wall2)
walls.add(wall3)
walls.add(wall4)
walls.add(wall5)
walls.add(wall6)
walls.add(wall7)

bullets = sprite.Group()

def game_over():
    game_over_image = transform.scale(image.load('algo.py\мега стена.png'), (700, 500))
    window.blit(game_over_image, (0, 0))
    player.speed_x = 0
    player.speed_y = 0
    finish = True

def win():

    win_image = transform.scale(image.load('algo.py\фон.jpg'), (700, 500))
    window.blit(win_image, (0, 0))
    player.speed_x = 0
    player.speed_y = 0
    finish = True

while run:
    time.delay(50)

    window.blit(background_image, (0, 0))

    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_w:
                player.speed_y = -5
            elif e.key == K_s:
                player.speed_y = 5
            elif e.key == K_a:
                player.speed_x = -5
            elif e.key == K_d:
                player.speed_x = 5
            elif e.key == K_RIGHT:
                player.fire()
            elif e.key == K_LEFT:
                player.fire1()

        elif e.type == KEYUP:
            if e.key == K_w:
                player.speed_y = 0
            elif e.key == K_s:
                player.speed_y = 0
            elif e.key == K_a:
                player.speed_x = 0
            elif e.key == K_d:
                player.speed_x = 0
        
    

    if finish != True:
        walls.draw(window)
        monsters.draw(window)
        bullets.draw(window)
        player.reset()
        chest.reset()
        player.update()
        bullets.update()
         

        sprite.groupcollide(monsters, bullets, True, True)
        sprite.groupcollide(walls, bullets, False, True)
        if (player.rect.x >= 700 or player.rect.x <= 0) or (player.rect.y >= 500 or player.rect.y <= 0):
            player.rect.x = 10 
            player.rect.y = 425
            

        if 340 <= player.rect.x == 360 and 400 <= player.rect.y >= 415:
            win()
        

        if sprite.spritecollide(player, walls, False):
            player.rect.x = 10 
            player.rect.y = 425 
            #game_over()

        if sprite.spritecollide(player, monsters, False):
            player.rect.x = 10 
            player.rect.y = 425 
        
       
       
        



        monsters.update()
    

    display.update()


