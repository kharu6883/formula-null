import evdev

devices = [evdev.InputDevice(path) for path in evdev.list_devices()]

master = None

for device in devices:
    if deivce.name == "8BitDo Lite gamepad":
        master = device

for event in device.read_loop():
    if event.type == evdev.ecodes.EV_KEY:
        print(evdev.categorize(event))
