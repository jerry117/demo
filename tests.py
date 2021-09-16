# # # coding = utf-8

# # import requests
# # from my_calendar import get_holidays
# # from requests.exceptions import Timeout
# # from unittest.mock import patch
# # import unittest

# # class TestCalendar(unittest.TestCase):
# #     @patch('my_calendar.requests')
# #     def test_get_holidays_timeout(self, mock_requests):
# #         mock_requests.get.side_effect = Timeout
# #         with self.assertRaises(Timeout):
# #             get_holidays()
# #             mock_requests.get.assert_called_once()

# #     # mock对象的一部分，使用patch()作为上下文管理器，可以用with语句。
# #     # def test_get_holidays_timeout(self):
# #     #     with patc('my_calendar.requests') as mock_requests:
# #     #         mock_requests.get.side_effect = Timeout
# #     #         with self.assertRaises(Timeout):
# #     #             get_holidays()
# #     #             mock_requests.get.assert_called_once()


# #     # 只是mock了get方法而不是整个requests包，其他属性还是与原来相同
# #     # @patch.object(requests, 'get', side_effect=requests.exceptions.Timeout)
# #     # def test_get_holidays_timeout(self, mock_requests):
# #     #     with self.assertRaises(requests.exceptions.Timeout):
# #     #         get_holidays()


# # if __name__ == "__main__":
# #     unittest.main()



# import unittest

# # A simple function to illustrate
# def parse_int(s):
#     return int(s)

# class TestConversion(unittest.TestCase):
#     def test_bad_int(self):
#         self.assertRaises(ValueError, parse_int, 'N/A')


#     def test_bad_int2(self):
#         self.assertRaisesRegex(ValueError, 'invalid literal .*',
#                                     parse_int, 'N/A')



import unittest
import os
import platform

class Tests(unittest.TestCase):
    def test_0(self):
        self.assertTrue(True)

    @unittest.skip('skipped test')
    def test_1(self):
        self.fail('should have failed!')

    @unittest.skipIf(os.name=='posix', 'Not supported on Unix')
    def test_2(self):
        import winreg

    @unittest.skipUnless(platform.system() == 'Darwin', 'Mac specific test')
    def test_3(self):
        self.assertTrue(True)

    @unittest.expectedFailure
    def test_4(self):
        self.assertEqual(2+2, 5)

if __name__ == '__main__':
    unittest.main()