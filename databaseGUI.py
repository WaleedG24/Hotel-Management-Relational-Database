"""
-----------------------------------------------
File: databaseGUI.py
Authors: Group 40
Course: CP363
Date: 2023-03-26
-----------------------------------------------
"""
import tkinter as tk
from tkinter import scrolledtext
import GUI_Functions

# Create the main window
root = tk.Tk()
root.title("Hotel Management Database")
root.configure(bg="#2C3E50")

# Create custom font
font_style = ("Helvetica", 12)

# Create custom color scheme
bg_color = "#222222"
fg_color = "#FFFFFF"
button_bg = "#FF5733"
button_fg = "#FFFFFF"
listbox_bg = "#333333"
listbox_fg = "#FFFFFF"
textbox_bg = "#333333"
textbox_fg = "#FFFFFF"
label_fg = "#FFFFFF"
# Configure the window
root.configure(bg=bg_color)



def drop_tables():
    GUI_Functions.drop_all_tables()
    status_label.config(text="Tables dropped")
    table_listbox.delete(0, tk.END) # Clear the listbox
    get_table_names() # Update the listbox to show only existing tables

def create_tables():
    GUI_Functions.create_tables()
    status_label.config(text="Tables created")
    display_tables()
    get_table_names()

def populate_tables():
    GUI_Functions.populate_tables()
    status_label.config(text="Tables populated")
    display_tables()

def query_all_tables():
    results = GUI_Functions.query_all_tables()
    display_tables(*results)
    status_label.config(text="Tables queried")

def display_tables(*tables):
    text_box.delete("1.0", "end")
    for i, table in enumerate(tables):
        text_box.insert("end", str(table))
        if i < len(tables) - 1:
            text_box.insert("end", "\n\n")

def query_table(table_name):
    results = GUI_Functions.query_table(table_name)
    display_tables(*results)
    status_label.config(text="Table {} queried".format(table_name[0]))

def get_table_names():
    table_names = GUI_Functions.get_table_names()
    for name in table_names:
        table_listbox.insert("end", name)

# def add_record(table_name, values):
#     GUI_Functions.add_record(table_name, values)
#     status_label.config(text="Record Added")
#     display_tables()

# def update_record(table_name, record_id, values):
#     GUI_Functions.update_record(table_name, record_id, values)
#     status_label.config(text="Record Updated")
#     display_tables()

def delete_record(table_name, record_id):
    GUI_Functions.delete_record(table_name, record_id)
    status_label.config(text="Record Deleted")
    display_tables()

def search_record(table_name, record_id):
    results = GUI_Functions.search_record(table_name, record_id)
    status_label.config(text="Record Found")
    print(results)
    if len(results) == 0:
            status_label.config(text="No Record Found")
            text_box.delete("1.0", "end")
            text_box.insert("end", "NO RECORD FOUND") 
    else:
        status_label.config(text="Record Found")
        display_tables(*results)

# Create the buttons 
drop_button = tk.Button(root, text="Drop Tables", command=drop_tables, font=font_style, bg=button_bg, fg=button_fg, borderwidth=2, relief="flat", highlightthickness=0)
create_button = tk.Button(root, text="Create Tables", command=create_tables, font=font_style, bg=button_bg, fg=button_fg, borderwidth=2, relief="flat", highlightthickness=0)
populate_button = tk.Button(root, text="Populate Tables", command=populate_tables, font=font_style, bg=button_bg, fg=button_fg, borderwidth=2, relief="flat", highlightthickness=0)
query_button = tk.Button(root, text="Query Tables", command=query_all_tables, font=font_style, bg=button_bg, fg=button_fg, borderwidth=2, relief="flat", highlightthickness=0)
delete_button = tk.Button(root, text="Delete Record", command=lambda: delete_record(table_listbox.get(table_listbox.curselection()), search_entry.get()), font=font_style, bg=button_bg, fg=button_fg, borderwidth=2, relief="flat", highlightthickness=0)
search_button = tk.Button(root, text="Search Record", command=lambda: search_record(table_listbox.get(table_listbox.curselection()), search_entry.get()), font=font_style, bg=button_bg, fg=button_fg, borderwidth=2, relief="flat", highlightthickness=0)
# Create a label to display status messages
status_label = tk.Label(root, text="Ready", font=font_style, fg=label_fg, bg=bg_color)

# Create the labels and entry box for the search bar
search_label = tk.Label(root, text="Select a table and Enter the Primary ID", font=font_style, fg=label_fg, bg=bg_color)
search_entry = tk.Entry(root, width=30, font=font_style, bg=textbox_bg, fg=textbox_fg)

# Create a text box to display the query results
text_box = scrolledtext.ScrolledText(root, height=15, width=50, wrap="word", font=font_style, bg=textbox_bg, fg=textbox_fg)

# Create a listbox to display table names
table_listbox = tk.Listbox(root, font=font_style, bg=listbox_bg, fg=listbox_fg)
get_table_names()
table_listbox.bind("<<ListboxSelect>>", lambda event: query_table(table_listbox.get(table_listbox.curselection())))
table_listbox_scrollbar = tk.Scrollbar(root, orient="vertical", command=table_listbox.yview)
table_listbox.config(yscrollcommand=table_listbox_scrollbar.set)


# Pack the buttons, labels, and entry box into the window
table_listbox.pack(side="left", padx=10, pady=10, fill="both", expand=False)
text_box.pack(side="bottom", padx=10, pady=10, fill="both", expand=False)
table_listbox_scrollbar.pack(side="left", padx=0, pady=10, fill="y")
drop_button.pack(side="left", padx=10, pady=10)
create_button.pack(side="left", padx=10, pady=10)
populate_button.pack(side="left", padx=10, pady=10)
query_button.pack(side="left", padx=10, pady=10)
status_label.pack(side="left", padx=10, pady=10)
search_label.pack(side="top", padx=10, pady=10)
search_entry.pack(side="top", padx=10, pady=10)
delete_button.pack(side="left", padx=10, pady=10)
search_button.pack(side="left", padx=10, pady=10)


# Start the main loop
root.mainloop()