from conans import ConanFile, CMake, tools


class DewallsConan(ConanFile):
    name = "dewalls"
    version = "1.0"
    license = "MIT"
    author = "Philip Schuchardt vpicaver@gmail.com"
    url = "https://github.com/Cavewhere/conan-cave-software"
    description = "A C++/Qt parser for Walls .wpj and .srv cave survey data format"
    topics = ("gis")
    settings = "os", "compiler", "build_type", "arch"
    options = {"fPIC": [True, False]}
    default_options = {"fPIC": True}
    generators = "cmake"
    requires = "qt/5.15.2@bincrafters/stable", "catch2/2.13.4"

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def source(self):
        self.run("git clone https://github.com/Cavewhere/dewalls.git")
        self.run("cd dewalls && git pull --tags")

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="dewalls")
        if self.settings.os != "Windows":
            cmake.definitions['CMAKE_POSITION_INDEPENDENT_CODE'] = self.options.fPIC
        cmake.build()
        #self.run("%s\bin\dewalls-test" % self.install_folder)

        # Explicit way:
        # self.run('cmake %s/hello %s'
        #          % (self.source_folder, cmake.command_line))
        # self.run("cmake --build . %s" % cmake.build_config)

    def package(self):
        self.copy("*.h", dst="include", src="dewalls/src")
        self.copy("*dewalls.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["dewalls"]

