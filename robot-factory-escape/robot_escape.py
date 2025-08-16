health = 100
energy = 50
minutes_left = 30

#Values
PIN_number = 427
VENT_COST = 6
SCRAPE_DAMAGE = 10
ALARM_PENALTY = 3
MAZE_REWARD = 5
MAZE_DAMAGE = 15


has_keycard = False

print("--------------------Welcome to Escape Game--------------------")
print(f"Minutes Left:{minutes_left}      Health: {health}      energy:{energy}")

while health > 0 and minutes_left > 0:
    choice1 = input("What choice Are u choosing \n(A) Vent Crawl (Cost Energy) \n(B) Security door (Needs PIN:) \n(C) Robot Arm Maze :\nWhat is Your choice(A/B/C):  ").lower()
    if choice1 == "a" :
        speed_run = input("DO u want to speedrun ")
        if speed_run == "yes":
            minutes_left -= 2
            energy -= 3
            if minutes_left % 5 ==0:
                energy += 6 
                print("You got batter now  u have +6 Energy")
            
        
        if energy % 2 == 0:
            energy -= VENT_COST
            minutes_left -= 5
        else:
            health -= SCRAPE_DAMAGE
            energy -= VENT_COST
            minutes_left -= 5
        minutes_left -= 1
        print(f"Your Current Status--     Health:{health},     energy:{energy},     Minutes left: {minutes_left}")
    elif choice1 == "b" :
        speed_run = input("DO u want to speedrun ")
        if speed_run == "yes":
            minutes_left -= 2
            energy -= 3
            if minutes_left % 5 ==0:
                energy += 6 
                print("You got batter now  u have +6 Energy")
        pin = int(input("Enter your PIN: "))
        if pin == PIN_number:
            has_keycard = True
            print("Congrats You found the Key Card")
        else:
            minutes_left -= ALARM_PENALTY
            print("You got alarm penalty -3 Minutes")
        minutes_left -= 1
        print(f"Your Current Status--Health:{health},energy:{energy},Minutes left: {minutes_left}")
    elif choice1 == "c":
        speed_run = input("DO u want to speedrun ")
        if speed_run == "yes":
            minutes_left -= 2
            energy -= 3
            if minutes_left % 5 ==0:
                energy += 6 
                print("You got batter now  u have +6 Energy")
        minutes_left -= 1
        for i in range(3):
            robo = input("Choose (T/F)").lower()
            if robo == "t":
                question1 = int(input("whats 3 + 2"))
                if question1 == 5:
                    energy += MAZE_REWARD
                    print("You got +5 Energy")
                else:
                    health -= MAZE_DAMAGE
                    print("You got -15 Health")
            elif robo == "f":
                health -= MAZE_DAMAGE
                print("You got -15 Health")
        print(f"Your Current Status--Health:{health},energy:{energy},Minutes left: {minutes_left}")
    else:
        print("Inavlid Option")

    if has_keycard and energy >=5 and minutes_left >= 1:
        print("You swipe keycard and escape! 🎉")
        break
    elif health <= 0:
        print("Knocked out")
        break
    elif minutes_left <= 0:
        print("Factorey Locks Down")
        break
print("\n📊 FINAL STATUS:")
print(f"Health: {health}")
print(f"Energy: {energy}")
print(f"Minutes Left: {minutes_left}")
print(f"Keycard: {has_keycard}")
