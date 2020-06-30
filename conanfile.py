from conans import ConanFile, CMake, tools

import os.path

class LexerConan(ConanFile):
    name = "lexer"
    license = "Proprietary"
    author = "Mikhail"
    topics = ("lexer")
    version = "1.0.0"

    settings = {
        "os": ["Windows"],
        "compiler": None,
        "build_type": None,
        "arch": None
    }
    options = {"shared": [True, False]}
    default_options = {
        "shared": False
    }
    
    generators = "cmake_paths"
    exports_sources = "*"
    no_copy_source = True

    def build_requirements(self):
        self.build_requires("cmake-toolkit/1.0.0@atd/stable")
        self.build_requires("cmake/3.17.1")

    def requirements(self):
        self.requires("qt/e5.12.4@mikhail/testing", private=False)

    def build(self):
        cmake = CMake(self)
        cmake.definitions["VERSION"] = self.version
        cmake.definitions["CMAKE_TOOLCHAIN_FILE"] = os.path.join(self.build_folder, "conan_paths.cmake")
        cmake.configure()
        cmake.build()
        
    def package(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.install()

    def package_info(self):
        #self.cpp_info.libs = tools.collect_libs(self) #remove
        self.cpp_info.components["core"].libs = ["core"]
        self.cpp_info.components["core"].requires = ["qt"]
        self.cpp_info.components["runner"].requires = ["core"]
        
