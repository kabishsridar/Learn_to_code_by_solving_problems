# defining a function named cone volume
def cone_volume():
    radius=float(input("enter radius(m): "))  # getting an input from user for radius
    height=float(input("enter height(m): "))  # getting an input from user for height
    volume=(1/3)*3.14*radius*radius*height # volume of cone is 1/3 *pi*r**2*h
    print("volume of the cone is: ",volume," m")
cone_volume()
# calling the function to execute
