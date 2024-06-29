# l = [5, 8, 1, 3, 2]
# search_for = 8
# result = "not found"

# i = 0
# while i < len(l):
#     if search_for == l[i]:
#         result = "found"
#         break
#     i += 1
# print(result)


l = [2, 3, 5, 8, 11, 12, 18]
search_for = 18
found = False
i = 0
j = len(l) - 1
while i <= j and not found:
    middle = (i + j) // 2
    if search_for == l[middle]:
        found = True
    elif search_for < l[middle]:
        j = middle - 1
    elif search_for > l[middle]:
        i = middle + 1
if found:
    print("found")
else:
    print("not found")



# for number in l:
#     if number == search_for:
#         result = "found"
#         break
    
# print(result)