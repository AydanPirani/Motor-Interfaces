from tkinter import *

current_device = None


def move(direction):
    if not current_device:
        print("Please select a device to connect to first.")
        return
    else:
        # TODO: PHYSICALLY MOVE DEVICES
        print(direction)
    return


def change_device(n_device):
    global current_device
    if current_device == n_device:
        print("Same device, no change!")
        return
    else:
        # TODO: PHYSICALLY CONNECT TO NEW DEVICE
        current_device = n_device
        print("Changed device to {}!".format(current_device))
    return


window = Tk()
devices = Frame(window)
movements = Frame(window)
frame1 = Frame(window)

device1 = Button(devices, text="Device1", command=lambda: change_device("device1"))
device2 = Button(devices, text="Device2", command=lambda: change_device("device2"))
device3 = Button(devices, text="Device3", command=lambda: change_device("device3"))
device1.grid(row=1, column=1, padx=10)
device2.grid(row=1, column=2, padx=10)
device3.grid(row=1, column=3, padx=10)

up = Button(movements, text="Up", command=lambda: move("up"))
down = Button(movements, text="Down", command=lambda: move("down"))
left = Button(movements, text="Left", command=lambda: move("left"))
right = Button(movements, text="Right", command=lambda: move("right"))
up.grid(row=1, column=2)
down.grid(row=3, column=2)
left.grid(row=2, column=1)
right.grid(row=2, column=3)

Label(frame1, text="Graph").grid(row=2, column=2)

devices.grid(row=1, columnspan=3, padx=20, pady=20)
Label(window, text="").grid(row=2)
movements.grid(row=2, padx=20, pady=20)

Label(window, text="graph", bg="white", height=10, width=20).grid(row=2, column=3, padx=20)

window.geometry("500x500")
window.rowconfigure([2], weight=1)
window.columnconfigure([2], weight=1)
window.mainloop()