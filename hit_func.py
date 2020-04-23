import random
from stats import Player_stats

def hit_rate():
     
    Attack_rand = (random.randint(1,100))
    Attack_mod = (Player_stats ['accuracy'])
    numb = (Attack_rand + Attack_mod)

    if numb >= 90:
        Critical_Hit = True
        print (numb,"CRITICAL HIT!")
    elif numb >= 50:
        Hit = True
        print (numb,"HIT!")
    elif numb >= 30:
        Parry = True
        print (numb,"Parry...")
    elif numb <= 29:
        Miss = True
        print (numb,"miss...")
    
hit_rate()