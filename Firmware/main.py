# CircuitPython firmware for lyric's macropad :D

import board
import digitalio
import time
import usb_hid

from rotaryio import IncrementalEncoder
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode
from adafruit_hid.mouse import Mouse

# display imports
import displayio
import adafruit_ssd1306
try:
    import adafruit_imageload
except Exception:
    adafruit_imageload = None


# pin setup

# keys
KEY_PINS = [board.GP26, board.GP27, board.GP28, board.GP29, board.GP4]
# Rotary encoder
ENC_A = board.GP2
ENC_B = board.GP1
ENC_SW = board.GP0

# OLED
I2C_SDA = board.GP6
I2C_SCL = board.GP7


# devices
kbd = Keyboard(usb_hid.devices)
consumer = ConsumerControl(usb_hid.devices)
mouse = Mouse(usb_hid.devices)


# key setup
class Button:
    def __init__(self, pin):
        self.pin = digitalio.DigitalInOut(pin)
        self.pin.direction = digitalio.Direction.INPUT
        self.pin.pull = digitalio.Pull.UP
        self._last = self.pin.value
        self._last_time = time.monotonic()
        self.debounce = 0.02 

    def fell(self):
        v = self.pin.value
        t = time.monotonic()
        if v != self._last:
            if (t - self._last_time) >= self.debounce:
                self._last = v
                self._last_time = t
                if not v:
                    return True
        else:
            self._last_time = t
        return False

buttons = [Button(p) for p in KEY_PINS]


# Encoder setup
encoder = IncrementalEncoder(ENC_A, ENC_B)
last_position = encoder.position

enc_switch = digitalio.DigitalInOut(ENC_SW)
enc_switch.direction = digitalio.Direction.INPUT
enc_switch.pull = digitalio.Pull.UP
enc_last = enc_switch.value
enc_debounce_t = time.monotonic()


# OLED init
i2c = board.I2C() 
WIDTH = 128
HEIGHT = 32

try:
    display_bus = displayio.I2CDisplay(i2c, device_address=0x3C, reset=None)
    display = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c)
    has_display = True
except Exception as e:
    # If display fails to init, continue without it
    print("init failed:", e)
    has_display = False

# draw image if present
if has_display and adafruit_imageload is not None:
    try:
        bmp, palette = adafruit_imageload.load("/splash.bmp",
                                               bitmap=displayio.Bitmap,
                                               palette=displayio.Palette)
        splash = displayio.TileGrid(bmp, pixel_shader=palette)
        g = displayio.Group()
        g.append(splash)
        display.show(g)
    except Exception as e:
        # no image, fall back to text
        display.fill(0)
        display.text("Lyric's Macropad", 0, 0, 1)
        display.show()
elif has_display:
    display.fill(0)
    display.text("Lyric's macropad", 0, 0, 1)
    display.show()

# key stuff

# alt + tab
def alt_tab():
    kbd.press(Keycode.ALT)
    kbd.press(Keycode.TAB)
    kbd.release_all()

# ctrl + tab
def ctrl_tab():
    kbd.press(Keycode.CONTROL)
    kbd.press(Keycode.TAB)
    kbd.release_all()

# mouse click middle button
def middle_click():
    mouse.press(4)
    time.sleep(0.02)
    mouse.release()

# alt + f4
def alt_f4():
    kbd.press(Keycode.ALT)
    kbd.press(Keycode.F4)
    kbd.release_all()

# super + L
def sup_l():
    kbd.press(Keycode.GUI)
    kbd.press(Keycode.L)
    kbd.release_all()

button_actions = [alt_tab, ctrl_tab, middle_click, alt_f4, sup_l]

# Main loop
print("Starting main loop")
while True:
    # buttons
    for i, btn in enumerate(buttons):
        if btn.fell():
            try:
                button_actions[i]()
            except Exception as e:
                print("Action failed:", e)

    # encoder
    pos = encoder.position
    if pos != last_position:
        diff = pos - last_position
        if diff > 0:
            consumer.send(ConsumerControlCode.VOLUME_INCREMENT)
        else:
            consumer.send(ConsumerControlCode.VOLUME_DECREMENT)
        last_position = pos

    # encoder switch
    cur = enc_switch.value
    tnow = time.monotonic()
    if cur != enc_last and (tnow - enc_debounce_t) > 0.05:
        enc_debounce_t = tnow
        enc_last = cur
        if not cur:
            # toggle mute
            consumer.send(ConsumerControlCode.MUTE)

    time.sleep(0.01)
