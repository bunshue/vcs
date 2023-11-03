#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
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

         void on_HistEqualize_triggered();

         void on_contrast_triggered();

         void on_light_triggered();

         void on_filter2D1_triggered();

         void on_filter2D2_triggered();

         void on_filter2D3_triggered();

         void on_filter2D4_triggered();

         void on_filter2D5_triggered();

         void on_filter2D6_triggered();

         void on_contrastAndLight_triggered();

         void on_actionCV_TM_SQDIFF_triggered();

         void on_actionCV_TM_SQDIFF_NORMED_triggered();

         void on_actionCV_TM_CCORR_triggered();

         void on_actionCV_TM_CCORR_NORMED_triggered();

         void on_actionCV_TM_CCOEFF_triggered();

         void on_actionCV_TM_CCOEFF_NORMED_triggered();

         void on_resizeSmall_triggered();

         void on_resizeBig_triggered();

         void on_mirrorHorizen_triggered();

         void on_mirrorVertical_triggered();

         void on_mirrorHorizenAndVertical_triggered();

         void on_wrapAffine_triggered();

         void on_rotateWrapAffine_triggered();

         void on_remapX_triggered();

         void on_remapY_triggered();

         void on_remapSmall_triggered();

         void on_remapRotate_triggered();

         void on_clockwise_triggered();

         void on_clockwiseResize_triggered();

         void on_UNclockwise_triggered();

         void on_zeroRotateResize_triggered();

         void on_actionTHRESH_BINARY_triggered();

         void on_actionTHRESH_BINARY_INV_triggered();

         void on_actionTHRESH_TRUNC_triggered();

         void on_actionTHRESH_TOZERO_triggered();

         void on_actionTHRESH_TOZERO_INV_2_triggered();

         void on_actionTHRESH_BINARY_2_triggered();

         void on_actionTHRESH_BINARY_3_triggered();

         void on_actionTHRESH_BINARY_INV_3_triggered();

         void on_actionTHRESH_TRUNC_2_triggered();

         void on_actionTHRESH_TOZERO_2_triggered();

         void on_actionTHRESH_TOZERO_INV_triggered();

         void on_actionTHRESH_BINARY_INV_4_triggered();

         void on_actionADAPTIVE_THRESH_MEAN_C_triggered();

         void on_actionADAPTIVE_THRESH_GAUSSIAN_C_triggered();

         void on_actionADAPTIVE_THRESH_MEAN_C_2_triggered();

         void on_actionADAPTIVE_THRESH_GAUSSIAN_C_2_triggered();

         void on_action_triggered();

         void on_action_2_triggered();

         void on_action_3_triggered();

         void on_action_4_triggered();

         void on_action_5_triggered();

         void on_remapDiagonal_triggered();

         void on_remapCopy_triggered();

         void on_actionTHRESH_BINARY_INV_2_triggered();

         void on_actionTHRESH_TRUNC_3_triggered();

         void on_actionTHRESH_TOZERO_3_triggered();

         void on_actionTHRESH_TOZERO_INV_3_triggered();

         void on_Clear_triggered();

private:
    Ui::MainWindow *ui;
};

#endif // MAINWINDOW_H
