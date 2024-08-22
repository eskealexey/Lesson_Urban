from runner_and_tournament import Tournament, Runner
import unittest


class TournamentTest(unittest.TestCase):
    is_frozen = True
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}


    def setUp(self):
        self.runner1 = Runner('Усейн', 10)
        self.runner2 = Runner('Андрей', 9)
        self.runner3 = Runner('Ник', 3)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_first_tournament(self):
        tour1 = Tournament(90, self.runner1, self.runner3)
        res = tour1.start()
        self.all_results.update(res)
        length = len(res)
        self.assertEqual(self.all_results[length], 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_second_tournament(self):
        tour1 = Tournament(90, self.runner2, self.runner3)
        res = tour1.start()
        self.all_results.update(res)
        length = len(res)
        self.assertEqual(self.all_results[length], 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_third_tournament(self):
        tour1 = Tournament(90, self.runner1, self.runner2, self.runner3)
        res = tour1.start()
        self.all_results.update(res)
        length = len(res)
        self.assertEqual(self.all_results[length], 'Ник')

    def tearDown(self):
        print(self.all_results)


class RunnerTest(unittest.TestCase):
    is_frozen = False

    def setUp(self):
        pass

    @unittest.skipIf(is_frozen,'Тесты в этом кейсе заморожены')
    def test_own(self):
        pass

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
