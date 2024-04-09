from conan import ConanFile
from conan.tools.cmake import CMake, cmake_layout

class AwsCppConan(ConanFile):
    name = "AwsCppDemo"
    version = "1.0"

    # Optional metadata
    license = "(c) ALi Ibrahim"
    author = "Ali Ibrahim allosheribraheem38@gmail.com"
    description = ""

    # Binary configuration
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeDeps", "CMakeToolchain"
    options = {"shared": [True, False]}
    default_options = {"shared": False}
    # Sources are located in the same place as this recipe, copy them to the recipe
    exports_sources = "CMakeLists.txt", "src/*", "include/*"
    
    def requirements(self):
        self.requires("aws-sdk-cpp/1.9.234")
        self.requires("ninja/1.11.1")
        
    def layout(self):
        cmake_layout(self)
    
    def build(self):
        cmake = CMake(self)
        if self.settings.compiler == "Visual Studio":
            cmake.generator = "Visual Studio 17 2022"
        else:
            cmake.generator = "Ninja"
        cmake.configure()
        cmake.build()

    def package(self):
        self.copy("*.h", dst="include", src="src")
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.dylib*", dst="lib", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["AwsCppDemo"]