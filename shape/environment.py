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

def environment_detect(shape):
        
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

shape = str(input("Please enter the shape to calculate its environment (triangle,circle,square,rhombus,rectangle) :"))
environment_detect(shape)
