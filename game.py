from pygame import *

init()

window = display.set_mode((700, 500))
display.set_caption('Labirint')

background_image = transform.scale(image.load('algo.py\дота.jpg'), (700,500))

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

wall1 = GameSprite('algo.py\мега стена.png',100, 100, 20, 400)
wall2 = GameSprite('algo.py\мега стена.png',200, 0, 20, 400)
wall3 = GameSprite('algo.py\мега стена.png',300, 100, 20, 400)
wall4 = GameSprite('algo.py\мега стена.png',400, 100, 400,20)
wall5 = GameSprite('algo.py\мега стена.png',320, 200, 300,20)
wall6 = GameSprite('algo.py\мега стена.png',400, 300, 400,20)
wall7 = GameSprite('algo.py\мега стена.png',320, 400, 300,20)

player = Player('algo.py\патрик.jpg', 10, 420, 50, 50, 0, 0)
run = True
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
        elif e.type == KEYUP:
            if e.key == K_w:
                player.speed_y = 0
            elif e.key == K_s:
                player.speed_y = 0
            elif e.key == K_a:
                player.speed_x = 0
            elif e.key == K_a:
                player.speed_x = 0

    if player.rect.x >= 340 and player.rect.y >= 400:
        game_over_image = transform.scale(image.load('algo.py\мега стена.png'), (700, 500))
        window.blit(game_over_image, (0, 0))
        run = False

    if sprite.collide_rect(player, wall1) or sprite.collide_rect(player, wall2) or sprite.collide_rect(player, wall3) or sprite.collide_rect(player, wall4) or sprite.collide_rect(player, wall5) or sprite.collide_rect(player, wall6) or sprite.collide_rect(player, wall7):
        player.speed_x = 0
        player.speed_y = 0

    wall1.reset()
    wall2.reset()
    wall3.reset()
    wall4.reset()
    wall5.reset()
    wall6.reset()
    wall7.reset()
    player.reset()
    player.update()
    display.update()


