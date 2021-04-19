
import logging
import RPi.GPIO as GPIO

class InterfaceHTSensor:

    def __init__(self, data_pin):

        self._logger = logging.getLogger(__name__)
        GPIO.setmode(GPIO.BOARD)

        self.data_pin = data_pin

        # setup GPIO pins
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.data_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    
    def __del__(self):
        """ Call GPIO.cleanup on all used pins
        """
        GPIO.cleanup(self.data_pin)

    def _parse_dht_data(data):
        h = None
        t = None
        if data[0]+data[1]+data[2]+data[3]==data[4]:
            h=int.from_bytes(bytes(data[0:2]),byteorder='big')*0.1
            t=int.from_bytes(bytes(data[2:4]),byteorder='big')*0.1
        else:
            #TODO: Raise checksum error
            pass
        return h,t

    def read_dht(self):
        GPIO.setup(self.data_pin, GPIO.OUT)
        GPIO.output(self.data_pin, GPIO.LOW)
        time.sleep(18*0.001)
        GPIO.output(self.data_pin, GPIO.HIGH) 
        time.sleep(40*0.000001);
        GPIO.setup(self.data_pin, GPIO.IN)
        pass

    def get_temperature(self):
        self._logger.info("Not yet implemented!")

    def get_humidity(self):
        self._logger.info("Not yet implemented!")

