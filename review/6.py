from colorama import Style,  Back

colors = [
    ("red", Back.RED), 
    ("green", Back.GREEN), 
    ("blue", Back.BLUE), 
    ("white", Back.WHITE), 
    ("black", Back.BLACK)
]

for c in colors:
    print(c[1] + c[0] + Style.RESET_ALL, end=" ")