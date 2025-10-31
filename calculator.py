print("==================")
print("Area Calculator 📐")
print("==================")

print("1) Triangle")
print("2) Rectangle")
print("3) Square")
print("4) Circle")
print("5) Quit")

shape = int(input("Which shape: "))
base = int(input("Base: "))
height = int(input("Height: "))

if shape ==1:
  area = base**2
elif shape ==2:
 area = base*height
elif shape ==3:
  area = (base*height)/2
elif shape ==4:
  area = 3.14*height**2

    
