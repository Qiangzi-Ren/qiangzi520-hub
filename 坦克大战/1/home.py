# coding: utf-8

import pygame


# 大本营类
class Home(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.homes = ['/home/renziqiang/文档/matlab/坦克大战/1/═╝╞¼/home/home1.png', '/home/renziqiang/文档/matlab/坦克大战/1/═╝╞¼/home/home2.png', '/home/renziqiang/文档/matlab/坦克大战/1/═╝╞¼/home/home_destroyed.png']
		self.home = pygame.image.load(self.homes[0])
		self.rect = self.home.get_rect()
		self.rect.left, self.rect.top = (3 + 12 * 24, 3 + 24 * 24)
		self.alive = True
	# 大本营置为摧毁状态
	def set_dead(self):
		self.home = pygame.image.load(self.homes[-1])
		self.alive = False