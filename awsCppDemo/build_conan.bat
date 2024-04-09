setlocal

@echo off
REM detect profile
conan profile detect

REM run conan install
conan install . --build=missing

REM Generate solution 
cmake  -DCMAKE_GENERATOR_TOOLSET=v141 -DCONAN_CMAKE_SILENT_OUTPUT=ON -Wno-dev . -B build