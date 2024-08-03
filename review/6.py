# from colorama import Style,  Back

# colors = [
#     ("red", Back.RED), 
#     ("green", Back.GREEN), 
#     ("blue", Back.BLUE), 
#     ("white", Back.WHITE), 
#     ("black", Back.BLACK)
# ]

# for c in colors:
#     print(c[1] + c[0] + Style.RESET_ALL, end=" ")
# x = open("test.txt", "w")
# print("hello", "sevin", sep="*", end=" ", file=x)
# print("welcome to python class", file=x)
import time
message = "welcome to python class"
for ch in message:
    print(ch, end="", flush=True)
    time.sleep(0.2)
    
# تمرین1     
# کد بالا را به گونه ای تغییر دهید که هر یک از کلمات با یک رنگ خاص نمایش داده شوند
# welcome     =>       green
# to          =>       blue
# python      =>       red
# class       =>       white

# تمرین 2
# یه متنی را از ورودی بگیرد و هر یک از کاراکترهای آن را با فاصله زمانی 
# 0.2 
# پرینت نمایید.