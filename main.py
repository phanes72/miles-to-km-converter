from tkinter import *
from decimal import Decimal


def calculate_button_clicked():

    miles_value = input_Miles.get()
    km_value = Decimal(miles_value) * Decimal(1.6)

    km_label_output.config(text=str(round(km_value, 2)))


window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=250, height=100)

is_equal_to_label = Label(text="is equal to", font=("Arial", 12, "bold"))
is_equal_to_label.grid(column=1, row=2)

input_Miles = Entry(width=10)
input_Miles.grid(column=3, row=1)

miles_label = Label(text="Miles", font=("Arial", 12, "bold"))
miles_label.grid(column=4, row=1)

calculate_button = Button(text="Calculate", command=calculate_button_clicked)
calculate_button.grid(column=3, row=3)

km_label_output = Label(text="", font=("Arial", 12, "bold"))
km_label_output.grid(column=3, row=2)

km_label = Label(text="Km", font=("Arial", 12, "bold"))
km_label.grid(column=4, row=2)

window.mainloop()
