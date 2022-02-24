#載入函式庫
import pygame
import random
#定義變數
black = (0, 0, 0) #定義黑色
white = (255, 255, 255) #定義白色
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
#PlayerBox
PlayerBoxX = 0
PlayerBoxY = 0
PlayerBoxW = 69
PlayerBoxH = 69
#RandomBox
RandomBoxW = 11
RandomBoxH = 11
Score = 0

#建立box類別
class Box(pygame.sprite.Sprite):
    def __init__(self, w, h, x, y, color):
        super().__init__()
        self.image = pygame.Surface([w, h])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
AllBoxGroup = pygame.sprite.Group()
AllSpriteGroup = pygame.sprite.Group()
        
for i in range(69):
    boxX = random.randrange(0, 500-PlayerBoxX)
    boxY = random.randrange(0, 500-PlayerBoxY)
    box = Box(RandomBoxW, RandomBoxH, boxX, boxY, white)
    AllBoxGroup.add(box)
    AllSpriteGroup.add(box)

MouseBox = Box(PlayerBoxW, PlayerBoxH, PlayerBoxX, PlayerBoxY, green)
AllSpriteGroup.add(MouseBox)

#遊戲初始設定
pygame.init() #初始遊戲
size = (500, 500)  #尺寸
screen = pygame.display.set_mode(size) #建立視窗
pygame.display.set_caption("yamada") #建立標題
done = False  #遊戲開關
clock = pygame.time.Clock() #畫面更新速度
font = pygame.font.Font(None, 50)
StartTime = pygame.time.get_ticks()

#遊戲執行設定
while not done:  #重複執行直到按下X結束
    for event in pygame.event.get(): #抓取事件
        if event.type == pygame.QUIT: #如果按下結束則遊戲結束
            done = True #改變done
        if event.type == pygame.MOUSEMOTION:
            MouseBox.rect.x = pygame.mouse.get_pos()[0]
            MouseBox.rect.y = pygame.mouse.get_pos()[1]
    
    screen.fill(black)
    text = font.render(str(Score), True, green)
    EndTime = pygame.time.get_ticks()
    time = font.render(str((EndTime - StartTime) / 1000), True, green)
    screen.blit(text, (10, 10))
    screen.blit(time, (10, 69))
    
    BlocksHitList = pygame.sprite.spritecollide(MouseBox, AllBoxGroup, True)
    
    for i in BlocksHitList:
        Score += 10101
        
    if (EndTime - StartTime) / 1000 > 10.682:
        done = True
    
    AllSpriteGroup.draw(screen)
    
    pygame.display.flip() #畫面更新
    clock.tick(100) #畫面更新每秒60次

#遊戲結束
pygame.quit()