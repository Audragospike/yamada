#載入函式庫
import pygame, random

#定義變數
black = (0, 0, 0) #定義黑色
white = (255, 255, 255) #定義白色
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
score = 0

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
        if self.rect.y <= 0:
            self.dy *= -1
        if self.rect.y >= 500:
            return True
        else:
            return False
            
    def collide(self):
        self.dy *= -1

class Block(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([40, 15])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Pad(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([5000, 6.9])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

#遊戲初始設定
pygame.init() #初始遊戲
size = (500, 500)  #尺寸
screen = pygame.display.set_mode(size) #建立視窗
pygame.display.set_caption("MINECWAF") #建立標題
done = False  #遊戲開關
clock = pygame.time.Clock() #畫面更新速度

AllSpriteGroup = pygame.sprite.Group()

GreenBall = Ball(250, 269, 19, green)
AllSpriteGroup.add(GreenBall)

AllBlockGroup = pygame.sprite.Group()
for i in range(4):
    for j in range(10):
        block = Block(blue, j*50+5, i*25+5)
        AllBlockGroup.add(block)
        AllSpriteGroup.add(block)
        
paddy = Pad(red, 250, 369)
AllSpriteGroup.add(paddy)

#遊戲執行設定
while not done:  #重複執行直到按下X結束
    for event in pygame.event.get(): #抓取事件
        if event.type == pygame.QUIT: #如果按下結束則遊戲結束
            done = True #改變done
        if event.type == pygame.MOUSEMOTION:
            paddy.rect.x = pygame.mouse.get_pos()[0]-500
            
    screen.fill(black)
    done = GreenBall.update()
    AllSpriteGroup.draw(screen)
    
    PadResult = pygame.sprite.collide_rect(GreenBall, paddy)
    if PadResult:
        GreenBall.collide()
    
    BlockResult = pygame.sprite.spritecollide(GreenBall,AllBlockGroup, True)
    if len(BlockResult) > 0:
        GreenBall.collide()
        score += len(BlockResult)
        pygame.display.set_caption(str(score)) #建立標題
    
    pygame.display.flip() #畫面更新
    clock.tick(100000) #畫面更新每秒60次

#遊戲結束
pygame.quit()