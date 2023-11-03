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
INCLUDEPATH+=E:\QTAndOpenCV\buildOpenCV3\include
E:\QTAndOpenCV\buildOpenCV3\include\opencv
E:\QTAndOpenCV\buildOpenCV3\include\opencv2
LIBS +=E:\QTAndOpenCV\buildOpenCV3\lib\libopencv_*.a

