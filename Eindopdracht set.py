import pygame
import random
import timer
import time

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
    for i,ki in random.sample(stapel,12):
        for j,kj in random.sample(stapel[i+1:],12):
            for r,kr in random.sample(stapel[j+1:],12):
                if set_of_niet(ki, kj, kr):
                    sets_gevonden.append((i,j,r)) #zoja, dan voegen we die toe aan een lijst met 
                                                  #mogelijkheden voor sets onder de 12 kaarten   
    return sets_gevonden


    
def main(stapel):
    pygame.init()
    
    
    menu=True
    while menu:
        scherm=pygame.display.set_mode((800,600)) #schermopmaak
        muis=pygame.mouse.get_pos()
        scherm.fill((255, 255, 255))
        pygame.display.set_caption("SETS")
        #pygame print een startrechthoek, als in de buurt geklikt, dan starten spel
        start_knop=pygame.font.SysFont("arial",30).render("Start game", True, (255,105,180))
        start_knop_rect=start_knop.get_rect()
        start_knop_rect.center=(400,300)
        for event in pygame.event.get():
            if event.type==pygame.MOUSEBUTTONDOWN:
                if 340 <= muis[0] <= 460 and 270 <= muis[1] <= 330:
                    menu=False
                    spel=True
    pygame.quit()
main(stapel)

    
     #stap voor stap bedenken wat erin moet en op welke volgorde dat moet gebeuren   
    
    
    

#Ideën voor het spel: Startscherm met optie knop starten en banner spel. 
                     #Spel start met 12 kaarten op het scherm. Opties voor kaarten aanvullen, timer en stopknop
                     #Spel geeft terug of het aangeklikte een set is of niet. Dus kaarten moeten aangekklikt kunnen worden. 
                     #Indien set, haal kaarten uit veld en voeg random 3 nieuwe toe.
                     #Indien geen sets in het veld, voeg 3 extra kaarten toe aan het veld.