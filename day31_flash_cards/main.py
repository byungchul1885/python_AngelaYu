from tkinter import *
import pandas
import random
import logging as l

l.basicConfig(format='[%(asctime)s.%(msecs)03d] %(message)s', 
              level=l.INFO, datefmt='%I:%M:%S')

BACKGROUND_COLOR = "#B1DDC6"

curr_card_dict = {}
to_learn_list = []

def make_learn_list():
    global to_learn_list
    
    try:
        df = pandas.read_csv("data/words_to_learn.csv")
        l.info(f"pandas read_csv(). word_to_learn\n{df}")
    except FileNotFoundError:
        ori_df = pandas.read_csv("data/french_words.csv")
        l.info(f"pandas read_csv(). french_words\n{ori_df}")
        
        to_learn_list = ori_df.to_dict(orient="records")
        l.info(f"\n{to_learn_list}")
    else:
        # [
        #  {'French': 'partie', 'English': 'part'}, 
        #  {'French': 'histoire', 'English': 'history'},
        #  ...
        # ]
        to_learn_list = df.to_dict(orient="records")
        l.info(f"\n{to_learn_list}")


def next_card():
    global curr_card_dict, flip_timer
    
    window.after_cancel(flip_timer)
    curr_card_dict = random.choice(to_learn_list)
    
    # 화면에 카드 리프레시
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=curr_card_dict["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    # 3초 후 영어로 바꿔서    
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=curr_card_dict["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


def is_known():
    """아는 단어 --> 체크 버튼 클릭 """
    
    to_learn_list.remove(curr_card_dict)
    print(len(to_learn_list))
    
    df = pandas.DataFrame(to_learn_list) 
    df.to_csv("data/words_to_learn.csv", index=False)
    
    next_card()



window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(
    image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
known_button = Button(
    image=check_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

make_learn_list()

next_card()

window.mainloop()



