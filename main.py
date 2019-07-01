import board
import digitalio
import time
import adafruit_dotstar as dotstar

dot = dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1, brightness=0.1)
led = digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT

i = 0

def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if (pos < 0) or (pos > 255):
        return (0, 0, 0)
    if pos < 85:
        return (int(255 - pos*3), int(pos*3), 0)
    elif pos < 170:
        pos -= 85
        return (0, int(255 - (pos*3)), int(pos*3))
    else:
        pos -= 170
        return (int(pos*3), 0, int(255 - pos*3))



while True:
    dot[0] = wheel(i & 255)
    # led.value = True
    # time.sleep(0.5)
    # led.value = False
    time.sleep(.1)

    i = (i+1) % 256
