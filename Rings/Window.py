# sourcery skip: avoid-builtin-shadow
import os
import sys
from tkinter import Tk, Frame, Button, Text, Entry, Label
from tkcalendar import Calendar, DateEntry
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
    list_of_rings.append("08:15 - 09:00")
    list_of_rings.append("09:15 - 10:00")
    list_of_rings.append("10:20 - 11:05")
    list_of_rings.append("11:25 - 12:10")
    list_of_rings.append("12:30 - 13:15")
    list_of_rings.append("13:35 - 14:20")
    list_of_rings.append("14:35 - 15:20")
    generate_rings_Schedule()
    print("Generate 45 min")

def Generate_30_min_day():
    print("Generate 30 min")
    
def Load_db():
    print("Load")

#cal = Calendar(Frame_Calendar, selectmode = "day", year=curent_day()[0], month = curent_day()[1], day = curent_day()[2])
#cal.pack(pady = 20, fill="both", expand=True)

start = DateEntry(Frame_Calendar, width=12, background='darkblue',
                  foreground='white', borderwidth=2)
start.grid(row = 0, column = 0, padx=5)
end = DateEntry(Frame_Calendar, width=12, background='darkblue',
                foreground='white', borderwidth=2)

end.grid(row = 1, column = 0, padx=5)

btn_Save = Button(Frame_Calendar,
        text='Save',
        font=('TkHeadingFont',10),
        bg = "#28393a",
        fg = 'white',
        padx=32,
        #pady=10,
        cursor = 'hand2',
        activebackground='#badee2',
        activeforeground='black',
        command=lambda:Save_Rings())
btn_Save.grid(row=2, column=0)

btn_Load_db = Button(Frame_Calendar,
        text='Load_Database',
        font=('TkHeadingFont',10),
        bg = "#28393a",
        fg = 'white',
        #padx=100,
        #pady=10,
        cursor = 'hand2',
        activebackground='#badee2',
        activeforeground='black',
        command=lambda:Load_db())
btn_Load_db.grid(row=3, column=0)

btn_Generate_45_min_day = Button(Frame_Calendar,
        text='Generate_45_min_day',
        font=('TkHeadingFont',10),
        bg = "#28393a",
        fg = 'white',
        #padx=80,
        #pady=10,
        cursor = 'hand2',
        activebackground='#badee2',
        activeforeground='black',
        command=lambda:Generate_45_min_day())
btn_Generate_45_min_day.grid(row=0, column=1)

btn_Generate_30_min_day = Button(Frame_Calendar,
        text='Generate_30_min_day',
        font=('TkHeadingFont',10),
        bg = "#28393a",
        fg = 'white',
        #padx=80,
        #pady=10,
        cursor = 'hand2',
        activebackground='#badee2',
        activeforeground='black',
        command=lambda:Generate_30_min_day())
btn_Generate_30_min_day.grid(row=1, column=1)

start_hour = Entry(Frame_Rings_Data)
start_hour.grid(row=0, column=0)
end___hour = Entry(Frame_Rings_Data)
end___hour.grid(row=0, column=1)

list_of_rings = []

def generate_rings_Schedule():
    for index, _ in enumerate(list_of_rings):
        lesson_l = Label(Frame_Rings_Data, text=list_of_rings[index])
        lesson_l.grid(row=1+index, column=0, columnspan=2)






























root.mainloop()

""" To Do list

    # Add image to object's
    # Way to enlarge image to see it easily
    


"""