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
    cv::Mat wmImage,ExtractWM;
    cv::Mat embedSrc,extractSrc;

    QImage img;
private slots:
    void on_openLenaJpg_triggered();

    void on_exitSystem_triggered();

    void on_openCustomeFile_triggered();

    void on_restoreFile_triggered();

    void on_copyright_triggered();

    void on_about_triggered();

    void on_action_triggered();
    void showLabel(cv::Mat m,QLabel *l);//开始设置的时候使用了void showLabel(cv::Mat m,QLabel l)，注意QLabel是指针。
    void showLabelGray(cv::Mat m,QLabel *l);
    void GrayBitImage(int n);
    void on_embed_triggered();

    void on_extract_triggered();



    void on_NEmbed_triggered();

    void on_NExtract_triggered();

    void on_Rcolor_triggered();

    void on_Gcolor_triggered();

    void on_Bcolor_triggered();

    void on_Rgrey_triggered();

    void on_Ggrey_triggered();

    void on_Bgrey_triggered();

    void on_first_triggered();

    void on_second_triggered();

    void on_third_triggered();

    void on_fourth_triggered();

    void on_fifth_triggered();

    void on_sixth_triggered();

    void on_seventh_triggered();

    void on_eighth_triggered();

    void on_firstGray_triggered();

    void on_secondGray_triggered();

    void on_thirdGray_triggered();

    void on_fourthGray_triggered();

    void on_fifthGray_triggered();

    void on_sixthGray_triggered();

    void on_seventhGray_triggered();

    void on_eighthGray_triggered();

    void on_BRembed_triggered();

    void on_BRextract_triggered();

    void on_NBRembed_triggered();

    void on_NBRextract_triggered();

    void on_zero_triggered();

    void on_one_triggered();

    void on_two_triggered();

    void on_three_triggered();

    void on_four_triggered();

    void on_five_triggered();

    void on_six_triggered();

    void on_seven_triggered();

    void on_zeroGray_triggered();

    void on_oneGray_triggered();

    void on_twoGray_triggered();

    void on_threeGray_triggered();

    void on_fourGray_triggered();

    void on_fiveGray_triggered();

    void on_sixGray_triggered();

    void on_sevenGray_triggered();

private:
    Ui::MainWindow *ui;
};

#endif // MAINWINDOW_H
