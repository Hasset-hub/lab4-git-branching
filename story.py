def intro():
    print("You wake up in a dark forest. You can go left or right.")
    choice = input("Which direction do you choose? (left/right): ").strip().lower()
    if choice == "left":
        left_path()
    elif choice == "right":
        right_path()
    else:
        print("You stand still, unsure what to do. The forest swallows you.")

def left_path():
    print("You walk left and find a mysterious glowing sword stuck in a stone.")
    print("You pull the sword free — you are destined to be the hero of the realm!")

def right_path():
    print("You head right and encounter a talking squirrel who challenges you to a duel.")
    print("You rush in bravely and defend the townsfolk with your newfound courage!")
if __name__ == "__main__":
    intro()
