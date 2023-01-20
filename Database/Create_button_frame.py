from tkinter import *
from datetime import datetime
from Work_with_Database import connect_to_database, Insert_data, Read_database

def add_object(List_for_Entrys):
    now = datetime.now()
    inserting_data = [entry_in.get() for entry_in in List_for_Entrys]
    inserting_data.append(now)
    
    connection, cursor = connect_to_database("IT_Park.db")
    Insert_data(connection, cursor, "IT_Product", inserting_data)
    print(f" Adding nest data to database: {inserting_data}")
    connection.close()
    list.append(inserting_data)

def delete_object(list):
    if list:
        list.pop()

def show_object():
    connection, cursor = connect_to_database("IT_Park.db")
    Read_database(connection, cursor)

def Create_Buttons(frame_buttons):                          # Create buttons to make some apperations with data
    btn_width = 35
    btn_Add_Object = Button(frame_buttons,
        text='Add_Object',
        font=('TkHeadingFont',20),
        bg = "#28393a",
        fg = 'white',
        padx=btn_width,
        pady=10,
        cursor = 'hand2',
        activebackground='#badee2',
        activeforeground='black',
        command=lambda:add_object())
    btn_Add_Object.grid(row=0, column=0)
    btn_Delete_Object = Button(frame_buttons,
        text='Delete_Object',
        font=('TkHeadingFont',20),
        bg = "#28393a",
        fg = 'white',
        padx=btn_width,
        pady=10,
        cursor = 'hand2',
        activebackground='#badee2',
        activeforeground='black',
        command=lambda:delete_object(list))
    btn_Delete_Object.grid(row=1, column=0)
    btn_Show_Objects = Button(frame_buttons,
        text='Show Objects',
        font=('TkHeadingFont',20),
        bg = "#28393a",
        fg = 'white',
        padx=btn_width,
        pady=10,
        cursor = 'hand2',
        activebackground='#badee2',
        activeforeground='black',
        command=lambda:show_object(list))
    btn_Show_Objects.grid(row=2, column=0)