import unittest



class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        Runner1 = Runner('Денис')
        for _ in range(10):
            Runner1.walk()
        self.assertEqual(Runner1.distance, 50)

    def test_run(self):
        Runner2 = Runner('Антон')
        for _ in range(10):
            Runner2.run()
        self.assertEqual(Runner2.distance, 100)

    def test_challenge(self):
        Runner3 = Runner('Дима')
        Runner4 = Runner('Вика')
        for _ in range(10):
            Runner3.run()
            Runner4.walk()
        self.assertNotEqual(Runner3.distance, Runner4.distance)



if __name__ == "__main__":
    unittest.main()