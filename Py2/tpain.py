from tkinter import *
from PIL import Image, ImageTk


class Window(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)

        self.master = master

        self.init_window()

    def init_window(self):
        self.master.title("GUI")
        self.pack(fill=BOTH, expand=1)

        #quitButton = Button(self, text="QUIT", command=self.client_exit)
        #quitButton.place(x=0, y=0)

        menu = Menu(self.master)
        self.master.config(menu=menu)

        file = Menu(menu)

        file.add_command(label='Exit', command=self.client_exit)

        menu.add_cascade(label='File', menu=file)

        ############################################
        edit = Menu(menu)
        edit.add_command(label='Show Image', command=self.showImg())
        edit.add_command(label='Show Text', command=self.showTxt)
        menu.add_cascade(label='Edit', menu=edit)

    def showImg(self):
        basewidth = 300
        load = Image.open('SF.jpg')
        wpercent = (basewidth/float(load.size[0]))
        hsize = int((float(load.size[1])*float(wpercent)))
        load = load.resize((basewidth,hsize),Image.ANTIALIAS)
        load.save('SF.jpg')
        render = ImageTk.PhotoImage(load)

        img = Label(self, image = render)
        img.image = render
        img.place(x=20, y=20)

    def showTxt(self):
        text = Label(self, text="Hey there good lookin!")
        text.pack()

    def client_exit(self):
        exit()

root = Tk()
root.geometry("600x600")
app = Window(root)
root.mainloop()