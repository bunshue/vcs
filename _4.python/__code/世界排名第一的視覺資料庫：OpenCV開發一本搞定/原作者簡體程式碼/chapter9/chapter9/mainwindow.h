#ifndef MAINWINDOW_H
#define MAINWINDOW_H
#define fileNumber 16
#define featureNumber 64
#include <QMainWindow>
#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/core/core.hpp>

#include <opencv2/imgproc/imgproc.hpp>
#include <QLabel>
#include <qdir.h>
namespace Ui {
class MainWindow;
}

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit MainWindow(QWidget *parent = 0);
    ~MainWindow();
    cv::Mat srcImage,dstImage,tempImage;
    QImage img;
    void showLabel(cv::Mat m,QLabel *l);
    //开始设置的时候使用了void showLabel(cv::Mat m,QLabel l)，注意QLabel是指针。
    void showLabelGray(cv::Mat,QLabel *l);
    void getFeature(cv::Mat m,int t[]);
    //函数 void getFeature(cv::Mat m,int t[])，通过数组参数传递得到的特征值。
    int* getFeature2(cv::Mat m);
    //函数int* getFeature2(cv::Mat m)，通过返回值获得特征值。
    int mm=8,nn=8;
    //mm，nn为缩小后图像的大小。
    int cc=64;
    //cc为图像简化色彩后的灰度级数。
    int FileFeature[fileNumber][featureNumber];
    //产生无重复的随机数；
   // static  int[]  GetRandomSequence0(int total);
    int total;//指定目录下文件个数。
    QList<QFileInfo> *fileInfo;
private slots:
    void on_openLenaJpg_triggered();

    void on_exitSystem_triggered();

    void on_openCustomeFile_triggered();

    void on_restoreFile_triggered();

    void on_copyright_triggered();

    void on_about_triggered();

    void on_pushButton_clicked();

    void on_pushButton_3_clicked();

    void on_pushButton_4_clicked();

    void on_pushButton_6_clicked();

    void on_pushButton_5_clicked();
    //设置srcImage为当前目录下序号为i的图像。
    void getImage(QList<QFileInfo> *fileInfo,int i);


    void on_pushButton_2_clicked();

    void on_action_triggered();

    void on_action_2_triggered();

    void on_action_3_triggered();

private:
    Ui::MainWindow *ui;
};

#endif // MAINWINDOW_H
