# sourcery skip: avoid-builtin-shadow
from tkinter import *
from Work_with_Database import connect_to_database, Insert_data
from datetime import datetime

list = []
entry_list = []

def add_object():
    now = datetime.now()
    inserting_data = [entry_in.get() for entry_in in List_for_Entrys]
    inserting_data.append(now)# Add new object to list of object, with list from entry's
    
    connection, cursor = connect_to_database("IT_Park.db")
    Insert_data(connection, cursor, "IT_Product", inserting_data)
    for i in cursor.execute("select * from IT_Product"):
        print(i)
    connection.close()
    list.append(inserting_data)
    
def delete_object(list):
    if list:
        list.pop()
        
def show_object(list):
    for item in list:
        print(item)                                        # Get data from entry's and return list of them
    

def Creating_root_of_window():                          # Crating root of the main program window
    root = Tk()
    root.title("Database")
    #root.iconbitmap("db.ico")
    #root.eval("tk::PlaceWindow . center")
    root.geometry("1587x400")
    bg_colour = '#3d6466'
    framebtn = frame_parameters(root, bg_colour, 0)
    frameent = frame_parameters(root, bg_colour, 1)
    
    #Button(root, text="Exit", command=root.quit).grid(row=0, column=0)
    return framebtn,frameent, root
def frame_parameters(root, bg_colour, row):                 # Define parameters for frame's
    parametrs = Frame(root,                                  # Put frame in root of the window
                         width = 400,                           #
                         height = 800,                          #
                         bg = bg_colour)                        # Background colour
    parametrs.tkraise()                                         #
    parametrs.pack_propagate(False)                             #
    parametrs.grid(row=row,                                     # Placement the frame in root
                   column=0,                                    #
                   sticky="nesw")                               #
    return parametrs
def Create_Entrys(frame_entry):                             # Create entrys to put data for the object to save
    Entry_Parameters(frame_entry, "Manufacture", 0)             # Create entry for Manufacture            of the object
    Entry_Parameters(frame_entry, "Model", 1)                   # Create entry for Model                  of the object
    Entry_Parameters(frame_entry, "Type", 2)                    # Create entry for Type                   of the object
    Entry_Parameters(frame_entry, "Serial Number", 3)           # Create entry for Serial number          of the object
    Entry_Parameters(frame_entry, "Inventarization Number", 4)  # Create entry for Inventarization number of the object
    Entry_Parameters(frame_entry, "Class", 5)                   # Create entry for Class where the product instaled
def Entry_Parameters(frame_entry, text, column):            # Define parameters for entry's
    entry_list.append(Entry(frame_entry,                     # Creating entry
                               width=20))
    entry_list[-1].insert(0, text)                              # Inserting text for the entry to help user with understanding what to put in it
    #entry_list[-1].grid(row=2, column=column)                   # Define placement of the entry

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
    btn_Delete_Object.grid(row=0, column=1)
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
    btn_Show_Objects.grid(row=0, column=2)

frame_buttons, frame_entry, root = Creating_root_of_window()
Create_Entrys(frame_entry)
Create_Buttons(frame_buttons)

List_for_Lables_and_Entry = ["E-v.\n", "Bilansikont\n","Klass\n", "Vara nr.\n",
                  "Alamnr.\n", "Inv.nr.\n", "Vara\n kirjeldus 1", "Kapit.Kp\n",
                  "Soetusmaksumus\n", "Kulum\n perioodini", "Jääkv.per\n", "Aadress\n",
                  "Aadressi\n text", "Ruum\n", "Kogus\n", "Ühik\n",
                  "Töötaja\n", "Eesnimi\n", "Perenimi\n", "L. 2\n",
                  "Vastutav\n isik", "Inventuuri\n kp.seisuga", "Inv.märkus\n"
                  ]
List_for_Lables = []
List_for_Entrys = []
for index, lable in enumerate(List_for_Lables_and_Entry):
    new_label = Label(frame_entry, text=lable, width=9).grid(row=1, column=index)
    List_for_Lables.append(new_label)
    #print(index)
for index, entry in enumerate(List_for_Lables_and_Entry):
    List_for_Entrys.append(Entry(frame_entry, width=9))
    List_for_Entrys[-1].grid(row=2, column=index)
    #print(index)

root.mainloop()

""" To Do list

    # Add image to object's
    # Way to enlarge image to see it easily
    


"""