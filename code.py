import time
from adafruit_circuitplayground import cp
import board
import adafruit_hcsr04
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.A4, echo_pin=board.A5)
keyboard = Keyboard(usb_hid.devices)

start_time = None
pressed_x = False

cp.pixels.brightness = 0.1

pixel_off_state = (0, 0, 0)
timer_for_recipe = 50

colour=[280,-25,0]
cp.pixels.brightness=0.1
number_of_steps = 5
neopixel_amount = len(cp.pixels)
lights_at_a_time = int(neopixel_amount//number_of_steps)

def col_changer(colour):
    if colour[0]>0 and colour[1]<255:
        colour[0]=colour[0]-25
        colour[1]=colour[1]+25
    else:
        colour=[0,250,0]

def reverse_col_changer(colour):
    if colour[0]>0 and colour[1]<255:
        colour[0]=colour[0]+25
        colour[1]=colour[1]-25
    else:
        colour=[0,250,0]

def timer_countdown():
    for i in range(10):
        cp.pixels[i] = (0, 0, 0)  # Turn off the light at index i
        cp.pixels.show()
        time.sleep(timer_for_recipe//10)  # One light turns off for every 10% of                        #the time on the timer has passed
pixel_index = 10

while True:
    if cp.switch:
        cp.red_led = True
        a=False
        b = False
        try:
            handDistance = int(sonar.distance)
        except RuntimeError:
            time.sleep(0.1)
            continue

        if handDistance <= 30:
            if start_time is None:
                start_time = time.time()

            elif time.time() - start_time >= 2 and not pressed_x:
                keyboard.press(Keycode.RIGHT_ARROW)
                keyboard.release_all()
                pressed_x = True
                a = True

        if handDistance > 30:
            start_time = None
            pressed_x = False

        if cp.button_a :
            keyboard.press(Keycode.X) #this triggers moving onto the next page in #figma
            keyboard.release_all()
            cp.pixels.fill((0, 255, 0))
            cp.pixels.show()
            time.sleep(timer_for_recipe//10) #had to add this here as once the #function was called it would turn off 1 light immediately which would not #accurately display the timer countdown
            timer_countdown()
            keyboard.press(Keycode.RIGHT_ARROW) #when the timer_countdown #method has finished running, this triggers moving onto the final figma page
            keyboard.release_all()

        if a == True and pixel_index >0:
            pixel_index -= lights_at_a_time
            for pixel in reversed(range(len(cp.pixels))):
                if pixel_index>=0 and pixel >= pixel_index and pixel < pixel_index+lights_at_a_time:
                    col_changer(colour)
                    cp.pixels[pixel] = colour

        if cp.button_b:
            b = True
            keyboard.press(Keycode.LEFT_ARROW)
            keyboard.release_all()


        if b == True and pixel_index < neopixel_amount:
            pixel_index += lights_at_a_time

            for pixel in range(len(cp.pixels)):
                if pixel < pixel_index and pixel >= pixel_index-lights_at_a_time:
                    print(pixel, pixel_index)
                    reverse_col_changer(colour)
                    cp.pixels[pixel] = [0,0,0]
        time.sleep(0.1)

    else:
        cp.red_led = False
        cp.pixels.fill(pixel_off_state)
        a = False
        b = False
