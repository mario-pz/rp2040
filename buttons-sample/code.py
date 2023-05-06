import board
import digitalio


def main():
    led1 = digitalio.DigitalInOut(board.GP0)
    led2 = digitalio.DigitalInOut(board.GP1)
    led3 = digitalio.DigitalInOut(board.GP2)
    led4 = digitalio.DigitalInOut(board.GP3)

    led1.direction = digitalio.Direction.OUTPUT
    led2.direction = digitalio.Direction.OUTPUT
    led3.direction = digitalio.Direction.OUTPUT
    led4.direction = digitalio.Direction.OUTPUT
    
    while True:
        led1.value = True
        led2.value = True
        led3.value = True
        led4.value = True


main()
