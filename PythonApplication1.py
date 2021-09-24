class card:
    cost=0
    name=" "
    description1=" "
    description2=" "
    def __init__(self,cost,name,description1,description2):
        self.cost=cost
        self.name=name
        self.description1=description1
        self.description2=description2
     


class minion(card):
    tier=0
    attack=0
    health=0
    sort=" "
    def __init__(self,tier,name,description1,description2,attack,health,sort):
        super().__init__(0,name,description1,description2)
        self.attack=attack
        self.health=health
        self.tier=tier
        self.sort=sort
    def _print_(self):
        print(" _________________________")
        print("|                         |")
        x=((24-len(self.name))/2)-1;
        print("|",end=' ')
        while x>0:
             print(" ",end='')
             x=x-1
        print(self.name,end=' ')
        x=((24-len(self.name))/2)-1;
        if len(self.name)%2==0:
            x=x+1
        while x>0:
             print(" ",end='')
             x=x-1
        print("|")
        print("|                         |")
        print("|                         |")
        print("|                         |")
        print("|                         |")
        print("|                         |")
        print("|                         |")
        print("|                         |")
        x=((24-len(self.description1))/2)-1;
        print("|",end=' ')
        while x>0:
             print(" ",end='')
             x=x-1
        print(self.description1,end=' ')
        x=((24-len(self.description1))/2)-1;
        if len(self.description1)%2==0:
            x=x+1
        while x>0:
             print(" ",end='')
             x=x-1
        print("|")
        x=((24-len(self.description2))/2)-1;
        print("|",end=' ')
        while x>0:
             print(" ",end='')
             x=x-1
        print(self.description2,end=' ')
        x=((24-len(self.description2))/2)-1;
        if len(self.description2)%2==0:
            x=x+1
        while x>0:
             print(" ",end='')
             x=x-1
        print("|")
        print("|                         |")
        print("|                         |")
        print("|                         |")
        x=((24-len(self.sort))/2)-1;
        print("|",end=' ')
        while x>0:
             print(" ",end='')
             x=x-1
        print(self.sort,end=' ')
        x=((24-len(self.sort))/2)-1;
        if len(self.sort)%2==0:
            x=x+1
        while x>0:
             print(" ",end='')
             x=x-1
        print("|                         |")
        print(self.attack,"_______________________",self.health)

class hero(minion):
    gold=0
    hand=[]
    placement=0
    tag=" "

class spell(card):
    pass

class secret(spell):
    condition=True

#global players
#global turn
#global pool
#global timer

#tidecaller
tidecaller=minion(1,"Murloc tidecaller","Whenever you summon a", "Murloc, gain +1 Attack",1,2,"Murloc")
tidecaller._print_()
print("hello world",end=' ')
print("hello world")