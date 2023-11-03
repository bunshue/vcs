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
    cv::Mat chaoticImg;
    QImage img;
private slots:
    void on_openLenaJpg_triggered();

    void on_exitSystem_triggered();

    void on_openCustomeFile_triggered();

    void on_restoreFile_triggered();

    void on_copyright_triggered();

    void on_about_triggered();

    void on_actionTest_triggered();
    //  void showLabel(Mat m, QLabel *l);
    void showLabel(cv::Mat m,QLabel *l);//开始设置的时候使用了void showLabel(cv::Mat m,QLabel l)，注意QLabel是指针。
void showLabelGray(cv::Mat m,QLabel *l);
    void on_blackAndWhite_triggered();

    void on_myGray_triggered();

    void on_myColor_triggered();

    void creatChaoticImage(float init);

    void on_cryp_triggered();

    void on_deCryp_triggered();

    void on_encryp_triggered();

    void on_Sencryp_triggered();

    void on_Sdecryp_triggered();

private:
    Ui::MainWindow *ui;
};

#endif // MAINWINDOW_H
