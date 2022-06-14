import pygame

class Kaarten:
    
    def __init__(self,kleur,vorm,vulling,aantal):
        self.kleur=kleur
        self.vorm=vorm
        self.vulling=vulling
        self.aantal=aantal
        
        kleur=['rood','groen','paars']
        vulling=['solide', 'gestreept', 'open']
        vorm=['diamand','squiggle','oval']
        aantal=['1','2','3']
        
kaarten.set = pygame.image.load('/Users/sterrecorver/Documents/Kaarten') 





		