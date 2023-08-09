from tkinter import *

def conversion():
    """Converts miles to kilometers"""
    value = miles_input.get()
    value_convert = round(float(value) * 1.60934, 2)
    km_value.config(text=f"{value_convert}")

window = Tk()
window.title("Miles to Kilometer")
window.minsize(width=300, height=100)

#Labels
miles_label = Label(text="Miles", font=("Arial", 10, "bold"))
miles_label.grid(column=7, row=0)

equals_label = Label(text="is equal to", font=("Arial", 10, "bold"))
equals_label.grid(column=4, row=1)

km_label = Label(text="km", font=("Arial", 10, "bold"))
km_label.grid(column=7, row=1)

km_value = Label(text="0", font=("Arial", 10, "bold"))
km_value.grid(column=6, row=1)

#Input

miles_input = Entry(width=10)
miles_input.grid(column=6, row=0)

#Button

button = Button(text="Convert", command=conversion)
button.grid(column=6, row=3)

window.mainloop()
