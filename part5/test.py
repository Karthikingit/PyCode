import unittest
import testing

class TestMain(unittest.TestCase):
    def to_do_stuff(self):
        test_param = 20
        result  = testing.any_name(test_param)
        self.assertEqual(result, 35)
    def to_do_stuff2(self):
        test_param2 = 'sdds'
        result = testing.any_name(test_param2)
        self.assertIsInstance(result, TypeError)

    def to_do_stuff3(self):
        test_param3 = None
        result = testing.any_name(test_param3)
        self.assertIsNone(result, 'enter correct value')





        
  