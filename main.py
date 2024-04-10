from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#A34343"
FONT_NAME = "Ariel"
current_card = {}
pokemon_img_list = []

df = pd.read_csv('pokemon.csv')
data = df[["pokedex_number", "name", "japanese_name"]].to_dict(orient='records')

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = data[random.randint(1, 721)] #1~721
    canvas.itemconfig(card_title, text="")
    canvas.itemconfig(card_word, text="")
    canvas.itemconfig(canvas_image, image=pokemon_img_list[current_card["pokedex_number"] - 1])
    count_down(3)


def show_answer():
    canvas.itemconfig(card_title, text=f'No.{current_card["pokedex_number"]} {current_card["name"]}')
    canvas.itemconfig(card_word, text=current_card["japanese_name"])


def count_down(count):
    global flip_timer
    if count > 0:
        canvas.itemconfig(timer_text, text=f"{count}")
        flip_timer = window.after(1000, count_down, count - 1)
    else:
        canvas.itemconfig(timer_text, text="")
        show_answer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flash Pokemon Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

#store images into a list
for i in range(1, 722):
    pokemon_img = PhotoImage(file=f"./pokemon/{i}.png")
    pokemon_img_list.append(pokemon_img)

#canvas
canvas = Canvas(width=800, height=500, highlightthickness=0, bg=BACKGROUND_COLOR)
pokemon_img = PhotoImage(file="./pokemon/448-mega.png")
canvas_image = canvas.create_image(400, 250, image=pokemon_img)
card_title = canvas.create_text(400, 50, text="", font=(FONT_NAME, 40, "italic"), fill="white")
card_word = canvas.create_text(400, 425, text="", font=(FONT_NAME, 40, "bold"), fill="white")
timer_text = canvas.create_text(100, 50, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

#button
# button_img = PhotoImage(file="./images/button.png")
button = Button(text="Next", highlightthickness=0, command=next_card, bg="#C0D6E8", width=20, font=(FONT_NAME, 20, "bold"))
button.grid(column=0, row=1, columnspan=2)

flip_timer = window.after(3000, func=show_answer)
next_card()

window.mainloop()
