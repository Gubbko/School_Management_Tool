# sourcery skip: avoid-builtin-shadow
import os
import sys
from tkinter import Tk, Frame, Button, Text
from tkcalendar import Calendar
from datetime import datetime

new_path = os.path.dirname(os.path.abspath(__file__)).split("\\")[:-1]
new_path.append("Database")
new_dir = "".join("\\" + i for i in new_path)
sys.path.append(new_dir[1:])
from Work_with_Database import connect_to_database, Insert_data

root = Tk()
root.title("Rings_schedule")
if os.path.exists("Bells.ico"): root.iconbitmap("Bells.ico")
else: print("Icon 'Bells.ico don't found")
#root.eval("tk::PlaceWindow . left")

Frame_Calendar = Frame(root, width = 800, height = 600, bg = '#3d6466')
Frame_Calendar.tkraise()
Frame_Calendar.pack_propagate(False)
Frame_Calendar.grid(row=0, column=0, sticky="nesw")

Frame_Rings_Data = Frame(root, width = 300, height = 600, bg = '#3d6466')
Frame_Rings_Data.tkraise()
Frame_Rings_Data.pack_propagate(False)
Frame_Rings_Data.grid(row=0, column=1, sticky="nesw")

   
def curent_day():
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    date = date.split(" ")
    date = date[0].split("-")
    date[0] = int(date[0])
    date[1] = int(date[1])
    date[2] = int(date[2])
    return date

def Save_Rings():
    print("Save")

def Generate_45_min_day():
    print("Generate 45 min")

def Generate_30_min_day():
    print("Generate 30 min")
    
def Load_db():
    print("Load")

cal = Calendar(Frame_Calendar, selectmode = "day", year=curent_day()[0], month = curent_day()[1], day = curent_day()[2])
cal.pack(pady = 20, fill="both", expand=True)


btn_Save = Button(Frame_Rings_Data,
        text='Save',
        font=('TkHeadingFont',20),
        bg = "#28393a",
        fg = 'white',
        padx=100,
        pady=10,
        cursor = 'hand2',
        activebackground='#badee2',
        activeforeground='black',
        command=lambda:Save_Rings())
btn_Save.grid(row=1, column=0, columnspan=2)

btn_Load_db = Button(Frame_Rings_Data,
        text='Load_Database',
        font=('TkHeadingFont',20),
        bg = "#28393a",
        fg = 'white',
        padx=100,
        pady=10,
        cursor = 'hand2',
        activebackground='#badee2',
        activeforeground='black',
        command=lambda:Load_db())
btn_Load_db.grid(row=0, column=0, columnspan=2)

btn_Generate_45_min_day = Button(Frame_Rings_Data,
        text='Generate_45_min_day',
        font=('TkHeadingFont',20),
        bg = "#28393a",
        fg = 'white',
        padx=80,
        pady=10,
        cursor = 'hand2',
        activebackground='#badee2',
        activeforeground='black',
        command=lambda:Generate_45_min_day())
btn_Generate_45_min_day.grid(row=2, column=0)

btn_Generate_30_min_day = Button(Frame_Rings_Data,
        text='Generate_30_min_day',
        font=('TkHeadingFont',20),
        bg = "#28393a",
        fg = 'white',
        padx=80,
        pady=10,
        cursor = 'hand2',
        activebackground='#badee2',
        activeforeground='black',
        command=lambda:Generate_30_min_day())
btn_Generate_30_min_day.grid(row=2, column=1)


textbox = Text(Frame_Rings_Data)
textbox.grid(row=3, column=0, columnspan=2)

































root.mainloop()

""" To Do list

    # Add image to object's
    # Way to enlarge image to see it easily
    


"""