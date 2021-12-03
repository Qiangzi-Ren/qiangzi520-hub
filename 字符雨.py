import pygame
import sys
import random

pygame.init()

resolution = width,height = 1200,800 #设置窗口大小和标题
windowSurface = pygame.display.set_mode(resolution) #设置分辨率并得到全局的【绘图表面】
pygame.display.set_caption("字符雨")#设置标题

bgSurface = pygame.Surface((width, height), flags=pygame.SRCALPHA)
pygame.Surface.convert(bgSurface)
bgSurface.fill(pygame.Color(0, 0, 0, 35))

# 创建时钟对象
clock = pygame.time.Clock()

if __name__ == '__main__':
    # 创建字符雨
    str1 = "01abcdefghijklmnopqurstuvwxyz"
    str1 = "朋友一生一起走,我一生一起走"
    letter = list(str1)
    font = pygame.font.Font("/home/renziqiang/下载/YaHeiConsolas.ttf", 14)
    texts = [
        font.render(str(letter[i]), True, (0, 255, 0)) for i in range(14)
    ]

    column = int(width/15)
    drops = [0 for i in range(column)]

    while True:
        # 处理用户输入
        for event in pygame.event.get():
            # 处理退出事件
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        windowSurface.blit(bgSurface, (0, 0))
        #绘制结束,刷新界面
        for i in range(len(drops)):
            text = random.choice(texts)

            windowSurface.blit(text, (i*15, drops[i]*15))

            drops[i] += 1
            if drops[i]*10 > height  or random.random() > 0.9 :
                drops[i] = 0
        pygame.display.flip()
        #  始终停留一帧的时长
        clock.tick(20)