from tkinter import *
from random import * 

window = Tk()
window.title("Rock Paper Scissor With Tkinter.")
window.geometry("600x600")
window.config(bg="grey")


rock_image = PhotoImage(file="image/rock.png")
paper_image = PhotoImage(file="image/paper.png")
scissors_image = PhotoImage(file="image/scissor.png")


image_list = [rock_image, paper_image, scissors_image]
random_number = randint(0,2)
disp_image = Label(window, width=200, height=200, bg="grey")
disp_image.pack(pady=50)
user_score_label = Label(window, text="Your Score: ", bg="Blue")
user_score_label.pack()

computer_score_label = Label(window, text="Computer's Score: ", bg="Blue")
computer_score_label.pack()
computer_score_label.place(x=470, y=330)


if random_number == 0:
    computer_choice = "r"
elif random_number == 1:
    computer_choice = "p"
elif random_number == 2:
    computer_choice = "s"


comparison_dict = {
    "rock" : {"r":1 , "p":0 , "s":2},
    "paper" : {"r":2 , "p":1 , "s":0},
    "scissors" : {"r":0 , "p":2 , "s":1}
}


def rock():
    if computer_choice == "r":
        label_result.config(text="It's a Tie!!! \n Your Choice: Rock | Computer's Choice: Rock")
        disp_image.config(image=rock_image, bg="grey")
    elif computer_choice == "p":
        label_result.config(text="You Lost!!! \n Your Choice: Rock | Computer's Choice: Paper")
        disp_image.config(image=paper_image, bg="grey")
    elif computer_choice == "s":
        label_result.config(text="You Won!!! \n Your Choice: Rock | Computer's Choice: Scissors")
        disp_image.config(image=scissors_image, bg="grey")
def scissors():
    if computer_choice == "s":
        label_result.config(text="It's a Tie!!! \n Your Choice: Scissors | Computer's Choice: Scissors")
        disp_image.config(image=scissors_image, bg="grey")
    elif computer_choice == "r":
        label_result.config(text="You Lost!!! \n Your Choice: Scissors | Computer's Choice: Rock")
        disp_image.config(image=rock_image, bg="grey")
    elif computer_choice == "p":
        label_result.config(text="You Won!!! \n Your Choice: Scissors | Computer's Choice: Paper")
        disp_image.config(image=paper_image, bg="grey")
def paper():
    if computer_choice == "p":
        label_result.config(text="It's a Tie!!! \n Your Choice: Paper | Computer's Choice: Paper")
        disp_image.config(image=paper_image, bg="grey")
    elif computer_choice == "s":
        label_result.config(text="You Lost!!! \n Your Choice: Paper | Computer's Choice: Scissors")
        disp_image.config(image=scissors_image, bg="grey")
    elif computer_choice == "r":
        label_result.config(text="You Won!!! \n Your Choice: Paper | Computer's Choice: Rock")
        disp_image.config(image=rock_image, bg="grey")

def reset():
    global disp_image
    global computer_choice
    random_number = randint(0,2)
    if random_number == 0:
        computer_choice = "r"
    elif random_number == 1:
        computer_choice = "p"
    elif random_number == 2:
        computer_choice = "s"
    disp_image = Label(window ,image="" ,width=200, height=200)
    label_result['text'] = ""

rock_button = Button(window, text="Rock", command=rock, width=7)
rock_button.place(x=230, y=320)
paper_button = Button(window, text="Paper", command=paper, width=7)
paper_button.place(x=290, y=320)
scissors_button = Button(window, text="Scissors", command=scissors, width=7)
scissors_button.place(x=350, y=320)
reset_button = Button(window, text="Reset", command=reset, width=7)
reset_button.place(x=290, y=350)
label_result = Label(window, text="")
label_result.pack(pady=85)


window.mainloop()