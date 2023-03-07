# Space functions
def triangle_s(height,base):
    s = height*base/2
    return s

def circle_s(radius):
    s = 3.14*radius**2
    return s

def square_s(side):
    s = side**2
    return s

def trapezius_s(height,base1,base2):
    s = (base1+base2)*height/2
    return s

def rhombus_s(diameter1,diameter2):
    s = diameter1*diameter2
    return s

def rectangle_s(width,length):
    s = width*length
    return s

# Environment functions
def triangle_e(side):
    e = side*3
    return e

def circle_e(radius):
    e = 3.14*radius*2
    return e

def square_e(side):
    e = side*4
    return e

def rhombus_e(side):
    e = side*4
    return e

def rectangle_e(width,length):
    e = (width+length)*2
    return e

# Volume functions
def globe(radius):
    v = 4/3 * 3.14 * radius**3
    return v

def cube(width,height,length):
    v = width*height*length
    return v

def cylinder(radius,height):
    v = height*3.14*radius**2
    return v

def triangle_prism(height,base,length):
    v = height*base/2*length
    return v

try :
    # Oprator recognize
    def detect_oprator(oprator):
        # Volume calculator
        if oprator == 'volume' :

            shape = str(input("Please enter the shape to calculate its volume (globe,cube,cylinder,triangle prism) :"))

            if shape == "globe" :
                radius = float(input("Please enter the radius :"))
                print("The volume of %s is"%("globe"),globe(radius))

            elif shape == "cube" :
                width = float(input("Please enter the width :"))
                height = float(input("Please enter the width :"))
                length = float(input("Please enter the width :"))
                print("The volume of %s is"%("cube"),cube(width,height,length))

            elif shape == "cylinder" :
                radius = float(input("Please enter the radius :"))
                height = float(input("Please enter the width :"))
                print("The volume of %s is"%("cylinder"),cylinder(radius,height))

            elif shape == "triangle prise" :
                height = float(input("Please enter the width :"))
                base = float(input("Please enter the base :"))
                length = float(input("Please enter the width :"))
                print("The volume of %s is"%("triangle prism"),triangle_prism(height,base,length))

            # Exeption handling(globe,cube,cylinder,triangle prism)
            else :
                print("Sorry! We can't calculate the volume of this shape.")

        # Space calculator
        elif oprator == 'space' :
            shape = str(input("Please enter the shape to calculate its space (triangle,circle,square,trapezius,rhombus,rectangle) :"))
            
            if shape == "triangle" :
                height = float(input("Please enter the height :"))
                base = float(input("Please enter the base :"))
                print("The space of %s is"%("triangle"),triangle_s(height,base))

            elif shape == "circle" :
                radius = float(input("Please enter the radius :"))
                print("The space of %s is"%("circle"),circle_s(radius))

            elif shape == "square" :
                s = float(input("Please enter the side :"))
                print("The space of %s is"%("square"),square_s(s))

            elif shape == "trapezius" :
                base_1 = float(input("Please enter the upper base :"))
                base_2 = float(input("Please enter the bottom base :"))
                height = float(input("Please enter the height :"))
                print("The space of %s is"%("trapezius"),trapezius_s(base_1,base_2,height))

            elif shape == "rhombus" :
                large_diameter = float(input("Please enter the large diameter :"))
                small_diameter = float(input("Please enter the small diameter :"))
                print("The space of %s is"%("rhombus"),rhombus_s(large_diameter,small_diameter))

            elif shape == "rectangle" :
                width = float(input("Please enter the width :"))
                length = float(input("Please enter the length :"))
                print("The space of %s is"%("rectangle"),rectangle_s(width,length))
            
            # Exeption handling(triangle,circle,square,trapezius,rhombus,rectangle)
            else :
                print("Sorry! We can't calculate the space of this shape.")
    
        # Environment calculator
        elif oprator == 'environment' :
            shape = str(input("Please enter the shape to calculate its environment (triangle,circle,square,rhombus,rectangle) :"))

            if shape == "triangle" :
                side = float(input("Please enter the side :"))
                print("The environment of %s is"%("triangle"),triangle_e(side))

            elif shape == "circle" :
                radius = float(input("Please enter the radius :"))
                print("The environment of %s is"%("circle"),circle_e(radius))

            elif shape == "square" :
                side = float(input("Please enter the side :"))
                print("The environment of %s is"%("square"),square_e(side))

            elif shape == "rhombus" :
                side = float(input("Please enter the side :"))
                print("The environment of %s is"%("rhombus"),rhombus_e(side))

            elif shape == "rectangle" :
                width = float(input("Please enter the width :"))
                length = float(input("Please enter the length :"))
                print("The environment of %s is"%("rectangle"),rectangle_e(width,length))

            # Exeption handling(triangle,circle,square,rhombus,rectangle)
            else :
                print("Sorry! We can't calculate the environment of this shape.")

        # Exeption handling(volume,space,environment)
        else : 
            print("Sorry! We can't recognize this oprator.")



except : 

    print("Somthing went wrong! Please enter an integer or float.")

else :
    # Welcom title
    print("""Welcome to space calculator.
_______________________________
-------------------------------""")
    # Program loop
    while True :

        # Get the oprator name
        oprator = str(input("Please enter an oprator to calculate (volume,space,environment) :"))
        detect_oprator(oprator)

        # Get a order to continue
        order = input("Do you wanna play again? please enter (y/n) :")

        # Exit the program
        if order == 'n' :
                print("Goodluck!")
                break
        
        # Play agine
        elif order == 'y' :
                pass
        
        # Exeption handling(y/n)
        else :
                print("Somthing went wrong! You didn't enter y or n.")
                break