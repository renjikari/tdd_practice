import unittest
from Semver import Semver
from collections import namedtuple


class SemverMajorTest(unittest.TestCase):

    def test_プラスで初期化できること(self): self.assertEqual(1, Semver(major=1).major)

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


class InitialSuper(unittest.TestCase):

    def setUp(self):
        self.semver = Semver(1, 4, 2)


class SemverEqualTest(InitialSuper):

    def make_candidates(self):
        C = namedtuple("C", "src, dst, expected")

        self.candidates = [
                C(src = self.semver, dst = Semver(1, 4, 2), expected=True),
                C(src = self.semver, dst = Semver(2, 4, 2), expected=False),
                C(src = self.semver, dst = Semver(1, 8, 2), expected=False),
                C(src = self.semver, dst = Semver(1, 4, 4), expected=False),
                ]

    def test_等価比較ができること(self):
        self.make_candidates()

        for c in self.candidates:
            with self.subTest():
                self.assertEqual(c.src == c.dst, c.expected)

    def test_不等価比較ができること(self):
        self.make_candidates()

        for c in self.candidates:
            with self.subTest():
                self.assertEqual(c.src != c.dst, not(c.expected))
       

class SemverCompareTest(InitialSuper):

    def make_candidates(self):
        C = namedtuple("C", "greater, less, expected")

        self.candidates = [
                C(greater = self.semver, less = Semver(0, 4, 2), expected= True),
                C(greater = self.semver, less = Semver(1, 2, 2), expected= True),
                C(greater = self.semver, less = Semver(1, 4, 0), expected= True),

                C(greater = self.semver, less = Semver(2, 4, 2), expected= False),
                C(greater = self.semver, less = Semver(1, 8, 2), expected= False),
                C(greater = self.semver, less = Semver(1, 4, 4), expected= False),
                ]


    def test_以上の比較ができること(self):

        self.make_candidates()
        for c in self.candidates:
            with self.subTest():
                self.assertEqual(c.greater >= c.less, c.expected)

    def test_より大きいの比較ができること(self):

        self.make_candidates()
        for c in self.candidates:
            with self.subTest():
                self.assertEqual(c.greater > c.less, c.expected)

    def test_以上とより大きいが違うこと(self):
        self.assertTrue(self.semver >= Semver(1,4,2))
        self.assertFalse(self.semver > Semver(1,4,2))


class SemverStrTest(InitialSuper):

    def test_オブジェクトを文字列化できる(self):
        self.assertEqual(str(self.semver), "1.4.2")


class SemverVersionUpTest(InitialSuper):

    def test_パッチバージョンアップ(self):
        self.semver.patch_verup()
        self.assertEqual(self.semver.patch, 3)

    def test_マイナーバージョンアップ(self):
        self.semver.minor_verup()
        self.assertEqual([self.semver.minor, self.semver.patch] , [5,0] )

    def test_メジャーバージョンアップ(self):
        self.semver.major_verup()
        self.assertEqual([self.semver.major, self.semver.minor, self.semver.patch] , [2,0,0] )


if __name__ == "__main__":
    unittest.main()
