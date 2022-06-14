import pygame

class Kaarten:
    
    def __init__(self,kleur,vorm,vulling,aantal):
        self.kleur=kleur
        self.vorm=vorm
        self.vulling=vulling
        self.aantal=aantal
            
        kleur=['green','purple','red']
        vorm=['diamond','oval','squiggle']
        vulling=['empty', 'filled', 'shaded']
        aantal=['1','2','3']
    
    
for kleur in ['green','purple','red']:
    for vorm in ['diamond','oval','squiggle']:
        for vulling in ['empty', 'filled', 'shaded']:
            for aantal in ['1','2','3']:
                pygame.image.load('/Users/sterrecorver/Documents/Kaarten/'+kleur+vorm+vulling+aantal+'.gif')
        
        
        





		