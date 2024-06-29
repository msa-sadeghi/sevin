# def add(a, b):
#     return a + b

# if __name__ == "__main__":
#     print(add(12, 13))



# l = [40, 200, 7000, 13, 10000]
# def find_max(l):
#     maximum = l[0]
#     for number in l:
#         if number > maximum:
#             maximum = number
#     return maximum

# print(find_max(l))

# a = "milk"
# b = "water"
# print(a, b)
# c = a
# a = b
# b = c

# print(a,b)

# a = "milk"
# b = "water"
# print(a, b)
# a,b = b,a

# print(a,b)
l = [5, 8, 1, 3, 2]

# l.sort()
# print(l)
def 
c =True
while c:
    c = False
    for i in range(len(l) - 1):
        if l[i] > l[i+1]:
            l[i], l[i+1] = l[i+1], l[i]
            c = True
print(l)