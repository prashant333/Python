print("Welcome to this interesting game!")
name = input("Enter your name: ")
age = int(input("Enter your age: "))

health = 10
if age >= 19:
    print("Hi " + name + "you are old enough to play game!")
    want_to_play = input("do you want to play game: (yes / no)").lower()
    if want_to_play == "yes":
        print("Let's play!")
        left_right = input("Please select which do you want to go.(Left/Right):").lower()
        if left_right == "right":
            swim_walk = input("There is lake ahead. Would you like to swim or walk around. (Swim/walk around)").lower()

            if swim_walk == "swim":
                health -=5
                print("You were bit by snake. You lost health. Health remaining", health)
            else:
                print("You crossed the lake successfully.")
        else:
            print("you fell in the well!! You loose.")
    else:
        print("That's cool. Have a nice day.")

else:
    print("Hi " + name + "you are under aged to play this game. ")
