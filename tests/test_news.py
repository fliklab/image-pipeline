import unittest
from src.mock_news import process
class TestNews(unittest.TestCase):
    def test_num(self):
        out = process({"config": {"num": 3}, "run_id": "t1"})
        self.assertEqual(len(out["news_items"]), 3)
if __name__ == "__main__":
    unittest.main()
