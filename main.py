import pygame
import random
pygame.init()
font1=pygame.font.SysFont(pygame.font.get_fonts()[2],30,True,False)
WIDTH,HEIGHT=800,500
global substitute,repeat
substitute={}
repeat=[]
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("hangman game")
def search(name,letter,underlines):
  if letter not in name:
    return False
  else:
    for i in range(len(name)):
      if letter==name[i]:
        if letter in substitute:
          repeat.append([letter,underlines[i]])
        else:
          substitute[letter]=underlines[i]     
    return True
class game():
  @staticmethod
  def gameloop(screen):
    exit=False
    FPS=60
    pos=0
    wordno=random.randint(1,9)
    buttons={"A":(0,3*HEIGHT/4),"B":(WIDTH/13,3*HEIGHT/4),"C":(2*WIDTH/13,3*HEIGHT/4),"D":(3*WIDTH/13,3*HEIGHT/4),'E':(4*WIDTH/13,3*HEIGHT/4),'F':(5*WIDTH/13,3*HEIGHT/4),'G':(6*WIDTH/13,3*HEIGHT/4),'H':(7*WIDTH/13,3*HEIGHT/4),'I':(8*WIDTH/13,3*HEIGHT/4),'J':(9*WIDTH/13,3*HEIGHT/4),'K':(10*WIDTH/13,3*HEIGHT/4),"L":(11*WIDTH/13,3*HEIGHT/4),"M":(12*WIDTH/13,3*HEIGHT/4),"N":(0,14*HEIGHT/16),'O':(WIDTH/13,14*HEIGHT/16),'P':(2*WIDTH/13,14*HEIGHT/16),'Q':(3*WIDTH/13,14*HEIGHT/16),'R':(4*WIDTH/13,14*HEIGHT/16),'S':(5*WIDTH/13,14*HEIGHT/16),'T':(6*WIDTH/13,14*HEIGHT/16),'U':(7*WIDTH/13,14*HEIGHT/16),'V':(8*WIDTH/13,14*HEIGHT/16),'W':(9*WIDTH/13,14*HEIGHT/16),'X':(10*WIDTH/13,14*HEIGHT/16),"Y":(11*WIDTH/13,14*HEIGHT/16),"Z":(12*WIDTH/13,14*HEIGHT/16)}
    words={1:"TIE",2:"DOCTOR",3:"BASKETBALL",4:"DEVELOPER",5:"TEST",6:"WRITE",7:"UNIVERSITY",8:"EDUCATION",9:"COMPUTER"}
    posx,posy=WIDTH/2.5,HEIGHT/1.4
    underlines={}
    for i in range(len(words[wordno])):
      underlines[i]=((posx,posy),(posx+30,posy))
      posx+=40
    posx=WIDTH/2.5
    clock=pygame.time.Clock()
    gameimages={0:pygame.image.load("files/hangman0.png"),1:pygame.image.load("files/hangman1.png"),2:pygame.image.load("files/hangman2.png"),3:pygame.image.load("files/hangman3.png"),4:pygame.image.load("files/hangman4.png"),5:pygame.image.load("files/hangman5.png"),6:pygame.image.load("files/hangman6.png")}
    while not(exit):
      screen.fill((255,255,255))
      if pos>=6:
        text=font1.render("GAME OVER",1,(0,0,0))
        screen.blit(text,(5*WIDTH/8,HEIGHT/2))
      elif len(repeat)+len(substitute)==len(words[wordno]):
        text=font1.render("CORRECT",1,(0,0,0))
        screen.blit(text,(5*WIDTH/8,HEIGHT/2))
      screen.blit(gameimages[pos],(WIDTH/4,HEIGHT/4))
      for i in underlines:
        pygame.draw.line(screen,(0,0,0),underlines[i][0],underlines[i][1],5)
        posx+=40
      for i in buttons:
        text=font1.render(i,1,(0,0,0))
        screen.blit(text,buttons[i])
        # pygame.draw.circle(screen,(0,0,0),[buttons[i][0]+15,buttons[i][1]+15],5)
      for event in pygame.event.get():
        if event.type==pygame.QUIT:
          exit=True
        elif event.type==pygame.KEYDOWN:
          if event.key==pygame.K_RETURN:
            repeat.clear()
            substitute.clear()
            game.gameloop(screen)
        elif event.type==pygame.MOUSEBUTTONDOWN:
          try:
            if ('A' in buttons) and buttons["A"][0]<=pygame.mouse.get_pos()[0]<=buttons["A"][0]+30 and buttons["A"][1]<=pygame.mouse.get_pos()[1]<=buttons["A"][1]+30:
              buttons.pop("A")
              wrong=search(words[wordno],'A',underlines)
              if not(wrong):
                pos+=1
            elif ('B' in buttons) and buttons["B"][0]<=pygame.mouse.get_pos()[0]<=buttons["B"][0]+30 and buttons["B"][1]<=pygame.mouse.get_pos()[1]<=buttons["B"][1]+30:
              buttons.pop("B")
              wrong=search(words[wordno],'B',underlines)
              if not(wrong):
                pos+=1
            elif ('C' in buttons) and buttons["C"][0]<=pygame.mouse.get_pos()[0]<=buttons["C"][0]+30 and buttons["C"][1]<=pygame.mouse.get_pos()[1]<=buttons["C"][1]+30:
              buttons.pop("C")
              wrong=search(words[wordno],'C',underlines)
              if not(wrong):
                pos+=1
            elif ('D' in buttons) and buttons["D"][0]<=pygame.mouse.get_pos()[0]<=buttons["D"][0]+30 and buttons["D"][1]<=pygame.mouse.get_pos()[1]<=buttons["D"][1]+30:
              buttons.pop("D")
              wrong=search(words[wordno],'D',underlines)
              if not(wrong):
                pos+=1
            elif ('E' in buttons) and buttons["E"][0]<=pygame.mouse.get_pos()[0]<=buttons["E"][0]+30 and buttons["E"][1]<=pygame.mouse.get_pos()[1]<=buttons["E"][1]+30:
              buttons.pop("E")
              wrong=search(words[wordno],'E',underlines)
              if not(wrong):
                pos+=1
            elif ('F' in buttons) and buttons["F"][0]<=pygame.mouse.get_pos()[0]<=buttons["F"][0]+30 and buttons["F"][1]<=pygame.mouse.get_pos()[1]<=buttons["F"][1]+30:
              buttons.pop("F")
              wrong=search(words[wordno],'F',underlines)
              if not(wrong):
                pos+=1
            elif ('G' in buttons) and buttons["G"][0]<=pygame.mouse.get_pos()[0]<=buttons["G"][0]+30 and buttons["G"][1]<=pygame.mouse.get_pos()[1]<=buttons["G"][1]+30:
              buttons.pop("G")
              wrong=search(words[wordno],'G',underlines)
              if not(wrong):
                pos+=1
            elif ('H' in buttons) and buttons["H"][0]<=pygame.mouse.get_pos()[0]<=buttons["H"][0]+30 and buttons["H"][1]<=pygame.mouse.get_pos()[1]<=buttons["H"][1]+30:
              buttons.pop("H")
              wrong=search(words[wordno],'H',underlines)
              if not(wrong):
                pos+=1
            elif ('I' in buttons) and buttons["I"][0]<=pygame.mouse.get_pos()[0]<=buttons["I"][0]+30 and buttons["I"][1]<=pygame.mouse.get_pos()[1]<=buttons["I"][1]+30:
              buttons.pop("I")
              wrong=search(words[wordno],'I',underlines)
              if not(wrong):
                pos+=1
            elif ('J' in buttons) and buttons["J"][0]<=pygame.mouse.get_pos()[0]<=buttons["J"][0]+30 and buttons["J"][1]<=pygame.mouse.get_pos()[1]<=buttons["J"][1]+30:
              buttons.pop("J")
              wrong=search(words[wordno],'J',underlines)
              if not(wrong):
                pos+=1
            elif ('K' in buttons) and buttons["K"][0]<=pygame.mouse.get_pos()[0]<=buttons["K"][0]+30 and buttons["K"][1]<=pygame.mouse.get_pos()[1]<=buttons["K"][1]+30:
              buttons.pop("K")
              wrong=search(words[wordno],'K',underlines)
              if not(wrong):
                pos+=1
            elif ('L' in buttons) and buttons["L"][0]<=pygame.mouse.get_pos()[0]<=buttons["L"][0]+30 and buttons["L"][1]<=pygame.mouse.get_pos()[1]<=buttons["L"][1]+30:
              buttons.pop("L")
              wrong=search(words[wordno],'L',underlines)
              if not(wrong):
                pos+=1
            elif ('M' in buttons) and buttons["M"][0]<=pygame.mouse.get_pos()[0]<=buttons["M"][0]+30 and buttons["M"][1]<=pygame.mouse.get_pos()[1]<=buttons["M"][1]+30:
              buttons.pop("M")
              wrong=search(words[wordno],'M',underlines)
              if not(wrong):
                pos+=1
            elif ('N' in buttons) and buttons["N"][0]<=pygame.mouse.get_pos()[0]<=buttons["N"][0]+30 and buttons["N"][1]<=pygame.mouse.get_pos()[1]<=buttons["N"][1]+30:
              buttons.pop("N")
              wrong=search(words[wordno],'N',underlines)
              if not(wrong):
                pos+=1
            elif ('O' in buttons) and buttons["O"][0]<=pygame.mouse.get_pos()[0]<=buttons["O"][0]+30 and buttons["O"][1]<=pygame.mouse.get_pos()[1]<=buttons["O"][1]+30:
              buttons.pop("O")
              wrong=search(words[wordno],'O',underlines)
              if not(wrong):
                pos+=1
            elif ('P' in buttons) and buttons["P"][0]<=pygame.mouse.get_pos()[0]<=buttons["P"][0]+30 and buttons["P"][1]<=pygame.mouse.get_pos()[1]<=buttons["P"][1]+30:
              buttons.pop("P")
              wrong=search(words[wordno],'P',underlines)
              if not(wrong):
                pos+=1
            elif ('Q' in buttons) and buttons["Q"][0]<=pygame.mouse.get_pos()[0]<=buttons["Q"][0]+30 and buttons["Q"][1]<=pygame.mouse.get_pos()[1]<=buttons["Q"][1]+30:
              buttons.pop("Q")
              wrong=search(words[wordno],'Q',underlines)
              if not(wrong):
                pos+=1
            elif ('R' in buttons) and buttons["R"][0]<=pygame.mouse.get_pos()[0]<=buttons["R"][0]+30 and buttons["R"][1]<=pygame.mouse.get_pos()[1]<=buttons["R"][1]+30:
              buttons.pop("R")
              wrong=search(words[wordno],'R',underlines)
              if not(wrong):
                pos+=1
            elif ('S' in buttons) and buttons["S"][0]<=pygame.mouse.get_pos()[0]<=buttons["S"][0]+30 and buttons["S"][1]<=pygame.mouse.get_pos()[1]<=buttons["S"][1]+30:
              buttons.pop("S")
              wrong=search(words[wordno],'S',underlines)
              if not(wrong):
                pos+=1
            elif ('T' in buttons) and buttons["T"][0]<=pygame.mouse.get_pos()[0]<=buttons["T"][0]+30 and buttons["T"][1]<=pygame.mouse.get_pos()[1]<=buttons["T"][1]+30:
              buttons.pop("T")
              wrong=search(words[wordno],'T',underlines)
              if not(wrong):
                pos+=1
            elif ('U' in buttons) and buttons["U"][0]<=pygame.mouse.get_pos()[0]<=buttons["U"][0]+30 and buttons["U"][1]<=pygame.mouse.get_pos()[1]<=buttons["U"][1]+30:
              buttons.pop("U")
              wrong=search(words[wordno],'U',underlines)
              if not(wrong):
                pos+=1
            elif ('V' in buttons) and buttons["V"][0]<=pygame.mouse.get_pos()[0]<=buttons["V"][0]+30 and buttons["V"][1]<=pygame.mouse.get_pos()[1]<=buttons["V"][1]+30:
              buttons.pop("V")
              wrong=search(words[wordno],'V',underlines)
              if not(wrong):
                pos+=1
            elif ('W' in buttons) and buttons["W"][0]<=pygame.mouse.get_pos()[0]<=buttons["W"][0]+30 and buttons["W"][1]<=pygame.mouse.get_pos()[1]<=buttons["W"][1]+30:
              buttons.pop("W")
              wrong=search(words[wordno],'W',underlines)
              if not(wrong):
                pos+=1
            elif ('X' in buttons) and buttons["X"][0]<=pygame.mouse.get_pos()[0]<=buttons["X"][0]+30 and buttons["X"][1]<=pygame.mouse.get_pos()[1]<=buttons["X"][1]+30:
              buttons.pop("X")
              wrong=search(words[wordno],'X',underlines)
              if not(wrong):
                pos+=1
            elif ('Y' in buttons) and buttons["Y"][0]<=pygame.mouse.get_pos()[0]<=buttons["Y"][0]+30 and buttons["Y"][1]<=pygame.mouse.get_pos()[1]<=buttons["Y"][1]+30:
              buttons.pop("Y")
              wrong=search(words[wordno],'Y',underlines)
              if not(wrong):
                pos+=1
            elif ('Z' in buttons) and buttons["Z"][0]<=pygame.mouse.get_pos()[0]<=buttons["Z"][0]+30 and buttons["Z"][1]<=pygame.mouse.get_pos()[1]<=buttons["Z"][1]+30:
              buttons.pop("Z")
              wrong=search(words[wordno],'Z',underlines)
              if not(wrong):
                pos+=1
          except:
            pass
      for i in substitute:
        text=font1.render(i,1,(0,0,0))
        screen.blit(text,(substitute[i][0][0],substitute[i][0][1]-30))
      for i in repeat:
        text=font1.render(i[0],1,(0,0,0))
        screen.blit(text,(i[1][0][0],i[1][0][1]-30))
      pygame.display.update()
      posx=WIDTH/2.5
      # clock.tick(FPS)
    pygame.quit()
game.gameloop(screen)
