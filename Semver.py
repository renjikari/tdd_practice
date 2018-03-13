class Semver(object):


    def __init__(self, major=0, minor=0, patch=0):

        self.semver = [major, minor, patch]

        for semver in self.semver:
            if not isinstance(semver, int):
                raise TypeError

        if major < 0 or minor < 0 or patch < 0:
            raise ValueError

        self.major = major
        self.minor = minor
        self.patch = patch

    def __eq__(self, other):
        return self.semver == [other.major, other.minor, other.patch]

    def __le__(self, other):
        return self.semver <= [other.major, other.minor, other.patch]

    def __lt__(self, other):
        return self.semver < [other.major, other.minor, other.patch]

    def __str__(self):
        return "{0}.{1}.{2}".format(str(self.major), str(self.minor), str(self.patch))

    def patch_verup(self):
        self.patch += 1

    def minor_verup(self):
        self.patch = 0
        self.minor += 1

    def major_verup(self):
        self.patch = 0
        self.minor = 0
        self.major += 1

