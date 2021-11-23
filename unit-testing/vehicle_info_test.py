import unittest
from .vehicle_info_after import VehicleInfo


class TestVehicleInfo(unittest.TestCase):

    def test_compute_tax_non_electric(self):
        breakpoint()
        v = VehicleInfo("BMW", False, 10000)
        self.assertEqual(v.compute_tax(), 500)

    pass

unittest.main()