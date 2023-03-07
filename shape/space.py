# shapes function definition
def triangle(height,base):
    s = height*base/2
    return s

def circle(radius):
    s = 3.14*radius**2
    return s

def square(side):
    s = side**2
    return s

def trapezius(height,base1,base2):
    s = (base1+base2)*height/2
    return s

def rhombus(diameter1,diameter2):
    s = diameter1*diameter2
    return s

def rectangle(width,length):
    s = width*length
    return s



# exeption handling
try :

    # shapes detect function
    def space_detect(shape):
        
        if shape == "triangle" :
            height = float(input("Please enter the height :"))
            base = float(input("Please enter the base :"))
            print("The space of %s is"%("triangle"),triangle(height,base))

        elif shape == "circle" :
            radius = float(input("Please enter the radius :"))
            print("The space of %s is"%("circle"),circle(radius))

        elif shape == "square" :
            s = float(input("Please enter the side :"))
            print("The space of %s is"%("square"),square(s))

        elif shape == "trapezius" :
            base_1 = float(input("Please enter the upper base :"))
            base_2 = float(input("Please enter the bottom base :"))
            height = float(input("Please enter the height :"))
            print("The space of %s is"%("trapezius"),trapezius(base_1,base_2,height))

        elif shape == "rhombus" :
            large_diameter = float(input("Please enter the large diameter :"))
            small_diameter = float(input("Please enter the small diameter :"))
            print("The space of %s is"%("rhombus"),rhombus(large_diameter,small_diameter))

        elif shape == "rectangle" :
            width = float(input("Please enter the width :"))
            length = float(input("Please enter the length :"))
            print("The space of %s is"%("rectangle"),rectangle(width,length))
        
        else :
            print("Sorry! We can't calculate the space of this shape.")

# exeption handling
except:
     
     print("Somthing went wrong! Please enter a number.")

else:

    # welcom title
    print("""Welcome to space calculator.
_______________________________""")

    while True :
        # get the name of shape
        shape = str(input("Please enter the shape to calculate its space (triangle,circle,square,trapezius,rhombus,rectangle) :"))
        space_detect(shape)

        # get a order to continue
        order = input("Do you wanna play again? please enter y/n :")

        # exit the program
        if order == 'n' :
                print("Goodluck!")
                break
        # play agine
        elif order == 'y' :
                pass
        # exeption handling
        else :
                print("Somthing went wrong! You didn't enter y or n.")
                break