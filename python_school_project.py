from tkinter import *
from tkinter import messagebox
from random import randint
import sys 

# Varaibel
root = Tk()
root.title("Math Game")
root.geometry("200x150")

number_term_1 = 0
number_term_2 = 100

number_1 = randint(number_term_1, number_term_2)
number_2 = randint(number_term_1, number_term_2)

# Function
def creat_random_operation():
    operation_list = {
        "plus" : "+",
        "minus" : "-",
        "multi" : "*",
        "division" : "/"
    }

    random_numebr = randint(1, 4)

    if random_numebr == 1:
        return 1, operation_list["plus"] 
    elif random_numebr == 2:
        return 2, operation_list["minus"]
    elif random_numebr == 3:
        return 3, operation_list["multi"]
    else:
        return 4, operation_list["division"]

math_operation_number, operation = creat_random_operation()

def get_number_and_computing(entry):
    global status

    user_answer = entry.get()

    if math_operation_number == 1:
        if user_answer == number_1 + number_2:
            status = True
        else:
            status = False
    elif math_operation_number == 2:
        if user_answer == number_1 - number_2:
            status = True
        else:
            status = False
    elif math_operation_number == 3:
        if user_answer == number_1 * number_2:
            status = True
        else:
            status = False
    else:
        try:
            if user_answer == number_1 / number_2:
                status = True
            else:
                status = False
        except Exception as err:
            messagebox.showerror(
                "Divistion Error",
                str(err)
            )

def show_meessage():
    global status
    if status == False:
        text_meessage = "You Answer Is Wrong\nPlease Try Again!"
        return text_meessage
    else:
        text_meessage = "Your Answer Is True\nGood!"
        return text_meessage

# Creat a widget
number_label_1 = Label(
    root,
    text = str(number_1)
)

number_label_2 = Label(
    root,
    text = str(number_2)
)

math_operation_label = Label(
    root,
    text = operation
)

useranswer_entery = Entry(
    root
)

computing_button = Button(
    root,
    text = "Calcluate",
    command = lambda:get_number_and_computing(useranswer_entery)
)

status_label = Label(
    root,
    text = lambda:show_meessage()
)

# Packing the widget
number_label_1.place(
    x = 55,
    y = 5
)

number_label_2.place(
    x = 115,
    y = 5
)

math_operation_label.place(
    x = 90,
    y = 5
)

useranswer_entery.place(
    x = 17,
    y = 40
)

computing_button.place(
    x = 50,
    y = 70
)

status_label.place(
    x = 30,
    y = 120
)

root.mainloop()