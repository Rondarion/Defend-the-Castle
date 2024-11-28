from pygame import *
from random import randint
from time import sleep
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QButtonGroup, QRadioButton,  
        QPushButton, QLabel)
bullets = sprite.Group()
monsters = sprite.Group()
collides = sprite.Group()
score = 0
prefer = 1
game = True
finish = False
clock = time.Clock()
max_lost = 1
FPS = 60
c = 0
max_win = 5
lost = 0
win_game = 0

font.init()
font1 = font.Font(None, 80)
win = font1.render('YOU WIN!', True, (255, 255, 255))
lose = font1.render('YOU LOSE!', True, (180, 0, 0))
font2 = font.Font(None, 36)
app = QApplication([])
lb_name = QLabel('Защити королевство,воин!') 
lb_me = QLabel('Крутой, великолепный, красивый, добрый, хороший и может быть гениальный Рома:)') 
btn_play = QPushButton('Играть')
btn_author = QPushButton('Автор') 
layout_ans1 = QVBoxLayout()
window_q = QWidget()

window_q.setWindowTitle('Memo Card') 
layout_ans1.addWidget(lb_name)
layout_ans1.addWidget(btn_play)
layout_ans1.addWidget(btn_author)
window_q.setLayout(layout_ans1)

class GameSprite(sprite.Sprite):
    #конструктор класса
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
 
        # каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (55, 55))
        self.speed = player_speed
 
        # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
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
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 10:
            self.rect.y += self.speed
    def fire(self):
       bullet = Bullet('true-fotor-bg-remover-2024112120731.png', self.rect.centerx + 5, self.rect.centery - 20, 1)
       bullets.add(bullet)      
    
        
class Enemy(GameSprite):
    def update(self):
        
        if self.rect.x > -70:
            self.rect.x -= self.speed
class Bullet(GameSprite):
   #движение врага
   def update(self):
        self.rect.x += self.speed
       #исчезает, если дойдет до края экрана
        if self.rect.x > player.rect.x + 35 :
            self.kill()
            
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Maze")
background = transform.scale(image.load("background_game.jpg"), (win_width, win_height))

def prefer_1():
    prefer = 2
    print(prefer)
    print(124)
    
    
def prefer_2():
    prefer = 1
    print(prefer)
    print(124)
    
def prefer_3():
    prefer = 3
    
    
btn_play.clicked.connect(prefer_1)
btn_author.clicked.connect(prefer_3)
    

#Персонажи игры:

player = Player('png-transparent-digital-art-knight-pixel-text-fictional-character-technology-643678440-fotor-bg-remover-2024112120346.png', 50, win_height /2, 10)
monster = Enemy('knigjt-fotor-bg-remover-20241121.png', 710, randint(10,490),2)
monsters.add(monster)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                        
                player.fire()
                
                
        if finish != True:
            window.blit(background,(0, 0))
            player.update()
            monster.update()
            bullets.update()
            player.reset()
            monster.reset()
            bullets.draw(window)
            сollides = sprite.groupcollide(monsters,bullets,True,True)
            text = font2.render('Счет: '+str(score),1,(255,255,255))
            window.blit(text,(10,20))

            text_lose = font2.render('Пропущено: '+str(lost),1,(255,255,255))
            window.blit(text_lose,(10,50))
            display.update()
        for c in collides:
            score = score + 1
            monster = Enemy('knigjt-fotor-bg-remover-20241121.png', 710, randint(10,490),2)
            monsters.add(monster)
        if sprite.spritecollide(player,monsters,False) or max_lost <= lost :
            finish = True
            game = False
        elif max_win <= score:
            win_game = True
            game = False
        if monster.rect.x < 0:
            lost += 1
            monster.rect.x = 1000
            monster.kill()
            monster = Enemy('knigjt-fotor-bg-remover-20241121.png', 710, randint(10,490),2)
            monsters.add(monster)
if finish == True:
    window.blit(lose,(200,200))  
                    
if win_game == True:
    window.blit(win,(200,200))
                     
                    
display.update()
clock.tick(FPS)
    


