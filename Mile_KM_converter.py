from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=300)


# converter
def km():
    mile = float(mile_entry.get())
    converted_km = round(mile * 1.609)
    label_converted_km.config(text=f"{converted_km}")


# Entry
mile_entry = Entry(width=10)
mile_entry.grid(column=2, row=1)

# Label
label_mile = Label(text="Miles")
label_mile.grid(column=3, row=1)

label_equal = Label(text="is equal to")
label_equal.grid(column=1, row=2)

label_converted_km = Label(text=0)
label_converted_km.config(width=10)
label_converted_km.grid(column=2, row=2)

label_km = Label(text="km")
label_km.grid(column=3, row=2)

# Button
button_calculate = Button(text="Calculate", command=km)
button_calculate.grid(column=2, row=3)

window.mainloop()
