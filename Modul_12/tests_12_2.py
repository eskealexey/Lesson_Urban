from runner_and_tournament import Tournament, Runner
import unittest


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = Runner('Усейн', 10)
        self.runner2 = Runner('Андрей', 9)
        self.runner3 = Runner('Ник', 3)

    def test_first_tournament(self):
        tour1 = Tournament(90, self.runner1, self.runner3)
        res = tour1.start()
        self.all_results.update(res)
        length = len(res)
        self.assertEqual(self.all_results[length], 'Ник')

    def test_second_tournament(self):
        tour1 = Tournament(90, self.runner2, self.runner3)
        res = tour1.start()
        self.all_results.update(res)
        length = len(res)
        self.assertEqual(self.all_results[length], 'Ник')

    def test_third_tournament(self):
        tour1 = Tournament(90, self.runner1, self.runner2, self.runner3)
        res = tour1.start()
        self.all_results.update(res)
        length = len(res)
        self.assertEqual(self.all_results[length], 'Ник')

    def tearDown(self):
        print(self.all_results)


if __name__ == "__main__":
    unittest.main()
