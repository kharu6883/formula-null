from time import sleep

# Pin setup
factory = PiGPIOFactory()

servo = Servo(12, min_pulse_width=0.0005, max_pulse_width=0.0025, pin_factory=factory)

IN3 = 17
IN4 = 27
ENB = 22

GPIO.setmode(GPIO.BCM)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)
GPIO.setup(ENB, GPIO.OUT)

pwm = GPIO.PWM(22, 1000)
pwm.start(0)

print("Looking for 8BitDo Remote...")

master = None

devices = [evdev.InputDevice(path) for path in evdev.list_devices()]

for device in devices:
    if device.name == "8BitDo Lite gamepad":
        master = device

# Servo positions
servo_val = 0

for event in master.read_loop():
    if event.type == 3:
        if event.value == 0:
            servo_val = -1
        elif event.value == 32768:
            servo_val = 0
        elif event.value == 65535:
            servo_val = 1

    if event.code == 305:
        if event.value == 1:
            GPIO.output(IN3, GPIO.HIGH)
            GPIO.output(IN4, GPIO.LOW)
            pwm.ChangeDutyCycle(100)
        elif event.value == 0:
            GPIO.output(IN3, GPIO.LOW)
            GPIO.output(IN4, GPIO.LOW)
            pwm.ChangeDutyCycle(0)
    elif event.code == 304:
        if event.value == 1:
            GPIO.output(IN3, GPIO.LOW)
            GPIO.output(IN4, GPIO.HIGH)
            pwm.ChangeDutyCycle(100)
        elif event.value == 0:
            GPIO.output(IN3, GPIO.LOW)
            GPIO.output(IN4, GPIO.LOW)
            pwm.ChangeDutyCycle(0)

    servo.value = servo_val
