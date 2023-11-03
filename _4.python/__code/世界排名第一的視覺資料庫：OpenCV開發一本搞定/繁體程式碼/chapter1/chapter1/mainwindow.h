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
    void on_action_2_triggered();

   void on_action_4_triggered();

   void on_action_3_triggered();

   void on_action_triggered();

   void on_action_5_triggered();

   void on_action_6_triggered();

   void on_action_7_triggered();

   void on_action_8_triggered();

   void on_copyright_triggered();

   void on_Horizen_triggered();

   void on_about_triggered();

   void on_openTestFile_triggered();

   void on_myExit_triggered();

   void on_openCustomeFile_triggered();

   void on_vertical_triggered();

   void on_horizenAndVertical_triggered();

   void on_restore_triggered();

   void on_about2_triggered();

   void on_about3_triggered();

   void on_actionSobel2_triggered();

   void on_actionSobel_triggered();

   void on_actionSobel5_triggered();

   void on_actionLaplacian_triggered();

   void on_actionCanny_triggered();

   void on_normalizeFilter_triggered();

   void on_GaussFilter_triggered();

   void on_medianFilter_triggered();

   void on_bilateralFilter_triggered();

   void on_Erosion_triggered();

   void on_dialation_triggered();

   void on_opening_triggered();

   void on_closing_triggered();

   void on_actionMorphological_Gradient_triggered();

   void on_topHat_triggered();

   void on_blackHat_triggered();

   void on_PyrUpAction_triggered();

   void on_PyrDownAction_triggered();

   void on_ResizeUp_triggered();

   void on_ResizeDown_triggered();

   void on_cNresize_triggered();

   void on_cResize_triggered();

   void on_antiClockwise_triggered();

   void on_NFlipResize_triggered();

   void on_Clear_triggered();

   void on_actionGuiyihua_triggered();

   void on_actionFeiguiyihua_triggered();

   void on_normalize_triggered();

   void on_NoNormalize_triggered();

private:
    Ui::MainWindow *ui;
};

#endif // MAINWINDOW_H
