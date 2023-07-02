# Write your code here :-)
import time
import board
import digitalio
import usb_hid

from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode


keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)

btn1 = digitalio.DigitalInOut(board.GP2)
btn1.direction = digitalio.Direction.INPUT
btn1.pull = digitalio.Pull.DOWN

btn2 = digitalio.DigitalInOut(board.GP3)
btn2.direction = digitalio.Direction.INPUT
btn2.pull = digitalio.Pull.DOWN

btn3 = digitalio.DigitalInOut(board.GP4)
btn3.direction = digitalio.Direction.INPUT
btn3.pull = digitalio.Pull.DOWN

btn4 = digitalio.DigitalInOut(board.GP5)
btn4.direction = digitalio.Direction.INPUT
btn4.pull = digitalio.Pull.DOWN

btn5 = digitalio.DigitalInOut(board.GP6)
btn5.direction = digitalio.Direction.INPUT
btn5.pull = digitalio.Pull.DOWN

btn6 = digitalio.DigitalInOut(board.GP7)
btn6.direction = digitalio.Direction.INPUT
btn6.pull = digitalio.Pull.DOWN

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

while True:
    if btn1.value:
        print("A")
        led.value = True
        keyboard.press(Keycode.A)
        time.sleep(0.1)
        keyboard.release(Keycode.A)
        led.value = False

    if btn2.value:
        print("B")
        led.value = True
        keyboard.press(Keycode.B)
        time.sleep(0.1)
        keyboard.release(Keycode.B)
        led.value = False

    if btn3.value:
        print("C")
        led.value = True
        keyboard.press(Keycode.C)
        time.sleep(0.1)
        keyboard.release(Keycode.C)
        led.value = False

    if btn4.value:
        print("D")
        led.value = True
        keyboard.press(Keycode.D)
        time.sleep(0.1)
        keyboard.release(Keycode.D)
        led.value = False

    if btn5.value:
        print("E")
        led.value = True
        keyboard.press(Keycode.E)
        time.sleep(0.1)
        keyboard.release(Keycode.E)
        led.value = False

    if btn6.value:
        print("F")
        led.value = True
        keyboard.press(Keycode.F)
        time.sleep(0.1)
        keyboard.release(Keycode.F)
        led.value = False

    time.sleep(0.1)
