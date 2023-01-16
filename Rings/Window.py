# sourcery skip: avoid-builtin-shadow
import os
import sys
from tkinter import Tk, Frame
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

cal = Calendar(Frame_Calendar, selectmode = "day", year=2023, month = 5, day = 22)
cal.pack(pady = 20, fill="both", expand=True)




































print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

root.mainloop()

""" To Do list

    # Add image to object's
    # Way to enlarge image to see it easily
    


"""