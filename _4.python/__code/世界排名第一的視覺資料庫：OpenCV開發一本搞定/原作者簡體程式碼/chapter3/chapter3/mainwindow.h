#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
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
private slots:
         void on_openLenaJpg_triggered();

         void on_exitSystem_triggered();

         void on_openCustomeFile_triggered();

         void on_restoreFile_triggered();

         void on_copyright_triggered();

         void on_about_triggered();

         void on_actionSobel_triggered();

         void on_actionCanny_triggered();

         void on_actionLaplacian_triggered();

         void on_actionDx_triggered();

         void on_actionDy_triggered();

         void on_actionDx_dy_triggered();

         void on_action1_triggered();

         void on_action3_triggered();

         void on_action5_triggered();

         void on_action7_triggered();

         void on_action1_2_triggered();

         void on_action0_5_triggered();

         void on_action2_triggered();

         void on_actionDelta_1_triggered();

         void on_actionDelta_0_triggered();

         void on_actionDelta_2_triggered();

         void on_action50_triggered();

         void on_action100_triggered();

         void on_action150_triggered();

         void on_action200_triggered();

         void on_actionAs_1_triggered();

         void on_actionAs_3_triggered();

         void on_actionAs_4_triggered();

         void on_actionFalse_triggered();

         void on_actionTrue_triggered();

         void on_actionKsize_1_triggered();

         void on_actionKsize_3_triggered();

         void on_actionKsize_5_triggered();

         void on_actionScale_1_triggered();

         void on_actionScale_0_5_triggered();

         void on_actionScale_3_triggered();

         void on_actionDelta_4_triggered();

         void on_actionDelta_50_triggered();

         void on_actionDelta_100_triggered();

         void on_actionX_triggered();

         void on_actionY_triggered();

         void on_actionX_y_triggered();

         void on_actionSscale_1_triggered();

         void on_actionSscale_0_5_triggered();

         void on_actionSscale_2_triggered();

         void on_actionSdelta_0_triggered();

         void on_actionSdelta_50_triggered();

         void on_actionSdelta_100_triggered();

         void on_actionScharr_triggered();

         void on_action_triggered();

         void on_Clear_triggered();

private:
    Ui::MainWindow *ui;
};

#endif // MAINWINDOW_H
