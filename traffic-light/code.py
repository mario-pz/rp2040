import time
import board
import digitalio


def main():
    green_led = digitalio.DigitalInOut(board.GP0)
    yellow_led = digitalio.DigitalInOut(board.GP1)
    red_led = digitalio.DigitalInOut(board.GP2)

    green_led.direction = digitalio.Direction.OUTPUT
    yellow_led.direction = digitalio.Direction.OUTPUT
    red_led.direction = digitalio.Direction.OUTPUT

    green_latency: float = 4.0
    yellow_latency: float = 1.0
    red_latency: float = 4.0

    while True:
        green_led.value = True
        time.sleep(green_latency)
        green_led.value = False
        yellow_led.value = True
        time.sleep(yellow_latency)
        yellow_led.value = False
        red_led.value = True
        time.sleep(red_latency)
        red_led.value = False


main()
