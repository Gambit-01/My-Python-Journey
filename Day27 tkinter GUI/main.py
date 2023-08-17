import tkinter

def button_clicked():
    distance_miles = int(input.get())
    distance_km = round(distance_miles * 1.60934)
    my_label.config(text = f"{distance_km}")

# window
window = tkinter.Tk()
window.title("Great things have small Beginnings" )
window.minsize(width = 200, height = 150)
window.config(padx = 50, pady = 50)

# label to be converted to km
my_label = tkinter.Label(text = "0",font = ("Ariel", 24, "bold"))
my_label.grid(row = 1, column = 1)

# entry for user input
input = tkinter.Entry(width = 15, text = "0")
input.grid(row = 0, column = 1)
input.get()

# button for calculate
button = tkinter.Button(text = "calculate", command = button_clicked,font = ("Ariel", 24, "bold"))
button.grid(row = 2, column = 1)

# km_label
km_label = tkinter.Label(text = "km", font = ("Ariel", 24, "bold"))
km_label.grid(row = 1, column = 2)

# miles_label
mile_label = tkinter.Label(text = "miles", font = ("Ariel", 24, "bold"))
mile_label.grid(row = 0, column =2)

# is equal to label
equal_to = tkinter.Label(text = "is equal to",font = ("Ariel", 24, "bold"))
equal_to.grid(row = 1 , column = 0)
equal_to.config(pady = 20)






window.mainloop()