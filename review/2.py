# name = 'Alenna'
# for i in range(3):
#  for i in name:
#     print(i+'!')
import datetime
q_a = {
    "who are you?" : "i'm  a chatbot",
    "time":datetime.datetime.now()
}

while True:
    user_q = input("say something, or 0 to exit") 
    if user_q == "0":
        break
    for question in q_a.keys():
        if user_q == question:
            print(q_a[user_q])