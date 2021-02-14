from conans import ConanFile, CMake, tools

class AsyncfutureConan(ConanFile):
    name = "asyncfuture"
    version = "1.0"
    license = "Apache-2.0 License"
    author = "Philip Schuchardt vpicaver@gmail.com"
    url = "https://github.com/Cavewhere/conan-cave-software"
    description = "Use QFuture like a Promise object (vpicaver fork of benlau)"
    topics = ("qtconcurrent", "asynchronous", "qt")

    # No settings/options are necessary, this is header only
    exports_sources = "asyncfuture.h"
    no_copy_source = True

    def source(self):
        self.run("git clone https://github.com/vpicaver/asyncfuture.git")

    def package(self):
        self.copy("asyncfuture.h", dst="include", src="asyncfuture")

    def package_id(self):
        self.info.header_only()

