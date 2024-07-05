import unittest
import main

class TestStudent(unittest.TestCase):
    def test1_walk(self):
        st1 = main.Student('Tom')
        for _ in range(10):
            st1.walk()
        res = st1.distance
        self.assertEqual(res,
                         500,
                         f"Дистанции не равны [дистанция человека {st1.name}] != 500")

    def test2_run(self):
        st2 = main.Student('Max')
        for _ in range(10):
            st2.run()
        res = st2.distance
        self.assertEqual(res,
                         1000,
                         f"Дистанции не равны [дистанция человека {st2.name}] != 1000")

    def test3_compare(self):
        self.st1 = main.Student("Katya")
        self.st2 = main.Student("Vasya")
        self.st1.run(), self.st2.walk()
        result_1, result_2 = self.st1.distance, self.st2.distance
        self.assertGreater(result_1,
                           result_2,
                           f"[бегущий человек] должен преодолеть дистанцию больше, чем [идущий человек]]")

        self.assertLess(result_2,
                        result_1,
                        f"[бегущий человек] должен преодолеть дистанцию больше, чем [идущий человек]]")


if __name__ == "__main__":
    unittest.main