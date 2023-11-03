#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc/imgproc.hpp>
#include <QLabel>
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
         void showLabel(cv::Mat m, QLabel *l);
         void showNumber(int n);
 int T[10][3][3];
private slots:
         void on_openLenaJpg_triggered();

         void on_exitSystem_triggered();

         void on_openCustomeFile_triggered();

         void on_restoreFile_triggered();

         void on_copyright_triggered();

         void on_about_triggered();

         void on_actionTest_triggered();

         void on_myDefine_triggered();

         void on_windowShow_triggered();

         void on_useResize_triggered();

         void on_horizen_triggered();

         void on_action_2_triggered();

         void on_vertical_triggered();

         void on_circle_triggered();

         void on_action_4_triggered();

         void on_mySum_triggered();

         void on_myAbstrct_triggered();

         void on_myTriple_triggered(bool checked);

         void on_myRand_triggered();

         void on_myIndex_triggered();

         void on_myRand2_triggered();

         void on_myRand3_triggered();

         void on_number0_triggered();

         void on_number1_triggered();

         void on_number2_triggered();

         void on_number4_triggered();

         void on_number3_triggered();

         void on_number5_triggered();

         void on_number6_triggered();

         void on_number7_triggered();

         void on_number8_triggered();

         void on_number9_triggered();

         void on_aboutMe_triggered();

         void on_contactUs_triggered();

         void on_myTriple_triggered();

         void on_Clear_triggered();

private:
    Ui::MainWindow *ui;
};

#endif // MAINWINDOW_H
