
import unittest

from json.decoder import JSONDecodeError
from openmylelium.interface_dht import InterfaceHTSensor

class TestInterfaceHTSensor(unittest.TestCase):

    def setUp(self):
        self.ht_sensor = InterfaceHTSensor()

    def tearDown(self):
        del self.ht

    def test__parse_dht_data(self):
        """ Test the data parser
        Use the specsheet example
        """
        # 0000 0010  1000 1100  0000 0001  0101 1111  1110 1110
        data = bytes([0x02, 0x8c, 0x01, 0x5f, 0xee])
        h,t=self.ht_sensor._parse_dht_data(data)
        self.assertEqual(h,65.2)
        self.assertEqual(t,35.1)