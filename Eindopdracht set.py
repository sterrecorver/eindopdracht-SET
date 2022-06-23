import pygame
import random
import timer
import time
from random import sample

class Kaarten:
    def __init__(self,kleur,vorm,vulling,aantal): #eigenschappen aan kaarten toekennen
        self.kleur=kleur
        self.vorm=vorm
        self.vulling=vulling
        self.aantal=aantal
        

kleur=['green','purple','red'] #mogelijke kleuren 
vorm=['diamond','oval','squiggle'] #mogelijke vormen
vulling=['empty', 'filled', 'shaded'] #mogelijke vorminkleuring
aantal=['1','2','3']
    
#kunnen we er iet beter een definitie van maken, zodat het de stapel teruggeefd?- vraag Lois
stapel = [] #het aanmaken van een stapel kaarten, met alle mogelijke combinaties van eigenschappen
for kleur in ['green','purple','red']:
    for vorm in ['diamond','oval','squiggle']:
        for vulling in ['empty', 'filled', 'shaded']:
            for aantal in ['1','2','3']:
                kaarten_toevoegen = Kaarten(kleur, vorm, vulling, aantal)
                stapel.append(kaarten_toevoegen)
                pygame.image.load('kaarten/'+kleur+vorm+vulling+aantal+'.gif')     
                geschudde_stapel=random.shuffle(stapel)
            
def gelijk_of_ongelijk(k1,k2,k3): #kijken wanneer 3 gelijk zijn of juist niet
    if k1 == k2 and k2 == k3:
        return True
    elif k1 != k2 and k2 != k3 and k3 != k1:
        return True
    else:
        return False
    
def set_of_niet(kaart_1,kaart_2,kaart_3): #controle of 3 kaarten een set vormen
    controle_vorm = gelijk_of_ongelijk(kaart_1.vorm, kaart_2.vorm, kaart_3.vorm)
    controle_kleur = gelijk_of_ongelijk(kaart_1.kleur, kaart_2.kleur, kaart_3.kleur)
    controle_vulling = gelijk_of_ongelijk(kaart_1.vulling, kaart_2.vulling, kaart_3.vulling)
    controle_aantal = gelijk_of_ongelijk(kaart_1.aantal, kaart_2.aantal, kaart_3.aantal)
    return controle_kleur and controle_vorm and controle_vulling and controle_aantal

def sets_in_spel_vinden(stapel): #neemt random 12 kaarten uit de stapel en bekijkt of er een set is tussen 3 kaarten
    sets_gevonden=[]            
    for i,ki in enumerate(sample(geschudde_stapel,12)):
        for j,kj in enumerate(sample(geschudde_stapel[i+1:],12),i+1):
            for r,kr in enumerate(sample(geschudde_stapel[j+1:],12),j+1):
                if set_of_niet(ki, kj, kr):
                    sets_gevonden.append((i,j,r))
                    if len(sets_gevonden)==1:
                        continue #zoja, dan voegen we die toe aan een lijst met 
                                                  #mogelijkheden voor sets onder de 12 kaarten   
    return sets_gevonden
  
def main(geschudde_stapel):
    
    pygame.init()
    menu = True
    
    while menu:
        #x,y = pygame.mouse.get_pos()
        #print(muis)
        
        scherm=pygame.display.set_mode((800,600)) #schermopmaak
        pygame.display.set_caption("SETS")
        font = pygame.font.SysFont('Arial', 25)
        scherm.fill((0, 255, 180))
        pygame.draw.rect(scherm, (255 , 255 , 255), [270, 40, 255, 90])
        scherm.blit(font.render('Get started!' , True, (255, 0 , 0 )), (350,70))
        pygame.display.update()
        
        for event in pygame.event.get():
            x,y=pygame.mouse.get_pos()
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 525 > x > 270 and 125 > y > 40:
                    menu=False
                    spel=True
                    pygame.display.update()
        
        
    # spel = True
    # while spel:
    #     scherm.fill((0,0,0))
        
    #     for event in pygame.event.get():
    #         if event.type==pygame.QUIT:
    #             pygame.quit()
    #             quit()
                
    #     for event in pygame.event.get():
    #         kaarten_gebruikt=[]    
    #         for i in range(13):
    #             kaarten_in_veld=random.choice(stapel)
    #             kaarten_gebruikt.append(kaarten_in_veld)
    #             kaarten_in_veld = pygame.image.load('kaarten/'+kleur+vorm+vulling+aantal+'.gif')
    #             kaarten_in_veld = pygame.transform.scale(kaarten_in_veld, (50,30))
                
                
                #twaalf random kaarten uit deck geplaatst op het scherm 
        #timer, als tijd voorbij, dan computer set vinden of indien geen set, 3 kaarten weg en drie nieuwe erbij. 
        #score
        #stop knop
        
    pygame.quit()
main(stapel)

    
     #stap voor stap bedenken wat erin moet en op welke volgorde dat moet gebeuren   
    
    
    

#Ideën voor het spel: Startscherm met optie knop starten en banner spel. 
                     #Spel start met 12 kaarten op het scherm. Opties voor kaarten aanvullen, timer en stopknop
                     #Spel geeft terug of het aangeklikte een set is of niet. Dus kaarten moeten aangekklikt kunnen worden. 
                     #Indien set, haal kaarten uit veld en voeg random 3 nieuwe toe.
                     #Indien geen sets in het veld, voeg 3 extra kaarten toe aan het veld.