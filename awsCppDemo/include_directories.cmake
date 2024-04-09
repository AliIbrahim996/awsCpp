function(set_include_directories_for_target target)
target_include_directories(${target} PRIVATE ${AWSSDK_INCLUDE_DIRS})
target_include_directories(${target} PRIVATE ${aws-crt-cpp_INCLUDE_DIRS})
target_include_directories(${target} PRIVATE ${aws-c-common_INCLUDE_DIRS})
# Add more include directories as needed
endfunction()
