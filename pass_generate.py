import random
import tkinter as tk
import pyperclip
up_ltr = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
low_ltr = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
spec_sumbs = ['$', '#', '@', '&', '!', '?', '%', '/', '|', '~', '(', ')', '{', '}', '[', ']', '=', '+', '-', '_', '>', '<', '*', '^', ';']
password = []
def generate_password():
    password.clear()
    numb = int(entry.get())
    for numb in range (0, numb):
        a = random.randint(0,4)
        if a == 0:
            b = random.randint(0, len(up_ltr)-1)
            password.append(up_ltr[b])
        elif a == 1:
            b = random.randint(0, len(low_ltr)-1)
            password.append(low_ltr[b])
        elif a == 2:
            b = random.randint(0, len(digits)-1)
            password.append(digits[b])
        else:
            b = random.randint(0, len(spec_sumbs)-1)
            password.append(spec_sumbs[b])
        password1 = ''.join(password)
        pyperclip.copy(password1)
window = tk.Tk()
window.title('Password generator')
label = tk.Label(window, text= "Enter quantity of symbols")
label.pack()
entry = tk.Entry(window)
entry.pack()
entry.focus()
generate_button = tk.Button(window, text = 'Generate', command = generate_password)
generate_button.pack()
window.mainloop()




        
    
