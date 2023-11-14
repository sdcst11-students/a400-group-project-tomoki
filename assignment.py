#!python3
# Volume Calculator
# Feel free to rename your variables
import math
def title():
    # Will display a title screen
    # input parameters: none needed
    # output parameters: None
    # Author: Copper
    # Modified:
    # title
    print("-= CALCULATOR =-\n")
    q1 = ('Press "1" to see instructions \nPress "2" to exit calculator\nType here -> ')
    if input(q1) == "1":
        instructions()
    elif input(q1) == "2":
        exit()
    else:
        print("Invalid Input")

def instructions():
    while True:
        print ('__________________________________')
        q2 = ('Press "1" to find circumference of a circle where given the radius\nPress "2" to find area of a circle where given the the radius\nPress "3" to find volume of a sphere where given the radius\nPress "4" to find surface area of a sphere where given the radius\nPress "5" for exponent calculator\nType here -> ')
        if input(q2) == "1":
            one()
        elif input(q2) == "2":
            two()
        elif input(q2) == "3":
            three()
        elif input(q2) == "4":
            four()
        elif input(q2) == "5":
            five()
        else:
            print("Invalid Input")
            # Will display instructions
            # input parameters: none needed
            # output parameters: None
            # Author:
            # Modified:
            return None

def exit():
    exit()

def one():
    q = "What is the radius of your circle? "
    circumference = float(input(q))*2*math.pi
    print(f"The circumference of your circle is {circumference}")

def two():
    q = "What is the radius of your circle? "
    area = (float(input(q))**2)*math.pi
    print(f"The area of your circle is {area}")  

def three():
    q = "What is the radius of your sphere? "
    volume = (float(input(q))**3)*math.pi*(4/3)
    print(f"The area of your circle is {volume}") 

def four():   
    q = "What is the radius of your sphere? "
    sa = (float(input(q))**2)*math.pi*4
    print(f"The surface area of your sphere is {sa}") 

def five():
    q = "What is the radius of your sphere? "


def main():
    """
    main block of code that will run your program and control program flow
    You will need to include a while loop to keep repeating the commands until
    the user chooses to exit
    """
    title()
    instructions()

    while True:
        
        # keep giving options to choose menu options until they choose to exit
        #unMainMenu()
        #getInput()
        #use input to decide which function to run


if __name__ == "__main__":
    main()
