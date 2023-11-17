#!python3
# Volume Calculator
# Feel free to rename your variables
import math
import time
def title():
    # Will display a title screen
    # input parameters: none needed
    # output parameters: None
    # Author: Copper
    # Modified:
    # title
    while True:
        choice = input('Press "1" to see instructions \nPress "2" to exit calculator\nType here -> ')
        if choice == "1":
            instructions()
            break
        elif choice == "2":
            print("Goodbye.")
            time.sleep(0.5)
            quit()
        else:
            print("Invalid Input")
            time.sleep(0.5)
            print("Try again")
            time.sleep(0.5)

def instructions():
    print('__________________________________')
    print('This calculator can do 5 tasks.\nThe options will be shown next')
    time.sleep(1)
    if input("press any key to continue\nType here -> ") == "1":
        menu()
    else:
        menu()

def menu():
    print ('__________________________________')
    print ('Press "1" to find circumference of a circle where you give the radius')
    print ('Press "2" to find area of a circle where you give the radius')
    print ('Press "3" to find volume of a sphere where give the radius')
    print ('Press "4" to find surface area of a sphere where you give the radius')
    print ('Press "5" to find largest square in a circle')
            # Will display instructions
            # input parameters: none needed
            # output parameters: None
            # Author:
            # Modified:

def circumference(r):
    return(r*2*math.pi)

def area(r):
    return((r**2*math.pi))

def volume(r):
    return((r**3)*math.pi*(4/3))

def surface_area(r):   
    return (((r**2)*math.pi)*4)

def square_in_circle(r):
    return ((r*(2**0.5))**2)


def main():
    while True:
        choice = input("Enter choice(1/2/3/4/5): ")

        if choice in ('1', '2', '3', '4', '5'):
            try:
                r = float(input("Enter radius: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            if choice == '1':
                x = (circumference(r))
                print("The circumference of your circle is ",round(x, 2))

            elif choice == '2':
                x = (area(r))
                print("The area of your circle is ",round(x, 2))

            elif choice == '3':
                x = (volume(r))
                print("The volume of your sphere is ", round(x, 2))

            elif choice == '4':
                x = (surface_area(r))
                print("The surface area of your sphere is ", round(x, 2))

            elif choice == '5':
                x = (square_in_circle(r))
                print("The maximal square in your circle has an area of ", round(x, 2))
            while True:
                next_calculation = input("Let's do next calculation? (yes/no): ")
                if next_calculation == "no":
                    print("Goodbye.")
                    time.sleep(0.5)
                    quit()
                elif next_calculation == "yes":
                    menu()
                    break
                else:
                    print('Answer with "yes" or "no" please.')
        else:
            print("Invalid Input")

    




        #keep giving options to choose menu options until they choose to exit
        #unMainMenu()
        #getInput()
        #use input to decide which function to run


if __name__ == "__main__":
    title()
    main()

