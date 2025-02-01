# x1 = int(input("enter a number: "))
# x2 = int(input("enter a number: "))

# if x1 % 2 == 0  or x2 % 2 == 0:
#     print("ok")
# my_tuple = ()
# for i in range(3):
#     x = float(input("> "))
#     my_tuple += (x,)
# print(my_tuple)
# c = 0
# for score in my_tuple:
#     if score == 20:
#         c += 1
# print(c)
            
# import turtle

# screen = turtle.Screen()
# message = turtle.textinput("my text", "enter something")
# char = turtle.textinput("char", "enter char")

# if char in message:
#     print("ok")
# else:
#     print("not ok")
# turtle.done()

# x = []
# s = 0
# g = 0
# for i in range(4):
#     a = int(input("enter a number:> "))
#     if a % 2 == 0:
#         s += a
#     if a > g:
#         g = a
#     x.append(a)
# print(s, g)

# x = ()
# y = ""
# for i in range(4):
#     a = input("enter a number:> ")
#     x += (a,)
#     if len(a) > len(y):
#         y = a
# print(x)
# print(y)


# friends = {}

# for i in range(5):
#     name = input("enter a name:> ")
#     age = int(input("enter an age:> "))
#     friends[name] = age
# print(friends)




# students = {}

# for i in range(5):
#     name = input("enter a name:> ")
#     class_number = int(input("enter class Number:> "))
#     students[name] = class_number
# print(students)
# students.popitem()
# print(students)


students_info = {}

# for i in range(5):
#     name = input("enter a name:> ")
#     student_score = float(input("enter student's score:> "))
#     students_info[name] = student_score
# print(students_info)
# students_info = {'armin': 18, 'babak': 11, 'sevin': 20, 'dara': 19, 'elena': 12}
# for x in students_info:
#     if students_info[x] > 17:
#         print(x)

# x = {
#     "name" : "sevin",
#     "age": 12
    
# }

# x["age"] = 10


# scores = {
#     "a" : 12,
#     "b" : 13,
#     "d" : 18,
#     "c" : 20,
    
# }

# for key in scores:
#     if scores[key] > 17 :
#         print(key)


# numbers = []
# for i in range(4):
#     x = int(input())
#     numbers.append(x)

# strings = ["a", "abcdef", "ab", "abc"]
# output = []

# for i in range(len(strings) -1, 0, -1):
#     for j in range(0, i):
#         if len(strings[j]) > len(strings[j + 1]):
#             strings[j], strings[j + 1] = strings[j + 1] , strings[j]

# print(strings)

# a = 1
# b = 2
# a,b = b,a

# print(a,b)


import turtle
import random
sc = turtle.Screen()

t= turtle.Turtle()

# def draw_shape(x,y):
#     sides = int(sc.numinput("sides", "enter sides number"))
#     color = sc.textinput("color", "enter the color")
#     t.penup()
#     t.goto(x,y)
#     t.pendown()
#     t.color(color)
#     for i in range(sides):
#         t.forward(80)
#         t.left(360/sides)
    
# t.write(1)
# sc.onclick(draw_shape)

# for i in range(5):
#     t.forward(80)
#     t.right(144)

colors = ("red", "blue", "black", "lightblue", "lightgreen", "darkgreen")
def draw_circle(x,y):
    t.penup()
    t.goto(x,y)
    t.color(random.choice(colors))
    t.pendown()
    t.begin_fill()
    t.circle(40)
    t.end_fill()

sc.onclick(draw_circle)

turtle.done()