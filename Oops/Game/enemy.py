class Enemy:
#class Enemy(object):
    def __init__(self,name="enemy",hit_points=0,lives=1):
        self.name=name
        self.hit_points=hit_points
        self.lives=lives
    
    # we make an take_damage method 
    def take_damage(self,damage):
        remaining_points = self.hit_points-damage # remaining points after being hit = hit_points-damage
        if remaining_points>=0:
            self.hit_points=remaining_points
            print("I took {} points damage and have left".format(damage,self.hit_points))
        else:
            self.lives-=1 # if current_points=0 then reduce life by 1
        
    def __str__(self):
        return "None {0.name}, Lives: {0.lives}, Hit Points: {0.hit_points}".format(self)
    
class Troll(Enemy):
    pass
            
        
        
