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

def volume_detect(shape):

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

shape = str(input("Please enter the shape to calculate its volume (globe,cube,cylinder,triangle prism) :"))
volume_detect(shape)
