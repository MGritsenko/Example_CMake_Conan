from conans import ConanFile, CMake, tools

import os

class LexerTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake_paths"

    def build_requirements(self):
        self.build_requires("cmake/3.17.1")

    def build(self):
        cmake = CMake(self)
        cmake.definitions["CMAKE_TOOLCHAIN_FILE"] = os.path.join(self.build_folder, "conan_paths.cmake")
        cmake.configure()
        cmake.build()
        with open(os.path.join(self.build_folder, str(self.settings.build_type), 'qt.conf'), 'w') as f:
            f.write('[Paths]\nPrefix = {}'.format(self.deps_cpp_info['qt'].rootpath))
        
    def imports(self):
        self.copy("runner.exe", dst=str(self.settings.build_type), src="bin")

    def test(self):
        if not tools.cross_building(self.settings):
            os.chdir(str(self.settings.build_type))
            self.run(".%srunner" % os.sep, run_environment=True)

