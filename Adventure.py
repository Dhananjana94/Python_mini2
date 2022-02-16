name = input("Enter your name: ")

print("Welcome",name,"to adventure park")

answer = input("You are in dirt road, it has come to end and you can go left or right."
               " So which way would you like to go (left/right): ").lower()


if answer == "left":
    ans = input("You come to a river. you can walk around it or swim across it. type swim or walk: ").lower()

    if ans == "swim":
        print("You tried to swim and eaten by aligator")

    elif ans == "walk":
        print("You walked for many miles, ran out of water and you lost the game")

    else:
        print("Not valied answer, You lost")

elif answer == "right":
    ans = input("You come to a bridge, it looks wobbly, do you want to cross it or head back(cross/back)? ").lower()

    if ans == "cross":
        NxtAns = input("You cross the bridge, do you want to meet a mechanic(yes/no)? ").lower()

        if NxtAns == "yes":
            print("You complete the mission, You win!!")

        elif NxtAns == "no":
            print("You did not complete the mission, you lost")

        else:
            print("Not valied answer, You lost")

    elif ans == "back":
        print("You did not complete the mission, You lost")

    else:
        print("Not valied answer, You lost")

else:
    print("Your answer is incorrect")

print("Thank you",name,"come back again!!")