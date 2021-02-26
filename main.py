import threading
import time
from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

window = None
current_device = None
current_distance = None
figure_frame = None
x_label = y_label = z_label = None

device_props = {
    "device1": {
        "name": "Device 1",
        "location": {"x": 0, "y": 0, "z": 0}
    },
    "device2": {
        "name": "Device 2",
        "location": {"x": 0, "y": 0, "z": 0}
    },
    "device3": {
        "name": "Device 3",
        "location": {"x": 0, "y": 0, "z": 0}
    },
}

fig = plt.figure()
plt.xlabel("Time Elapsed")
plt.ylabel("Square of Time Elapsed")
ax = fig.gca()

x = []
y = []


def display(label, text):
    label.config(text=text)
    return


def move(axis, direction, label):
    dist = current_distance.get()
    direction *= abs(int(dist)) if dist else 1

    if not current_device:
        return
    else:
        # TODO: PHYSICALLY MOVE DEVICES
        display(label, int(label["text"]) + direction)
        device_props[str(current_device)]["location"][axis] += direction
    return


def change_device(n_device, label):
    global current_device
    if current_device == n_device:
        return
    else:
        # TODO: PHYSICALLY CONNECT TO NEW DEVICE
        current_device = n_device

        display(label, "Currently connected to \"{}\"".format(device_props[current_device]["name"]))

        display(x_label, device_props[str(current_device)]["location"]["x"])
        display(y_label, device_props[str(current_device)]["location"]["y"])
        display(z_label, device_props[str(current_device)]["location"]["z"])

    return


def create_devices_frame(head):
    devices = Frame(head)

    global current_distance
    current_distance = Entry(devices)

    currently_connected = Label(devices, text="Connect to a device to start!")
    device1 = Button(devices, text=device_props["device1"]["name"],
                     command=lambda: change_device("device1", currently_connected))
    device2 = Button(devices, text=device_props["device2"]["name"],
                     command=lambda: change_device("device2", currently_connected))
    device3 = Button(devices, text=device_props["device3"]["name"],
                     command=lambda: change_device("device3", currently_connected))

    device1.grid(row=1, column=1, padx=10)
    device2.grid(row=1, column=2, padx=10)
    device3.grid(row=1, column=3, padx=10)
    currently_connected.grid(row=2, columnspan=3, pady=5)
    Label(head, text="").grid(row=3)
    Label(devices, text="Movement Distance: ").grid(row=4, column=1)
    current_distance.grid(row=4, column=2, columnspan=2)
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

    global x_label, y_label, z_label
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


def create_window():
    head = Tk()
    movements_frame = create_movements_frame(head)
    devices_frame = create_devices_frame(head)

    devices_frame.grid(row=1, columnspan=3, padx=20, pady=20)
    Label(head, text="").grid(row=2)
    movements_frame.grid(row=2, padx=20, pady=20)

    global fig, figure_frame
    figure_frame = FigureCanvasTkAgg(fig, head).get_tk_widget()
    figure_frame.grid(row=2, column=3, padx=20)

    head.title("Device Control Interface")
    head.rowconfigure([2], weight=1)
    head.columnconfigure([2], weight=1)
    return head


iterations = 0
window = create_window()


def task():
    if not window:
        sys.exit()
    global iterations, figure_frame, ax
    iterations += 1
    x.append(iterations)
    y.append(iterations ** 2)
    ax.plot(iterations, iterations ** 2, ".")
    figure_frame = FigureCanvasTkAgg(fig, window).get_tk_widget()
    figure_frame.grid(row=2, column=3, padx=20)
    window.after(2000, task)


def on_close():
    print(x)
    print()
    print(y)
    window.destroy()


window.after(2000, task)
window.protocol("WM_DELETE_WINDOW", on_close)
window.mainloop()
