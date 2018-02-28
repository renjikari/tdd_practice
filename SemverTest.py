import unittest
from Semver import Semver


class SemverMajorTest(unittest.TestCase):

    def setUp(self):
        self.semver = Semver(1, 4, 2)

    def test_プラスで初期化できること(self):
        self.assertEqual(1, self.semver.major)
        self.assertEqual(4, self.semver.minor)
        self.assertEqual(2, self.semver.patch)

    def test_整数型以外で初期化するとTypeErrorが返ってくること(self):
       with self.assertRaises(TypeError):
           Semver('1')
       with self.assertRaises(TypeError):
           Semver(1, '4')
       with self.assertRaises(TypeError):
           Semver(1, 4, '2')

    def test_マイナスで初期化するとValueErrorが返ってくること(self):
       with self.assertRaises(ValueError):
           Semver(-1)
       with self.assertRaises(ValueError):
           Semver(1, -4,)
       with self.assertRaises(ValueError):
           Semver(1, 4, -2)

    def test_等価比較ができること(self):
       self.assertTrue(self.semver == Semver(1, 4, 2))
       self.assertFalse(self.semver == Semver(2, 4, 2))
       self.assertFalse(self.semver == Semver(1, 8, 2))
       self.assertFalse(self.semver == Semver(1, 4, 4))

    def test_不等価比較ができること(self):
       self.assertTrue(self.semver != Semver(2, 4, 2))
       self.assertTrue(self.semver != Semver(1, 8, 2))
       self.assertTrue(self.semver != Semver(1, 4, 4))

    def test_以上の比較ができること(self):
       self.assertTrue(self.semver >= Semver(1, 4, 2))
       self.assertTrue(self.semver >= Semver(0, 4, 2))
       self.assertTrue(self.semver >= Semver(1, 2, 2))
       self.assertTrue(self.semver >= Semver(1, 4, 0))

       self.assertFalse(self.semver >= Semver(2, 4, 2))
       self.assertFalse(self.semver >= Semver(1, 8, 2))
       self.assertFalse(self.semver >= Semver(1, 4, 4))

    def test_以下の比較ができること(self):
       self.assertTrue(self.semver <= Semver(1, 4, 2))
       self.assertTrue(self.semver <= Semver(2, 4, 2))
       self.assertTrue(self.semver <= Semver(1, 8, 2))
       self.assertTrue(self.semver <= Semver(1, 4, 4))

       self.assertFalse(self.semver <= Semver(0, 4, 2))
       self.assertFalse(self.semver <= Semver(1, 2, 2))
       self.assertFalse(self.semver <= Semver(1, 4, 0))

    def test_より大きいの比較ができること(self):
       self.assertFalse(self.semver > Semver(1, 4, 2))
       self.assertTrue(self.semver > Semver(0, 4, 2))
       self.assertTrue(self.semver > Semver(1, 2, 2))
       self.assertTrue(self.semver > Semver(1, 4, 0))

    def test_より小さいの比較ができること(self):
       self.assertFalse(self.semver < Semver(1, 4, 2))
       self.assertTrue(self.semver < Semver(2, 4, 2))
       self.assertTrue(self.semver < Semver(1, 8, 2))
       self.assertTrue(self.semver < Semver(1, 4, 4))


if __name__ == "__main__":
    unittest.main()
