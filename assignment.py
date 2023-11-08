#!python3
# Volume Calculator
# Feel free to rename your variables


def title():
    # Will display a title screen
    # input parameters: none needed
    # output parameters: None
    # Author: Copper
    # Modified:
    # title
    print("-= SUPER ULTRA CALCULATOR =- 2000\n")
    q1 = ('Press "1" to see instructions')
    q2 = ('Press "2" to exit calculator')
    if input(q1) == 1:
        instructions()
    if input(q2) == 2:
        exit()
    return input

def instructions():
    print('__________________________________\nYou will enter in a number that represents "x"')
    print('Press "1" to find circumference of a circle where "x" is the radius')
    print('Press "2" to find area of a circle where "x" is the radius')
    print('Press "3" to find volume of a sphere where "x" is the radius')    
    print('Press "4" to find surface area of a sphere where "x" is the radius')
    print('Press "5" to find how many spheres would be needed to reach the moon from earth if the spheres were chaining together to make a line and "x" is the radius of a circle in meters')
    # Will display instructions
    # input parameters: none needed
    # output parameters: None
    # Author:
    # Modified:
    return None



def main():
    """
    main block of code that will run your program and control program flow
    You will need to include a while loop to keep repeating the commands until
    the user chooses to exit
    """
    title()
    while True:
        # keep giving options to choose menu options until they choose to exit
        pass

if __name__ == "__main__":
    main()
