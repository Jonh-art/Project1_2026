#5
from gpiozero import LED, Button
from time import sleep
from random import uniform
import sys

led = LED(4)
left_button = Button(14)
right_button = Button(15)

left_name = input('left player name is: ')
right_name = input('right player name is: ')

print("Game start! Wait for LED off...")
led.on()
sleep(uniform(5, 10))
led.off()

def pressed(button):
    if button.pin.number == 14:
        print(left_name + ' won this round!')
    else:
        print(right_name + ' won this round!')
    print("\nNext round...")
    led.on()
    sleep(uniform(5, 10))
led.off()

right_button.when_pressed = pressed
left_button.when_pressed = pressed


