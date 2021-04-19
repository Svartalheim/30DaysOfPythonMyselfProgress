age = 17
height = 165.0
print('Complex number: ', 1+1j)

# triangle
base = int(input("Enter base: "))
height = int(input("Enter height: "))
area = (base * height)/2
print("The area of the triangle is", area)

# triangle side
a = int(input("Enter side a: "))
b = int(input("Enter side b: "))
c = int(input("Enter side c: "))
perimeter = a + b + c
print("The perimeter of the triangle is ", perimeter)

'''area + perimeter'''
length = int(input("Length: "))
width = int(input("Width: "))
area = length*width
perimeters = 2*(length+width)
print("The area of rectangle is: ", area, "\n And the perimeter is: ", perimeters)

# circle
radius = int(input("Enter radius: "))
pi = 3.14
circleArea = pi * (radius ** 2)
circumference = 2 * pi * radius
print("The area of circle is ", circleArea, "\n And the circumference is ", circumference)

# slope
xIntercept = 4
yIntercept = (2*xIntercept)-2
print("X-Intercept is ", xIntercept, "\nAnd the Y-Intercept is ", yIntercept)
print(xIntercept > yIntercept)
print(xIntercept < yIntercept)
print(xIntercept == yIntercept)

# kuadrat
kuadratX = -1.5
kuadratY = 0
kuadratTotal = (kuadratY**2) + (6*kuadratX) + 9
print("Kuadrat dari Y ", kuadratTotal)

print(len('python') == len('jargon'))  # False
print(len('python') != len('jargon'))  # True
print(len('python') < len('jargon'))   # True
print(len('python') != len('jargon'))      # False
print(len('python') == len('jargon'))      # True
print(len('python') == len('jargon'))  # True
print(len('python') > len('jargon'))   # False

print('I hope this course is not full of jargon.', 'jargon' in 'I hope this course is not full of jargon.')
print( "There is no 'on' in both dragon and python", not 'on' in 'python' and 'on' in 'jargon')
print(str(float(len('python'))))

number = int(input("Number: "))
if (number % 2) == 0 :
  print("Even")
else:
  print("Odd")

print(7//3 == int(2.7))
print(type('10') == type(10))
print(int('9.8') == 10)

a = 1
b = 2
c = 3
d = 4
e = 5
print("",a , a, a, a, a,"\n",b ,a ,b*a ,b*b ,b**3 ,"\n",c ,a ,c*a ,c*c , c**3,"\n",d ,a ,d*a ,d*d ,d**3,"\n",e ,a ,e*a ,e*e ,e**3)
