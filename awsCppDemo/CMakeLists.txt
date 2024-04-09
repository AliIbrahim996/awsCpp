cmake_minimum_required(VERSION 3.2)

project(AwsCppDemo)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)
include(set_dirs.cmake)
include(include_directories.cmake)

# Find AWSSDK
find_package(AWSSDK REQUIRED)

# Source files
file(GLOB_RECURSE SOURCES "src/*.cpp")
file(GLOB_RECURSE HEADERS "include/*.h" "include/*.hpp")

# Add executable
add_executable(${PROJECT_NAME} main.cpp ${SOURCES} ${HEADERS})
set_target_properties(${PROJECT_NAME} PROPERTIES
                      CXX_STANDARD 17
                      CXX_STANDARD_REQUIRED ON)

# Include directories
target_include_directories(${PROJECT_NAME} PRIVATE "include")
set_include_directories_for_target(${PROJECT_NAME})

# Link libraries
target_link_libraries(${PROJECT_NAME} PRIVATE ${AWSSDK_LIBRARIES})