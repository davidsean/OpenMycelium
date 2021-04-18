
import logging
import RPi.GPIO as GPIO
from .interface_relay import InterfaceRelay

class InterfaceHeater(InterfaceRelay):

    def __init__(self, power_pin, pwm_pin=None):

        self._logger = logging.getLogger(__name__)

        self.power_pin = power_pin
        self.pwm_pin = pwm_pin
        
        super().__init__(self.power_pin)

        # setup GPIO pins
        GPIO.setmode(GPIO.BOARD)
        if self.pwm_pin is not None:
            self._setup_pwm()

    def __del__(self):
        """ Call GPIO.cleanup on all used pins
        """
        if self.pwm_pin is not None:
            GPIO.cleanup(self.pwm_pin)

    def _setup_pwm(self):
        GPIO.setup(self.pwm_pin, GPIO.OUT)
