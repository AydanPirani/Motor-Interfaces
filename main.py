from tkinter import *


current_device = None


def move(axis, direction, label):
    if not current_device:
        print("Please select a device to connect to first.")
        return
    else:
        # TODO: PHYSICALLY MOVE DEVICES
        print(axis, direction)
        label.config(text=str(int(label["text"]) + direction))
    return


def change_device(n_device, label):
    global current_device
    if current_device == n_device:
        print("Same device, no change!")
        return
    else:
        # TODO: PHYSICALLY CONNECT TO NEW DEVICE
        current_device = n_device

        label.config(text="Currently connected to \"{}\"".format(current_device))

        print("Changed device to {}!".format(current_device))
    return


def create_devices_frame(head):
    devices = Frame(head)

    currently_connected = Label(devices, text="Connect to a device to start!")
    device1 = Button(devices, text="Device1", command=lambda: change_device("device1", currently_connected))
    device2 = Button(devices, text="Device2", command=lambda: change_device("device2", currently_connected))
    device3 = Button(devices, text="Device3", command=lambda: change_device("device3", currently_connected))

    device1.grid(row=1, column=1, padx=10)
    device2.grid(row=1, column=2, padx=10)
    device3.grid(row=1, column=3, padx=10)
    currently_connected.grid(row=2, columnspan=3, pady=5)

    return devices


def create_movements_frame(head):
    movements = Frame(head)

    movement_header = Label(movements, text="Adjust Current Device:")
    x_positive = Button(movements, text="+x", width=5, command=lambda: move("x", 1, x_label))
    x_negative = Button(movements, text="-x", width=5, command=lambda: move("x", -1, x_label))
    y_positive = Button(movements, text="+y", width=5, command=lambda: move("y", 1, y_label))
    y_negative = Button(movements, text="-y", width=5, command=lambda: move("y", -1, y_label))
    z_positive = Button(movements, text="+z", width=5, command=lambda: move("z", 1, z_label))
    z_negative = Button(movements, text="-z", width=5, command=lambda: move("z", -1, z_label))

    x_label = Label(movements, text="0", width=4, height=2)
    y_label = Label(movements, text="0", width=4)
    z_label = Label(movements, text="0", width=4)

    movement_header.grid(row=1, column=1, columnspan=3)
    x_negative.grid(row=2, column=1, padx=15)
    x_label.grid(row=2, column=2, padx=15)
    x_positive.grid(row=2, column=3, padx=15)

    y_negative.grid(row=3, column=1, padx=15)
    y_label.grid(row=3, column=2, padx=15)
    y_positive.grid(row=3, column=3, padx=15)

    z_negative.grid(row=4, column=1, padx=15)
    z_label.grid(row=4, column=2, padx=15)
    z_positive.grid(row=4, column=3, padx=15)

    return movements


window = Tk()

frame1 = Frame(window)

devices_frame = create_devices_frame(window)
movements_frame = create_movements_frame(window)

Label(frame1, text="Graph").grid(row=2, column=2)

devices_frame.grid(row=1, columnspan=3, padx=20, pady=20)
Label(window, text="").grid(row=2)
movements_frame.grid(row=2, padx=20, pady=20)

Label(window, text="graph", bg="white", height=10, width=20).grid(row=2, column=3, padx=20)

window.rowconfigure([2], weight=1)
window.columnconfigure([2], weight=1)
window.mainloop()