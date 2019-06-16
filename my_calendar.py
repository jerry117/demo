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
datetime = Mock()

def is_weekday():
    today = datetime.today()

    return (0 <= today.weekday() < 5)


# mock .today()返回周二
datetime.today.return_value = tuesday

print(datetime.today().weekday())
print(datetime.today().weekday())
# 测试周二是工作日
assert is_weekday()

datetime.today.return_value = saturday

assert not is_weekday()

# mock一个requests来控制自身行为
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

        # 简洁的新式配置.configure_mokc()
        # holidays = {'12/25':'christmas', '7/4': 'independence day',}
        # response_mock = Mock(**{'json.return_value': holidays})

        return response_mock

    def test_get_holidays_logging(self):
        # 测试成功，打印请求
        requests.get.side_effect = self.log_request
        assert get_holidays()['12/25'] == 'christmas'


    def test_get_holidays_retry(self):
        # 创建一个新的mock对象模拟响应
        response_mock = Mock()
        response_mock.status_code = 200
        response_mock.json.return_value = {'12/25':'christmas', '7/4': 'independence day',}
        # 为.get()设置侧面影响
        requests.get.side_effect = [Timeout, response_mock]
        # 测试第一个请求抛出timeout异常
        with self.assertRaises(Timeout):
            get_holidays()
        # 重试，期望返回成功的响应
        assert get_holidays()['12/25'] == 'christmas'
        # 最后，断言.get()被调用3次，包括上一次，本来两次
        assert requests.get.call_count == 3







if __name__ == "__main__":
    unittest.main()


