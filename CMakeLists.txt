cmake_minimum_required(VERSION 3.22)
project(cli_skeleton)

set(CMAKE_CXX_STANDARD 14)

include_directories(.)
include_directories(menu)
include_directories(menu/account/draw)
include_directories(menu/account/login)
include_directories(menu/account/recover)
include_directories(menu/account/register)
include_directories(menu/data/connect)
include_directories(menu/data/draw)
include_directories(mongodb)
include_directories(mongodb/account)
include_directories(mongodb/account/login)
include_directories(mongodb/account/recover)
include_directories(mongodb/account/register)

add_executable(cli_skeleton
        menu/account/draw/x.cpp
        menu/account/draw/x.h
        menu/account/login/x.cpp
        menu/account/login/x.h
        menu/account/recover/x.cpp
        menu/account/recover/x.h
        menu/account/register/x.cpp
        menu/account/register/x.h
        menu/data/connect/x.cpp
        menu/data/connect/x.h
        menu/data/draw/x.cpp
        menu/data/draw/x.h
        menu/menu.cpp
        menu/menu.h
        mongodb/account/login/x.cpp
        mongodb/account/login/x.h
        mongodb/account/recover/x.cpp
        mongodb/account/recover/x.h
        mongodb/account/register/x.cpp
        mongodb/account/register/x.h
        mongodb/account/x.cpp
        mongodb/account/x.h
        mongodb/x.cpp
        mongodb/x.h
        main.cpp
        main.h)
