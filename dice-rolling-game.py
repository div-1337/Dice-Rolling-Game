
#CREDITS: Github/div-1337 and Github/aroravansh619




import random
from tkinter import *
from PIL import ImageTk, Image
import os

# CREATING THE MAIN WINDOW
home = Tk()
home.title("Ludo")
home.geometry("1920x1080")



shuffle_count = 0
shuffle_max = 8


def show_dice():
    global shuffle_count
    shuffle_count = 0
    ShuffleDice()



#FUNCTION WHICH SHOWS THE FINAL DICE

def ShowFinalDice():

    i = random.randint(1,6)
    image_path = os.path.join("dice_outcomes", f"dice{i}.png")
    openimg = Image.open(image_path)
    result = ImageTk.PhotoImage(openimg)
    dice.config(image = result)
    dice.image = result




# FUNCTION WHICH SHUFFLES THE DICE
def ShuffleDice():
   
    global shuffle_count
    if shuffle_count < shuffle_max:


            #DICE IMAGES    
        i = random.randint(1,6)
        image_path = os.path.join("dice_outcomes", f"dice{i}.png")
        openimg = Image.open(image_path)
        result = ImageTk.PhotoImage(openimg)
        dice.config(image = result)
        dice.image = result
            
            #DICE RESULT NUMBER
        dice_num.config(text = f"The dice's result is {i}")
        shuffle_count += 1
        home.after(100, ShuffleDice)


    else: 
    
        ShowFinalDice()



# BUTTON TO ROLL THE DICE
btn = Button(home, text="Roll The Dice", command = show_dice)
btn.pack()

# PICTURE OF THE DICE
dice = Label(home)
dice.pack()

# NUMBER OF THE DICE
dice_num = Label(home)
dice_num.pack()

home.mainloop()



