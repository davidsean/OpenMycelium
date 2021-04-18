
import logging
import RPi.GPIO as GPIO

class InterfaceRelay:

    def __init__(self, pin):

        self._logger = logging.getLogger(__name__)
        self.pin = pin

        # setup GPIO pins
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pin, GPIO.OUT)

    def __del__(self):
        """ Call GPIO.cleanup on all used pins
        """
        GPIO.cleanup(self.pin)


    def activate(self):
        GPIO.output(self.pin, GPIO.HIGH)
        self._logger.info("Set relay pin high")

    def deactivate(self):
        GPIO.output(self.pin, GPIO.LOW)
        self._logger.info("Set relay pin low")
