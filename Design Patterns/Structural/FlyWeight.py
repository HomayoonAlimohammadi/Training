class BulletContext:
    def __init__(self, x, y, z, velocity):
        self.x = x
        self.y = y
        self.z = z
        self.velocity = velocity
        

class BulletFlyweight:
    def __init__(self):
        self.asset = '■■►'
        self.bullets = []
        
    def bullet_factory(self, x, y, z, velocity):
        bull = [b for b in self.bullets if b.x==x and b.y==y and b.z==z and b.velocity==velocity]
        if not bull:
            bull = BulletContext(x,y,z,velocity)
            self.bullets.append(bull)
        else:
            bull = bull[0]
            
        return bull
        
    def print_bullets(self):
        print('Bullets:')
        for bullet in self.bullets:
            print(str(bullet.x)+' '+str(bullet.y)+' '+str(bullet.z)+' '+str(bullet.velocity))


bf = BulletFlyweight()
bf.bullet_factory(1,1,1,10)
bf.bullet_factory(3,2,1,20)
bf.bullet_factory(1,1,1,10)
bf.print_bullets()
