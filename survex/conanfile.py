import os
from conans import ConanFile, CMake, tools

class SurvexConan(ConanFile):
    name = "survex"
    version = "1.2.44"
    license = "GPL-2.0"
    author = "Olly Betts"
    url = "https://survex.com"
    description = "cave surveying and mapping software"
    topics = ("<gis>", "<geography>", "<mapping>", "<survey>")
    settings = "os", "compiler", "build_type", "arch"
#    options = {"fPIC": [True, False]}
#    default_options = {"fPIC": True}
    generators = "cmake"
    requires = "proj/6.3.1", "wxwidgets/3.1.4@bincrafters/stable", "glew/2.1.0@bincrafters/stable"
    default_options = {"wxwidgets:webview": False}

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def source(self):
        git = tools.Git(folder="survex")
        git.clone("https://github.com/Cavewhere/survex.git", branch="cmake")
        #git.run("describe")
        #self.run("git clone --single-branch --branch cmake https://github.com/Cavewhere/survex.git")
#        self.run("git checkout cmake")
        # This small hack might be useful to guarantee proper /MT /MD linkage
        # in MSVC if the packaged project doesn't have variables to set it
        # properly
#        tools.replace_in_file("hello/CMakeLists.txt", "PROJECT(HelloWorld)",
#                              '''PROJECT(HelloWorld)
#include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
#conan_basic_setup()''')

    def build(self):
        self.run("cpan Locale::PO")

        cmake = CMake(self)
        cmake.definitions["CONAN_EXPORTED"] = "true"
#        cmake.definitions['CMAKE_POSITION_INDEPENDENT_CODE'] = self.options.fPIC
        cmake.configure(source_folder="survex")
        cmake.build()

        # Explicit way:
        # self.run('cmake %s/hello %s'
        #          % (self.source_folder, cmake.command_line))
        # self.run("cmake --build . %s" % cmake.build_config)

    def package(self):
        #self.copy("*.h", dst="include", src="hello")
        #self.copy("*survex_core.lib", dst="lib", keep_path=False)
        self.copy("cavern*", src="bin", dst="bin", keep_path=False)
        self.copy("diffpos*", src="bin", dst="bin", keep_path=False)
        self.copy("dump3d*", src="bin", dst="bin", keep_path=False)
        self.copy("extend*", src="bin", dst="bin", keep_path=False)
        self.copy("survexport*", src="bin", dst="bin", keep_path=False)
        self.copy("sorterr*", src="bin", dst="bin", keep_path=False)
        self.copy("aven*", src="bin", dst="bin", keep_path=False)
        self.copy("*.msg", src="bin", dst="bin", keep_path=False)
        #self.copy("cavern*", dst="bin", keep_path=False)
        #self.copy("*.so", dst="lib", keep_path=False)
        #self.copy("*.dylib", dst="lib", keep_path=False)
        #self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        bin_path = os.path.join(self.package_folder, "bin")
        self.output.info("Appending PATH environment variable: {}".format(bin_path))
        self.env_info.PATH.append(bin_path)

#    def package_id(self):
#        proj = self.info.requires["proj"]

#        # Any change in the proj version will change current Package ID
#        proj.version = proj.full_version

#        # Changes in major and minor versions will change the Package ID but
#        # only a proj patch won't. E.g., from 1.2.3 to 1.2.89 won't change.
#        proj.version = proj.full_version.minor()


#    def package_info(self):
        #self.cpp_info.libs = ["hello"]

