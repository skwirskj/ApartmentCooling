from unittest import TestCase
import feels_like


class TestFeelsLike(TestCase):
    def test_calc_feel_like(self):
        tester = feels_like.FeelsLike()
        assert tester.calc_feel_like(80, 0), 77.8

    def test_get_feel_likes(self):
        tester = feels_like.FeelsLike()
        tester.add_data(92, 50)
        tester.add_data(85, 10)
        tester.add_data(103, 57)

        correct_feel = {0 : 98.5, 1 : 81.9, 2 : 136.5}

        tester.get_feel_likes()

        for i in range(len(correct_feel)):
            assert tester.feels[i], correct_feel[i]

    def test_add_data(self):
        tester = feels_like.FeelsLike()
        tester.add_data(92,50)
        tester.add_data(85, 10)
        tester.add_data(103, 57)
        assert len(tester.temps), 3
        assert len(tester.humid), 3
        assert tester.time, 3
