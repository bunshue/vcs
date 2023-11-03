#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc/imgproc.hpp>
#include <QLabel>

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
    cv::Mat testImage,srcImage[10],tempImage;//testImage值要測試的數字圖形，srcImage指已經有的用來實現分類別的數字圖形
    Mat dstImage;  //用於在圖形處理算法示範時在右側顯示的目的圖形
    QImage img;
    float testFeature[25];//該陣列用來儲存待檢驗數字圖形的特征值。
    float srcFeature[10][25];//用來儲存原始數字圖形的特征值。只有10個數字0~9的圖形
    void getFeature(cv::Mat m,float a[25]);//這裡定義一個取得圖形特征的函數。
    float ouDistance(float a[25],float b[25]);
    float oDistance(float a[25],float b[25]);
    int getResultNumber();
    void showLabel(cv::Mat m,QLabel *l);//開始設定的時候使用了void showLabel(cv::Mat m,QLabel l)，注意QLabel是指標。

private slots:
    void on_openTestJpg_triggered();

    void on_exitSystem_triggered();

    void on_openCustomeFile_triggered();

    void on_restoreFile_triggered();

    void on_copyright_triggered();

    void on_about_triggered();

    void on_showImage_triggered();

    void on_showMessage_triggered();

    void on_ImageAndMessage_triggered();

    void on_horizenFlip_triggered();

    void on_VerticalFlip_triggered();

    void on_VerticalAndHorizen_triggered();

    void on_erode_triggered();

    void on_dialate_triggered();

    void on_open_triggered();

    void on_close_triggered();

    void on_topHat_triggered();

    void on_blackHat_triggered();

    void on_actionSobel_triggered();

    void on_actionCanny_triggered();

    void on_actionLaplacian_triggered();

    void on_actionScharr_triggered();

    void on_gray_triggered();

    void on_binValue_triggered();

    void on_invertColor_triggered();

    void on_rSpace_triggered();

    void on_gSpace_triggered();

    void on_bSpace_triggered();

    void on_actionRtong_triggered();

    void on_Rchannel_triggered();

    void on_Gchannel_triggered();

    void on_Bchannel_triggered();

    void on_about_2_triggered();

    void on_aboutMe_triggered();

    void on_contacctUs_triggered();

    void on_openLenaJpg_triggered();

    void on_Clear_triggered();

private:
    Ui::MainWindow *ui;
};

#endif // MAINWINDOW_H
