#!/bin/bash

# detect profile
conan profile detect

# run conan install
conan install . --build=missing || exit 2

# Generate solution
cmake -DCMAKE_GENERATOR_TOOLSET=v141 -DCONAN_CMAKE_SILENT_OUTPUT=ON -Wno-dev . -B build || exit $?