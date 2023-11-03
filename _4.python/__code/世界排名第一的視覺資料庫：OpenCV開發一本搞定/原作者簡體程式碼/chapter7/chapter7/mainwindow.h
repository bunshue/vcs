#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <QLabel>
//#include "opencv2/contrib/contrib.hpp"
#include <opencv2/imgproc/imgproc.hpp>
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
 void showLabel(cv::Mat m,QLabel *l);//开始设置的时候使用了void showLabel(cv::Mat m,QLabel l)，注意QLabel是指针。
private slots:
         void on_openLenaJpg_triggered();

         void on_exitSystem_triggered();

         void on_openCustomeFile_triggered();

         void on_restoreFile_triggered();

         void on_copyright_triggered();

         void on_about_triggered();

         void on_actionTest_triggered();
         void on_tu1_triggered();

         void on_tu2_triggered();

         void on_tu3_triggered();

         void on_tu4_triggered();

         void on_aoA_triggered();

         void on_aoB_triggered();

         void on_aoC_triggered();

         void on_aoD_triggered();

         void on_action_triggered();

         void on_action_2_triggered();

         void on_action_3_triggered();

         void on_action_4_triggered();

         void on_woodCarving_triggered();

         void on_pencil_triggered();

         void on_sketch_triggered();

         void on_diffuse_triggered();

         void on_blur_triggered();

         void on_soft_triggered();

         void on_sharp_triggered();

         void on_filterMax_triggered();

         void on_filterMin_triggered();

         void on_picBook_triggered();

         void on_colorMap_triggered();

         void on_rChanel_triggered();

         void on_gChanel_triggered();

         void on_bChanel_triggered();

         void on_inverse_triggered();

         void on_highLight_triggered();

         void on_blackAndWhiteInverse_triggered();

         void on_casting_triggered();

         void on_freezing_triggered();

         void on_oldPic_triggered();

         void on_exchangeRG_triggered();

         void on_toGray_triggered();

         void on_toBin_triggered();

         void on_Clear_triggered();

private:
    Ui::MainWindow *ui;
};

#endif // MAINWINDOW_H
