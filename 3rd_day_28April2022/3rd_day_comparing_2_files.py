
#comparing two files

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import os
files_path=[]

# create the root window
root = tk.Tk()
root.title('Tkinter File Dialog')
root.resizable(False, False)
root.geometry('300x150')


def select_files():
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '.')
    )

    filenames = fd.askopenfilenames(
        title='Open files',
        initialdir='/',
        filetypes=filetypes)

    showinfo(
        title='Select Files to get Compared',
        message="files Get Selected"
    )
    if len(filenames)==2:
        files_path.append(list(filenames)[0])
        files_path.append(list(filenames)[1])

        print("files path is ::::", files_path)

        # reading files

        from tabulate import tabulate
        f1 = open(files_path[0], "r")
        f2 = open(files_path[1], "r")
        i = 0

        for line1 in f1:
            i += 1
            for line2 in f2:

                # matching line1 from both files
                if line1 == line2:
                    # print IDENTICAL if similar
                    print("Line ", i, ": IDENTICAL")
                else:
                    print("Line ", i, ":")
                    # else print that line from both files
                    print("\tFile 1:", line1, end='')
                    print("\tFile 2:", line2, end='')
                    f = open("third.txt", "a+")
                    f.write(line1)
                    f.write(line2)

                    print("these lines are not identical")
                    data = [[f'file1 line{i}', f'file2 line{i}'], [line1, line2]]

                    print(tabulate(data, headers='firstrow', showindex='always',

                                   tablefmt='fancy_grid'))
                break

        # closing files
        f1.close()
        f2.close()


    else:
        showinfo(
            title='status',
            message="Failed"
        )

# open button
open_button = ttk.Button(
    root,
    text='Open Files',
    command=select_files
)
open_button.pack(expand=True)
root.mainloop()

