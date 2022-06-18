from tkinter import *
from tkinter.scrolledtext import ScrolledText


class InterfaceGUI:
    def __init__(self, parent):
        self.root = Frame(parent, bg="white")
        self.root.grid(row=0, column=0)
        self.student_detail = Frame(
            self.root, bg="white", width=650, height=550)
        self.student_detail.grid(row=0, column=0)
        self.student_detail.grid_propagate(0)
        self.window = Frame(self.root, bg="white", width=650, height=550)
        self.window.grid(row=0, column=0)
        self.main_frame = Frame(self.window, bg="#e3cbb3")
        self.main_frame.grid(row=0, column=0)
        self.menu_frame = Frame(self.main_frame, bg="white")
        self.menu_frame.grid(row=0, column=0)
        self.order_frame = Frame(self.menu_frame, width=350, height=550,
                                 bg="#e3cbb3")
        self.order_frame.grid(row=0, column=0)
        self.order_frame.grid_propagate(0)
        detail_order = Frame(self.menu_frame, width=300,
                             height=400, bg="white")
        detail_order.grid(row=0, column=0)
        detail_order.grid_propagate(0)

        #
        #
        #
        # Creating LABEL and BUTTON for ORDER FRAME
        append = Button(
            self.order_frame, text="Append Order", bd=0, bg="#EEDFD1", command=self.append)
        append.grid(row=1, column=0, padx=30)
        coffirm_order = Button(
            self.order_frame, text="Confirm Order", bd=0, bg="#EEDFD1", command=lambda: [self.hide_frame(self.window), self.show_frame(self.student_detail)])
        coffirm_order.grid(row=1, column=2, pady=390, padx=2)
        reset_order = Button(
            self.order_frame, text="Reset Order", bd=0, bg="#EEDFD1")
        reset_order.grid(row=1, column=3, padx=2)
        self.scroll = ScrolledText(detail_order, height=22, width=30)
        self.scroll.grid(row=2, column=1, padx=20, pady=20)

        #
        #
        # Creating COFFEE Menu

        self.coffee_frame = Frame(self.menu_frame,
                                  height=600,  bg="white")
        self.coffee_frame.grid(row=0, column=1, rowspan=15)
        title_frame = Frame(self.coffee_frame, bg="white")
        title_frame.grid(row=2, column=1, rowspan=5, pady=10)
        name_frame = Frame(self.coffee_frame, bg="white")
        name_frame.grid(row=3, column=2)
        price_frame = Frame(self.coffee_frame, bg="white")
        price_frame.grid(row=3, column=3)
        quantity_frame = Frame(self.coffee_frame, bg="white")
        quantity_frame.grid(row=3, column=4)
        change_frame = Frame(self.coffee_frame)
        change_frame.grid(row=4, column=1, columnspan=6)

        self.qmages = []
        self.qmages.append(PhotoImage(file="logo_image.png"))
        self.qmages.append(PhotoImage(file="first_image.png"))
        self.qmageLabel_first = Label(self.coffee_frame, image=self.qmages[1], height=150,
                                      width=950, padx=20)
        self.qmageLabel_first.grid(row=0, column=1, columnspan=7)
        self.qmageLabel_first = Label(self.order_frame, image=self.qmages[0], height=100,
                                      width=100, padx=20, bg="#e3cbb3")
        self.qmageLabel_first.grid(row=0, column=0, columnspan=7)

        # add label/title
        coffee = Label(title_frame, text="COFFEE",
                       font=("Comic Sans MS", 25, "bold"), bg="white")
        coffee.grid(row=1, column=1)
        sandwiches = Button(title_frame, text="Sandwiches",
                            font=("Comic Sans MS", 10, "bold", "underline"), bg="white", bd=0, command=lambda: self.raise_frame(sandwiches_frame))
        sandwiches.grid(row=2, column=1)
        dessert = Button(title_frame, text="Desert",
                         font=("Comic Sans MS", 10, "bold", "underline"), bg="white", bd=0, command=lambda: self.raise_frame(self.dessert_frame))
        dessert.grid(row=3, column=1)
        sides = Button(title_frame, text="Sides",
                       font=("Comic Sans MS", 10, "bold", "underline"), bg="white", bd=0, command=lambda: self.raise_frame(self.side_frame))
        sides.grid(row=4, column=1)
        espresso = Label(self.coffee_frame, text="ESPRESSO",
                         font=("Courier", 20, "bold"), bg="white")
        espresso.grid(row=1, column=2, rowspan=2)
        price = Label(self.coffee_frame, text="$", bg="white")
        price.grid(row=2, column=3)
        quantity = Label(self.coffee_frame, text="Qty", bg="white")
        quantity.grid(row=2, column=4)

        # Creating a COFFEE NAME checkbox list
        self.cafe_string = ["Americano", "Cappuccino", "Double Espresso",
                            "Latte", "Macchiato", "Mint Chocolate", "Mocha", "White Mocha"]
        self.cafe_check_btns = []
        for self.c in range(len(self.cafe_string)):  # set up each Checkbutton
            self.v = StringVar()
            self.cafe_check_btns.append(Checkbutton(name_frame, bg="white", width=20, fg="black", variable=self.v,
                                                    anchor=W, font=("", 12), onvalue=self.cafe_string[self.c],
                                                    offvalue="*",
                                                    text=self.cafe_string[self.c]
                                                    ))
            self.cafe_check_btns[self.c].var = self.v
            self.cafe_check_btns[self.c].deselect()
            self.cafe_check_btns[self.c].grid(
                column=2, rowspan=10, sticky=W, padx=0, ipady=5)

        # Creating a COFFEE PRICE list
        coffee_price_string = ["5.00", "5.00",
                               "5.00", "5.00", "5.00", "5.00", "5.00", "5.00", "5.00"]
        self.coffee_price = []
        for i in range(len(coffee_price_string)):  # set up each Label
            self.coffee_price.append(Label(price_frame, bg="white", font=("", 12), width=20, fg="black",

                                           text=coffee_price_string[i]
                                           ))
            self.coffee_price[i].var = self.v
            self.coffee_price[i].grid(
                column=3, rowspan=10, sticky=W, padx=0, ipady=5)

        # Creating entry box for quantity for COFFEE
        self.coffee_quantity_string = [
            " ", " ", " ", " ", " ", " ", " ", " ", " "]
        self.coffee_quantity = []

        for i in range(len(self.coffee_quantity_string)):
            self.coffee_quantity.append(
                Entry(quantity_frame, width=5, bg="#e3cbb3", font=("", 12), fg="black", borderwidth=None))

            self.coffee_quantity[i].var = self.v
            self.coffee_quantity[i].grid(
                column=4, rowspan=10, sticky=W, ipady=3, pady=4)

        # Adding arrow to move to the next frame
        self.btn_left = Button(change_frame,
                               text="<", command=lambda: self.raise_frame(self.coffee_frame))
        self.btn_right = Button(change_frame,
                                text=">", command=lambda: self.raise_frame(sandwiches_frame))
        self.btn_left.grid(row=4, column=4, sticky=W)
        self.btn_right.grid(row=4, column=5, sticky=E)

        #
        #
        #
        # Creating SANDWICHES menu

        sandwiches_frame = Frame(self.menu_frame,
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

        self.qmg = []
        self.qmg.append(PhotoImage(file="second_image.png"))
        self.qmageLabel_first = Label(sandwiches_frame, image=self.qmg[0], height=150,
                                      width=950, padx=20)
        self.qmageLabel_first.grid(row=0, column=1, columnspan=7)

        # add label/title
        sandwiches = Label(sandwiches_title_frame, text="SANDWICHES",
                           font=("Comic Sans MS", 25, "bold"), bg="white")
        sandwiches.grid(row=1, column=1)
        coffee = Button(sandwiches_title_frame, text="Coffee",
                        font=("Comic Sans MS", 10, "bold", "underline"), bg="white", bd=0, command=lambda: self.raise_frame(self.coffee_frame))
        coffee.grid(row=2, column=1)
        dessert = Button(sandwiches_title_frame, text="Desert",
                         font=("Comic Sans MS", 10, "bold", "underline"), bg="white", bd=0, command=lambda: self.raise_frame(self.dessert_frame))
        dessert.grid(row=3, column=1)
        sides = Button(sandwiches_title_frame, text="Sides",
                       font=("Comic Sans MS", 10, "bold", "underline"), bg="white", bd=0, command=lambda: self.raise_frame(self.side_frame))
        sides.grid(row=4, column=1)

        price = Label(sandwiches_frame, text="$", bg="white")
        price.grid(row=2, column=3)
        quantity = Label(sandwiches_frame, text="Qty", bg="white")
        quantity.grid(row=2, column=4)

        # Creating a  SANDWICHES NAME checkbox list
        self.sandwiches_string = ["Egg", "Cheece", "Chicken", "Salad", "Chicken & Avocado",
                                  "Bacon & Egg", "Beef & Egg", "Ham & Cheece"]
        self.check_btns = []
        for i in range(len(self.sandwiches_string)):  # set up each Checkbutton
            self.v = StringVar()
            self.check_btns.append(Checkbutton(sandwiches_name_frame, bg="white", width=20, fg="black", variable=self.v,
                                               anchor=W, font=("", 12), onvalue=self.sandwiches_string[i],
                                               offvalue="*",
                                               text=self.sandwiches_string[i]
                                               ))
            self.check_btns[i].var = self.v
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
            self.sandwiches_price[i].var = self.v
            self.sandwiches_price[i].grid(
                column=3, rowspan=10, sticky=W, padx=0, ipady=5)

        # Creating entry box for quantity for SANDWICHES
        self.sandwiches_quantity_string = [
            " ", " ", " ", " ", " ", " ", " ", " ", " "]
        self.sandwiches_quantity = []

        for i in range(len(self.sandwiches_quantity_string)):
            self.sandwiches_quantity.append(
                Entry(sandwiches_quantity_frame, width=5, bg="#e3cbb3", font=("", 12), fg="black", borderwidth=None))

            self.sandwiches_quantity[i].var = self.v
            self.sandwiches_quantity[i].grid(
                column=4, rowspan=10, sticky=W, ipady=3, pady=4)

        self.btn_left = Button(sandwiches_change_frame,
                               text="<", command=lambda: self.raise_frame(self.coffee_frame))
        self.btn_right = Button(sandwiches_change_frame,
                                text=">", command=lambda: self.raise_frame(self.dessert_frame))
        self.btn_left.grid(row=4, column=4, sticky=W)
        self.btn_right.grid(row=4, column=5, sticky=E)

        #
        #
        #
        # Creating DESSERT menu

        self.dessert_frame = Frame(self.menu_frame,
                                   height=600,  bg="white")
        self.dessert_frame.grid(row=0, column=1, rowspan=15)
        dessert_title_frame = Frame(self.dessert_frame, bg="white")
        dessert_title_frame.grid(row=2, column=1, rowspan=5, pady=10)
        dessert_name_frame = Frame(self.dessert_frame, bg="white")
        dessert_name_frame.grid(row=3, column=2)
        dessert_price_frame = Frame(self.dessert_frame, bg="white")
        dessert_price_frame.grid(row=3, column=3)
        dessert_quantity_frame = Frame(self.dessert_frame, bg="white")
        dessert_quantity_frame.grid(row=3, column=4)
        dessert_change_frame = Frame(self.dessert_frame)
        dessert_change_frame.grid(row=4, column=1, columnspan=6)

        self.pic = []
        self.pic.append(PhotoImage(file="third_image.png"))
        self.qmageLabel_first = Label(self.dessert_frame, image=self.pic[0], height=150,
                                      width=950, padx=20)
        self.qmageLabel_first.grid(row=0, column=1, columnspan=7)

        # add label/title
        dessert = Label(dessert_title_frame, text="DESSERT",
                        font=("Comic Sans MS", 25, "bold"), bg="white")
        dessert.grid(row=1, column=1)
        sandwiches = Button(dessert_title_frame, text="Sandwiches",
                            font=("Comic Sans MS", 10, "bold", "underline"), bg="white", bd=0, command=lambda: self.raise_frame(sandwiches_frame))
        sandwiches.grid(row=2, column=1)
        coffee = Button(dessert_title_frame, text="Coffee",
                        font=("Comic Sans MS", 10, "bold", "underline"), bg="white", bd=0, command=lambda: self.raise_frame(self.coffee_frame))
        coffee.grid(row=3, column=1)
        sides = Button(dessert_title_frame, text="Sides",
                       font=("Comic Sans MS", 10, "bold", "underline"), bg="white", bd=0, command=lambda: self.raise_frame(self.side_frame))
        sides.grid(row=4, column=1)
        price = Label(self.dessert_frame, text="$", bg="white")
        price.grid(row=2, column=3)
        quantity = Label(self.dessert_frame, text="Qty", bg="white")
        quantity.grid(row=2, column=4)

        # Creating a DESSERT NAME checkbox list
        self.dessert_string = ["Lava Cake", "Cheece Cake", "Carrot Cake", "Sponge Slice"
                               "Blueberry Cup-Cake", "Custard Slice", "Apple Slice", "Custard Pie", "Apple Pie"]
        self.check_btns = []
        for i in range(len(self.dessert_string)):  # set up each Checkbutton
            self.v = StringVar()
            self.check_btns.append(Checkbutton(dessert_name_frame, bg="white", width=20, fg="black", variable=self.v,
                                               anchor=W, font=("", 12), onvalue=self.dessert_string[i],
                                               offvalue="*",
                                               text=self.dessert_string[i]
                                               ))
            self.check_btns[i].var = self.v
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
            self.dessert_price[i].var = self.v
            self.dessert_price[i].grid(
                column=3, rowspan=10, sticky=W, padx=0, ipady=5)

        # Creating entry box for quantity for DESSERT
        self.dessert_quantity_string = [
            " ", " ", " ", " ", " ", " ", " ", " ", " "]
        self.dessert_quantity = []

        for i in range(len(self.dessert_quantity_string)):
            self.dessert_quantity.append(
                Entry(dessert_quantity_frame, width=5, bg="#e3cbb3", font=("", 12), fg="black", borderwidth=None))

            self.dessert_quantity[i].var = self.v
            self.dessert_quantity[i].grid(
                column=4, rowspan=10, sticky=W, ipady=3, pady=4)

        self.btn_left = Button(dessert_change_frame,
                               text="<", command=lambda: self.raise_frame(sandwiches_frame))
        self.btn_right = Button(dessert_change_frame,
                                text=">", command=lambda: self.raise_frame(self.side_frame))
        self.btn_left.grid(row=4, column=4, sticky=W)
        self.btn_right.grid(row=4, column=5, sticky=E)

        #
        #
        #
        # Creating Side menu

        self.side_frame = Frame(self.menu_frame,
                                height=600,  bg="white")
        self.side_frame.grid(row=0, column=1, rowspan=15)
        side_title_frame = Frame(self.side_frame, bg="white")
        side_title_frame.grid(row=2, column=1, rowspan=5, pady=10)
        side_name_frame = Frame(self.side_frame, bg="white")
        side_name_frame.grid(row=3, column=2)
        side_price_frame = Frame(self.side_frame, bg="white")
        side_price_frame.grid(row=3, column=3)
        side_quantity_frame = Frame(self.side_frame, bg="white")
        side_quantity_frame.grid(row=3, column=4)
        self.side_change_frame = Frame(self.side_frame, bg="white")
        self.side_change_frame.grid(row=4, column=1, columnspan=8)

        self.photos = []
        self.photos.append(PhotoImage(file="forth_image.png"))
        self.qmageLabel_first = Label(self.side_frame, image=self.photos[0], height=150,
                                      width=950, padx=20)
        self.qmageLabel_first.grid(row=0, column=1, columnspan=6)

        # add label/title
        side = Label(side_title_frame, text="SIDES",
                     font=("Comic Sans MS", 25, "bold",), bg="white")
        side.grid(row=1, column=1)
        sandwiches = Button(side_title_frame, text="Sandwiches",
                            font=("Comic Sans MS", 10, "bold", "underline"), bg="white", bd=0, command=lambda: self.raise_frame(sandwiches_frame))
        sandwiches.grid(row=2, column=1)
        dessert = Button(side_title_frame, text="Dessert",
                         font=("Comic Sans MS", 10, "bold", "underline"), bg="white", bd=0, command=lambda: self.raise_frame(self.dessert_frame))
        dessert.grid(row=3, column=1)
        coffee = Button(side_title_frame, text="Coffee",
                        font=("Comic Sans MS", 10, "bold", "underline"), bg="white", bd=0, command=lambda: self.raise_frame(self.coffee_frame))
        coffee.grid(row=4, column=1)
        price = Label(self.side_frame, text="$", bg="white")
        price.grid(row=2, column=3)
        quantity = Label(self.side_frame, text="Qty", bg="white")
        quantity.grid(row=2, column=4, sticky=W, padx=32)

        # Creating a SIDE NAME checkbox list
        self.side_string = ["Chips", "Wedges", "Chicken Nuggets",
                            "Mash Potato", "Galic Bread", "Ham Bun", "Pizza Bread", "Sausage", "Spring Roll"]
        self.check_btns = []
        for i in range(len(self.side_string)):  # set up each Checkbutton
            self.v = StringVar()
            self.check_btns.append(Checkbutton(side_name_frame, bg="white", width=20, fg="black", variable=self.v,
                                               anchor=W, font=("", 12), onvalue=self.side_string[i],
                                               offvalue="*",
                                               text=self.side_string[i]
                                               ))
            self.check_btns[i].var = self.v
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
            self.side_price[i].var = self.v
            self.side_price[i].grid(
                column=3, rowspan=10, sticky=W, padx=0, ipady=6)

        # Creating entry box for quantity for SIDES
        self.side_quantity_string = [
            " ", " ", " ", " ", " ", " ", " ", " ", " "]
        self.side_quantity = []

        for self.q in range(len(self.side_quantity_string)):
            self.side_quantity.append(
                Entry(side_quantity_frame, width=5, bg="#e3cbb3", font=("", 12), fg="black", borderwidth=None))

            self.side_quantity[self.q].grid(
                column=4, rowspan=10, sticky=W, ipady=3, pady=4)

        # Move <> Button
        self.btn_left = Button(
            self.side_change_frame, text="<", command=lambda: self.raise_frame(self.dessert_frame))
        self.btn_right = Button(
            self.side_change_frame, text=">", command=lambda: self.raise_frame(self.side_frame))
        self.btn_left.grid(row=5, column=2, sticky=W)
        self.btn_right.grid(row=5, column=3, sticky=E)

        # Validation text
        self.error = Label(side_quantity_frame, text="", bg="white", width=20)
        self.error.grid(row=105, columnspan=2, column=4)
        #
        #
        #

        #
        self.detail_frame = Frame(
            self.student_detail, bg="#e3cbb3", width=650, height=500)
        self.detail_frame.grid(row=0, column=0)
        student_frame = Frame(self.student_detail, bg="#e3cbb3")
        student_frame.grid(row=1, column=1)

        self.pho = []
        self.pho.append(PhotoImage(file="fifth_image.png"))
        self.imageLabel_first = Label(self.student_detail, image=self.pho[0], height=150,
                                      width=1227, padx=20)
        self.imageLabel_first.grid(row=0, column=0, columnspan=7)

        # Adding Label
        first_name = Label(student_frame, text="First Name:",
                           bg="#e3cbb3", font=("", 12, "bold"))
        first_name.grid(row=1, column=2, padx=60, pady=10)
        last_name = Label(student_frame, text="Last Name:",
                          bg="#e3cbb3", font=("", 12, "bold"))
        last_name.grid(row=1, column=3, padx=60, pady=10)
        year_level = Label(student_frame, text="Year Level: ",
                           bg="#e3cbb3", font=("", 12, "bold"))
        year_level.grid(row=1, column=4, padx=60, pady=10)
        contact = Label(
            student_frame, text="Contact Details - Email:", bg="#e3cbb3", font=("", 12, "bold"))
        contact.grid(row=1, column=5,  padx=60, pady=10)
        new_order = Button(student_frame, text="New Order", bd=0, bg="#EEDFD1",
                           command=lambda: [self.show_frame(self.window), self.raise_frame(self.coffee_frame), self.hide_frame(self.student_detail)])
        new_order.grid(row=3, column=5, padx=10, pady=10)

        # Adding entry box
        first_n = Entry(student_frame, width=30, font=("", 10))
        first_n.grid(row=2, column=2, padx=60, pady=5)
        last_n = Entry(student_frame, width=30, font=("", 10))
        last_n.grid(row=2, column=3, padx=60, pady=5)
        year_l = Entry(student_frame, width=15, font=("", 10))
        year_l.grid(row=2, column=4, padx=60, pady=5)
        con = Entry(student_frame, width=30, font=("", 10))
        con.grid(row=2, column=5, padx=60, pady=5)

        for frame in (self.coffee_frame, sandwiches_frame, self.dessert_frame, self.side_frame, self.detail_frame):
            frame.grid(row=0, column=1, sticky='news')

        # Event Binding (interactive label)
        coffee.bind("<coffee_btn>", self.raise_frame(
            self.coffee_frame), self.hide_frame(self.student_detail))

    def raise_frame(self, frame):
        frame.tkraise()

    def append(self):
        for self.c in range(len(self.cafe_check_btns)):
            if self.cafe_check_btns[self.c].var.get() != "*":
                self.scroll.insert(END, "Please type in qantity in number")

    def confirm(self):
        self.main_frame.destroy()

    def hide_frame(self, frame):
        frame.grid_forget()

    def show_frame(self, frame):
        frame.grid()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Ormiston Cafe")
    cafe = InterfaceGUI(root)
    root.mainloop()
