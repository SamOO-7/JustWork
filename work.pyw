import time
from tkinter import *
from tkinter import ttk
from playsound import playsound


def countdown(t):
    global ProgressBar
    global root
    while t:
        mins, secs = divmod(t, 60)
        timeFormat = '{:02d}:{:02d}'.format(mins, secs)
        label2.config(text=str(timeFormat))

        ctime = time.time()
        while time.time() < ctime + 1:
            if secondButtonClicked:
                break
            time.sleep(0.05)
            ProgressBar["value"] = timeToWork * 60 - t + (time.time()-ctime)
            root.update()
        t -= 1

    playsound('pop.mp3')
    root.update()


def start():
    global clicked
    clicked = True


def start2():
    global secondButtonClicked
    global root
    secondButtonClicked = True


while True:
    clicked = False

# First window  ----------------  First window
    inputWindow = Tk()
    inputWindow.title("Work")
    inputWindow.geometry("450x200")

    e = Entry(inputWindow, font=("Helvetica ", 20))
    e.grid(row=0, column=0)
    e.insert(0, "Task")

    e2 = Entry(inputWindow, font=("Helvetica ", 20))
    e2.grid(row=1, column=0)
    e2.insert(0, "10")
    l1 = Label(inputWindow, text="minutes", font=("Helvetica ", 30))
    l1.grid(row=1, column=1)

    b = Button(inputWindow, text="Start", command=start, font=("Helvetica ", 30), fg="Green")
    b.grid(row=2, column=0)

    while not clicked:
        inputWindow.update()

    task = str(e.get())
    timeToWork = float(e2.get().replace(",", "."))

    inputWindow.destroy()
# First window  ----------------  First window


# SECOND window ------------------------------------------- SECOND window
    secondButtonClicked = False
    root = Tk()
    root.title("Work")
    root.geometry("400x230")
    root.attributes('-topmost', True)

    label1 = Label(root, text=task, fg='green', justify="center", font=("Helvetica ", 60))
    label1.pack()

    label2 = Label(root, text=timeToWork, fg='green', justify="center", font=("Helvetica ", 60))
    label2.pack()

    ProgressBar = ttk.Progressbar(root, orient=HORIZONTAL, length=400, mode='determinate')
    ProgressBar.pack()
    ProgressBar["maximum"] = timeToWork*60
    ProgressBar["value"] = 0

    button = Button(root, text="stop", command=start2, font=("Helvetica ", 10), bg="Green", width= 400)
    button.pack()

    countdown(round(timeToWork*60))

    root.destroy()
# SECOND window ------------------------------------------- SECOND window
