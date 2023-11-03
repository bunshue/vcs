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
    //開始設定的時候使用了void showLabel(cv::Mat m,QLabel l)，注意QLabel是指標。
    void showLabelGray(cv::Mat,QLabel *l);
    void getFeature(cv::Mat m,int t[]);
    //函數 void getFeature(cv::Mat m,int t[])，透過陣列參數傳遞得到的特征值。
    int* getFeature2(cv::Mat m);
    //函數int* getFeature2(cv::Mat m)，透過傳回值獲得特征值。
    int mm=8,nn=8;
    //mm，nn為拉遠後圖形的大小。
    int cc=64;
    //cc為圖形簡化色彩後的灰階級數。
    int FileFeature[fileNumber][featureNumber];
    //產生無重復的隨機數；
   // static  int[]  GetRandomSequence0(int total);
    int total;//指定目錄下檔案個數。
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
    //設定srcImage為目前目錄下序號為i的圖形。
    void getImage(QList<QFileInfo> *fileInfo,int i);


    void on_pushButton_2_clicked();

    void on_action_triggered();

    void on_action_2_triggered();

    void on_action_3_triggered();

private:
    Ui::MainWindow *ui;
};

#endif // MAINWINDOW_H
