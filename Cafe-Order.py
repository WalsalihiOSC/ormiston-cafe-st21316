from tkinter import *
from tkinter.font import Font


class InterfaceGUI:
    def __init__(self, parent):

        coffee_frame = Frame(parent, width=200, height=500, bg="#e3cbb3")
        coffee_frame.grid(row=0, column=0, rowspan=15)
        main_frame = Frame(parent, width=400, height=500, bg="white")
        menu_frame = Frame(main_frame, width=200, height=500, bg="white")
        menu_frame.grid(row=1, column=2, rowspan=14)
        price_frame = Frame(main_frame, width=100, height=500, bg="white")
        price_frame.grid(row=3, column=3, rowspan=13)
        quantity_frame = Frame(main_frame, width=100, height=500, bg="white")
        price_frame.grid(row=3, column=4, rowspan=13)
        main_frame.grid(row=0, column=1, rowspan=15, columnspan=3)

        # Label
        coffee_label = Label(menu_frame, text="Coffee", font=("Raleway", 16))
        coffee_label.grid(row=2, column=1)

        # Creating a 'coffee name' checkbox list
        cafe_string = ["Americano", "Cappuccino", "Double Espresso",
                       "Latte", "Macchiato", "Mint Chocolate", "Mocha", "White Mocha"]
        self.check_btns = []
        for i in range(len(cafe_string)):  # set up each Checkbutton
            v = StringVar()
            self.check_btns.append(Checkbutton(menu_frame, width=20, variable=v,
                                               anchor=W, onvalue=cafe_string[i],
                                               offvalue="*",
                                               text=cafe_string[i]
                                               ))
            self.check_btns[i].var = v
            self.check_btns[i].deselect()
            self.check_btns[i].grid(column=2, rowspan=10, sticky=W)

        # Creating a 'coffee price list'
        coffee_price_string = ["$", "5.00", "5.00",
                               "5.00", "5.00", "5.00", "5.00", "5.00", "5.00", "5.00"]
        self.coffee_price = []
        for i in range(len(coffee_price_string)):  # set up each Label
            q = StringVar()
            self.coffee_price.append(Label(price_frame, width=20,
                                           anchor=E,
                                           text=coffee_price_string[i]
                                           ))
            self.coffee_price[i].var = v
            self.coffee_price[i].grid(sticky=W)

        # Creating entry box for quantity
        coffee_quantity_string = ["", "",
                                  "", "", "", "", "", "", ""]
        self.coffee_quantity_entry = []
        for i in range(len(coffee_quantity_string)):

            self.coffee_quantity_entry.append(Entry(quantity_frame, width=20,
                                                    ))
            self.coffee_quantity_entry[i].var = v
            self.coffee_quantity_entry[i].grid(sticky=W)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Ormiston Cafe")
    cafe = InterfaceGUI(root)
    root.mainloop()
