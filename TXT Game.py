import random
bow = 4
arrow = 10
sword = 7
heal = 5
health = 100
defense = 15
gold = 100
kidhlp = 0


play = int(input("Type 1 if you wanna play \n type 2 if you dont.: "))
if play == 2:
    print("too bad")
    name = input("What is your name:    ")
    print("ok", name, "your gonna have to play this game till you beat it, break it, or die. \n Have fun")
elif play == 1:

    name = input("What is your name:    ")
    print("ok", name, "your gonna have to play this game till you beat it, break it, or die. \n Have fun")
else:
    print("That wasnt one of the options")
if name == "god" or name == "God":
    print("You have max stats\n")
    bow += 2000
    arrow += 200
    sword += 20000
    heal += 2000
    health += 2000
    defense += 2000
    gold += 2000


area1 = 0
c1l = True
while c1l:
    c1 = int(input(" What do you wanna do\n Show items (1) \nMove to a new location (2)\n*******************\n: "))
    if c1 == 1:
        
        print("You have", gold , "Gold, You have a bow that deals",bow,"damage\nYou have a sword that deals",sword,"damage\n You have", arrow, "arrows\n You have" ,heal,"healing potions\n You have", health,"HP\n You have", defense,"Defense")

    elif c1 == 2:
        area1 += 1
        print("you move farther through the trees")
    if area1 == 4:
        print("Youve found a old man in front of a tree")
        globals
        c1l = False

c2l = True
while c2l == True:
    tk = int(input("Do you want to talk to the old man: Yes(1) No(2): "))
    if tk == 2:
        print("you leave the old man the old man")
        print("You walk away and see another old man")
    elif tk == 1:
        c2l = False
        print("The old man tells you a long and boring story about something lame\n you start to walk away when he says\n'wait I need you to go into this maze and find my key card'")
c3l = True
while c3l == True:
    tk1 = int(input("Do you want to go to the maze: Yes(1) No(2): "))
    if tk1 == 2:
        print("The old man slaps you and says that not how you talk to your elders\n now try again")
    elif tk1 == 1:
        print("The old man leads you to the edge of the forest\n he says 'well good luck' and leaves")
        c3l = False


LR = 0
UD = 0
ttl = 0
mzl = True
while mzl:
    move = int(input("\nLeft (1) Right (2) Up (3) down (4)\n"))
    if move == 1:
        LR += -1
        ttl += 1
    elif move == 2:
        LR += 1
        ttl += 1
    elif move == 3:
        UD += 1
        ttl += 1
    elif move == 4:
        UD += -1
        ttl += 1
    else:
        print("thats not a opiton!")
    if UD == 3 and LR == -2:
        print("Youve finished the maze")
        mzl = False
    if ttl == 10:
        print("Youve finished the maze")
        mzl = False

keycard = 10
print("The old man appers :o\n He Tells you to journy to the train station\n************************\n")
while keycard > 1:
    old = int(input("Would you like to move forward (1)\n Or check stats (2)\n Or Move back (3)\n***********\n"))
    if old == 1:
        keycard += -1
        if keycard == 9:
            k1 = int(input("you see a tree would you like to explore it? \n Yes(1) No(2)"))
            if k1 == 1:
                print("You find a cheast, but the lock is broken")
                k1s = int(input("Would you like to use your sword to open the chest\n Yes(1) No(2)\n***********\n"))
                if k1s == 1:
                    print("You Found 5 arowws, but your sword was chiped and lost 2 damage")
                    arrow += 5
                    sword += -2
                elif k1s == 2:
                    print("You walk away\n")
                else:
                    print("That was not a option\n")
            elif k1 == 2:
                print("You Move forward\n")
        elif keycard == 8:
            print("You see a sigh, left(1) says short cut, right(2) says standered route\n***********\n")
            dirc1 = int(input("Where would you like to go\n"))
            if dirc1 == 1:
                keycard += -3
                print("Youve moved closer to the train station\n")
            elif dirc1 == 2:
                print("You move forward\n")
        elif keycard == 7:
            chc1 = int(input("You see a chest on the side of the rode\n Open it(1) walk away(2)\n***********\n"))
            if chc1 == 1:
                print("Youve gained 10 health and 3 damage to your sword\n")
            elif chc1 == 2:
                print("You move deeper into the forest\n")
        elif keycard == 6:
            print("You Move forward through the forest\n")
        elif keycard == 5:
            kid = int(input("You see a kid on the side of the trail\n Help him (1) Leave him(2)"))
            if kid == 1:
                print("You lose 1 health Potion\n The kid says thank you and runs off")
                heal += -1
                kidhlp += 1
            elif kid == 2:
                print("You walk away\n")
        elif keycard == 4:
            print("You walked into a Bee nest, You lost 10 HP\n")
            health += -10
        elif keycard == 3:
            print("You Move Forward Through the forest\n")
        elif keycard == 2:
            print("You can see the Train Station!\n")
        elif keycard == 1:
            print("You Have made it to the station!\n")

        else:
            print("Something went wrong, try again later\n")

    elif old == 2:
        print("You have", gold , "Gold, You have a bow that deals",bow,"damage\nYou have a sword that deals",sword,"damage\n You have", arrow, "arrows\n You have" ,heal,"healing potions\n You have", health,"HP\n You have", defense,"Defense")
    elif old == 3:
        keycard += 2
        print("You have travled back through the forest.\n")
    else:
        print("Not a option")


def oldmans(keptrd, oldman):
    while oldman:

        qus = int(input("The Old man arives, He walks up to you and offers to sell you items\n look at items(1) Move to the train(2)\n ***********\n"))
        if qus == 1:
            keptrd = True
            while keptrd:
                trade = int(input("3 Arrows 10 gold (1)\n Health potion 25 gold (2)\n Sword upgrade 50 gold (3)\n Leave(4)\n"))
                if trade == 1:
                    global gold
                    global arrow
                    global heal
                    global sword
                    gold += -10
                    if gold < 0:
                        print("You dont have enugh gold")
                        gold += 10
                    elif gold >= 0:
                        arrow += 3
                        print("You got 3 more arrows\n")
                elif trade == 2:
                    gold += -25
                    if gold < 0:
                        print("You dont have enugh gold")
                        gold += 25
                    elif gold >= 0:
                        heal += 1
                        print("You got 1 more health Potion\n")
                elif trade == 3:
                    gold += -50
                    if gold < 0:
                        print("You dont have enugh gold")
                        gold += 50
                    elif gold >= 0:
                        sword += 7
                        print("You got a better sword\n")
                elif trade == 4:
                    keptrd = False
        elif qus ==2:
            oldman = False
            print("You Board The train\n")
oldmans(True,True)

def train_fight(train_1,boss1,boss1hp,train_car1,tr1p,tr2p,tr3p,pers,done1):
    global gold
    global heal
    global arrow
    global sword
    global health

    while done1 == 0:
        
        tr1 = int(input("Would you like to move forward (1)\n Or check stats (2)\n Or Move back (3)\n***********\n"))
        if tr1 == 1:
            
        
            
            
            if train_car1 == 2:
                tr1 = int(input("Would you like to move forward (1)\n Or check stats (2)\n Or Move back (3)\n***********\n"))
                tr1c1 = tr1
                if tr1c1 == 1:
                    tr1p += -1
                    if tr1p == 4:
                        pas1 = int(input("You See a lady with her kids\n talk to them(1) Leave them alone(2)\n"))
                        if pas1 == 1:
                            print("They say \n'Im travling to the adoption center to drop of my kid'")
                        elif pas1 == 2:
                            print("You walk away from the People\n")
                        else:
                            print("You walk away\n")
                    elif tr1p == 3:
                        pas2 = int(input("You meet a man with a suit case\n talk to them(1) Leave them alone(2)\n"))
                        if pas2 == 1:
                            print("They say \n'Im going to a very important meeting with Joe biden and kendrick lamar'")
                        elif pas2 == 2:
                            print("You walk away from the People\n")
                        else:
                            print("You walk away\n")
                    elif tr1p == 2:
                        pas3 = int(input("You meet a bald man\n talk to them(1) Leave them alone(2)\n"))
                        if pas3 == 1:
                            print("They say \n'Im going to teach my chem 1010 class'")
                        elif pas3 == 2:
                            print("You walk away from the People\n")
                        else:
                            print("You walk away\n")
                    elif tr1p == 1:
                        pas4 = int(input("You meet a dog\n talk to them(1) Leave them alone(2)\n"))
                        if pas4 == 1:
                            print("They say nothing cause their a dog\n''")
                        elif pas4 == 2:
                            print("You walk away from the People\n")
                        else:
                            print("You walk away\n")
                    elif tr1p == 0:
                        train_car1 += -1
                        print("You moved to the next car\n")
                        
                elif tr1c1 == 2:
                    print("You have", gold , "Gold, You have a bow that deals",bow,"damage\nYou have a sword that deals",sword,"damage\n You have", arrow, "arrows\n You have" ,heal,"healing potions\n You have", health,"HP\n You have", defense,"Defense")
                elif tr1c1 == 3:
                    tr1p += 2
            elif train_car1 == 1:
                tr2c1 = tr1
                if tr2c1 == 1:
                    tr2p += -1
                    if tr2p == 4:
                        pas12 = int(input("You meet a lady with a odd hair cut\n talk to them(1) Leave them alone(2)\n"))
                        if pas12 == 1:
                            print("They say \n'I Think it looks good(Their wrong)'")
                        elif pas12 == 2:
                            print("You walk away from the People\n")
                    elif tr2p == 3:
                        pas22 = int(input("You meet a child\n talk to them(1) Leave them alone(2)\n"))
                        if pas22 == 1:
                            print("They say \n'Stranger Danger'")
                        elif pas22 == 2:
                            print("You walk away from the People\n")
                    elif tr2p == 2:
                        pas32 = int(input("You the kid from the trail\n talk to them(1) Leave them alone(2)\n"))
                        if pas3 == 1:
                            if kidhlp == 1:
                                heal += 3
                                print("The Kid gave you 3 health potions for helping him out")
                            elif kidhlp == 0:
                                print("The kid does not talk to you becuase you did not help him")
                        elif pas32 == 2:
                            print("You walk away from the People\n")
                    elif tr2p == 1:
                        pas42 = int(input("There is a old lady sitting with a strange box\n talk to them(1) Leave them alone(2)\n"))
                        
                        if pas42 == 1:
                            pers += 1
                            train_car1 += -1
                            print("They say \n'I found this key, I think its important'")
                        elif pas42 == 2:
                            print("You walk away from the People\n")
                        elif pas42 == 1:
                            train_car1 += -1
                            print("You moved to the next car\n")
                        else:
                            print("You walk away\n")
                    else:
                        print("Thats not a option")
                            
            elif train_car1 < 0 and pers == 1:
                boss1 = True
                print("You walk into the Room\n the conductor is waiting for you\n He says that the engine is acting up and there is something we need to help him fix\n")
                print("You walk down the stairs and see a monstor made of coal")
                hpb = 250
                tb = True
                while tb:
                    if hpb < 0:
                        tb = False
                        done1 = 1
                        print('You have Killed the boss')
                        print("You got 200 gold, and 5 health potions\n You also are at full health")
                        gold += 200
                        health = 100
                        heal += 5
                    elif health < 0:
                        print("You lost, good game")
                        break
                    else:
                        a1 = int(input("Pick your move\n Sword(1) Bow(2) Heal(3) Run(4)"))
                        if a1 == 1:
                            hpb += -sword
                            print("You dealt", sword,"To the boss\n The boss has", hpb,"Left\n")
                            bossdmg1 = random.randint(1,10)
                            health += -bossdmg1
                            print("The boss dealt", bossdmg1,"you have",health,"left\n")

                        elif a1 == 2:
                            if arrow > 0:
                                arrow += -1
                                hpb += -bow
                                print("You dealt", bow,"To the boss, and have", arrow,"left\n The boss has", hpb,"Left\n")
                            elif arrow == 0:
                                print('You are out of arrows, you attack did nothing to the boss')
                        elif a1 == 3:
                            heal += -1
                            if heal > 0:
                                
                                health += 25
                                print("You used a health potion, you have",health,"HP")
                            elif heal == 0:
                                print("You are out of healing potions\n")
                                health += 25
                                print("You used a health potion, you have",health,"HP")
                            elif heal < 0:
                                print("You cannot do that, you are out of healing poitions")

                        elif a1 == 4:
                            train_car1 += 2
                            print("You left the boss fight")
                            tb = False
                        else:
                            print("Thats not a option\n")
                        
            elif train_car1 == 0 and pers == 0:
                print("You look at the door, but it cant be opened without a key\n go back and find the person with the key.\n")
                train_car1 += 3
            else:
                print("You Move forward\n")
                train_car1 += -1
        elif tr1 == 2:
            print("You have", gold , "Gold, You have a bow that deals",bow,"damage\nYou have a sword that deals",sword,"damage\n You have", arrow, "arrows\n You have" ,heal,"healing potions\n You have", health,"HP\n You have", defense,"Defense")
        elif tr1 == 3:
            train_car1 += 2
            print("You have travled back through the Train\n")
        else:
            print("Not a option")

def train_fight2(train_1,boss1,boss1hp,train_car1,tr1p,tr2p,tr3p,pers,done1):
    global gold
    global heal
    global arrow
    global sword
    global health
    while done1 == 0:
        
        tr1 = int(input("Would you like to move forward (1)\n Or check stats (2)\n Or Move back (3)\n***********\n"))
        
        if tr1 == 1:
            
            if train_car1 == 2:
                tr1 = int(input("Would you like to move forward (1)\n Or check stats (2)\n Or Move back (3)\n***********\n"))
                tr1c1 = tr1
                if tr1c1 == 1:
                    tr1p += -1
                    if tr1p == 4:
                        pas1 = int(input("You See a lady with her kids\n talk to them(1) Leave them alone(2)\n"))
                        if pas1 == 1:
                            print("They say \n'Im travling to the adoption center to drop of my kid'")
                        elif pas1 == 2:
                            print("You walk away from the People\n")
                        else:
                            print("You walk away\n")
                    elif tr1p == 3:
                        pas2 = int(input("You see a person with the top part of a pice of papper\n talk to them(1) Leave them alone(2)\n"))
                        if pas2 == 1:
                            print("They say \n'I found this pice of paper with the number 3 onit, it might be useful'")
                        elif pas2 == 2:
                            print("You walk away from the People\n")
                        else:
                            print("You walk away\n")
                    elif tr1p == 2:
                        pas3 = int(input("You meet a man with orange hair\n talk to them(1) Leave them alone(2)\n"))
                        if pas3 == 1:
                            print("They say \n'Im going to make this game great again'")
                        elif pas3 == 2:
                            print("You walk away from the People\n")
                        else:
                            print("You walk away\n")
                    elif tr1p == 1:
                        pas4 = int(input("You see a dog with a pice of papper\n talk to them(1) Leave them alone(2)\n"))
                        if pas4 == 1:
                            print("They say \n'i found this pice of paper with the number 9 on it, it might be useful'")
                        elif pas4 == 2:
                            print("You walk away from the People\n")
                        else:
                            print("You walk away\n")
                    elif tr1p == 0:
                        train_car1 += -1
                        print("You moved to the next car\n")
                        
                elif tr1c1 == 2:
                    print("You have", gold , "Gold, You have a bow that deals",bow,"damage\nYou have a sword that deals",sword,"damage\n You have", arrow, "arrows\n You have" ,heal,"healing potions\n You have", health,"HP\n You have", defense,"Defense")
                elif tr1c1 == 3:
                    tr1p += 1
            if train_car1 == 1:
                tr1 = int(input("Would you like to move forward (1)\n Or check stats (2)\n Or Move back (3)\n***********\n"))
                tr2c1 = tr1
                if tr2c1 == 1:
                    tr2p += -1
                    if tr2p == 4:
                        pas12 = int(input("You see a kid playing with a toy\n Take the toy(1) Leave them alone(2)\n"))
                        if pas12 == 1:
                            print("You try to take the toy \n'You get hit and lose 25 HP'")
                            health += -25
                        elif pas12 == 2:
                            print("You walk away from the People\n")
                    elif tr2p == 3:
                        pas22 = int(input("You see a bald man with a pice of paper\n talk to them(1) Leave them alone(2)\n"))
                        if pas22 == 1:
                            print("They say \n'i found this pice of paper with the number 4 on it, it might be useful'")
                        elif pas22 == 2:
                            print("You walk away from the People\n")
                    elif tr2p == 2:
                        pas32 = int(input("You see a ginger with a computer\n talk to them(1) Leave them alone(2)\n"))
                        if pas3 == 1:
                            print("They say \n'Im making this lame game right now, and its messed up but I wont tell you that'")
                        elif pas32 == 2:
                            print("You walk away from the People\n")
                    elif tr2p == 1:
                        pas42 = int(input("There is a old lady sitting with a strange pice of paper\n talk to them(1) Leave them alone(2)\n"))
                        
                        if pas42 == 1:
                            print("They say \n'I found this pice of paper with the number 2 on it, I think its important'")
                        elif pas42 == 2:
                            print("You walk away from the People\n")
                        elif pas42 == 1:
                            train_car1 += -1
                            print("You moved to the next car\n")
                        else:
                            print("You walk away\n")
                    else:
                        print("Thats not a option")
                            
            if train_car1 == 0 :
                code = int(input("There is a keypad with 4 digit code\n Enter the code: "))
                if code == 3942:
                    boss1 = True
                    print("You walk into the Room\n the conductor is missing")
                    print("You walk down the stairs and see a creature, its hostile\n")
                    while boss1:
                        
                        
                        if boss1hp < 0:
                            boss1 = False
                            done1 = 1
                            print('You have Killed the boss')
                            print("You got 150 gold, and 3 health potions\n You also are at full health")
                            gold += 150
                            health = 100
                            heal += 3
                        elif health < 0:
                            print("You lost, good game")
                            break
                        else:
                            a1 = int(input("Pick your move\n Sword(1) Bow(2) Heal(3) Run(4)"))
                            if a1 == 1:
                                boss1hp += -sword
                                print("You dealt", sword,"To the boss\n The boss has", boss1hp,"Left\n")
                                bossdmg1 = random.randint(1,10)
                                health += -bossdmg1
                                print("The boss dealt", bossdmg1,"you have",health,"left\n")

                            elif a1 == 2:
                                if arrow > 0:
                                    arrow += -1
                                    boss1hp += -bow
                                    print("You dealt", bow,"To the boss, and have", arrow,"left\n The boss has", boss1hp,"Left\n")
                                elif arrow == 0:
                                    print('You are out of arrows, you attack did nothing to the boss')
                            elif a1 == 3:
                                heal += -1
                                if heal > 0:
                                    
                                    health += 25
                                    print("You used a health potion, you have",health,"HP")
                                elif heal == 0:
                                    print("You are out of healing potions\n")
                                    health += 25
                                    print("You used a health potion, you have",health,"HP")
                                elif heal < 0:
                                    print("You cannot do that, you are out of healing poitions")

                            elif a1 == 4:
                                train_car1 += 1
                                print("You left the boss fight")
                                boss1 = False
                            else:
                                print("Thats not a option\n")
                    else:
                        print("You need to talk to the passengers to find the code\n")
                        train_car1 += 1
                            
            if train_car1 == 0:
                print("You look at the door, but it cant be opened without a key\n go back and find the person with the key.\n")
                train_car1 += 3
            else:
                print("You found a pice of paper with a code on it\n It says '3942' \n")
                train_car1 += -1
        elif tr1 == 2:
            print("You have", gold , "Gold, You have a bow that deals",bow,"damage\nYou have a sword that deals",sword,"damage\n You have", arrow, "arrows\n You have" ,heal,"healing potions\n You have", health,"HP\n You have", defense,"Defense")
        elif tr1 == 3:
            train_car1 += 2
            print("You have travled back through the Train\n")
        else:
            print("Not a option")

train_fight(True,True,250,3,3,2,3,0,0)

train_1 = True
boss1 = True
boss1hp = 200
train_car1 = 3
tr1p = 3
tr2p = 3
tr3p = 3
pers = 0
done1 = 0
oldmans(True,True)
train_fight2(True,True,500,3,3,2,3,0,0)
final = True
fnhp = 1000
five = 5
twen = 20
fndmg = random.randint(five,twen)
while final:
    if name == "god" or name == "God":
        fnhp += 999999
        five += 95
        twen += 180
        
    else:
        sword += 3
    oldmans(True,True)
    fn1 = int(input("Do you want to Go to the final Train\n Yes(1) No(2)\n"))
    if fn1 == 1:
        final = True
        while final:
                        
                        
            if fnhp < 0:
                final = False
                done1 = 1
                print('You have Killed the boss')
                print("This is the end, Thanks for Playing my game\n maker Sam")
                break
            elif health < 0:
                print("You lost, good game")
                done1 = 1
                final = False
                break
            else:
                a1 = int(input("Pick your move\n Sword(1) Bow(2) Heal(3) Run(4)"))
                if a1 == 1:
                    fnhp += -sword
                    print("You dealt", sword,"To the boss\n The boss has", fnhp,"Left\n")
                    fndmg = random.randint(five,twen)
                    health += -fndmg
                    print("The boss dealt", fndmg,"you have",health,"left\n")

                elif a1 == 2:
                    if arrow > 0:
                        arrow += -1
                        fnhp += -bow
                        print("You dealt", bow,"To the boss, and have", arrow,"left\n The boss has", fnhp,"Left\n")
                    elif arrow == 0:
                        print('You are out of arrows, you attack did nothing to the boss')
                elif a1 == 3:
                    heal += -1
                    if heal > 0:
                                    
                        health += 25
                        print("You used a health potion, you have",health,"HP")
                    elif heal == 0:
                        print("You are out of healing potions\n")
                        health += 25
                        print("You used a health potion, you have",health,"HP")
                    elif heal < 0:
                        print("You cannot do that, you are out of healing poitions")

                elif a1 == 4:
                        
                    print("You left the boss fight")
                    final = False
                else:
                    print("Thats not a option\n The boss still attacks you")
                    fndmg = random.randint(five,twen)
                    health += -fndmg
                    print("The boss dealt", fndmg,"you have",health,"left\n")

