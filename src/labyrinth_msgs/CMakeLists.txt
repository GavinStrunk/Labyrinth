cmake_minimum_required(VERSION 3.5)
project(labyrinth_msgs)

set(CMAKE_CXX_STANDARD 17)

find_package(ament_cmake REQUIRED)
find_package(rosidl_default_generators REQUIRED)

set(msg_files
 "msg/Servo.msg"
)

rosidl_generate_interfaces(${PROJECT_NAME}
   ${msg_files}
)

ament_export_dependencies(rosidl_default_runtime)
ament_package()
