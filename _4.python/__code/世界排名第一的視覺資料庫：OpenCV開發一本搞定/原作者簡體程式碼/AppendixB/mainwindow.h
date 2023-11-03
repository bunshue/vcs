#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <QString>
#include <QFileDialog>
#include <QMessageBox>
#include <opencv/cv.h>
#include <QTextCodec>
#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc/imgproc.hpp>
#include "mainwindow.h"
#include "ui_mainwindow.h"
using namespace cv;

namespace Ui {
class MainWindow;
}

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit MainWindow(QWidget *parent = 0);
    ~MainWindow();
    //srcImage，源文件。dstImage，目标文件。tempImage，临时文件。
    cv::Mat srcImage,dstImage,tempImage;
    //img，Qimage类型文件，用于显示时使用。
    QImage img;

private slots:
    //打开当前目录下测试文件lena.jpg
    void on_openLenaJpg_triggered();
    //打开自定义文件
    void on_openCustomeFile_triggered();
    //还原图像，将标签“目标图像”内图像替换为原始图像
    void on_restoreFile_triggered();
    //清除标签内图像
    void on_CLEAR_triggered();
    //退出系统
    void on_exitSystem_triggered();
    //版权说明
    void on_copyright_triggered();
    //关于
    void on_about_triggered();
    //临时测试用。
    void on_action_triggered();

private:
    Ui::MainWindow *ui;
};

#endif // MAINWINDOW_H
