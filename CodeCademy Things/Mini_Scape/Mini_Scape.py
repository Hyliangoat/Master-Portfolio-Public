class Player:
    def __init__(self, name, health, weapon, armor, item, buff):
        self.name = name
        self.health = health
        self.weapon = weapon
        self.armor = armor
        self.item = item
        self.buff = buff

    def __repr__(self):
        info = "Player Name: {name}, Player Health: {health}, Player Weapon: {weapon}, Player Armor: {armor}, Player Item: {item}, Player Buff: {buff}".format(name = self.name, health = self.health, weapon = self.weapon, armor = self.armor, item = self.item, buff = self.buff)
        return info
    
    
def move(p1_choice, p2_choice):
    p1 = p1_choice
    p2 = p2_choice

    #First, see if they used an item and apply a buff or tell them they failed to use an item
    if p1 == 3 and player_one.item == 1:
        print(player_one.name + " eats a lobster!")
        player_one.health += 50
        player_one.item = 0
    elif p1 == 3 and player_one.item == 2:
        print(player_one.name + " has chosen to use their attack potion!")
        player_one.buff = "Attack"
        player_one.item = 0
    elif p1 == 3 and player_one.item == 3:
        print(player_one.name + " has chosen to use their defense potion!")
        player_one.buff = "Def"
        player_one.item = 0
    elif p1 == 3 and player_one.item == 0:
        print(player_one.name,  "tried to use an item, but failed. No more remain.")
    
    if p2 == 3 and player_two.item == 1:
        print(player_two.name + " eats a lobster!")
        player_two.health += 50
        player_two.item = 0
    elif p2 == 3 and player_two.item == 2:
        print(player_two.name + " has chosen to use their attack potion!")
        player_two.buff = "Attack"
        player_two.item = 0
    elif p2 == 3 and player_two.item == 3:
        print(player_two.name + " has chosen to use their defense potion!")
        player_two.buff = "Def"
        player_two.item = 0
    elif p2 == 3 and player_two.item == 0:
        print(player_two.name, "tried to use an item, but failed. No more remain.")
    

    #Player 1 attacks (Side note for me 10 weak, 20 med, 30 strong) (def pot 5, 10, 20) (att pot, 20, 30, 40 )
    #-----------------------------------------------Scimitar------------------------------------------
    if p1 == 1 and p2 != 2:
        print(player_one.name + " attacks!")
        #Scimitar vs plate (med)
        if player_one.weapon == 1 and player_two.armor == 1:
            #Check Buff
            if player_one.buff == "Attack":
                #Check opponent buff
                if player_two.buff == "Def":
                    player_two.health -= 20
                else:
                    player_two.health -= 30
            else:
                if player_two.buff == "Def":
                    player_two.health -= 10
                else:
                    player_two.health -= 20
        #Scimitar vs leather (strong)
        elif player_one.weapon == 1 and player_two.armor == 2:
            #Check Buff
            if player_one.buff == "Attack":
                #Check opponent buff
                if player_two.buff == "Def":
                    player_two.health -= 30
                else:
                    player_two.health -= 40
            else:
                if player_two.buff == "Def":
                    player_two.health -= 20
                else:
                    player_two.health -= 30
        #Scimitar vs Enchanted Robes (weak)
        elif player_one.weapon == 1 and player_two.armor == 3:
            #Check Buff
            if player_one.buff == "Attack":
                #Check opponent buff
                if player_two.buff == "Def":
                    player_two.health -= 10
                else:
                    player_two.health -= 20
            else:
                if player_two.buff == "Def":
                    player_two.health -= 5
                else:
                    player_two.health -= 10
        
        #--------------------------------------------------Bow----------------------------------------------
        #Bow vs plate (weak)
        if player_one.weapon == 2 and player_two.armor == 1:
            #Check Buff
            if player_one.buff == "Attack":
                #Check opponent buff
                if player_two.buff == "Def":
                    player_two.health -= 10
                else:
                    player_two.health -= 20
            else:
                if player_two.buff == "Def":
                    player_two.health -= 5
                else:
                    player_two.health -= 10
        #Bow vs leather (med)
        elif player_one.weapon == 2 and player_two.armor == 2:
            #Check Buff
            if player_one.buff == "Attack":
                #Check opponent buff
                if player_two.buff == "Def":
                    player_two.health -= 20
                else:
                    player_two.health -= 30
            else:
                if player_two.buff == "Def":
                    player_two.health -= 10
                else:
                    player_two.health -= 20
        #Bow vs Enchanted Robes (strong)
        elif player_one.weapon == 2 and player_two.armor == 3:
            #Check Buff
            if player_one.buff == "Attack":
                #Check opponent buff
                if player_two.buff == "Def":
                    player_two.health -= 30
                else:
                    player_two.health -= 40
            else:
                if player_two.buff == "Def":
                    player_two.health -= 20
                else:
                    player_two.health -= 30
        
        #--------------------------------------Staff-------------------------------------------
        #Staff vs plate (strong)
        if player_one.weapon == 3 and player_two.armor == 1:
            #Check Buff
            if player_one.buff == "Attack":
                #Check opponent buff
                if player_two.buff == "Def":
                    player_two.health -= 30
                else:
                    player_two.health -= 40
            else:
                if player_two.buff == "Def":
                    player_two.health -= 20
                else:
                    player_two.health -= 30
        #Staff vs leather (weak)
        elif player_one.weapon == 3 and player_two.armor == 2:
            #Check Buff
            if player_one.buff == "Attack":
                #Check opponent buff
                if player_two.buff == "Def":
                    player_two.health -= 10
                else:
                    player_two.health -= 20
            else:
                if player_two.buff == "Def":
                    player_two.health -= 5
                else:
                    player_two.health -= 10
        #Staff vs Enchanted Robes (med)
        elif player_one.weapon == 3 and player_two.armor == 3:
            #Check Buff
            if player_one.buff == "Attack":
                #Check opponent buff
                if player_two.buff == "Def":
                    player_two.health -= 20
                else:
                    player_two.health -= 30
            else:
                if player_two.buff == "Def":
                    player_two.health -= 10
                else:
                    player_two.health -= 20
        

    #Player 2 attacks (Side note for me 10 weak, 20 med, 30 strong) (def pot 5, 10, 20) (att pot, 20, 30, 40 )
    #----------------------------------------------------Scimitar---------------------------------------------
    if p2 == 1 and p1 != 2:
        print(player_two.name + " attacks!")
        #Scimitar vs plate (med)
        if player_two.weapon == 1 and player_one.armor == 1:
            #Check Buff
            if player_two.buff == "Attack":
                #Check opponent buff
                if player_one.buff == "Def":
                    player_one.health -= 20
                else:
                    player_one.health -= 30
            else:
                if player_one.buff == "Def":
                    player_one.health -= 10
                else:
                    player_one.health -= 20
        #Scimitar vs leather (strong)
        elif player_two.weapon == 1 and player_one.armor == 2:
            #Check Buff
            if player_two.buff == "Attack":
                #Check opponent buff
                if player_one.buff == "Def":
                    player_one.health -= 30
                else:
                    player_one.health -= 40
            else:
                if player_one.buff == "Def":
                    player_one.health -= 20
                else:
                    player_one.health -= 30
        #Scimitar vs Enchanted Robes (weak)
        elif player_two.weapon == 1 and player_one.armor == 3:
            #Check Buff
            if player_two.buff == "Attack":
                #Check opponent buff
                if player_one.buff == "Def":
                    player_one.health -= 10
                else:
                    player_one.health -= 20
            else:
                if player_one.buff == "Def":
                    player_one.health -= 5
                else:
                    player_one.health -= 10
        
        #--------------------------------Bow--------------------------------
        #Bow vs plate (weak)
        if player_two.weapon == 2 and player_one.armor == 1:
            #Check Buff
            if player_two.buff == "Attack":
                #Check opponent buff
                if player_one.buff == "Def":
                    player_one.health -= 10
                else:
                    player_one.health -= 20
            else:
                if player_one.buff == "Def":
                    player_one.health -= 5
                else:
                    player_one.health -= 10
        #Bow vs leather (med)
        elif player_two.weapon == 2 and player_one.armor == 2:
            #Check Buff
            if player_two.buff == "Attack":
                #Check opponent buff
                if player_one.buff == "Def":
                    player_one.health -= 20
                else:
                    player_one.health -= 30
            else:
                if player_one.buff == "Def":
                    player_one.health -= 10
                else:
                    player_one.health -= 20
        #Bow vs Enchanted Robes (strong)
        elif player_two.weapon == 2 and player_one.armor == 3:
            #Check Buff
            if player_two.buff == "Attack":
                #Check opponent buff
                if player_one.buff == "Def":
                    player_one.health -= 30
                else:
                    player_one.health -= 40
            else:
                if player_one.buff == "Def":
                    player_one.health -= 20
                else:
                    player_one.health -= 30
        
        #---------------------------------------Staff------------------------------------------------
        #Staff vs plate (strong)
        if player_two.weapon == 3 and player_one.armor == 1:
            #Check Buff
            if player_two.buff == "Attack":
                #Check opponent buff
                if player_one.buff == "Def":
                    player_one.health -= 30
                else:
                    player_one.health -= 40
            else:
                if player_one.buff == "Def":
                    player_one.health -= 20
                else:
                    player_one.health -= 30
        #Staff vs leather (weak)
        elif player_two.weapon == 3 and player_one.armor == 2:
            #Check Buff
            if player_two.buff == "Attack":
                #Check opponent buff
                if player_one.buff == "Def":
                    player_one.health -= 10
                else:
                    player_one.health -= 20
            else:
                if player_one.buff == "Def":
                    player_one.health -= 5
                else:
                    player_one.health -= 10
        #Staff vs Enchanted Robes (med)
        elif player_two.weapon == 3 and player_one.armor == 3:
            #Check Buff
            if player_two.buff == "Attack":
                #Check opponent buff
                if player_one.buff == "Def":
                    player_one.health -= 20
                else:
                    player_one.health -= 30
            else:
                if player_one.buff == "Def":
                    player_one.health -= 10
                else:
                    player_one.health -= 20

    #Players block
    if p2 == 2:
        print(player_two.name, "blocked all attacks!")
    if p1 == 2:
        print(player_two.name, "blocked all attacks!")








#Initial sequence
#The input is turned into an integer because python doesn't automatically do that and I didn't want to quote every instance of a number in the script

print("Welcome to MiniScape")
print("Two players enter, only one leaves alive.")
print("First, you will take turns creating your characters and choosing your equipment")
input("Do not let the other player see your equipment. Press enter to continue")


#Player one info
p1_name = input("Player one, state your name: ")
p1_weapon = int(input("What weapon will you choose? (1) Scimitar. (2) Long Bow. (3). Staff with runes: "))
p1_armor = int(input("What will you outfit yourself with? (1) Platemail. (2) Leather. (3). Enchanted Robes: "))
p1_item = int(input("Take one sacred item to use in battle: (1) Lobster. (2) Attack Potion. (3) Defense Potion: "))
player_one =  Player(p1_name, 100, p1_weapon, p1_armor, p1_item, 0)
print(chr(27) + "[2J")
#Player two info
p2_name = input("Player two, state your name: ")
p2_weapon = int(input("What weapon will you choose? (1) Scimitar. (2) Long Bow. (3). Staff with runes: "))
p2_armor = int(input("What will you outfit yourself with? (1) Platemail. (2) Leather. (3). Enchanted Robes: "))
p2_item = int(input("Take one sacred item to use in battle: (1) Lobster. (2) Attack Potion. (3) Defense Potion: "))
player_two =  Player(p2_name, 100, p2_weapon, p2_armor, p2_item, 0)
print(chr(27) + "[2J")

#Battle loop
while player_one.health > 0 and player_two.health > 0: 

    #Input, if they input non-integer, except it 
    p1_check = False
    p2_check = False
    p1_move = 0
    p2_move = 0
    
    while p1_check == False:
        try:
            p1_move = int(input(player_one.name + " choose your move. (1) Attack. (2) Defend. (3) Use item: "))
        except ValueError:
            print("Only input numbers")
        if p1_move != 1 and p1_move != 2 and p1_move != 3:
            print ("Number must be 1, 2, or 3")
        else:
            p1_check = True
    print(chr(27) + "[2J")
    while p2_check == False:
        try:
            p2_move = int(input(player_two.name + " choose your move. (1) Attack. (2) Defend. (3) Use item: "))
        except ValueError:
            print("Only input numbers")
        if p2_move != 1 and p2_move != 2 and p2_move != 3:
            print ("Number must be 1, 2, or 3")
        else:
            p2_check = True
    print(chr(27) + "[2J")
    move(p1_move, p2_move)
    print(player_one.name + "'s health: " + str(player_one.health))
    print(player_two.name + "'s health: " + str(player_two.health))

    input("Press enter to continue to next round")
    print(chr(27) + "[2J")
print(chr(27) + "[2J")
if player_one.health <= 0:
    print(player_two.name + " is victorious.")
    print(player_two.name + " gloats over " + player_one.name + "'s corpse.")
    input("Press enter to end game. Thank you for playing.")
else:
    print(player_one.name + " is victorious.")
    print(player_one.name + " gloats over " + player_two.name + "'s corpse.")
    input("Press enter to end game. Thank you for playing.")

