import os

file_names = os.listdir("./images")
for f_n in file_names:
    os.rename(
        f"./images/{f_n}", 
        f"./images/{f_n}".replace(" ", "").replace("(", "").replace(")", "")
              )
    
    