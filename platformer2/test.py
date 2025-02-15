# import random
# import tkinter as tk

# def check_user_guess():
#     if int(user_value.get()) == secret_number:
#         label_output.config(text="correct")
#     elif int(user_value.get()) < secret_number:
#         label_output.config(text="your guess is less than secret number")
#     elif int(user_value.get()) > secret_number:
#         label_output.config(text="your guess is greater than secret number")
      
# root = tk.Tk()
# user_value = tk.StringVar()
# label = tk.Label(root, text="enter a number between 1 - 100")
# label.pack()
# entry = tk.Entry(root, textvariable=user_value)
# entry.pack()
# button = tk.Button(root, text="submit", command=check_user_guess)
# button.pack()
# label_output = tk.Label(root, text="")
# label_output.pack()
# def generate_secret_number():
#     return random.randint(1,100)

# secret_number = generate_secret_number()
# root.mainloop()
             
        
            
import pygame
screen = pygame.display.set_mode((400, 300))
pygame.init()
user_text = ''
input_rect = pygame.Rect(200, 200, 140, 30)
f = pygame.font.SysFont("arial", 20)
active = False
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(event.pos):
                active  = True
                
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                user_text = user_text[:-1]
            else:
                user_text += event.unicode
                
    pygame.draw.rect(screen, "green", input_rect)  
    u_t = f.render(user_text, True, "red")   
    if active:
        screen.blit(u_t, input_rect.topleft)  
    pygame.display.update()