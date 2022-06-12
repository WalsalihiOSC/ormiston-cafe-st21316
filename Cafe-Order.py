from tkinter import *


class InterfaceGUI:
    def __init__(self, parent):

        menu_frame = Frame(parent, bg="white")
        menu_frame.grid(row=0, column=0)
        #
        #
        # Creating COFFEE Menu
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
        change_frame.grid(row=4, column=1, columnspan=6)

        self.images = []
        self.images.append(PhotoImage(file="logo.png"))
        self.images.append(PhotoImage(file="first_image.png"))
        self.imageLabel_first = Label(coffee_frame, image=self.images[1], height=150,
                                      width=950, padx=20)
        self.imageLabel_first.grid(row=0, column=1, columnspan=7)

        # add label/title
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

        # Creating a COFFEE NAME checkbox list
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

        # Creating a COFFEE PRICE list
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

        # Creating entry box for quantity for COFFEE
        coffee_quantity_string = [
            " ", " ", " ", " ", " ", " ", " ", " ", " "]
        self.coffee_quantity = []

        for i in range(len(coffee_quantity_string)):
            self.coffee_quantity.append(
                Entry(quantity_frame, width=5, bg="#e3cbb3", font=("", 12), fg="black", borderwidth=None))

            self.coffee_quantity[i].var = v
            self.coffee_quantity[i].grid(
                column=4, rowspan=10, sticky=W, ipady=3, pady=4)

        # Adding arrow to move to the next frame
        self.btn_left = Button(change_frame,
                               text="<", command=lambda: self.raise_frame(coffee_frame))
        self.btn_right = Button(change_frame,
                                text=">", command=lambda: self.raise_frame(sandwiches_frame))
        self.btn_left.grid(row=4, column=4, sticky=W)
        self.btn_right.grid(row=4, column=5, sticky=E)

        #
        #
        #
        # Creating SANDWICHES menu

        sandwiches_frame = Frame(menu_frame,
                                 height=600, bg="white")
        sandwiches_frame.grid(row=0, column=1, rowspan=15)
        sandwiches_title_frame = Frame(
            sandwiches_frame,  bg="white")
        sandwiches_title_frame.grid(row=2, column=1, rowspan=5, pady=10)
        sandwiches_name_frame = Frame(sandwiches_frame, bg="white")
        sandwiches_name_frame.grid(row=3, column=2)
        sandwiches_price_frame = Frame(sandwiches_frame, bg="white")
        sandwiches_price_frame.grid(row=3, column=3)
        sandwiches_quantity_frame = Frame(sandwiches_frame, bg="white")
        sandwiches_quantity_frame.grid(row=3, column=4)
        sandwiches_change_frame = Frame(sandwiches_frame)
        sandwiches_change_frame.grid(row=4, column=1, columnspan=6)

        self.img = []
        self.img.append(PhotoImage(file="logo.png"))
        self.img.append(PhotoImage(file="second_image.png"))
        self.imageLabel_first = Label(sandwiches_frame, image=self.img[1], height=150,
                                      width=950, padx=20)
        self.imageLabel_first.grid(row=0, column=1, columnspan=7)

        # add label/title
        sandwiches = Label(sandwiches_title_frame, text="SANDWICHES",
                           font=("Comic Sans MS", 25, "bold"), bg="white")
        sandwiches.grid(row=1, column=1)
        coffee = Label(sandwiches_title_frame, text="Coffee",
                       font=("Comic Sans MS", 10, "bold"), bg="white")
        coffee.grid(row=2, column=1)
        dessert = Label(sandwiches_title_frame, text="Desert",
                        font=("Comic Sans MS", 10, "bold"), bg="white")
        dessert.grid(row=3, column=1)
        sides = Label(sandwiches_title_frame, text="Sides",
                      font=("Comic Sans MS", 10, "bold"), bg="white")
        sides.grid(row=4, column=1)

        price = Label(sandwiches_frame, text="$", bg="white")
        price.grid(row=2, column=3)
        quantity = Label(sandwiches_frame, text="Qty", bg="white")
        quantity.grid(row=2, column=4)

        # Creating a  SANDWICHES NAME checkbox list
        sandwiches_string = ["Egg", "Cheece", "Chicken", "Salad", "Chicken & Avocado",
                             "Bacon & Egg", "Beef & Egg", "Ham & Cheece"]
        self.check_btns = []
        for i in range(len(sandwiches_string)):  # set up each Checkbutton
            v = StringVar()
            self.check_btns.append(Checkbutton(sandwiches_name_frame, bg="white", width=20, fg="black", variable=v,
                                               anchor=W, font=("", 12), onvalue=sandwiches_string[i],
                                               offvalue="*",
                                               text=sandwiches_string[i]
                                               ))
            self.check_btns[i].var = v
            self.check_btns[i].deselect()
            self.check_btns[i].grid(
                column=2, rowspan=10, sticky=W, padx=0, ipady=5)

        # Creating a SANDWICHES PRICE price list
        sandwiches_price_string = ["4.00", "4.00",
                                   "4.00", "4.00", "5.00", "5.00", "5.00", "5.00", "5.00"]
        self.sandwiches_price = []
        for i in range(len(sandwiches_price_string)):  # set up each Label
            self.sandwiches_price.append(Label(sandwiches_price_frame, bg="white", font=("", 12), width=20, fg="black",

                                               text=sandwiches_price_string[i]
                                               ))
            self.sandwiches_price[i].var = v
            self.sandwiches_price[i].grid(
                column=3, rowspan=10, sticky=W, padx=0, ipady=5)

        # Creating entry box for quantity for SANDWICHES
        sandwiches_quantity_string = [
            " ", " ", " ", " ", " ", " ", " ", " ", " "]
        self.sandwiches_quantity = []

        for i in range(len(sandwiches_quantity_string)):
            self.sandwiches_quantity.append(
                Entry(sandwiches_quantity_frame, width=5, bg="#e3cbb3", font=("", 12), fg="black", borderwidth=None))

            self.sandwiches_quantity[i].var = v
            self.sandwiches_quantity[i].grid(
                column=4, rowspan=10, sticky=W, ipady=3, pady=4)

        self.btn_left = Button(sandwiches_change_frame,
                               text="<", command=lambda: self.raise_frame(coffee_frame))
        self.btn_right = Button(sandwiches_change_frame,
                                text=">", command=lambda: self.raise_frame(dessert_frame))
        self.btn_left.grid(row=4, column=4, sticky=W)
        self.btn_right.grid(row=4, column=5, sticky=E)

        #
        #
        #
        # Creating DESSERT menu

        dessert_frame = Frame(menu_frame,
                              height=600,  bg="white")
        dessert_frame.grid(row=0, column=1, rowspan=15)
        dessert_title_frame = Frame(dessert_frame, bg="white")
        dessert_title_frame.grid(row=2, column=1, rowspan=5, pady=10)
        dessert_name_frame = Frame(dessert_frame, bg="white")
        dessert_name_frame.grid(row=3, column=2)
        dessert_price_frame = Frame(dessert_frame, bg="white")
        dessert_price_frame.grid(row=3, column=3)
        dessert_quantity_frame = Frame(dessert_frame, bg="white")
        dessert_quantity_frame.grid(row=3, column=4)
        dessert_change_frame = Frame(dessert_frame)
        dessert_change_frame.grid(row=4, column=1, columnspan=6)

        self.pic = []
        self.pic.append(PhotoImage(file="logo.png"))
        self.pic.append(PhotoImage(file="third_image.png"))
        self.imageLabel_first = Label(dessert_frame, image=self.pic[1], height=150,
                                      width=950, padx=20)
        self.imageLabel_first.grid(row=0, column=1, columnspan=7)

        # add label/title
        dessert = Label(dessert_title_frame, text="DESSERT",
                        font=("Comic Sans MS", 25, "bold"), bg="white")
        dessert.grid(row=1, column=1)
        sandwiches = Label(dessert_title_frame, text="Sandwiches",
                           font=("Comic Sans MS", 10, "bold"), bg="white")
        sandwiches.grid(row=2, column=1)
        coffee = Label(dessert_title_frame, text="Coffee",
                       font=("Comic Sans MS", 10, "bold"), bg="white")
        coffee.grid(row=3, column=1)
        sides = Label(dessert_title_frame, text="Sides",
                      font=("Comic Sans MS", 10, "bold"), bg="white")
        sides.grid(row=4, column=1)
        price = Label(dessert_frame, text="$", bg="white")
        price.grid(row=2, column=3)
        quantity = Label(dessert_frame, text="Qty", bg="white")
        quantity.grid(row=2, column=4)

        # Creating a DESSERT NAME checkbox list
        dessert_string = ["Lava Cake", "Cheece Cake", "Carrot Cake", "Sponge Slice"
                          "Blueberry Cup-Cake", "Custard Slice", "Apple Slice", "Custard Pie", "Apple Pie"]
        self.check_btns = []
        for i in range(len(dessert_string)):  # set up each Checkbutton
            v = StringVar()
            self.check_btns.append(Checkbutton(dessert_name_frame, bg="white", width=20, fg="black", variable=v,
                                               anchor=W, font=("", 12), onvalue=dessert_string[i],
                                               offvalue="*",
                                               text=dessert_string[i]
                                               ))
            self.check_btns[i].var = v
            self.check_btns[i].deselect()
            self.check_btns[i].grid(
                column=2, rowspan=10, sticky=W, padx=0, ipady=5)

        # Creating a DESSERT PRICE list
        dessert_price_string = ["3.00", "3.00",
                                "3.00", "4.00", "3.00", "3.00", "3.00", "5.00", "5.00"]
        self.dessert_price = []
        for i in range(len(dessert_price_string)):  # set up each Label
            self.dessert_price.append(Label(dessert_price_frame, bg="white", font=("", 12), width=20, fg="black",

                                            text=dessert_price_string[i]
                                            ))
            self.dessert_price[i].var = v
            self.dessert_price[i].grid(
                column=3, rowspan=10, sticky=W, padx=0, ipady=5)

        # Creating entry box for quantity for DESSERT
        dessert_quantity_string = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        self.dessert_quantity = []

        for i in range(len(dessert_quantity_string)):
            self.dessert_quantity.append(
                Entry(dessert_quantity_frame, width=5, bg="#e3cbb3", font=("", 12), fg="black", borderwidth=None))

            self.dessert_quantity[i].var = v
            self.dessert_quantity[i].grid(
                column=4, rowspan=10, sticky=W, ipady=3, pady=4)

        self.btn_left = Button(dessert_change_frame,
                               text="<", command=lambda: self.raise_frame(sandwiches_frame))
        self.btn_right = Button(dessert_change_frame,
                                text=">", command=lambda: self.raise_frame(side_frame))
        self.btn_left.grid(row=4, column=4, sticky=W)
        self.btn_right.grid(row=4, column=5, sticky=E)

        #
        #
        #
        # Creating Side menu

        side_frame = Frame(menu_frame,
                           height=600,  bg="white")
        side_frame.grid(row=0, column=1, rowspan=15)
        side_title_frame = Frame(side_frame, bg="white")
        side_title_frame.grid(row=2, column=1, rowspan=5, pady=10)
        side_name_frame = Frame(side_frame, bg="white")
        side_name_frame.grid(row=3, column=2)
        side_price_frame = Frame(side_frame, bg="white")
        side_price_frame.grid(row=3, column=3)
        side_quantity_frame = Frame(side_frame, bg="white")
        side_quantity_frame.grid(row=3, column=4)
        side_change_frame = Frame(side_frame)
        side_change_frame.grid(row=4, column=1, columnspan=6)

        self.photos = []
        self.photos.append(PhotoImage(file="logo.png"))
        self.photos.append(PhotoImage(file="forth_image.png"))
        self.imageLabel_first = Label(side_frame, image=self.photos[1], height=150,
                                      width=950, padx=20)
        self.imageLabel_first.grid(row=0, column=1, columnspan=7)

        # add label/title
        side = Label(side_title_frame, text="SIDES",
                     font=("Comic Sans MS", 25, "bold"), bg="white")
        side.grid(row=1, column=1)
        sandwiches = Label(side_title_frame, text="Sandwiches",
                           font=("Comic Sans MS", 10, "bold"), bg="white")
        sandwiches.grid(row=2, column=1)
        dessert = Label(side_title_frame, text="Dessert",
                        font=("Comic Sans MS", 10, "bold"), bg="white")
        dessert.grid(row=3, column=1)
        coffee = Label(side_title_frame, text="Coffee",
                       font=("Comic Sans MS", 10, "bold"), bg="white")
        coffee.grid(row=4, column=1)
        price = Label(side_frame, text="$", bg="white")
        price.grid(row=2, column=3)
        quantity = Label(side_frame, text="Qty", bg="white")
        quantity.grid(row=2, column=4)

        # Creating a SIDE NAME checkbox list
        side_string = ["Chips", "Wedges", "Chicken Nuggets",
                       "Mash Potato", "Galic Bread", "Ham Bun", "Pizza Bread", "Sausage", "Spring Roll"]
        self.check_btns = []
        for i in range(len(side_string)):  # set up each Checkbutton
            v = StringVar()
            self.check_btns.append(Checkbutton(side_name_frame, bg="white", width=20, fg="black", variable=v,
                                               anchor=W, font=("", 12), onvalue=side_string[i],
                                               offvalue="*",
                                               text=side_string[i]
                                               ))
            self.check_btns[i].var = v
            self.check_btns[i].deselect()
            self.check_btns[i].grid(
                column=2, rowspan=10, sticky=W, padx=0, ipady=3)

        # Creating a SIDE PRICE list
        side_price_string = ["4.00", "4.00",
                             "4.00", "4.00", "3.00", "3.00", "3.00", "4.00", "4.00"]
        self.side_price = []
        for i in range(len(side_price_string)):  # set up each Label
            self.side_price.append(Label(side_price_frame, bg="white", font=("", 12), width=20, fg="black",

                                         text=side_price_string[i]
                                         ))
            self.side_price[i].var = v
            self.side_price[i].grid(
                column=3, rowspan=10, sticky=W, padx=0, ipady=6)

        # Creating entry box for quantity for SIDES
        side_quantity_string = [
            " ", " ", " ", " ", " ", " ", " ", " ", " "]
        self.side_quantity = []

        for i in range(len(side_quantity_string)):
            self.side_quantity.append(
                Entry(side_quantity_frame, width=5, bg="#e3cbb3", font=("", 12), fg="black", borderwidth=None))

            self.side_quantity[i].var = v
            self.side_quantity[i].grid(
                column=4, rowspan=10, sticky=W, ipady=3, pady=4)

        self.btn_left = Button(
            side_change_frame, text="<", command=lambda: self.raise_frame(dessert_frame))
        self.btn_right = Button(
            side_change_frame, text=">", command=lambda: self.raise_frame(side_frame))
        self.btn_left.grid(row=4, column=3, sticky=W)
        self.btn_right.grid(row=4, column=4, sticky=E)

        for frame in (coffee_frame, sandwiches_frame, dessert_frame, side_frame):
            frame.grid(row=0, column=1, sticky='news')

    def raise_frame(self, frame):
        frame.tkraise()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Ormiston Cafe")
    cafe = InterfaceGUI(root)
    root.mainloop()
