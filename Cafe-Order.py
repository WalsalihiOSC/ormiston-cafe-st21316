from tkinter import *


class InterfaceGUI:
    def __init__(self, parent):

        menu_frame = Frame(parent, bg="white")
        menu_frame.grid(row=0, column=0)
        order_frame = Frame(menu_frame, width=250, height=550,
                            bg="#e3cbb3")
        order_frame.grid(row=0, column=0)
        coffee_frame = Frame(menu_frame,
                             height=600,  bg="white")
        coffee_frame.grid(row=0, column=1, rowspan=15)
        title_frame = Frame(coffee_frame, bg="white")
        title_frame.grid(row=2, column=1, rowspan=5, pady=10)
        name_frame = Frame(coffee_frame, bg="white")
        name_frame.grid(row=3, column=2)
        price_frame = Frame(coffee_frame, bg="white")
        price_frame.grid(row=3, column=3)
        quantity_frame = Frame(coffee_frame, bg="white")
        quantity_frame.grid(row=3, column=4)
        change_frame = Frame(coffee_frame)
        change_frame.grid(row=4, column=1, columnspan=4)

        self.photos = []
        self.photos.append(PhotoImage(file="logo.png"))
        self.photos.append(PhotoImage(file="first_image.png"))
        self.imageLabel_first = Label(coffee_frame, image=self.photos[1], height=150,
                                      width=950, padx=20)
        self.imageLabel_first.grid(row=0, column=1, columnspan=7)
        # add label

        coffee = Label(title_frame, text="COFFEE",
                       font=("Comic Sans MS", 25, "bold"), bg="white")
        coffee.grid(row=1, column=1)
        sandwiches = Label(title_frame, text="Sandwiches",
                           font=("Comic Sans MS", 10, "bold"), bg="white")
        sandwiches.grid(row=2, column=1)
        dessert = Label(title_frame, text="Desert",
                        font=("Comic Sans MS", 10, "bold"), bg="white")
        dessert.grid(row=3, column=1)
        sides = Label(title_frame, text="Sides",
                      font=("Comic Sans MS", 10, "bold"), bg="white")
        sides.grid(row=4, column=1)
        espresso = Label(coffee_frame, text="ESPRESSO",
                         font=("Courier", 20, "bold"), bg="white")
        espresso.grid(row=1, column=2, rowspan=2)
        price = Label(coffee_frame, text="$", bg="white")
        price.grid(row=2, column=3)
        quantity = Label(coffee_frame, text="Qty", bg="white")
        quantity.grid(row=2, column=4)

        # Creating a 'coffee name' checkbox list
        cafe_string = ["Americano", "Cappuccino", "Double Espresso",
                       "Latte", "Macchiato", "Mint Chocolate", "Mocha", "White Mocha"]
        self.check_btns = []
        for i in range(len(cafe_string)):  # set up each Checkbutton
            v = StringVar()
            self.check_btns.append(Checkbutton(name_frame, bg="white", width=20, fg="black", variable=v,
                                               anchor=W, font=("", 12), onvalue=cafe_string[i],
                                               offvalue="*",
                                               text=cafe_string[i]
                                               ))
            self.check_btns[i].var = v
            self.check_btns[i].deselect()
            self.check_btns[i].grid(
                column=2, rowspan=10, sticky=W, padx=0, ipady=5)

        # Creating a 'coffee price list'
        coffee_price_string = ["5.00", "5.00",
                               "5.00", "5.00", "5.00", "5.00", "5.00", "5.00", "5.00"]
        self.coffee_price = []
        for i in range(len(coffee_price_string)):  # set up each Label
            self.coffee_price.append(Label(price_frame, bg="white", font=("", 12), width=20, fg="black",

                                           text=coffee_price_string[i]
                                           ))
            self.coffee_price[i].var = v
            self.coffee_price[i].grid(
                column=3, rowspan=10, sticky=W, padx=0, ipady=5)

        # Creating entry box for quantity
        coffee_quantity_string = [
            " ", " ", " ", " ", " ", " ", " ", " ", " "]
        self.coffee_quantity = []

        for i in range(len(coffee_quantity_string)):
            self.coffee_quantity.append(
                Entry(quantity_frame, width=5, bg="#e3cbb3", font=("", 12), fg="black", borderwidth=None))

            self.coffee_quantity[i].var = v
            self.coffee_quantity[i].grid(
                column=4, rowspan=10, sticky=W, ipady=3, pady=4)

        self.btn_right = Button(parent, text=">", command=self.moveRight)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Ormiston Cafe")
    cafe = InterfaceGUI(root)
    root.mainloop()
