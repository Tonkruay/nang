class Mybot:
    x = 2
    y = 3
    
    def sum(self):
        return self.x + self.y
    
    def setvar(self,x,y):
        self.x = x
        self.y = y

bot1 = Mybot()
bot2 = Mybot()
bot2.setvar(3,4)
print(bot2.sum())
print(bot1.x)
print(bot2.x)
#print
#print(bot1.sum(2,3))
