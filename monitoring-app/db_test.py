from cgi import test
import unittest

import modules.usage_db_i as dbi
from modules.log_wrap import *
import os


class TestsDB(unittest.TestCase):
    @wrap(entering, exiting)
    def setUp(self):
        pass

    @wrap(entering, exiting)
    def test_get_usage_type_value(self):
        # test if handles passing invalid values correctly
        test_result = self.assertRaises(ValueError, dbi.get_usage, "t")
        logger.debug("Test finished")

    @wrap(entering, exiting)
    def test_get_all__usage_type_value(self):
        # repeat above test for get_all_usage
        test_result = self.assertRaises(ValueError, dbi.get_all_usage, "t")
        logger.debug("Test finished")

    @wrap(entering, exiting)
    def test_get_usage_return_type(self):
        # test if return type is an array and unified between cpu, disk, memory usages
        for t in ["c", "d", "m"]:
            result = dbi.get_usage(t)
            test_result = self.assertIsInstance(result, type([]))
        logger.debug("Test finished")

    @wrap(entering, exiting)
    def test_get_all_usage_return_type(self):
        # repeat above test for get_all_usage
        for t in ["c", "d", "m"]:
            result = dbi.get_all_usage(t)
            test_result = self.assertIsInstance(result, type([]))
        logger.debug("Test finished")

    @wrap(entering, exiting)
    def test_get_usage_hour_param(self):
        # test if handles different value types for hour param
        for t in ["c", "d", "m"]:
            self.assertRaises(TypeError, dbi.get_usage, t, hour="DANIEL")
        logger.debug("Test finished")

    @wrap(entering, exiting)
    def test_get_usage_type_param(self):
        # test if handles different value types for type param
        for t in [10, 10.0, True, [], {}, self]:
            self.assertRaises(TypeError, dbi.get_usage, t)
        logger.debug("Test finished")

    @wrap(entering, exiting)
    def test_get_all_usage_type_param(self):
        # repeat above test for get_all_usage
        for t in [10, 10.0, True, [], {}, self]:
            self.assertRaises(TypeError, dbi.get_usage, t)
        logger.debug("Test finished")

    @wrap(entering, exiting)
    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
