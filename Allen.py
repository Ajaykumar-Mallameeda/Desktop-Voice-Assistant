from tkinter import *
from PIL import Image, ImageTk
import speech_to_text
import action

root = Tk()
root.title("A.L.L.E.N")
root.geometry("650x875")
root.resizable(False, False)
root.config(bg="#6F8FAF")


def ask():
    user_val = speech_to_text.speech_to_text()
    bot_val = action.Action(user_val)
    text.insert(END, "User--->" + user_val + "\n")
    if bot_val is not None:
        text.insert(END, "BOT<---" + str(bot_val) + "\n")
        if bot_val == "ok sir":
            root.destroy()


def send():
    send = entry.get()
    bot = action.Action(send)
    text.insert(END, "User--->" + send + "\n")
    if bot is not None:
        text.insert(END, "BOT<---" + str(bot) + "\n")
        if bot == "ok sir":
            root.destroy()


def delete():
    text.delete("1.0", "end")


# Frame
frame = LabelFrame(root, padx=100, pady=7, borderwidth=3, relief="raised", highlightbackground="#356696")
frame.config(bg="#6F8FAF")
frame.grid(row=0, column=1, padx=55, pady=10)

# Title label
text_label = Label(frame, text="A.L.L.E.N", font=("comic sans ms", 14, "bold"), highlightbackground="#356696")
text_label.grid(row=0, column=0, padx=10, pady=10)

# Assistant image (optional — place assets/assistant.png in the repo)
try:
    image = ImageTk.PhotoImage(Image.open("assets/assistant.png"))
    image_label = Label(frame, image=image)
    image_label.grid(row=1, column=0, padx=20, pady=10)
except (FileNotFoundError, AttributeError):
    pass

#text label
text = Text(root , font= ('courier 10 bold'), bg ="#356696")
text.grid(row= 2 , column= 0)
text.place(x = 125, y = 475 , width = 375 , height = 100)

#entry widget
entry = Entry(root , justify=CENTER)
entry.place(x= 125 , y = 600 , width = 375 , height = 30)


#button1 for ask function
Button1 = Button(root,text ="ASK" , bg="#356696", pady=16 , padx= 40 , borderwidth=3 , relief=SOLID, command=ask  )
Button1.place(x =70, y= 645)


#button2 for send function
Button2 = Button(root,text ="SEND" , bg="#356696", pady=16 , padx= 40 , borderwidth=3 , relief=SOLID, command=send  )
Button2.place(x =400, y= 645)

#button3 for delete function
Button3 = Button(root,text ="DELETE" , bg="#356696", pady=16 , padx= 40 , borderwidth=3 , relief=SOLID, command=delete  )
Button3.place(x =225, y= 645)

root.mainloop()
