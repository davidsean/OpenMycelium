
import logging
import time
import RPi.GPIO as GPIO

class InterfaceFan:

    def __init__(self, power_pin, tach_pin=None, pwm_pin=None):

        self._logger = logging.getLogger(__name__)

        self.power_pin = power_pin
        self.tach_pin = tach_pin
        self.pwm_pin = pwm_pin

        # setup GPIO pins
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.power_pin, GPIO.OUT)
        if self.tach_pin is not None:
            self._setup_tachometer()
        if self.pwm_pin is not None:
            self._setup_pwm()

    def __del__(self):
        """ Call GPIO.cleanup on all used pins
        """
        GPIO.cleanup(self.power_pin)
        if self.tach_pin is not None:
            GPIO.remove_event_detect(self.tach_pin)
            GPIO.cleanup(self.tach_pin)
        if self.pwm_pin is not None:
            GPIO.cleanup(self.pwm_pin)

    def _setup_tachometer(self):
        self._num_pulses = 0
        GPIO.setup(self.tach_pin, GPIO.IN)
        GPIO.add_event_detect(self.tach_pin, GPIO.FALLING, callback=self._tach_callback)

    def _tach_callback(self):
        """ called on every pulse of the tachometer
        """
        self._num_pulses +=1

    def _setup_pwm(self):
        GPIO.setup(self.pwm_pin, GPIO.OUT)

    def read_speed(self, read_time=1):
        if self.tach_pin is None:
            self._logger.warning("Fan not configured for reading speed")
            return
        self._logger.warning("Seading speed is not yet implemented")
        self._num_pulses = 0
        time.sleep(read_time)
        speed = self._num_pulses/read_time
        return speed*60

    def set_speed(self):
        if self.pwm_pin is None:
            self._logger.warning("Fan not configured for changing speed")
            return
        self._logger.warning("Setting speed is not yet implemented")
        
    def activate(self):
        GPIO.output(self.power_pin, GPIO.HIGH)
        self._logger.info("Set fan power pin high")

    def deactivate(self):
        GPIO.output(self.power_pin, GPIO.LOW)
        self._logger.info("Set fan power pin low")
