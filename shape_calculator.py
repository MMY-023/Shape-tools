# Space functions
def triangle_s(height,base):
    return height*base/2

def circle_s(radius): 
    return 3.14*radius**2

def square_s(side):
    return side**2

def trapezius_s(height,base1,base2):
    return (base1+base2)*height/2

def rhombus_s(diameter1,diameter2):
    return diameter1*diameter2

def rectangle_s(width,length):
    return width*length

# Environment functions
def triangle_e(side):
    return side*3

def circle_e(radius):
    return 3.14*radius*2

def square_e(side):
    return side*4

def rhombus_e(side):
    return side*4

def rectangle_e(width,length):
    return (width+length)*2

# Volume functions
def globe(radius):
    return 4/3 * 3.14 * radius**3

def cube(width,height,length):
    return width*height*length

def cylinder(radius,height):
    return height*3.14*radius**2

def triangle_prism(height,base,length):
    return height*base/2*length

# Oprator recognize
def detect_oprator(oprator):
        # Volume calculator
        if oprator == 'volume' :
            # get a shape name to start the calculate volume opration
            shape = input("Please enter the shape to calculate its volume (globe,cube,cylinder,triangle prism) :")

            if shape == "globe" :
                # Exception handling(integer,float)
                try :
                    radius = float(input("Please enter the radius :"))
                except :
                    print("Something went wrong! Please enter an integer or float")
                else :   
                    print("The volume of globe is",globe(radius))

            elif shape == "cube" :
                # Exception handling(integer,float)
                try :
                    width = float(input("Please enter the width :"))
                    height = float(input("Please enter the height :"))
                    length = float(input("Please enter the length :"))
                except :
                    print("Something went wrong! Please enter an integer or float")
                else :
                    print("The volume of cube is",cube(width,height,length))
          
            elif shape == "cylinder" :
                # Exception handling(integer,float)
                try : 
                    radius = float(input("Please enter the radius :"))
                    height = float(input("Please enter the width :"))
                except :
                    print("Something went wrong! Please enter an integer or float")
                else:
                    print("The volume of cylinder is",cylinder(radius,height))

            elif shape == "triangle prise" :
                # Exception handling(integer,float)
                try :
                    height = float(input("Please enter the width :"))
                    base = float(input("Please enter the base :"))
                    length = float(input("Please enter the width :"))
                except :
                    print("Something went wrong! Please enter an integer or float")
                else :
                    print("The volume of triangle prism is",triangle_prism(height,base,length))

            # Exeption handling(globe,cube,cylinder,triangle prism)
            else :
                print("Sorry! We can't calculate the volume of this shape.")

        # Space calculator
        elif oprator == 'space' :
            # get a shape name to start the calculate volume opration
            shape = input("Please enter the shape to calculate its space (triangle,circle,square,trapezius,rhombus,rectangle) :")
            
            if shape == "triangle" :
                # Exception handling(integer,float)
                try :
                    height = float(input("Please enter the height :"))
                    base = float(input("Please enter the base :"))
                except :
                    print("Something went wrong! Please enter an integer or float")   
                else :
                    print("The space of triangle is",triangle_s(height,base))

            elif shape == "circle" :
                # Exception handling(integer,float)
                try :
                    radius = float(input("Please enter the radius :"))
                except :
                    print("Something went wrong! Please enter an integer or float") 
                else :
                    print("The space of circle is",circle_s(radius))

            elif shape == "square" :
                # Exception handling(integer,float)
                try :
                    side = float(input("Please enter the side :"))
                except :
                    print("Something went wrong! Please enter an integer or float")   
                else :  
                    print("The space of square is",square_s(side))

            elif shape == "trapezius" :
                # Exception handling(integer,float)
                try :
                    base_1 = float(input("Please enter the upper base :"))
                    base_2 = float(input("Please enter the bottom base :"))
                    height = float(input("Please enter the height :"))
                except : 
                    print("Something went wrong! Please enter an integer or float")  
                else :  
                    print("The space of trapezius is",trapezius_s(base_1,base_2,height))

            elif shape == "rhombus" :
                # Exception handling(integer,float)
                try :
                    large_diameter = float(input("Please enter the large diameter :"))
                    small_diameter = float(input("Please enter the small diameter :"))
                except :    
                    print("Something went wrong! Please enter an integer or float")      
                else :  
                    print("The space of rhombus is",rhombus_s(large_diameter,small_diameter))

            elif shape == "rectangle" :
                # Exception handling(integer,float)
                try :
                    width = float(input("Please enter the width :"))
                    length = float(input("Please enter the length :"))
                except :
                    print("Something went wrong! Please enter an integer or float")
                else :
                    print("The space of rectangle is",rectangle_s(width,length))
            
            # Exeption handling(triangle,circle,square,trapezius,rhombus,rectangle)
            else :
                print("Sorry! We can't calculate the space of this shape.")
    
        # Environment calculator
        elif oprator == 'environment' :
            # get a shape name to start the calculate volume opration
            shape = input("Please enter the shape to calculate its environment (triangle,circle,square,rhombus,rectangle) :")

            if shape == "triangle" :
                # Exception handling(integer,float)
                try :
                    side = float(input("Please enter the side :"))
                except :
                    print("Something went wrong! Please enter an integer or float")
                else :   
                    print("The environment of triangle is",triangle_e(side))

            elif shape == "circle" :
                # Exception handling(integer,float)
                try :
                    radius = float(input("Please enter the radius :"))
                except :
                    print("Something went wrong! Please enter an integer or float")
                else :
                    print("The environment of circle is",circle_e(radius))

            elif shape == "square" :
                # Exception handling(integer,float)
                try :
                    side = float(input("Please enter the side :"))
                except :
                    print("Something went wrong! Please enter an integer or float")
                else :
                    print("The environment of square is",square_e(side))

            elif shape == "rhombus" :
                # Exception handling(integer,float)
                try :
                    side = float(input("Please enter the side :"))
                except :
                    print("Something went wrong! Please enter an integer or float")
                else :
                    print("The environment of rhombus is",rhombus_e(side))

            elif shape == "rectangle" :
                # Exception handling(integer,float)
                try :
                    width = float(input("Please enter the width :"))
                    length = float(input("Please enter the length :"))
                except :
                    print("Something went wrong! Please enter an integer or float")
                else :
                    print("The environment of rectangle is",rectangle_e(width,length))

            # Exeption handling(triangle,circle,square,rhombus,rectangle)
            else :
                print("Sorry! We can't calculate the environment of this shape.")

        # Exeption handling(volume,space,environment)
        else : 
            print("Sorry! We can't recognize this oprator.")

# Welcom title
print("""Welcome to shape calculator.
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
