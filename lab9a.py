#1
def q1():
    def fun():
        print("This is fun function")
    def disp():
        print("This is disp function")
    def msg():
        print("This is msg function")
    l=[fun,disp,msg]
    for i in l:
        i()
q1()

#2
def q2():
    l1=[1,2,3,4,5,6]
    l2=[6,5,4,3,2,1]
    l=list(map(lambda x,y:x+y,l1,l2))
    print(l)
q2()

#3
import random
def q3():
    l=[random.randint(-15,15) for i in range(10)]
    sq_l=list(map(lambda x:x*x,l))
    print(sq_l)
q3()

#4
def q4():
    lst = ['madam','Python',"malayalam",12321]
    def isPalindrome(s):
        if(type(s)==str):
            if(s[::-1]==s[::]):
                return True
            else:
                return False
        else:
            return False
    l=list(filter(isPalindrome,lst))
    print(l)
q4()

#5
def q5():
    def filterFaculty(faculty:list):
        return list(filter(lambda x: True if len(x)>8 else False,faculty))
    print(filterFaculty(["FVA J","JHQAFVC","GYUKVDCQA","GYYLwcblwlcja"]))
q5()
