name = input("Enter your name, brave traveler: ")
print(f"Greetings, {name}! Your journey begins now.")

choice = input("You find yourself on a dusty path that splits in two directions. Do you wish to go 'left' towards the dark forest or 'right' towards the mountain trail? ").lower()

if choice == "left":
    choice = input("You venture into the forest and soon find a wide, rushing river. Do you choose to 'swim' across it or take the safer route and 'walk' around? ").lower()

    if choice == "swim":
        print("You bravely dive into the river but are swiftly caught by the current and meet a watery fate. The journey ends here.")
    elif choice == "walk":
        print("You decide to walk around the river. The journey is long, and as night falls, you find yourself lost and out of supplies. You succumb to the elements.")
    else:
        print("That's not a valid choice, and without a clear decision, you're lost in the forest. Game over.")

elif choice == "right":
    choice = input("You take the mountain trail and soon come to a shaky old bridge. It looks dangerous. Do you 'cross' it or 'turn back'? ").lower()
    
    if choice == "turn back":
        print("You decide it's too risky and turn back. Unfortunately, as you retreat, you are ambushed by bandits. Your adventure ends here.")
    elif choice == "cross":
        choice = input("Carefully, you cross the bridge and find an old traveler on the other side. Do you choose to 'talk' to the traveler or 'ignore' them and continue on your way? ").lower()
        
        if choice == "talk":
            print("You approach the traveler, who shares tales of great wisdom and gifts you a magical amulet for your kindness. You have won this adventure!")
        elif choice == "ignore":
            print("You ignore the traveler and walk past, but they curse you for your rudeness. You suddenly feel very weak and fall to the ground. Your journey ends here.")
        else:
            print("That's not a valid choice, and without a decision, you stand still until nightfall, where dangers find you. Game over.")
    else:
        print("That's not a valid choice, and without a clear decision, you remain indecisive until it's too late. Game over.")

else:
    print("That's not a valid choice, and your hesitation causes you to miss your adventure entirely. Game over.")

print("Thank you for trying", name)
