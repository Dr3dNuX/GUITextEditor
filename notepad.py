from tkinter import *
from tkinter import filedialog
from tkinter import font
from tkinter import colorchooser
import subprocess

# set varable for open file name
global open_status_name
open_status_name = False

global selected
selected = False

root = Tk()
root.title('TextEditor')
root.geometry('1200x600')

"""
This is a note about the functions with "e=None" in the arguments place I have this bacause 
when you bind keys in python using tkinter the binding passes an event meaning it
passes something to the function but when you use "command=print_text" with buttons the button 
does not pass anything to the function so you get en error of 
takes 1 positional arguments but 0 was given 
so im using defaults to get around this bug
"""


# Create New File Funciton
def new_file():
    global open_status_name
    open_status_name = False
    my_text.delete('1.0', END)
    root.title('New File - TextPad!')
    status_bar.config(text='New File' + ' '*8)

# Creating Open File Function
def open_file():
    #del prevous text
    my_text.delete('1.0', END)

    # grab file name
    text_file = filedialog.askopenfilename(initialdir='~/Documents/', title='Open File', filetypes=(('Text Files', '*.txt'), ("All Files", '*.*')))
    
    # chck to see if file has been open make name global
    if text_file:
        global open_status_name
        open_status_name = text_file
        print(open_status_name)
    
    #update status bars
    name = text_file
    status_bar.config(text=name)
    root.title('{} - TextPad!'.format(name.split('/')[-1]))

    # Open the File
    text_file = open(text_file, 'r')
    stuff = text_file.read()
    # add file to textbox
    my_text.insert(END, stuff)
    # close the file
    text_file.close()

# save as function
def save_as_file():
    text_file = filedialog.asksaveasfilename(defaultextension='.*', initialdir='~/Documents/', title='Save File', filetypes=(('All Files','*.*'),('Text Files','*.txt')))
    if text_file:
        # update bars
        name = text_file
        status_bar.config(text=f'Saved: {name}')
        root.title('{} - TextPad!'.format(name.split('/')[-1]))

        # save the file
        text_file = open(text_file, 'w')
        text_file.write(my_text.get(1.0, END))
        text_file.close()

def save_file(e=None):
    global open_status_name
    if open_status_name:
        text_file = open(open_status_name, 'w')
        text_file.write(my_text.get(1.0, END))
        text_file.close()
        status_bar.config(text=f'Saved: {open_status_name}')
    else:
        save_as_file()

# cut text
def cut_text(e=None):
    global selected
    if e:
        selected = root.clipboard_get()
    else:
        if my_text.selection_get():
            # grab selected text from text box
            selected = my_text.selection_get()
            # deleat selected text form text box
            my_text.delete('sel.first', 'sel.last')
            root.clipboard_clear()
            root.clipboard_append(selected)


# copy text
def copy_text(e=None):
    global selected
    # check to see if we used keyboard shortcuts
    if e:
        selected = root.clipboard_get()
    
    elif my_text.selection_get():
        selected = my_text.selection_get()
        root.clipboard_clear()
        root.clipboard_append(selected)
        

# paste text
def paste_text(e=None):
    global selected
    if e:
        selected = root.clipboard_get()
    else:
        if selected:
            position = my_text.index(INSERT)
            my_text.insert(position, selected)

# toolbar functions

#bold it func
def bold_it():
    # create our font
    bold_font = font.Font(my_text, my_text.cget('font'))
    bold_font.configure(weight='bold')

    # config a tag
    my_text.tag_configure('bold', font=bold_font)
    
    # def current tags
    current_tags = my_text.tag_names('sel.first')

    # if to check if tag has been set
    if 'bold' in current_tags:
        my_text.tag_remove('bold', 'sel.first', 'sel.last')
    else:
        my_text.tag_add('bold', 'sel.first', 'sel.last')


#italics it function
def italics_it():
    # create our font
    italics_font = font.Font(my_text, my_text.cget('font'))
    italics_font.configure(slant='italic')

    # config a tag
    my_text.tag_configure('italic', font=italics_font)
    
    # def current tags
    current_tags = my_text.tag_names('sel.first')

    # if to check if tag has been set
    if 'italic' in current_tags:
        my_text.tag_remove('italic', 'sel.first', 'sel.last')
    else:
        my_text.tag_add('italic', 'sel.first', 'sel.last')


def text_color():
    # pick a color
    my_color = colorchooser.askcolor()[1]
    if my_color:
    # create our font
        color_font = font.Font(my_text, my_text.cget('font'))

    # config a tag
        my_text.tag_configure('colored', font=color_font, foreground=my_color)
    
    # def current tags
        current_tags = my_text.tag_names('sel.first')

    # if to check if tag has been set
        if 'italic' in current_tags:
            my_text.tag_remove('colored', 'sel.first', 'sel.last')
        else:
            my_text.tag_add('colored', 'sel.first', 'sel.last')

# change bg color
def bg_color():
    my_color = colorchooser.askcolor()[1]
    if my_color:
        my_text.config(bg=my_color)

# change all text color
def all_text_color():
    my_color = colorchooser.askcolor()[1]
    if my_color:
        my_text.config(fg=my_color)

# Print file Function
def print_file():
    """
    alright this function is weird so im going to describe it
    basically its an lpr linux print command wrapper
    it writes the lines of the text file to the stdin file
    then flushes them with .closed()
    after its been flushed the lpr command will send your 
    text to your default printer.

    I found some of this code on stack overflow from a user named: Anuj Gupta
    """

    # opening the file using open() and tk filedialog
    file_to_print = open(filedialog.askopenfilename(initialdir='~/Documents/', title='Open File', filetypes=(('Text Files', '*.txt'), ("All Files", '*.*'))))
    lpr = subprocess.Popen('/usr/bin/lpr', stdin=subprocess.PIPE)
    
    # loop to read then write encoded lines to stdin
    for line in file_to_print:
        lpr.stdin.write(line.encode('utf-8'))
    
    lpr.stdin.close()


# select all

def select_all(e=None):
    # add sel tag to select text
    my_text.tag_add('sel', '1.0', 'end')

def clear_all():
    my_text.delete(1.0, END)

# Create a toolbar frame
toolbar_frame = Frame(root)
toolbar_frame.pack(fill=X)

# Create Main Frame
my_frame = Frame(root)
my_frame.pack(pady=5)

#create our scrollbar for the textbox
text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)

# horizontal scrollbar
hor_scroll = Scrollbar(my_frame,orient='horizontal')
hor_scroll.pack(side=BOTTOM, fill=X)

# Create Text Box
my_text =Text(my_frame, width=97, heigh=25, font=(('Helvetica'),16), selectbackground='yellow', selectforeground='black', undo=True, yscrollcommand=text_scroll.set, xscrollcommand=hor_scroll.set,wrap='none')
my_text.pack()

text_scroll.config(command=my_text.yview)
hor_scroll.config(command=my_text.xview)

# create menu
my_menu = Menu(root)
root.config(menu=my_menu)

# add file menu
file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label='File',menu=file_menu)
file_menu.add_command(label='New', command=new_file)
file_menu.add_command(label='Open', command=open_file)
file_menu.add_command(label='Save', command=save_file)
file_menu.add_command(label='Save As', command=save_as_file)
file_menu.add_separator()
file_menu.add_command(label='Print File', command=print_file)
file_menu.add_separator()
file_menu.add_command(label='Exit', command=root.quit)

# add edit menu
edit_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label='Edit',menu=edit_menu)
edit_menu.add_command(label='Cut', command=cut_text)
edit_menu.add_command(label='Copy', command=copy_text)
edit_menu.add_command(label='Paste', command=paste_text)
edit_menu.add_separator()
edit_menu.add_command(label='Undo', command=my_text.edit_undo)
edit_menu.add_command(label='Redo', command=my_text.edit_redo)
edit_menu.add_separator()
edit_menu.add_command(label='Select All', command=select_all)
edit_menu.add_command(label='Clear', command=clear_all)

# Color menu
color_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label='Color',menu=color_menu)
color_menu.add_command(label='Selected Text', command=text_color)
color_menu.add_command(label='All Text', command=all_text_color)
color_menu.add_command(label='Background', command=bg_color)


# add status bar
status_bar = Label(root, text='Ready' + ' '*8,anchor=E)
status_bar.pack(fill=X,side=BOTTOM, ipady=5)

# edit bindings
root.bind('<Control-Key-x>', cut_text)
root.bind('<Control-Key-c>', copy_text)
root.bind('<Control-Key-v>', paste_text)

# select bindings
root.bind('<Control-Key-a>', select_all)

# save binding
root.bind('<Control-Key-s>', save_file)

# Create Buttons

# bold Button
bold_button = Button(toolbar_frame, text='Bold', command=bold_it)
bold_button.grid(row=0, column=0, sticky=W)

# italics Button
italics_button = Button(toolbar_frame, text='Italics', command=italics_it)
italics_button.grid(row=0, column=1)

# undo button
undo_button = Button(toolbar_frame, text='Undo', command=my_text.edit_undo)
undo_button.grid(row=0, column=2)

# redo button
redo_button = Button(toolbar_frame, text='Redo', command=my_text.edit_redo)
redo_button.grid(row=0, column=3)

# text color
color_text_button = Button(toolbar_frame, text='Text Color', command=text_color)
color_text_button.grid(row=0, column=4)
root.mainloop()