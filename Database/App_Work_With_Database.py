# sourcery skip: avoid-builtin-shadow
from tkinter import *
from Create_Entry_data_Frame import *
from Create_button_frame import *

list = []
entry_list = []
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

def Creating_root_of_window(x,y):                          # Crating root of the main program window
    root = Tk()
    root.title("Database")
    #root.iconbitmap("db.ico")
    #root.eval("tk::PlaceWindow . center")
    root.geometry(f"{x}x{y}")
    bg_colour = '#3d6466'
    framebtn = frame_parameters(root, bg_colour, 0)
    frameent = frame_parameters(root, bg_colour, 1)
    
    #Button(root, text="Exit", command=root.quit).grid(row=0, column=0)
    return framebtn,frameent, root
def frame_parameters(root, bg_colour, col):                # Define parameters for frame's
    parametrs = Frame(root,                                  # Put frame in root of the window
                         width = 400,                           #
                         height = 800,                          #
                         bg = bg_colour)                        # Background colour
    parametrs.tkraise()                                         #
    parametrs.pack_propagate(False)                             #
    parametrs.grid(row=0,                                     # Placement the frame in root
                   column=col,                                    #
                   sticky="nesw",
                   pady=5)                               #
    return parametrs

frame_buttons, frame_entry, root = Creating_root_of_window(496,len(List_for_Lables_and_Entry)*23+5)

def entr_frame():
    Create_Labes(List_for_Lables_and_Entry, frame_entry)
    return Create_Entry(List_for_Lables_and_Entry, frame_entry)

def btn_frame(entrys):
    Create_Buttons(frame_buttons, entrys)

entrys = entr_frame()
btn_frame(entrys)

root.mainloop()
