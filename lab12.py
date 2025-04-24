#1
class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imaginary - other.imaginary)

    def __mul__(self, other):
        real = self.real * other.real - self.imaginary * other.imaginary
        imaginary = self.real * other.imaginary + self.imaginary * other.real
        return ComplexNumber(real, imaginary)
    def __truediv__(self, other):
        denominator = other.real ** 2 + other.imaginary ** 2
        real = (self.real * other.real + self.imaginary * other.imaginary) / denominator
        imaginary = (self.imaginary * other.real - self.real * other.imaginary) / denominator
        return ComplexNumber(real, imaginary)

    def __str__(self):
        sign = '+' if self.imaginary >= 0 else '-'
        return f"{self.real} {sign} {abs(self.imaginary)}i"


c1 = ComplexNumber(4, 5)    
c2 = ComplexNumber(2, -3)  

print("First Complex Number: ", c1)
print("Second Complex Number:", c2)
print("Addition:", c1 + c2)
print("Subtraction:", c1 - c2)
print("Multiplication:", c1 * c2)
print("Division:", c1 / c2)

#2
class Matrix:
    def __init__(self, data):
        if len(data) != 3 or any(len(row) != 3 for row in data):
            raise ValueError("Only 3x3 matrices are supported.")
        self.data = data

    def __add__(self, other):
        result = [
            [self.data[i][j] + other.data[i][j] for j in range(3)]
            for i in range(3)
        ]
        return Matrix(result)

    def __mul__(self, other):
        result = [
            [sum(self.data[i][k] * other.data[k][j] for k in range(3)) for j in range(3)]
            for i in range(3)
        ]
        return Matrix(result)

    def transpose(self):
        result = [
            [self.data[j][i] for j in range(3)]
            for i in range(3)
        ]
        return Matrix(result)

    def display(self):
        for row in self.data:
            print(row)
        print()
A = Matrix([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

B = Matrix([
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
])

print("Matrix A:")
A.display()

print("Matrix B:")
B.display()

C = A + B
print("A + B:")
C.display()

D = A * B
print("A * B:")
D.display()

print("Transpose of A:")
A_T = A.transpose()
A_T.display()

print("Transpose of B:")
B_T = B.transpose()
B_T.display()

#3
class solid:
    def __init__(self):
        pass
    def surfaceArea(self):
        pass
    def volume(self):
        pass
class cube:
    def __init__(self,side):
        self.side=side
    def surfaceArea(self):
        return 6*self.side*self.side
    def volume(self):
        return (self.side)**3
class cuboid:
    def __init__(self,l,b,h):
        self.l=l
        self.b=b
        self.h=h
    def surfaceArea(self):
        return 2*((self.l*self.b)+(self.b*self.h)+(self.h*self.l))
    def volume(self):
        return self.l*self.b*self.h
solid=cube(5)
print(solid.volume(),solid.surfaceArea())

#4
class Shape:
    def __init__(self):
        pass
    def perimeter():
        pass
class circle:
    def __init__(self,radius):
        self.r=radius
    def perimeter(self):
        return 2*3.14*self.radius
class square:
    def __init__(self,side):
        self.r=side
    def perimeter(self):
        return 4*self.side
class rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def perimeter(self):
        return 2*(self.length+self.breadth)
class equilateralTriangle:
    def __init__(self,side):
        self.base=side
    def perimeter(self):
        return 3*self.side

#5
class a:
    def __init__(self,hours,minutes,seconds):
        self.hours=hours
        self.minutes=minutes
        self.seconds=seconds
    def standardised(self):
        if(self.seconds>59):
            count=self.seconds//60
            self.seconds%=60
            self.minutes+=count
        if(self.minutes>59):
            count=self.minutes//60
            self.minutes%=60
            self.hours+=count
        if(self.hours>23):
            self.hours%=23
        return self.hours,self.minutes,self.seconds
    def __add__(self,other):
        self.hours+=other.hours
        self.minutes+=other.minutes
        self.seconds+=other.seconds
        self.standardised()
        return self.hours,self.minutes,self.seconds
    def __sub__(self,other):
        self.hours-=other.hours
        self.minutes-=other.minutes
        self.seconds-=other.seconds
        self.standardised()
        return self.hours,self.minutes,self.seconds
current=a(4,49,40)
early=a(2,12,30)
add=current+early
print(add)

#6
class Date:
    def __init__(self,date1):
        self.date1=date1
    def __eq__(self,other):
        for i in range(len(self.date1)):
            if self.date1[i]==other.date1[i]:
                continue
            else:
                return False
        return True
a=Date([20,10,12])
b=Date([20,11,12])
print(a==b) #false

#7
class Weather:
    def __init__(self, parameters):
        self.parameters = parameters

    def __contains__(self, item):
        return item in self.parameters

today_weather = Weather(["Temperature", "Humidity", "Pressure", "Wind", "Visibility"])

if "Humidity" in today_weather:
    print("Humidity data is available.")

if "Rainfall" not in today_weather:
    print("Rainfall data is not available.")

#8
class String:
    def __init__(self,string):
        self.string=string
    def __iadd__(self,other):
        self.string += other.string
        return self
    def toLower(self):
        return self.string.lower()
    def toUpper(self):
        return self.string.upper()
    def display(self):
        return self.string
s1=String("roniitt")
s2=String("RROONNIIITTT")
s1+=s2
upperCase=s1.toUpper()    
lowerCase=s2.toLower()    
print("s1+=s2",s1.display())
print(upperCase)
print(lowerCase)
