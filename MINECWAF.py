#載入函式庫
import pygame, random

#定義變數
black = (0, 0, 0) #定義黑色
white = (255, 255, 255) #定義白色
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

class Ball(pygame.sprite.Sprite):
    dx = 0
    dy = 0
    x = 0
    y = 0
    def __init__(self, srx, sry, radius, color):
        pygame.sprite.Sprite.__init__(self)
        self.x = srx
        self.y = sry
        self.image = pygame.Surface([radius*2, radius*2])
        pygame.draw.circle(self.image, color, (radius, radius), radius, 0)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.dx = random.randint(7, 10) * random.choice([1, -1])
        self.dy = random.randint(7, 10) * -1
    
    def update(self):
        self.x += self.dx
        self.y += self.dy
        self.rect.x = self.x
        self.rect.y = self.y
        if self.rect.x <= 0 or self.rect.x >= 500:
            self.dx *= -1
        if self.rect.y <= 0 or self.rect.y >= 500:
            self.dy *= -1

#遊戲初始設定
pygame.init() #初始遊戲
size = (500, 500)  #尺寸
screen = pygame.display.set_mode(size) #建立視窗
pygame.display.set_caption("MINECWAF") #建立標題
done = False  #遊戲開關
clock = pygame.time.Clock() #畫面更新速度

AllSpriteGroup = pygame.sprite.Group()
RedBall = Ball(250, 400, 69, red)
AllSpriteGroup.add(RedBall)

GreenBall = Ball(250, 400, 69, green)
AllSpriteGroup.add(GreenBall)

BlueBall = Ball(250, 400, 69, blue)
AllSpriteGroup.add(BlueBall)

WhiteBall = Ball(250, 400, 69, white)
AllSpriteGroup.add(WhiteBall)

#遊戲執行設定
while not done:  #重複執行直到按下X結束
    for event in pygame.event.get(): #抓取事件
        if event.type == pygame.QUIT: #如果按下結束則遊戲結束
            done = True #改變done
    screen.fill(black)
    RedBall.update()
    GreenBall.update()
    BlueBall.update()
    WhiteBall.update()
    AllSpriteGroup.draw(screen)
    
    pygame.display.flip() #畫面更新
    clock.tick(6942069420694206942069420) #畫面更新每秒60次

#遊戲結束
pygame.quit()