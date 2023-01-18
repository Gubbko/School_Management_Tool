# sourcery skip: avoid-builtin-shadow
import os
import sys
from tkinter import OptionMenu, StringVar, Tk, Frame, Button, Text, Entry, Label
from tkcalendar import DateEntry
from datetime import datetime
from tkinter import ttk

new_path = os.path.dirname(os.path.abspath(__file__)).split("\\")[:-1]
new_path.append("Database")
new_dir = "".join("\\" + i for i in new_path)
sys.path.append(new_dir[1:])
from Work_with_Database import connect_to_database, Insert_data
#-------------------------------------------------------------------------------------------------------
#-----Variables-----------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------
List_of_options = ["By_Text",
                   "By_Generator_Simple",
                   "By_Generator_Advanced"]

list_of_rings = []

index = 1

#-------------------------------------------------------------------------------------------------------
#-----Functions-----------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------

def Generate_45_min_day(Frame_By_Generator):
    list_of_rings.clear()
    list_of_rings.append("08:15 - 09:00")
    list_of_rings.append("09:15 - 10:00")
    list_of_rings.append("10:20 - 11:05")
    list_of_rings.append("11:25 - 12:10")
    list_of_rings.append("12:30 - 13:15")
    list_of_rings.append("13:35 - 14:20")
    list_of_rings.append("14:35 - 15:20")
    generate_rings_Schedule(Frame_By_Generator)

def Generate_30_min_day(Frame_By_Generator):
    list_of_rings.clear()
    list_of_rings.append("08:15 - 09:45")
    list_of_rings.append("09:00 - 09:30")
    list_of_rings.append("09:50 - 11:05")
    list_of_rings.append("11:25 - 12:10")
    list_of_rings.append("12:30 - 13:15")
    list_of_rings.append("13:35 - 14:20")
    list_of_rings.append("14:35 - 15:20")
    generate_rings_Schedule(Frame_By_Generator)

def generate_rings_Schedule(frame):
    for index, _ in enumerate(list_of_rings):
        lesson_l = Label(frame, text=list_of_rings[index])
        lesson_l.pack()
        #lesson_l.grid(row=1+index, column=0, columnspan=2)

def Rings_By_Text():
    Frame_By_Text = Frame(root)
    Frame_By_Text.grid(row=1,column=1)
    
    Text_Box = Text(Frame_By_Text, height=10, width=20)
    Text_Box.pack()

def Rings_By_Generator():
    Frame_By_Generator = Frame(root)
    Frame_By_Generator.grid(row=1,column=1)
    
    btn_Generate_45_min_day = Button(Frame_By_Generator,
            text='Generate_45_min_day',
            font=('TkHeadingFont',10),
            bg = "#28393a",
            fg = 'white',
            #padx=80,
            #pady=10,
            cursor = 'hand2',
            activebackground='#badee2',
            activeforeground='black',
            command=lambda:Generate_45_min_day(Frame_By_Generator))
    btn_Generate_45_min_day.pack()

    btn_Generate_30_min_day = Button(Frame_By_Generator,
            text='Generate_30_min_day',
            font=('TkHeadingFont',10),
            bg = "#28393a",
            fg = 'white',
            #padx=80,
            #pady=10,
            cursor = 'hand2',
            activebackground='#badee2',
            activeforeground='black',
            command=lambda:Generate_30_min_day(Frame_By_Generator))
    btn_Generate_30_min_day.pack()

def Rings_Advanced():
    
    Frame_Advanced = Frame(root)
    Frame_Advanced.grid(row=1,column=1)
    
    btn_Add_Lesson = Button(Frame_Advanced,
            text='Add Lesson',
            font=('TkHeadingFont',10),
            bg = "#28393a",
            fg = 'white',
            #padx=80,
            #pady=10,
            cursor = 'hand2',
            activebackground='#badee2',
            activeforeground='black',
            command=lambda:Add_Lesson(Frame_Advanced))
    btn_Add_Lesson.grid(row=0,column=0)
    
    btn_Save = Button(Frame_Advanced,
            text='Save',
            font=('TkHeadingFont',10),
            bg = "#28393a",
            fg = 'white',
            #padx=80,
            #pady=10,
            cursor = 'hand2',
            activebackground='#badee2',
            activeforeground='black',
            command=lambda:Save_Lessons())
    btn_Save.grid(row=0,column=1)
    
def Add_Lesson(Frame_Advanced):
    global index
    Entry(Frame_Advanced).grid(row=index,column=0)
    Entry(Frame_Advanced).grid(row=index,column=1)
    index += 1

def Save_Lessons():
    pass
    
def selected():
    #Label(root, text=clicked.get()).grid(row=1,column=5)
    if clicked.get() == List_of_options[0]:
        Rings_By_Text()
    elif clicked.get() == List_of_options[1]:
        Rings_By_Generator()
    elif clicked.get() == List_of_options[2]:
        Rings_Advanced()

#-------------------------------------------------------------------------------------------------------
#-----Main----------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------

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


my_btn = Button(root, text="Run", command = selected)
my_btn.grid(row=2,column=0)

#cal = Calendar(Frame_Calendar, selectmode = "day", year=curent_day()[0], month = curent_day()[1], day = curent_day()[2])
#cal.pack(pady = 20, fill="both", expand=True)

start = DateEntry(Frame_Calendar, width=12, background='darkblue',
                  foreground='white', borderwidth=2)
start.grid(row = 0, column = 0, padx=5)
end = DateEntry(Frame_Calendar, width=12, background='darkblue',
                foreground='white', borderwidth=2)

end.grid(row = 1, column = 0, padx=5)

start_hour = Entry(Frame_Rings_Data)
start_hour.grid(row=0, column=0)
end___hour = Entry(Frame_Rings_Data)
end___hour.grid(row=0, column=1)

clicked = StringVar()
clicked.set(List_of_options[0])

drop = OptionMenu(root,clicked, *List_of_options)
drop.grid(row=1,column=0)


























root.mainloop()

""" To Do list

    # Add image to object's
    # Way to enlarge image to see it easily
    


"""