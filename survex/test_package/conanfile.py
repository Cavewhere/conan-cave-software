import os

from conans import ConanFile, CMake, tools


class SurvexTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"

    def build(self):
        cmake = CMake(self)
        # Current dir is "test_package/build/<build_id>" and CMakeLists.txt is
        # in "test_package"
        cmake.configure()
        cmake.build()

    def imports(self):
        self.copy("*.dll", dst="bin", src="bin")
        self.copy("*.dylib*", dst="bin", src="lib")
        self.copy('*.so*', dst='bin', src='lib')

    def test(self):
        if not tools.cross_building(self):
            os.chdir("bin")
            self.run(".%scavern --help" % os.sep)
            self.run(".%sdiffpos --help" % os.sep)
            self.run(".%sdump3d --help" % os.sep)
            self.run(".%sextend --help" % os.sep)
            self.run(".%ssurvexport --help" % os.sep)
            self.run(".%ssorterr --help" % os.sep)
            self.run(".%saven --help" % os.sep)
