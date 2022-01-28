# GUITextEditor
This is a customizable Text Editor witten in python using tkinter with some basic features baked in.


Welcome to the GUI Text editor written in python this is a great project that has very good documentation to make it easy to edit and customize there is plenty of comments to describe the sections of the GUI and functions.

This was a great project to work on and build I learned a lot from this and even added some of my own features that being said 90% of the source code credit goes to John Elder from Codemy.com I recommend you subscribe and check out his YouTube channel.

The print feature used in this program is Linux only sadly I build a LPR command wrapper function that writes to the stdin file then flushes it to send the file / text to your default printer. Make sure you set that before trying to print anything or else the command will just hang. You can set your default printer using CUPS a command built into most standard Linux systems. 

FEATURES:

save / open files.
create new files and save them.
color your text while editing.
color your text editor background.
simple status bar to help see whats going on with your editor.
bold / italics buttons and tool bars.
undo / redo buttons and bindings.
key bindings to commands:  CTRL + A to select all,  CTRL + C to copy etc…
print your text files NOTE: linux only.

HOW TO USE THIS SOFTWARE:

step one clone the repo and download the snake file 'notepad.py'

![gitclone](https://user-images.githubusercontent.com/84602650/151616532-f05193ca-7b89-4046-bb09-29bcc45add6e.jpeg)

step two run the notepad.py file using your python 3.X interpreter

![running](https://user-images.githubusercontent.com/84602650/151616578-194fa750-cb86-4c4f-923b-f91a62dc5c31.jpeg)

the software will launch and you can begin editing the text by default there is no file open
so the text you are editing is a new file.

![startpage](https://user-images.githubusercontent.com/84602650/151616598-149b8896-dee2-402a-8266-305d67caf1c7.jpeg)


After you have finished editing your new file hit  CTRL + S to open a file dialog box to save
your new file or you can use the FILE menu to save the file. After you enter a name and click
save you have saved your new text file.

![saving](https://user-images.githubusercontent.com/84602650/151616637-cdc45a9c-e1f8-4c05-8ec5-6b86253b0959.jpeg)


After you have saved or open a file the text editor status bar will display the location of that file 
and the boxes title will display the file name you are working on.

![title](https://user-images.githubusercontent.com/84602650/151616698-170acc21-ed4a-4c08-ac2b-ae56bc24bede.jpeg)

![statusbar](https://user-images.githubusercontent.com/84602650/151616839-293df80f-e42b-4930-8ebc-b824989fc1e0.jpeg)


You can also print your files using the print function when clicked it will prompt you to select your file
after you select your file it will immediately start printing. Example page down below.


![printtest](https://user-images.githubusercontent.com/84602650/151618243-1655e417-b3e4-4a73-bdd5-40ae783c1751.jpeg)
