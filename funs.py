"""
function addTwo(x, y) {
    return x + y;
}

let s = addTwo(4, 2)


"""


# global variable
PI = 3.14

def calculate_area_of_circle(radius):
    return PI * (radius * radius)
    

def addTwo(x, y):
    return x + y
    
s = addTwo(4, 2)
print(s)

area = calculate_area_of_circle(10)
# print ("Area of circle with radius 10 =" + str(area))

print ("Area of Circle with radius 10 = {}".format(area))