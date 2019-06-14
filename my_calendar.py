# coding = utf-8

from datetime import datetime
from unittest.mock import Mock
import requests
import unittest
from requests.exceptions import Timeout

# 测试数据
tuesday = datetime(year=2019, month=1, day=1)
# print(tuesday)
saturday = datetime(year=2019, month=1, day=5)

# mock一个datetime来控制今天日期
datetime1 = Mock()

def is_weekday():
    today = datetime.today()

    return (0 <= today.weekday() < 5)


# mock .today()返回周二
datetime1.today.return_value = tuesday

print(datetime1.today().weekday())
print(datetime.today().weekday())
# 测试周二是工作日
assert is_weekday()

datetime1.today.return_value = saturday

assert is_weekday()

requests = Mock()

def get_holidays():
    r = requests.get('http://mock.guorou.local/mock/11/api/1/speaking_test/live_ranking_list')
    if r.status_code == 200:
        return r.json()
    return None


class TestCalendar(unittest.TestCase):
    def test_get_holidays_timeout(self):
        # 测试连接超时
        requests.get.side_effect = Timeout
        with self.assertRaises(Timeout):
            get_holidays()


    def log_request(self, url):
        # 测试输出模拟请求日志
        print(f'making a request to {url}.')
        print('request received!')
        # 创建一个新的mock对象模拟响应
        response_mock = Mock()
        response_mock.status_code = 200
        response_mock.json.return_value = {'12/25':'christmas', '7/4': 'independence day',}

        return response_mock

    def test_get_holidays_logging(self):
        requests.get.side_effect = self.log_request
        assert get_holidays()['12/25'] == 'christmas'


    def test_get_holidays_retry(self):
        response_mock = Mock()
        response_mock.status_code = 200
        response_mock.json.return_value = {'12/25':'christmas', '7/4': 'independence day',}

        requests.get.side_effect = [Timeout, response_mock]

        with self.assertRaises(Timeout):
            get_holidays()

        assert get_holidays()['12/25'] == 'christmas'

        assert requests.get.call_count == 3







if __name__ == "__main__":
    unittest.main()


