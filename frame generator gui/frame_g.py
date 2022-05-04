import tkinter as tk
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile
import cv2
import os 
import random

def path_event():
    # get input data
    input_path = input_box.get('1.0','end')
    input_path = input_path.replace("\n","")

    # if input is empty
    if input_path == "":
        instruction = tk.Label(root, text="Empty input received. Enter path again",bg="#C2C9FF",fg="#747ED1")
        instruction.grid(columnspan=3,column=0,row=6)
        return

    # variable initialization 
    video_file_path = file.name

    vidObj = cv2.VideoCapture(video_file_path)
    count = 0
    success = True
    
    directory = "frames"

    fpath = os.path.join(input_path,directory)
    
    # creating "frames" directory 
    try :
        os.mkdir(fpath)
   
        
    
        # modifying path into required format
        if "\\" in fpath:
            fpath = "/".join(fpath.split("\\"))
        
        # generating frames
        while success:
            success, image = vidObj.read()
            if success == True:
                cv2.imwrite("{}/frame{}.jpg".format(fpath,count), image)
            count += 1


        # displaying random frame 
        rand = random.randrange(0,count)
        img = Image.open("{}/frame{}.jpg".format(fpath,rand))
        img = img.resize((200,100))
        img = ImageTk.PhotoImage(img)
        img_label = tk.Label(image=img)
        img_label.image = img
        img_label.grid(column = 1, row = 7)
    
    except:
        instruction = tk.Label(root, text="Invalid path. Enter path again",bg="#C2C9FF",fg="red")
        instruction.grid(columnspan=3,column=0,row=6)
    


def open_file():

    browse_text.set("Loading ...")
    
    # file access
    global file
    file = askopenfile(parent=root, title="Choose a file",filetypes=[('Video Files',['.mp4','.webm','.mkv','.wmv'])])

    if file:
        
        # Enter path
        instruction = tk.Label(root, text="Enter path where frames will be stored",bg="#C2C9FF",fg="#747ED1",font="Raleway")
        instruction.grid(columnspan=3,column=0,row=3)

        global input_box 
        input_box = tk.Text(root, height=1, width=40,padx=5)
        input_box.grid(column=1, row=4)

        # submit response on event 
        global submit_text
        submit_text = tk.StringVar()
        submit_btn = tk.Button(root,textvariable=submit_text,bg="#747ED1", fg="#C2C9FF",command=lambda : path_event(), height=2, width=8)
        submit_btn.grid(column=1,row=5)
        submit_text.set("Submit")

        browse_text.set("Browse")


# initialize tkinter
root = tk.Tk()
root.title("Frame generator")

# create canvas
canvas = tk.Frame(root, width=1000, height=500, bg="#C2C9FF")
canvas.grid(columnspan=3, rowspan=8)

# add logo
logo = Image.open("logo.png")
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column = 1, row = 0)

# upload file
instruction = tk.Label(root, text="Generate frames by uploading a video",bg="#C2C9FF",fg="#747ED1",font="Raleway")
instruction.grid(columnspan=3,column=0,row=1)

browse_text = tk.StringVar()
browse_btn = tk.Button(root, textvariable=browse_text,command=lambda : open_file(),bg="#747ED1", fg="#C2C9FF", height=2, width=8)
browse_text.set("Upload file")
browse_btn.grid(column=1,row=2)


root.mainloop()