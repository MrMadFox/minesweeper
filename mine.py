import random
clicks=0
class block:

    def __init__(self, x):
        self.position=x
        self.opened = 0
        self.bomb = 0
    def update(self):
        global clicks
        if self.opened==0:
            pygame.draw.rect(s,(255,0,0),(((self.position)%n)*50,((self.position)//n)*50,50,50))
            pygame.draw.rect(s, (0, 0, 0), (((self.position) % n) * 50, ((self.position) // n) * 50, 50, 50),2)
        else:
            pygame.draw.rect(s, (0, 255, 0), (((self.position) % n) * 50, ((self.position) // n) * 50, 50, 50))
            pygame.draw.rect(s, (0, 0, 0), (((self.position) % n) * 50, ((self.position) // n) * 50, 50, 50), 2)
            distext=0
            if self.bomb==-1:
                distext=-1
                print("game over u lost")
                pygame.quit()
                quit()
            else:
                to_check=[]
                lb,rb,ub,db=0,0,0,0
                if (self.position+1)//n ==(self.position)//n:
                    to_check.append(self.position+1)
                    rb=1
                if (self.position - 1) // n == (self.position) // n:
                    to_check.append(self.position - 1)
                    lb=1
                if (self.position -n)>=0:
                    to_check.append(self.position -n)
                    ub=1
                if (self.position +n)<n*n:
                    to_check.append(self.position +n)
                    db=1
                if ub and rb:
                    to_check.append(self.position-n+1)
                if ub and lb:
                    to_check.append(self.position-n-1)
                if db and rb:
                    to_check.append(self.position+n+1)
                if db and lb:
                    to_check.append(self.position+n-1)

                for j in to_check:
                    if l[j].bomb==-1:
                        distext=distext+1
            if distext!=-1:
                clicks=clicks+1
                if clicks==n*n-number_of_bombs:
                    print("game over u won")
                    pygame.quit()
                    quit()

            texts=text.render(str(distext),True,(0,0,0))
            s.blit(texts,(((self.position)%n)*50+10,((self.position)//n)*50))

n=int(input())
number_of_bombs=int(input())
import pygame
pygame.init()
pygame.font.init()
s=pygame.display.set_mode((n*50,n*50))
s.fill((0,0,0))
pygame.display.update()
text=pygame.font.SysFont('Comic Sans MS', 30)
l=[]
for j in range(n**2):
    l.append(block(j))
def updateall():
    for j in l:
        j.update()
    pygame.display.update()
updateall()
if n*n>number_of_bombs:
    bomblist=random.sample(range(0, n*n), number_of_bombs)
    for jj in bomblist:
        l[jj].bomb=-1
else:
    l[0].bomb=-1
while(1):
    for i in pygame.event.get():
        if i.type==12:
            pygame.quit()
            quit()
        if i.type==pygame.MOUSEBUTTONDOWN:
            if i.button==1:
                x,y=i.pos
                x=x//50
                y=y//50
                mousepos=y*n+x
                if l[mousepos].opened==0:
                    l[mousepos].opened=1
                    l[mousepos].update()
                    pygame.display.update()
            elif i.button==3:
                x,y=i.pos
                x=(x//50)*50
                y=(y//50)*50
                texts = text.render("FL", True, (0, 0, 0))
                s.blit(texts, (x+10,y) )
                pygame.display.update()
