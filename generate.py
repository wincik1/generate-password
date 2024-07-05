import random
import tkinter

number_of_symbols = 8

def generate(number_of_symbols=6):
    import random
    symbols = []
    for i in range(number_of_symbols):
        num = random.randint(1, 3)
        if num == 1:
            symbols.append(random.choice('abcdefghijklmnopqrstuvwxyz'))
        elif num == 2:
            symbols.append(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
        elif num == 3:
            symbols.append(random.choice('0123456789'))
    password = ''.join(str(symb) for symb in symbols)
    text.delete('1.0', tkinter.END)
    text.insert('1.0', password)

window = tkinter.Tk()
window.config(background = "black")
window.title("Password")
window.geometry("800x600")

text = tkinter.Text(
    font=("arial", 40, "bold"),
    height = 1,
    width = number_of_symbols + 1,
    bg="black",
    fg="white",
    borderwidth=18
)
text.pack(expand=1)

tkinter.Button(
    text='Generate',
    font=("arial", 40, "bold"),
    bg="black",
    fg="white",
    command=lambda: generate(8)
).pack(expand = 1)

window.mainloop()
