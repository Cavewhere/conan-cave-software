cmake_minimum_required(VERSION 3.1)
project(PackageTest CXX)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

message("Survex bin:${CONAN_BIN_DIRS_SURVEX}")

find_program(CAVERN_COMMAND "cavern"
    PATHS ${CONAN_BIN_DIRS_SURVEX}
    REQUIRED)

#get_filename_component(CAVERN_FILENAME ${CAVERN_COMMAND} NAME)
file(COPY ${CONAN_BIN_DIRS_SURVEX} DESTINATION ${PROJECT_BINARY_DIR})

#add_executable(example example.cpp)
#target_link_libraries(example ${CONAN_LIBS})

# CTest is a testing tool that can be used to test your project.
# enable_testing()
# add_test(NAME example
#          WORKING_DIRECTORY ${CMAKE_BINARY_DIR}/bin
#          COMMAND example)
