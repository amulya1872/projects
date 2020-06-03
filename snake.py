import pygame
import time
import random
pygame.init()
wid,hei=800,600
screen=pygame.display.set_mode((wid,hei))
pygame.display.set_caption("snake")
white=(255,255,255)
blue=(0,0,255)
red=(255,0,0)
black=(0,0,0)
yellow=(255,255,102)
green=(0,255,0)

x1=wid/2
y1=hei/2
x2=0
y2=0
snake_block=10
snake_speed=10
clock=pygame.time.Clock()
font_style=pygame.font.SysFont("bahanschrift",25)
score_font=pygame.font.SysFont("comicsanms",35)

def yscore(score):
	value=score_font.render("Your score : "+str(score),True,yellow)
	screen.blit(value,[0,0])

def our_snake(snake_block,snake_list):
	for x in snake_list:
		pygame.draw.rect(screen,black,[x[0],x[1],10,10])


def message(msg,color):
	mesg=font_style.render(msg,True,color)
	screen.blit(mesg,[wid/6,hei/3])
def gameloop():
	gameover=False
	gameclose=False
	x1=wid/2
	y1=hei/2
	x2=0
	y2=0
	snake_list=[]
	lengthofsnake=1
	foodx=round(random.randrange(0,wid-snake_block)/10.0)*10.0
	foody=round(random.randrange(0,hei-snake_block)/10.0)*10.0

	while not gameover:
		while gameclose==True:
			screen.fill(blue)
			message("You Lost! press Q-Quit or C-play Again",red)
			pygame.display.update()
			for event in pygame.event.get():
				if event.type==pygame.KEYDOWN:
					if event.key==pygame.K_q:
						gameover=True
						gameclose=False
					if event.key==pygame.K_c:
						gameloop()

		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				gameover=True
			if event.type==pygame.KEYDOWN:
				if event.key==pygame.K_LEFT:
					x2=-10
					y2=0
				elif event.key==pygame.K_RIGHT:
					x2=10
					y2=0
				elif event.key==pygame.K_UP:
					x2=0
					y2=-10
				elif event.key==pygame.K_DOWN:
					x2=0
					y2=10
		if x1>=wid or x1<0 or y1>=hei or y1<0:
			gameclose=True
		x1+=x2
		y1+=y2

		screen.fill(blue)

		pygame.draw.rect(screen,green,[foodx,foody,10,10])
		snake_head=[]
		snake_head.append(x1)
		snake_head.append(y1)
		snake_list.append(snake_head)
		if len(snake_list) > lengthofsnake:
			del snake_list[0]

		for x in snake_list[:-1]:
			if x==snake_head:
				gameclose=True

		our_snake(10,snake_list)
		yscore(lengthofsnake-1)

		pygame.display.update()
		if x1==foodx and y1==foody:
			foodx=round(random.randrange(0,wid-snake_block)/10.0)*10.0
			foody=round(random.randrange(0,hei-snake_block)/10.0)*10.0
			lengthofsnake+=1
		clock.tick(snake_speed)



	pygame.quit()
	quit()
gameloop()