from tkinter import *
import pandas as pd
import time

#Wait 3 secs to change flip the card, then wait for user to click approve or disapprove, attach approved cards to a dict, and unapproved pnes to a dict.

BACKGROUND_COLOR = "#B1DDC6"
window = Tk()
window.title("Flashcard Game: Learn Interactively!")
window.config(width=800,height=600,bg=BACKGROUND_COLOR,padx=50,pady=50)
"----------------------------------------------------Database--------------------------------------------------------------------------"

# Data file
file = "./data/french_words.csv"
count_fr = 0
count_eng = 0
french_word = None
data = pd.read_csv(file)
french_words = data["French"].tolist()
english_words = data["English"].tolist()
english_word = None
#--------------------------------------------------#

learned_dict = {}
not_learned_dict = {}

is_game_on = True
def flip_card():
    global canvas_back,back_text_p,english_words,english_word,count_eng,is_game_on

    try:
        english_word = english_words[count_eng]
        print(f'This is count for english: {count_eng}')
    except IndexError:
        canvas_back.itemconfig(back_text_p,text="Congrats! You finished the series.",font=("Arial",20,"bold"))
        is_game_on == False
    else:
        canvas_front.grid_remove()
        canvas_back.itemconfig(back_text_p,text=english_word)
        canvas_back.grid(column=0, row=0, columnspan=2)




#Use this to flip back to french word and append to app or disapp list based on user preference.
def next():
    global count,french_words,french_word,front_text_p,canvas_back,is_game_on
    try:
        french_word = french_words[count_fr]
        print(f'This is count for french: {count_fr}')
    except IndexError:
        canvas_back.grid_remove()
        canvas_front.grid(column=0, row=0, columnspan=2)
        canvas_front.itemconfig(front_text_p, text="Congrats! You completed the series.", font=("Arial", 20, "bold"))
        is_game_on == False
    else:
        canvas_back.grid_remove()
        canvas_front.itemconfig(front_text_p, text=french_word)
        canvas_front.grid(column=0, row=0, columnspan=2)
        window.after(3000,flip_card)

def next_word():
    global count_eng,count_fr
    count_eng +=1
    count_fr +=1

def approve_append():
    global learned_dict,french_word,english_word,french_words,count_fr
    if count_fr < len(french_words):
        learned_dict[french_words[count_fr - 1]] = english_word
        print(learned_dict)


def disapprove_append():
    global not_learned_dict,french_word,english_word,french_words,count_fr
    if count_fr < len(french_words):
        not_learned_dict[french_words[count_fr - 1]] = english_word
        print(not_learned_dict)

def initialize_game():
    global count_fr
    canvas_front.itemconfig(front_text_p,text=french_words[0])
    count_fr +=1
    window.after(3000,flip_card)



"---------------------------- GUI SETTINGS---------------------------------------------------------------------------"

card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
approve_image = PhotoImage(file="./images/right.png")
disapprove_image = PhotoImage(file="./images/wrong.png")

canvas_front = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR,)
canvas_front.create_image(400, 526 / 2, image=card_front_img)
canvas_front.grid(column=0, row=0, columnspan=2)

canvas_back = Canvas(width=800,height=526,highlightthickness=0,bg=BACKGROUND_COLOR)
canvas_back.create_image(400,526/2,image=card_back_img)
back_text_title = canvas_back.create_text(400,150,text="English",font=("Arial",40,"italic"))
back_text_p = canvas_back.create_text(400,263,text="English word",font=("Arial",60,"bold"))




approve_b = Button(image=approve_image,highlightthickness=0,bg=BACKGROUND_COLOR,command= lambda:[next(),approve_append(),next_word()])
approve_b.grid(column=0,row=1)

disapprove_b = Button(image=disapprove_image,highlightthickness=0,bg=BACKGROUND_COLOR,command= lambda:[next(),disapprove_append(),next_word()])
disapprove_b.grid(column=1,row=1)


front_text_title = canvas_front.create_text(400, 150, text="French", font=("Arial", 40, "italic"))
front_text_p = canvas_front.create_text(400, 263, text="", font=("Arial", 60, "bold"))



initialize_game()






window.mainloop()
