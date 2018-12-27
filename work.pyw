import time
from tkinter import *
from tkinter import ttk
from playsound import playsound

# Default values
task = "Task"
timeToWork = "10"


def countdown(t):
    global ProgressBar
    global root
    while t:
        mins, secs = divmod(t, 60)
        timeFormat = '{:02d}:{:02d}'.format(mins, secs)
        timeLabel.config(text=str(timeFormat))

        ctime = time.time()
        while time.time() < ctime + 1:
            if stopClicked:
                break
            time.sleep(0.05)
            ProgressBar["value"] = timeToWork * 60 - t + (time.time()-ctime)
            root.update()
        t -= 1
    playsound('pop.mp3')


def startFunction():
    global startClicked
    startClicked = True


def stopFunction():
    global stopClicked
    stopClicked = True


root = Tk()
root.title("Work")
root.geometry("450x210")
root.attributes('-topmost', True)  # window on top of other windows

while True:
    startClicked = False

# First window  ----------------  First window
    entry1 = Entry(root, font=("Helvetica ", 20))
    entry1.grid(row=0, column=0)
    entry1.insert(0, task)

    entry2 = Entry(root, font=("Helvetica ", 20))
    entry2.grid(row=1, column=0)
    entry2.insert(0, timeToWork)
    l1 = Label(root, text="minutes", font=("Helvetica ", 30))
    l1.grid(row=1, column=1)

    b = Button(root, text="Start", command=startFunction, font=("Helvetica ", 30), fg="Green")
    b.grid(row=2, column=0)

    while not startClicked:
        root.update()

    task = str(entry1.get())
    timeToWork = float(entry2.get().replace(",", "."))

    for widget in root.winfo_children():
        widget.destroy()
# First window  ----------------  First window


# SECOND window ------------------------------------------- SECOND window
    stopClicked = False

    taskLabel = Label(root, text=task, fg='green', justify="center", font=("Helvetica ", 40))
    taskLabel.pack()

    timeLabel = Label(root, text=timeToWork, fg='green', justify="center", font=("Helvetica ", 60))
    timeLabel.pack()

    ProgressBar = ttk.Progressbar(root, orient=HORIZONTAL, length=450, mode='determinate')
    ProgressBar.pack()
    ProgressBar["maximum"] = timeToWork*60

    button = Button(root, text="stop", command=stopFunction, font=("Helvetica ", 10), bg="Green", width= 420)
    button.pack()

    countdown(round(timeToWork*60))

    for widget in root.winfo_children():
        widget.destroy()
# SECOND window ------------------------------------------- SECOND window
