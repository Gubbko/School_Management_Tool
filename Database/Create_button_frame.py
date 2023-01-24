from tkinter import Button
from datetime import datetime
from Work_with_Database import connect_to_database, Insert_data, Read_database, Remove_Item_from_Database

List_for_Lables_and_Entry = [       "ID",
                                    "E_v",      
                                    "Bilansikont",
                                    "Klass",
                                    "Vara_nr",
                                    "Alamnr",
                                    "Inv_nr",
                                    "Vara_kirjeldus_1",
                                    "Kapit_Kp",
                                    "Soetusmaksumus",
                                    "Kulum_perioodini",
                                    "Jääkv_per",
                                    "Aadress",
                                    "Aadressi_text",
                                    "Ruum",
                                    "Kogus",
                                    "Ühik",
                                    "Töötaja",
                                    "Eesnimi",
                                    "Perenimi",
                                    "L__2",
                                    "Vastutav_isik",
                                    "Inventuuri_kp_seisuga",
                                    "Inv_märkus",
                                    "Date_when_added"]

def add_object(List_for_Entrys):
    now = datetime.now()
    inserting_data = [entry_in.get() for entry_in in List_for_Entrys]
    inserting_data.append(now)
    
    connection, cursor = connect_to_database("IT_Park.db")
    Insert_data(connection, cursor, "IT_Product", inserting_data)
    print(f" Adding nest data to database: {inserting_data}")
    connection.close()
    #list.append(inserting_data, 1)

def delete_object(List_for_Entrys):
    now = datetime.now()
    inserting_data = [entry_in.get() for entry_in in List_for_Entrys]
    inserting_data.append(now)
    connection, cursor = connect_to_database("IT_Park.db")
    Remove_Item_from_Database(connection, cursor, "IT_Product", inserting_data, List_for_Lables_and_Entry)
    connection.close()

def show_object(Table):
    connection, cursor = connect_to_database(Table)
    Read_database(connection, cursor, "IT_Product")

def Create_Buttons(frame_buttons, entrys):                          # Create buttons to make some apperations with data
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
        command=lambda:add_object(entrys))
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
        command=lambda:delete_object(entrys))
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
        command=lambda:show_object("IT_Park.db"))
    btn_Show_Objects.grid(row=2, column=0)