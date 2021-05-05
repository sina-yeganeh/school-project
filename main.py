from tkinter import *
from sys import exit
from setting import (
    ROOT_NAME,
    ROOT_BACKGROUND,
    WINDOW_SIZE,
    FONT,
    TEXT_SIZE,
    TEXT_COLOR,
    BACKGROUND_BUTTON_COLOR,
    IMAGE_LIST_NAME
)

def write_log(error):
    with open("log_error.log", 'a') as file:
        file.write(str(error))

def load_images(name):
    try:
        image = PhotoImage(
            file=name
        )
    except:
        pass
    else:
        return image

# def make_window():
#     try:
#         global root
#         root = Tk()
#         root.title(GAME_NAME)
#         root.geometry(WINDOW_SIZE)
#     except Exception as err:
#         write_log(err)
#     else:
#         return root

def make_text(window_position, label_text, x_position, y_position):
    try:
        lbl = Label(
            window_position,
            text=label_text,
            fg=TEXT_COLOR,
            bg=ROOT_BACKGROUND
        ).grid(row=x_position, column=y_position)
    except Exception as err:
        write_log(err)
    else:
        return lbl

def make_buuton(window_position, button_text, button_image, x_position, y_position):
    global btn
    try:
        btn = Button(
            window_position,
            text=button_text,
            bg=BACKGROUND_BUTTON_COLOR,
            fg=TEXT_COLOR,
            # width=3,
            # height=3,
            # image=button_image,
            command=lambda:show_image(button_image)
        )
        btn.grid(row=x_position, column=y_position)
    except Exception as err:
        write_log(err)
    else:
        return btn

def show_image(button_image):
    btn.configure(
        image=button_image
    )

if __name__ == '__main__':
    root = Tk()
    root.title(ROOT_NAME)
    root.geometry(WINDOW_SIZE)

    CAT    = load_images(IMAGE_LIST_NAME[0])
    COVID  = load_images(IMAGE_LIST_NAME[1])
    MASK   = load_images(IMAGE_LIST_NAME[2])
    PYTHON = load_images(IMAGE_LIST_NAME[3])
    FINISH = load_images(IMAGE_LIST_NAME[4])

    # welcome_lbl = make_text(root, "Hello From Sina!", 0, 0)
    
    button_1 = make_buuton(root, None, CAT, 0, 0)
    button_2 = make_buuton(root, None, CAT, 0, 1)
    button_3 = make_buuton(root, None, COVID, 0, 2)
    button_4 = make_buuton(root, None, MASK, 1, 0)
    button_5 = make_buuton(root, None, COVID, 1, 1)
    button_6 = make_buuton(root, None, MASK, 1, 2)
    button_7 = make_buuton(root, None, PYTHON, 3, 0)
    button_8 = make_buuton(root, None, PYTHON, 3, 1)

    # root_background = make_text(root, None, 0, 0)
    root.mainloop()