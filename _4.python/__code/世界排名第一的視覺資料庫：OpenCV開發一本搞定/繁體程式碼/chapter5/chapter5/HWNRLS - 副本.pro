#-------------------------------------------------
#
# Project created by QtCreator 2014-06-17T21:28:29
#
#-------------------------------------------------

QT       += core gui

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

TARGET = MIPALS
TEMPLATE = app


SOURCES += main.cpp\
        mainwindow.cpp

HEADERS  += mainwindow.h

FORMS    += mainwindow.ui
INCLUDEPATH+=d:\opencv249\include\opencv\
                    d:\opencv249\include\opencv2\
                    d:\opencv249\include

LIBS+=d:\opencv249\lib\libopencv_calib3d249.dll.a\
        d:\opencv249\lib\libopencv_contrib249.dll.a\
        d:\opencv249\lib\libopencv_core249.dll.a\
        d:\opencv249\lib\libopencv_features2d249.dll.a\
        d:\opencv249\lib\libopencv_flann249.dll.a\
        d:\opencv249\lib\libopencv_gpu249.dll.a\
        d:\opencv249\lib\libopencv_highgui249.dll.a\
        d:\opencv249\lib\libopencv_imgproc249.dll.a\
        d:\opencv249\lib\libopencv_legacy249.dll.a\
        d:\opencv249\lib\libopencv_ml249.dll.a\
        d:\opencv249\lib\libopencv_objdetect249.dll.a\
        d:\opencv249\lib\libopencv_video249.dll.a
