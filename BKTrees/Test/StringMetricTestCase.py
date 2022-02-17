import unittest
from ..Metric import StringMetric

class StringMetricTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.StringMetric = StringMetric

    def test_levenshtein_distance(self):
        self.assertEqual(
            StringMetric.levenshtein_distance(
                a='kitten',
                b='sitting'
            ),
            3
        )

if __name__ == '__main__':
    unittest.main()
