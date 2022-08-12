from pynput.mouse import Controller, Button
from time import sleep
mouse = Controller()
p = mouse.position
print(p)
mouse.position = (590, 622)
mouse.click(Button.right, 900)