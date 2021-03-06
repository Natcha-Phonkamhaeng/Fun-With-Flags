import sys
import random
from tkinter import *
from PIL import ImageTk, Image
import os
from random import randint
from tkinter import messagebox


root = Tk()
root.title('Fun with flags')
root.geometry('400x400')

#Creating Menu bar
my_menu = Menu(root)
root.config(menu=my_menu)


# starting the game
def start():
    destroy_children_widget()
    flag_frame.pack(fill='both', expand=True)


    show_flags = Label(flag_frame)
    show_flags.pack(pady=15)

    list_flags = os.listdir('assets')

    answer_list = []
    count = 1


    while count < 5:
        random_flags = randint(0, len(list_flags) - 1)

        if count == 1:
            global answer
            answer = list_flags[random_flags].replace('.png','').title()

            global flags_img
            flags_img = ImageTk.PhotoImage(Image.open('assets/' + list_flags[random_flags]))
            show_flags.config(image=flags_img)

        answer_list.append(list_flags[random_flags])
        list_flags.remove(list_flags[random_flags])
        random.shuffle(list_flags)

        count += 1

    random.shuffle(answer_list)
    print(answer_list)
    print(answer)

    # Creating radio button choice
    global choice_var
    choice_var = StringVar()
    choice_var.set(None)

    choice_1 = Radiobutton(flag_frame, text=answer_list[0].replace('.png', '').title(), variable=choice_var, value=answer_list[0].replace('.png', '').title()).pack()
    choice_2 = Radiobutton(flag_frame, text=answer_list[1].replace('.png', '').title(), variable=choice_var, value=answer_list[1].replace('.png', '').title()).pack()
    choice_3 = Radiobutton(flag_frame, text=answer_list[2].replace('.png', '').title(), variable=choice_var, value=answer_list[2].replace('.png', '').title()).pack()
    choice_4 = Radiobutton(flag_frame, text=answer_list[3].replace('.png', '').title(), variable=choice_var, value=answer_list[3].replace('.png', '').title()).pack()

    # Creating 'Next' button to random flags image
    next_button = Button(flag_frame, text='Answer', command=is_correct)
    next_button.pack(pady=15)


def is_correct():
    if choice_var.get() == answer:
        messagebox.showinfo('Correct', 'CORRECT!!')
        start()
    else:
        messagebox.showinfo('Wrong Answer', 'Try Again')


def destroy_children_widget():
    for widget in title_frame.winfo_children():
        widget.destroy()

    for widget in flag_frame.winfo_children():
        widget.destroy()

    title_frame.pack_forget()
    flag_frame.pack_forget()


def color():
    pass

#Creating Menu items --> 'START' --> 'Start, Exit'
flags_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label='Option', menu=flags_menu)
flags_menu.add_command(label='Color', command=color)
flags_menu.add_separator()
flags_menu.add_command(label='Exit', command=root.quit)


# Creating title frame
title_frame = Frame(root, width=400, height=400, bg='light blue')
title_frame.pack(fill='both', expand=True)

title_label = Label(title_frame, text='Fun With Flags Game', font=('Comic Sans MS', 20, 'bold'), bg='light blue')
title_label.pack(pady=100)

title_button = Button(title_frame, text='Begin', command=start, width=20, font=('Comic Sans MS', 10, 'bold'))
title_button.pack()

# Creating Game Frame
flag_frame = Frame(root, width=400, height=400)

root.bind('<Escape>', lambda x: sys.exit())
root.mainloop()