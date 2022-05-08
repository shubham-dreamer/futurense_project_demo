import flask
from tkinter import *

def tktr():


    # Create the root window

    root = Tk()
    root.title("Welcome to the Page")
    root.geometry("450x300")

    # Create button to open toplevel1
    label1 = Label(root, text="Click on the button to open")

    label1.pack()

    def DB_ARCHITECURE():
        but_label = Label(root,
                          text="A Database Architecture is a representation of DBMS design.\n It helps to design, develop, implement, and maintain the database management system.\n A DBMS architecture allows dividing the database system into individual components that can be\n independently modified, changed, replaced, and altered. It also helps to understand the components of a database.")
        but_label.pack(side="top", fill="both", expand=True, padx=20, pady=20)

    def ACID_PROPERTIES():
        but_label = Label(root,
                          text="The ACID properties, in totality, provide a mechanism to ensure the correctness and consistency of a database\n in a way such that each transaction is a group of operations that acts as a single unit, produces consistent results, acts in isolation from other operations,\n and updates that it makes are durably stored. ")
        but_label.pack(side="top", fill="both", expand=True, padx=20, pady=20)

    def open_Create():
        but_label = Label(root,
                          text="CREATE TABLE TABLE_NAME(COLUMN_NAME1,) ")
        but_label.pack(side="top", fill="both", expand=True, padx=20, pady=20)

    def open_Alter():
        global label
        label = Label(root,
                      text="Alter Table Table_Name Modify/Add/Drop Column Column_Name")
        label.pack(side="top", fill="both", expand=True, padx=20, pady=20)

    def open_Drop():
        global label
        label = Label(root,
                      text="DROP TABLE table_name")
        label.pack(side="top", fill="both", expand=True, padx=20, pady=20)

    def open_INSERT():
        # global label
        label = Label(root,
                      text="Insert Table_Name(Column1,Column2,Column3......ColumnN) values(value1,value2,value3,value4..........valueN)")
        label.pack(side="top", fill="both", expand=True, padx=20, pady=20)

    def open_UPDATE():
        update_label = Label(root,
                             text="UPDATE TABLE_NAME SET VALUE=REQUIRED VALUE WHERE CONDITION")
        update_label.pack(side="top", fill="both", expand=True, padx=20, pady=20)

    def open_DELETE():
        delete_label = Label(root,
                             text="DELETE TABLE_NAME WHERE CONDITION")
        delete_label.pack(side="top", fill="both", expand=True, padx=20, pady=20)

    def des():
        button.destroy()
        label1.destroy()

    def open_DDL():
        label.destroy()
        button2.destroy()
        button3.destroy()
        button4.destroy()
        button5.destroy()
        button1.destroy()

        button6 = Button(root, text="Create", command=open_Create)
        button7 = Button(root, text="Alter", command=open_Alter)
        button8 = Button(root, text="Drop", command=open_Drop)

        # Create exit button.
        button9 = Button(root, text="Exit",
                         command=root.destroy)
        button6.pack()
        button7.pack()
        button8.pack()
        button9.pack()
        button6.config(height=5, width=25)
        button7.config(height=5, width=25)
        button8.config(height=5, width=25)
        button9.config(height=5, width=25)

    def open_Toplevel1():
        global label
        global button1
        global button2
        global button3
        global button4
        global button5
        # global u

        des()

        # Create label
        label = Label(root,
                      text="Click Any Button From the Following")

        # Create Exit button
        button1 = Button(root, text="Exit",
                         command=root.destroy)

        # create button to open toplevel2
        button2 = Button(root, text="DML", command=open_DML)
        button3 = Button(root, text="DDL", command=open_DDL)
        button4 = Button(root, text="DB Architecture", command=DB_ARCHITECURE)
        button5 = Button(root, text="ACID PROPERTIES", command=ACID_PROPERTIES)

        label.pack()
        button2.pack()
        button3.pack()
        button4.pack()
        button5.pack()
        button1.pack()
        # u.pack()
        button1.config(height=5, width=25)
        button2.config(height=5, width=25)
        button3.config(height=5, width=25)
        button4.config(height=5, width=25)
        button5.config(height=5, width=25)

    def open_DML():
        global button6
        global button7
        global button8
        global button9
        label.destroy()
        button2.destroy()
        button3.destroy()
        button4.destroy()
        button5.destroy()
        button1.destroy()

        button6 = Button(root, text="Insert", command=open_INSERT)
        button7 = Button(root, text="Update", command=open_UPDATE)
        button8 = Button(root, text="Delete", command=open_DELETE)

        # Create exit button.
        button9 = Button(root, text="Exit",
                         command=root.destroy)

        button6.pack()
        button7.pack()
        button8.pack()
        button9.pack()

        button6.config(height=5, width=25)
        button7.config(height=5, width=25)
        button8.config(height=5, width=25)
        button9.config(height=5, width=25)

    button = Button(root, text="DB OPERATION", command=open_Toplevel1)
    button.place(x=175, y=125)

    def main_page():
        global heading_label
        global first_button
        label.destroy()
        button1.destroy()
        button2.destroy()
        button3.destroy()
        button4.destroy()
        button5.destroy()

        heading_label = Label(root, text="Click on the button to open")

        heading_label.pack()
        first_button = Button(root, text="DB OPERATION",
                              command=lambda: [heading_label.destroy(), first_button.destroy(), open_Toplevel2])
        # position the button
        first_button.place(x=175, y=125)

    root.mainloop()


#making a variable app and using Flask function
app= flask.Flask(__name__)

app.config["DEBUG"]=True
@app.route('/',methods=['GET'])
def home():
    tktr()

    return "your application is running succes"
app.run(host='192.168.4.89',port=86,debug=True,threaded=True)
