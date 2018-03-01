import unittest
from Semver import Semver


class SemverMajorTest(unittest.TestCase):

    def test_プラスで初期化できること(self):
        self.assertEqual(1, Semver(major=1).major)

    def test_整数型以外で初期化するとTypeErrorが返ってくること(self):
       with self.assertRaises(TypeError):
           Semver(major = '1')

    def test_マイナスで初期化するとValueErrorが返ってくること(self):
       with self.assertRaises(ValueError):
           Semver(major = -1)

class SemverMinorTest(unittest.TestCase):

    def test_プラスで初期化できること(self):
        self.assertEqual(1, Semver(minor=1).minor)

    def test_整数型以外で初期化するとTypeErrorが返ってくること(self):
       with self.assertRaises(TypeError):
           Semver(minor = '1')

    def test_マイナスで初期化するとValueErrorが返ってくること(self):
       with self.assertRaises(ValueError):
           Semver(minor = -1)


class SemverPatchTest(unittest.TestCase):

    def test_プラスで初期化できること(self):
        self.assertEqual(1, Semver(patch=1).patch)

    def test_整数型以外で初期化するとTypeErrorが返ってくること(self):
       with self.assertRaises(TypeError):
           Semver(patch = '1')

    def test_マイナスで初期化するとValueErrorが返ってくること(self):
       with self.assertRaises(ValueError):
           Semver(patch = -1)


class SemverEqualTest(unittest.TestCase):

    def setUp(self):
        self.semver = Semver(1, 4, 2)

    def test_等価比較ができること(self):
       self.assertTrue(self.semver == Semver(1, 4, 2))
       self.assertFalse(self.semver == Semver(2, 4, 2))
       self.assertFalse(self.semver == Semver(1, 8, 2))
       self.assertFalse(self.semver == Semver(1, 4, 4))

    def test_不等価比較ができること(self):
       self.assertTrue(self.semver != Semver(2, 4, 2))
       self.assertTrue(self.semver != Semver(1, 8, 2))
       self.assertTrue(self.semver != Semver(1, 4, 4))

class SemverLeTest(unittest.TestCase):

    def setUp(self):
        self.semver = Semver(1, 4, 2)

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


class SemverLtTest(unittest.TestCase):

    def setUp(self):
        self.semver = Semver(1, 4, 2)

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
