from unittest import TestCase, main
from ..Metric import StringMetric
from . import test_cases

class StringMetricTestCase(TestCase):

    def setUp(self) -> None:
        self.StringMetric = StringMetric

    def test_levenshtein_distance(self):
        for algorthim in test_cases.levenshtein_algorithms:
            for test_case in test_cases.levenshtein_distance_test_cases:
                with self.subTest():
                    a, b, answer = test_case
                    self.assertEqual(
                        StringMetric.levenshtein_distance(
                            a=a,
                            b=b,
                            algorithm=algorthim
                        ),
                        answer
                    )
    def test_damerau_levenshtein_distance(self):
        for algorthim in test_cases.damerau_levenshtein_algorithm:
            for test_case in test_cases.levenshtein_distance_test_cases:
                with self.subTest():
                    a, b, answer = test_case
                    self.assertEqual(
                        StringMetric.damerau_levenshtein_distance(
                            a=a,
                            b=b,
                            algorithm=algorthim
                        ),
                        answer
                    )


if __name__ == '__main__':
    main()
