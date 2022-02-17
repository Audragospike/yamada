#載入函式庫
import pygame
from queue import Queue
import random
#定義變數
black = (0, 0, 0) #定義黑色
white = (255, 255, 255) #定義白色
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

#建立Segment
SegmentWidth = 15
SegmentHeight = 15
SegmentGap = 5
SegmentX = 0
SegmentY = 0

Yamada = 0

XChange = SegmentWidth + SegmentGap
YChange = 0
#建立Segment類別
class Segment(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()
        self.image = pygame.Surface([SegmentWidth, SegmentHeight])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

#遊戲初始設定
pygame.init() #初始遊戲
size = (500, 500)  #尺寸
screen = pygame.display.set_mode(size) #建立視窗

done = False  #遊戲開關
clock = pygame.time.Clock() #畫面更新速度
pygame.display.set_caption("Yamada") #建立標題
AllSegmentGroup = pygame.sprite.Group()
AllSegmentQueue = Queue()

for i in range(2):
    x = (SegmentWidth + SegmentGap) * i
    y = 0
    segment = Segment(x, y, green)
    AllSegmentGroup.add(segment)
    AllSegmentQueue.put(segment)
    SegmentX = x
    SegmentY = y
    
CheeseX = random.randrange(0, 25) * 20
CheeseY = random.randrange(0, 25) * 20
CheeseSegment = Segment(CheeseX, CheeseY, green)
AllSegmentGroup.add(CheeseSegment)



#遊戲執行設定
while not done:  #重複執行直到按下X結束
    for event in pygame.event.get(): #抓取事件
        if event.type == pygame.QUIT: #如果按下結束則遊戲結束
            done = True #改變done
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                print("cheese")
            if event.key == pygame.K_UP:
                XChange = 0
                YChange = (SegmentHeight + SegmentGap) * -1
            if event.key == pygame.K_DOWN:
                XChange = 0
                YChange = SegmentHeight + SegmentGap
            if event.key == pygame.K_RIGHT:
                XChange = SegmentWidth + SegmentGap
                YChange = 0
            if event.key == pygame.K_LEFT:
                XChange = (SegmentWidth + SegmentGap) * -1
                YChange = 0
    screen.fill(black)
    
    
    
    SegmentX = SegmentX + XChange
    SegmentY = SegmentY + YChange
    segment = Segment(SegmentX, SegmentY, green)
    AllSegmentGroup.add(segment)
    AllSegmentQueue.put(segment)
    
    if SegmentX == CheeseX and SegmentY == CheeseY:
        AllSegmentGroup.remove(CheeseSegment)
        
        CheeseX = random.randrange(0, 25) * 20
        CheeseY = random.randrange(0, 25) * 20
        CheeseSegment = Segment(CheeseX, CheeseY, green)
        AllSegmentGroup.add(CheeseSegment)
        Yamada += 1
        pygame.display.set_caption(str(Yamada)) #ya motha
    
    else:
        LastQueue = AllSegmentQueue.get()
        AllSegmentGroup.remove(LastQueue)
    
    AllSegmentGroup.draw(screen)  
    pygame.display.flip() #畫面更新
    clock.tick(5) #畫面更新每秒60次

#遊戲結束
pygame.quit()