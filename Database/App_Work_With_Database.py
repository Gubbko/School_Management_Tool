# sourcery skip: avoid-builtin-shadow
from tkinter import *
from Create_Entry_data_Frame import *
from Create_button_frame import *

list = []
entry_list = []
List_for_Lables_and_Entry = ["E-v.",      
                                    "Bilansikont",
                                    "Klass",
                                    "Vara nr.",
                                    "Alamnr.",
                                    "Inv.nr.",
                                    "Vara kirjeldus 1",
                                    "Kapit.Kp",
                                    "Soetusmaksumus",
                                    "Kulum perioodini",
                                    "Jääkv.per",
                                    "Aadress",
                                    "Aadressi text",
                                    "Ruum",
                                    "Kogus",
                                    "Ühik",
                                    "Töötaja",
                                    "Eesnimi",
                                    "Perenimi",
                                    "L. 2",
                                    "Vastutav isik",
                                    "Inventuuri kp.seisuga",
                                    "Inv.märkus"]

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
def frame_parameters(root, bg_colour, col):                 # Define parameters for frame's
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

frame_buttons, frame_entry, root = Creating_root_of_window(496,532)

def entr_frame():
    Create_Labes(List_for_Lables_and_Entry, frame_entry)
    return Create_Entry(List_for_Lables_and_Entry, frame_entry)

def btn_frame(entrys):
    Create_Buttons(frame_buttons, entrys)

entrys = entr_frame()
btn_frame(entrys)

root.mainloop()
