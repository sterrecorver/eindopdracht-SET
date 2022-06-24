import pygame
import random

class Kaarten:
    def __init__(self,kleur,vorm,vulling,aantal): #eigenschappen aan kaarten toekennen
        self.kleur=kleur
        self.vorm=vorm
        self.vulling=vulling
        self.aantal=aantal
        

kleur=['green','purple','red'] #mogelijke kleuren 
vorm=['diamond','oval','squiggle'] #mogelijke vormen
vulling=['empty', 'filled', 'shaded'] #mogelijke vorminkleuring
aantal=['1','2','3'] #mogelijk aantal
    

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

def sets_in_spel_vinden(kaarten_gebruikt): #bekijkt voor de 12 kaarten op het scherm of er een set is tussen 3 kaarten
    sets_gevonden=[]            
    for i in kaarten_gebruikt:
        for j in kaarten_gebruikt:
            for r in kaarten_gebruikt:
                if i != j and j != r and r != i:
                    if set_of_niet(i, j, r):
                        sets_gevonden.append([i,j,r])               
    return sets_gevonden
  
def main(stapel):
    
    pygame.init()
    menu = True
    
    while menu:
        
        scherm=pygame.display.set_mode((800,600)) #schermopmaak instellen
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
        
    scherm.fill((69,139,0))
    pygame.draw.rect(scherm, (255 , 255 , 255), [220, 540, 400, 60])
    kaarten_gebruikt=[]
    
    for i in range(4): #het toevoegen van 4 random kaartel  uit de  stapel aan de eerste rij
        kaarten_in_veld = random.choice(stapel)
        kaarten_gebruikt.append(kaarten_in_veld)
        stapel.remove(kaarten_in_veld)
        kaarten_in_veld = pygame.image.load('kaarten/'+kaarten_in_veld.kleur+kaarten_in_veld.vorm+kaarten_in_veld.vulling+kaarten_in_veld.aantal+'.gif')
        kaarten_in_veld = pygame.transform.scale(kaarten_in_veld, (120,100))
        scherm.blit(kaarten_in_veld, (130 + 140 * i,100 ))
        
    
    for i in range(4): #het toevoegen van 4 random kaartel  uit de  stapel aan de tweede rij
        kaarten_in_veld=random.choice(stapel)
        kaarten_gebruikt.append(kaarten_in_veld)
        stapel.remove(kaarten_in_veld)
        kaarten_in_veld = pygame.image.load('kaarten/'+kaarten_in_veld.kleur+kaarten_in_veld.vorm+kaarten_in_veld.vulling+kaarten_in_veld.aantal+'.gif')
        kaarten_in_veld = pygame.transform.scale(kaarten_in_veld, (120,100))
        scherm.blit(kaarten_in_veld, (130 + 140 * i,220 ))
       
    
    for i in range(4): #het toevoegen van 4 random kaartel  uit de  stapel aan de derde rij
        kaarten_in_veld=random.choice(stapel)
        kaarten_gebruikt.append(kaarten_in_veld)
        stapel.remove(kaarten_in_veld)
        kaarten_in_veld = pygame.image.load('kaarten/'+kaarten_in_veld.kleur+kaarten_in_veld.vorm+kaarten_in_veld.vulling+kaarten_in_veld.aantal+'.gif')
        kaarten_in_veld = pygame.transform.scale(kaarten_in_veld, (120,100))
        scherm.blit(kaarten_in_veld, (130 + 140 * i,340 ))
        
    print(sets_in_spel_vinden(kaarten_gebruikt))
    for i in range(len(sets_in_spel_vinden(kaarten_gebruikt))):
        print(sets_in_spel_vinden(kaarten_gebruikt)[i])
    print(len(sets_in_spel_vinden(kaarten_gebruikt)))
    lst = []
    lst_1 = []
    
    
    while spel:
        
        pygame.display.flip()
        for event in pygame.event.get():
            
            if event.type==pygame.QUIT:
                pygame.quit()
                spel = False
            if event.type == pygame.KEYDOWN:
                #geeft aan wat er moet gebeuren als er enter wordt gedrukt op het toetsenbord
                if event.key == pygame.K_RETURN:
                    for i in lst:
                        if len(lst_1) < len(lst) - 2:
                            lst_1.extend(i.split())
                            #in deze waslijst aan if statements wordt er gekeken naar van welke vorm de input is en daardoor wordt er de juiste cijfers bij gekozen
                    if len(lst_1) == 6:
                        input_1 = int(''.join(lst_1[0:2]))
                        input_2 = int(''.join(lst_1[2:4]))
                        input_3 = int(''.join(lst_1[4:6]))
                    elif len(lst_1) == 5 and lst[1] == ' ':
                        input_1 = int(''.join(lst_1[0:1]))
                        input_2 = int(''.join(lst_1[1:3]))
                        input_3 = int(''.join(lst_1[3:5]))
                    elif len(lst_1) == 5 and lst[4] == ' ':
                        input_1 = int(''.join(lst_1[0:2]))
                        input_2 = int(''.join(lst_1[2:3]))
                        input_3 = int(''.join(lst_1[3:5]))
                    elif len(lst_1) == 5 and lst[5] == ' ':
                        input_1 = int(''.join(lst_1[0:2]))
                        input_2 = int(''.join(lst_1[2:4]))
                        input_3 = int(''.join(lst_1[4:5]))
                    elif len(lst_1) == 4 and lst[2] == ' ':
                        input_1 = int(''.join(lst_1[0:2]))
                        input_2 = int(''.join(lst_1[2]))
                        input_3 = int(''.join(lst_1[3]))
                    elif len(lst_1) == 4 and lst[1] == ' ' and lst[4] == ' ':
                        input_1 = int(''.join(lst_1[0]))
                        input_2 = int(''.join(lst_1[1:3]))
                        input_3 = int(''.join(lst_1[3]))
                    elif len(lst_1) == 4 and lst[3] == ' ':
                        input_1 = int(''.join(lst_1[0]))
                        input_2 = int(''.join(lst_1[1]))
                        input_3 = int(''.join(lst_1[2:4]))
                    else:
                        input_1 = int(''.join(lst_1[0]))
                        input_2 = int(''.join(lst_1[1]))
                        input_3 = int(''.join(lst_1[2]))
                    #deze variabele poging geeft een lijst die van dezelfde vorm is van de gevonden sets door de computer    
                    poging = [ kaarten_gebruikt[input_1-1] , kaarten_gebruikt[input_2-1] , kaarten_gebruikt[input_3-1]]
                    #hier wordt gecontroleerd of de poging juist is vergeleken met de gevonden sets met de computer
                    if len(sets_in_spel_vinden(kaarten_gebruikt)) > 0 :
                        for i in range(len(sets_in_spel_vinden(kaarten_gebruikt))):
                            if poging == sets_in_spel_vinden(kaarten_gebruikt)[i]: #resultata bij invullen van een goede set
                                scherm.fill((255,200,0))    #geeft een leuke pop-up aangezien we niet verder kwamen na 1 gevonden set
                                pygame.draw.rect(scherm, (255 , 255 , 255), [270, 40, 255, 90])
                                scherm.blit(font.render('Je hebt SET!' , True, (255, 200 , 0 )), (350,70))
                                pygame.display.flip()
                            else: #resultaat  van het invullen van een onjuiste  set
                                scherm.fill((0,0,0))    #geeft een leuke pop-up aangezien we niet verder kwamen na 1 gevonden set
                                pygame.draw.rect(scherm, (255 , 255 , 255), [270, 40, 255, 90])
                                scherm.blit(font.render('Game over' , True, (255, 200 , 0 )), (350,70))
                                pygame.display.flip()      
                           
                    else: # als er geen set is gevonden door de computer stopt het spel en ben je game over, variant omdat we niet verder kwamen 
                        scherm.fill((255, 0 ,0))
                        pygame.draw.rect(scherm, (255 , 255 , 255), [270, 40, 255, 90])
                        scherm.blit(font.render('Game over' , True, (255, 0 , 0 )), (350,70))
                        pygame.display.flip()
                            
                # zorgt ervoor dat je getypte dingen kan verwijderen       
                elif event.key == pygame.K_BACKSPACE and len(lst) > 0:
                    lst.pop()
                    
                else:
                    letter = event.unicode
                    if letter.isdigit() ==  True or letter == ' ':
                        if len(lst) < 9:
                            lst.append(letter)
                        else: 
                            None
                pygame.draw.rect(scherm, (255 , 255 , 255), [220, 540, 400, 60])
                scherm.blit(font.render(''.join(lst) , True, (255, 0 , 0 )), (320,550))
                pygame.display.update()
        
    pygame.quit()
main(stapel)

    