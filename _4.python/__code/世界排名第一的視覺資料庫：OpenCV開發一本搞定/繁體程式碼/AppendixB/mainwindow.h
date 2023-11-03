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
    //srcImage，源檔案。dstImage，目的檔案。tempImage，暫存檔。
    cv::Mat srcImage,dstImage,tempImage;
    //img，Qimage型態檔案，用於顯示時使用。
    QImage img;

private slots:
    //開啟目前目錄下測試檔案lena.jpg
    void on_openLenaJpg_triggered();
    //開啟自訂檔案
    void on_openCustomeFile_triggered();
    //復原圖形，將標簽“目的圖形”內圖形置換為原始圖形
    void on_restoreFile_triggered();
    //清除標簽內圖形
    void on_CLEAR_triggered();
    //離開系統
    void on_exitSystem_triggered();
    //版權說明
    void on_copyright_triggered();
    //關於
    void on_about_triggered();
    //臨時測試用。
    void on_action_triggered();

private:
    Ui::MainWindow *ui;
};

#endif // MAINWINDOW_H
