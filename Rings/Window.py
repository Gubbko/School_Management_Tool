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



def curent_day():
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    date = date.split(" ")
    date = date[0].split("-")
    date[0] = int(date[0])
    date[1] = int(date[1])
    date[2] = int(date[2])
    return date

cal = Calendar(Frame_Calendar, selectmode = "day", year=curent_day()[0], month = curent_day()[1], day = curent_day()[2])
cal.pack(pady = 20, fill="both", expand=True)






































root.mainloop()

""" To Do list

    # Add image to object's
    # Way to enlarge image to see it easily
    


"""