import unittest
from app import app

class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_stops_page(self):
        response = self.app.get('/stops')
        self.assertEqual(response.status_code, 200)

    def test_search_page(self):
        response = self.app.get('/search?q=Aberdeen')
        self.assertEqual(response.status_code, 200)

    def test_stop_detail_valid(self):
        # 替换成数据库中真实存在的 NaptanCode 进行测试
        response = self.app.get('/stop/123456')
        self.assertIn(response.status_code, [200, 404])  # 取决于 NaptanCode 是否存在

    def test_404_page(self):
        response = self.app.get('/nonexistentpage')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
