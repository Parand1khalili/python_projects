from tkinter import Tk, Label, Button, Entry, END
from tkinter.ttk import Treeview
from user import User

user_list = [
    User("Sina", "Kohgerd", "002123123123"),
    User("Asal", "Akbari", "002567567567"),
    User("Yekta", "Farzadnia", "00234534531"),
]

window = Tk()
window.title("Treeview Application")

window.grid_rowconfigure(2, weight=1)
window.grid_columnconfigure(0, weight=1)

header_label = Label(window, text="Treeview Application")
header_label.grid(row=0, column=0, pady=10, padx=10)


def show_user_form(firstname="", lastname="", nationalcode=""):
    user_form = Tk()
    if firstname == "":
        user_form.title("Create User Form")
    else:
        user_form.title("Update User Form")

    firstname_label = Label(user_form, text="First Name")
    firstname_label.grid(row=0, column=0, pady=10, padx=10, sticky="e")

    firstname_entry = Entry(user_form, width=30)
    firstname_entry.insert(0, firstname)
    firstname_entry.grid(row=0, column=1, pady=10, padx=(0, 20), sticky="w")

    lastname_label = Label(user_form, text="Last Name")
    lastname_label.grid(row=1, column=0, pady=(0, 10), padx=10, sticky="e")

    lastname_entry = Entry(user_form, width=30)
    lastname_entry.insert(0, lastname)
    lastname_entry.grid(row=1, column=1, pady=(0, 10), padx=(0, 20), sticky="w")

    nationalcode_label = Label(user_form, text="National Code")
    nationalcode_label.grid(row=2, column=0, pady=(0, 10), padx=10, sticky="e")

    nationalcode_entry = Entry(user_form, width=30)
    nationalcode_entry.insert(0, nationalcode)
    nationalcode_entry.grid(row=2, column=1, pady=(0, 10), padx=(0, 20), sticky="w")

    def submit():
        firstname_data = firstname_entry.get()
        lastname_data = lastname_entry.get()
        nationalcode_data = nationalcode_entry.get()

        #update
        if firstname != "":
            for user in user_list:
                if user.national_code == nationalcode:
                    user.first_name = firstname_data
                    user.last_name = lastname_data
                    user.national_code = nationalcode_data

        #insert            
        else:
            new_user = User(firstname_data, lastname_data, nationalcode_data)
            user_list.append(new_user)

        load_table()
        user_form.destroy()

    submit_button = Button(user_form, text="Submit", command=submit)
    submit_button.grid(row=3, column=1, pady=(0, 10), padx=0, sticky="w")

    user_form.mainloop()


insert_button = Button(window, text="Insert", command=show_user_form)
insert_button.grid(row=1, column=0, pady=(0, 10), padx=10, sticky="e")


def update_user():
    selection_item = table.selection()[0]
    for user in user_list:
        if user.national_code == selection_item:
            show_user_form(user.first_name, user.last_name, user.national_code)


update_button = Button(window, text="Update", command=update_user, state="disabled")
update_button.grid(row=1, column=0, pady=(0, 10), padx=10)


def delete_user():
    selected_items = table.selection()

    for item in selected_items:
        remove(item)

    load_table()


def remove(nationalcode):
    for user in user_list:
        if user.national_code == nationalcode:
            user_list.remove(user)
            


delete_button = Button(window, text="Delete", command=delete_user, state="disabled")
delete_button.grid(row=1, column=0, pady=(0, 10), padx=10, sticky="w")

table = Treeview(window, columns=("firstname", "lastname"))
table.grid(row=2, column=0, pady=(0, 10), padx=10, sticky="nsew")

table.heading("#0", text="NO")
table.heading("#1", text="First Name")
table.heading("#2", text="Last Name")

item_list = []


def load_table():
    for item in item_list:
        table.delete(item)

    item_list.clear()

    row_number = 1
    for user in user_list:
        item = table.insert("", END, iid=user.national_code, text=str(row_number),
                            values=(user.first_name, user.last_name))
        item_list.append(item)
        row_number += 1


load_table()

table.column("#0", width=70, anchor="w")
table.column("#1", anchor="w")
table.column("#2", anchor="w")


def button_management(event):
    selection_items = table.selection()

    if len(selection_items) == 1:
        update_button.config(state="normal")
        delete_button.config(state="normal")
    elif len(selection_items) > 1:
        update_button.config(state="disabled")
        delete_button.config(state="normal")
    else:
        update_button.config(state="disabled")
        delete_button.config(state="disabled")


table.bind("<<TreeviewSelect>>", button_management)

window.mainloop()
