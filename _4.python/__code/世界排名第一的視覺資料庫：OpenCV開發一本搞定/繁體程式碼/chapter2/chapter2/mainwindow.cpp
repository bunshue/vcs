#include "mainwindow.h"
#include "ui_mainwindow.h"
#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QString>
#include <QFileDialog>
#include <QMessageBox>
#include <opencv/cv.h>
#include <QTextCodec>
#include "opencv2/highgui/highgui.hpp"
#include "opencv2/imgproc/imgproc.hpp"
#include <iostream>
#include <stdio.h>
using namespace cv;
using namespace std;
//  版權訊息：  lilizong[at]gmail.com
MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::on_openLenaJpg_triggered()
{
    srcImage = cv::imread("lena.jpg");
    if(!srcImage.data)
    {
        QMessageBox msgBox;
        msgBox.setText(tr("預設的測試檔案不存在，可以用以下兩種模式的一種：1）複製一個檔案到目前目錄下，並命名為lena.jpg. 2)使用自訂模式開啟一個自訂檔案。"));
        msgBox.exec();
    }
    else
    {
        cv::cvtColor(srcImage,srcImage,CV_BGR2RGB);
        img = QImage((const unsigned char*)(srcImage.data),srcImage.cols,srcImage.rows, srcImage.cols*srcImage.channels(),QImage::Format_RGB888);
        ui->label1->clear();
        img=  img.scaled(ui->label1->width(), ui->label1->height());
        ui->label1->setPixmap(QPixmap::fromImage(img));
        //ui->processPushButton->setEnabled(true);
        //   ui->label1->resize(ui->label1->pixmap()->size());//設定目前標簽為圖形大小
        // ui->label1->resize(img.width(),img.height());

        //this->setWidget(label1);
    }
}

void MainWindow::on_exitSystem_triggered()
{
    exit(0);
}

void MainWindow::on_openCustomeFile_triggered()
{
    QString filename = QFileDialog::getOpenFileName(this,tr("Open Image"),"",tr("Image File(*.bmp *.jpg *.jpeg *.png)"));
    QTextCodec *code = QTextCodec::codecForName("gb18030");
    std::string name = code->fromUnicode(filename).data();
    srcImage = cv::imread(name);
    if(!srcImage.data)
    {
        QMessageBox msgBox;
        msgBox.setText(tr("找不到資料"));
        msgBox.exec();
    }
    else
    {
        cv::cvtColor(srcImage,srcImage,CV_BGR2RGB);
        img = QImage((const unsigned char*)(srcImage.data),srcImage.cols,srcImage.rows, srcImage.cols*srcImage.channels(), QImage::Format_RGB888);
        ui->label1->clear();
        img=  img.scaled(ui->label1->width(), ui->label1->height());
        ui->label1->setPixmap(QPixmap::fromImage(img));
        //ui->processPushButton->setEnabled(true);
        //   ui->label1->resize(ui->label1->pixmap()->size());//設定目前標簽為圖形大小
        // ui->label1->resize(img.width(),img.height());

        //this->setWidget(label1);
    }
}

void MainWindow::on_restoreFile_triggered()
{
    srcImage.copyTo(dstImage);
    img = QImage((const unsigned char*)
                 (dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),
                 QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_copyright_triggered()
{
    QMessageBox::information(this,"版權",tr("本軟體版權所有者為：天津職業技術師范大學。若果使用，請聯繫：lilizong@gmail.com"));
}

void MainWindow::on_about_triggered()
{
    QMessageBox::information(this,"關於",tr("本軟體目前版本為1.0，由李立宗等人開發。若果有問題，歡迎聯繫：lilizong@gmail.com"));
    return;
}

void MainWindow::on_HistEqualize_triggered()
{
    //直方圖均衡化
    //定義一個陣列，用來儲存各通道圖片的向量
    vector<Mat> splitBGR(srcImage.channels());
    //分割通道，儲存到splitBGR中
    split(srcImage,splitBGR);
    //對各個通道分別進行直方圖均衡化
    for(int i=0; i<srcImage.channels(); i++)
        equalizeHist(splitBGR[i],splitBGR[i]);
    Mat mergeImg;//合並後的圖形
    //合並通道
    merge(splitBGR,mergeImg);
    //複製圖形
    mergeImg.copyTo(dstImage);
    // cv::cvtColor(dstImage,dstImage,CV_BGR2RGB);  //開啟檔案時已經完成BRG到RGB的轉換
    //顯示圖形
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_contrast_triggered()
{
    //調節比較度
    //這裡僅僅調整alpha的值，beta預設為0.
    srcImage.convertTo(dstImage,-1,2);
    //顯示圖形
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_light_triggered()
{
    //調節亮度
    //這裡僅僅調整beta的值，alpha設定為1.
    srcImage.convertTo(dstImage,-1,1,80);
    //顯示圖形
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_filter2D1_triggered()
{
    //算子1
    //建立核
    Mat kernel = (Mat_<float>(3, 3) << 0, -1, 0, -1, 5, -1, 0, -1, 0);
    //套用函數filter2D處理。
    filter2D(srcImage,dstImage, srcImage.depth(), kernel);
    //顯示圖形
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_filter2D2_triggered()
{
    //算子2
    //建立核
    Mat kernel(3,3,CV_32F,Scalar(-1));
    // 分配像素值
    kernel.at<float>(1,1) = 8;
    //呼叫函數filter2D處理
    filter2D(srcImage,dstImage, srcImage.depth(), kernel);
    //顯示圖形
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_filter2D3_triggered()
{
    //算子3
    //建構核
    Mat kernel(3,3,CV_32F,Scalar(-1));
    kernel.at<float>(1,1) = 8.9;
    //呼叫filter2D函數
    filter2D(srcImage,dstImage, srcImage.depth(), kernel);
    //顯示圖形
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_filter2D4_triggered()
{
    //算子4
    Mat kernel(3,3,CV_32F,cv::Scalar(0));
    kernel.at<float>(1,1) = 5.0;
    kernel.at<float>(0,1) = -1.0;
    kernel.at<float>(2,1) = -1.0;
    //呼叫filter2D
    filter2D(srcImage,dstImage, srcImage.depth(), kernel);
    //顯示圖形
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_filter2D5_triggered()
{
    //算子5
    Mat kernel(3,3,CV_32F,cv::Scalar(0));
    kernel.at<float>(1,1) = 5.0;
    kernel.at<float>(1,0) = -1.0;
    kernel.at<float>(1,2) = -1.0;
    //呼叫filter2D
    filter2D(srcImage,dstImage, srcImage.depth(), kernel);
    //顯示圖形
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_filter2D6_triggered()
{
    //算子6
    Mat kernel = (Mat_<float>(3, 3) << 0, -1, 0, -1, 6, -1, 0, -1, 0);
    filter2D(srcImage,dstImage, srcImage.depth(), kernel);
    //顯示圖形
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_contrastAndLight_triggered()
{
    //同時調節亮度、比較度
    //同時調整參數alpha、beta
    srcImage.convertTo(dstImage,-1,2,80);
    //顯示圖形
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_actionCV_TM_SQDIFF_triggered()
{
    //SQDIFF效果
    //定義範本、結果
    Mat templ;
    Mat result;
    /* match_method只能取0~5之中的某一個值，即：
      * method=TM_SQDIFF             （0）
      * method=TM_SQDIFF_NORMED      （1）
        method=TM_CCORR              （2）
        method=TM_CCORR_NORMED       （3）
        method=TM_CCOEFF ·           （4）
        method=TM_CCOEFF_NORMED      （5）
    */
    //設定比對方法
    int match_method=0;
    /***************************************開啟範本檔案*********************************************/
    //注意這裡在主界面的左上角加入了一個標簽，專門用於顯示範本圖形
    QString filename = QFileDialog::getOpenFileName(this,tr("開啟範本圖形"),"",tr("Image File(*.bmp *.jpg *.jpeg *.png)"));
    QTextCodec *code = QTextCodec::codecForName("gb18030");
    std::string name = code->fromUnicode(filename).data();
    templ = cv::imread(name);
    if(!templ.data)
    {
        QMessageBox msgBox;
        msgBox.setText(tr("找不到資料"));
        msgBox.exec();
    }
    else
    {
        cv::cvtColor(templ,templ,CV_BGR2RGB);
        img = QImage((const unsigned char*)(templ.data),templ.cols,templ.rows, templ.cols*templ.channels(), QImage::Format_RGB888);
        ui->label3->clear();
        img=  img.scaled(ui->label3->width(), ui->label3->height());
        ui->label3->setPixmap(QPixmap::fromImage(img));
    }
    /***************************************開啟範本檔案*********************************************/
    //用於顯示的圖形
    Mat img_display;
    //複製圖形srcImage到img_display
    srcImage.copyTo( img_display );
    //產生結果
    int result_cols =  srcImage.cols - templ.cols + 1;
    int result_rows = srcImage.rows - templ.rows + 1;
    /*
     * 需要注意，目的圖形的大小為int result_cols =  srcImage.cols - templ.cols + 1;
    int result_rows = srcImage.rows - templ.rows + 1;
    這是因為範本沿著原始圖形上的每一個點進行檢查，而產生一個目的圖形內的點，
    當圖形檢查到其右側時，只能檢查到其從左側數第 srcImage.cols - templ.cols + 1個點。
    當圖形檢查到其下側時，只能檢查到其從上側數第 srcImage.rows - templ.rows + 1個點。
    */
    result.create( result_cols, result_rows, CV_32FC1 );
    //進行範本比對動作
    cv::matchTemplate( srcImage, templ, result, match_method );
    normalize( result, result, 0, 1, NORM_MINMAX, -1, Mat() );
    //使用minMaxLoc對比對結果進行定位
    double minVal;
    double maxVal;
    Point minLoc;
    Point maxLoc;
    Point matchLoc;
    minMaxLoc( result, &minVal, &maxVal, &minLoc, &maxLoc, Mat() );
    //對於SQDIFF和SQDIFF_NORMED，最好的比對時最小值，其他的是最大值。
    if( match_method  == TM_SQDIFF || match_method == TM_SQDIFF_NORMED )
        matchLoc = minLoc;
    else
        matchLoc = maxLoc;
    //處理結果
    rectangle( img_display, matchLoc, Point( matchLoc.x + templ.cols , matchLoc.y + templ.rows ), Scalar::all(0), 2, 8, 0 );
    rectangle( result, matchLoc, Point( matchLoc.x + templ.cols , matchLoc.y + templ.rows ), Scalar::all(0), 2, 8, 0 );
    img_display.copyTo(dstImage);
    //顯示結果
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
    //視窗顯示測試
    //char* image_window = "Source Image";
    // char* result_window = "Result window";
    // imshow( image_window, img_display );
    //imshow( result_window, result );
}

void MainWindow::on_actionCV_TM_SQDIFF_NORMED_triggered()
{
    Mat templ;
    Mat result;
    /* match_method只能取0~5之間的值，即：
      *method=CV_TM_SQDIFF_NORMED
        method=CV_TM_CCORR
        method=CV_TM_CCORR_NORMED
        method=CV_TM_CCOEFF
        method=CV_TM_CCOEFF_NORMED*/
    int match_method=1;
    char* image_window = "Source Image";
    char* result_window = "Result window";
    /***************************************開啟範本檔案*********************************************/
    QString filename = QFileDialog::getOpenFileName(this,tr("Open Image"),"",tr("Image File(*.bmp *.jpg *.jpeg *.png)"));
    QTextCodec *code = QTextCodec::codecForName("gb18030");
    std::string name = code->fromUnicode(filename).data();
    templ = cv::imread(name);
    if(!templ.data)
    {
        QMessageBox msgBox;
        msgBox.setText(tr("找不到資料"));
        msgBox.exec();
    }
    else
    {
        cv::cvtColor(templ,templ,CV_BGR2RGB);
        img = QImage((const unsigned char*)(templ.data),templ.cols,templ.rows, templ.cols*templ.channels(), QImage::Format_RGB888);
        ui->label3->clear();
        img=  img.scaled(ui->label3->width(), ui->label3->height());
        ui->label3->setPixmap(QPixmap::fromImage(img));
        //ui->processPushButton->setEnabled(true);
        //   ui->label1->resize(ui->label1->pixmap()->size());//設定目前標簽為圖形大小
        // ui->label1->resize(img.width(),img.height());

        //this->setWidget(label1);
    }
    /***************************************開啟範本檔案*********************************************/
    Mat img_display;

    srcImage.copyTo( img_display );

    /// Create the result matrix
    int result_cols =  srcImage.cols - templ.cols + 1;
    int result_rows = srcImage.rows - templ.rows + 1;
    /*
     * 需要注意，目的圖形的大小為int result_cols =  srcImage.cols - templ.cols + 1;
    int result_rows = srcImage.rows - templ.rows + 1;
    這是因為範本沿著原始圖形上的每一個點進行檢查，而產生一個目的圖形內的點，
    當圖形檢查到其右側時，只能檢查到其從右側數第 srcImage.cols - templ.cols + 1個點。
    當圖形檢查到其下側時，只能檢查到其從下側數第 srcImage.rows - templ.rows + 1個點。
    */
    result.create( result_cols, result_rows, CV_32FC1 );

    /// Do the Matching and Normalize
    cv::matchTemplate( srcImage, templ, result, match_method );
    normalize( result, result, 0, 1, NORM_MINMAX, -1, Mat() );

    /// Localizing the best match with minMaxLoc
    double minVal; double maxVal; Point minLoc; Point maxLoc;
    Point matchLoc;

    minMaxLoc( result, &minVal, &maxVal, &minLoc, &maxLoc, Mat() );

    /// For SQDIFF and SQDIFF_NORMED, the best matches are lower values. For all the other methods, the higher the better
    if( match_method  == CV_TM_SQDIFF || match_method == CV_TM_SQDIFF_NORMED )
    { matchLoc = minLoc; }
    else
    { matchLoc = maxLoc; }

    /// Show me what you got
    rectangle( img_display, matchLoc, Point( matchLoc.x + templ.cols , matchLoc.y + templ.rows ), Scalar::all(0), 2, 8, 0 );
    rectangle( result, matchLoc, Point( matchLoc.x + templ.cols , matchLoc.y + templ.rows ), Scalar::all(0), 2, 8, 0 );
    img_display.copyTo(dstImage);
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
    // imshow( image_window, img_display );
    //imshow( result_window, result );
}

void MainWindow::on_actionCV_TM_CCORR_triggered()
{
    //CCORR效果
    //定義範本、結果
    Mat templ;
    Mat result;
    /* match_method只能取0~5之中的某一個值，即：
      * method=TM_SQDIFF             （0）
      * method=TM_SQDIFF_NORMED      （1）
        method=TM_CCORR              （2）
        method=TM_CCORR_NORMED       （3）
        method=TM_CCOEFF ·           （4）
        method=TM_CCOEFF_NORMED      （5）
    */
    //設定比對方法
    int match_method=2;
    /***************************************開啟範本檔案*********************************************/
    //注意這裡在主界面的左上角加入了一個標簽，專門用於顯示範本圖形
    QString filename = QFileDialog::getOpenFileName(this,tr("開啟範本圖形"),"",tr("Image File(*.bmp *.jpg *.jpeg *.png)"));
    QTextCodec *code = QTextCodec::codecForName("gb18030");
    std::string name = code->fromUnicode(filename).data();
    templ = cv::imread(name);
    if(!templ.data)
    {
        QMessageBox msgBox;
        msgBox.setText(tr("找不到資料"));
        msgBox.exec();
    }
    else
    {
        cv::cvtColor(templ,templ,CV_BGR2RGB);
        img = QImage((const unsigned char*)(templ.data),templ.cols,templ.rows, templ.cols*templ.channels(), QImage::Format_RGB888);
        ui->label3->clear();
        img=  img.scaled(ui->label3->width(), ui->label3->height());
        ui->label3->setPixmap(QPixmap::fromImage(img));
    }
    /***************************************開啟範本檔案*********************************************/
    //用於顯示的圖形
    Mat img_display;
    //複製圖形srcImage到img_display
    srcImage.copyTo( img_display );
    //產生結果
    int result_cols =  srcImage.cols - templ.cols + 1;
    int result_rows = srcImage.rows - templ.rows + 1;
    /*
     * 需要注意，目的圖形的大小為int result_cols =  srcImage.cols - templ.cols + 1;
    int result_rows = srcImage.rows - templ.rows + 1;
    這是因為範本沿著原始圖形上的每一個點進行檢查，而產生一個目的圖形內的點，
    當圖形檢查到其右側時，只能檢查到其從左側數第 srcImage.cols - templ.cols + 1個點。
    當圖形檢查到其下側時，只能檢查到其從上側數第 srcImage.rows - templ.rows + 1個點。
    */
    result.create( result_cols, result_rows, CV_32FC1 );
    //進行範本比對動作
    cv::matchTemplate( srcImage, templ, result, match_method );
    normalize( result, result, 0, 1, NORM_MINMAX, -1, Mat() );
    //使用minMaxLoc對比對結果進行定位
    double minVal;
    double maxVal;
    Point minLoc;
    Point maxLoc;
    Point matchLoc;
    minMaxLoc( result, &minVal, &maxVal, &minLoc, &maxLoc, Mat() );
    //對於SQDIFF和SQDIFF_NORMED，最好的比對時最小值，其他的是最大值。
    if( match_method  == TM_SQDIFF || match_method == TM_SQDIFF_NORMED )
        matchLoc = minLoc;
    else
        matchLoc = maxLoc;
    //處理結果
    rectangle( img_display, matchLoc, Point( matchLoc.x + templ.cols , matchLoc.y + templ.rows ), Scalar::all(0), 2, 8, 0 );
    rectangle( result, matchLoc, Point( matchLoc.x + templ.cols , matchLoc.y + templ.rows ), Scalar::all(0), 2, 8, 0 );
    img_display.copyTo(dstImage);
    //顯示結果
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
    //視窗顯示測試
    //char* image_window = "Source Image";
    // char* result_window = "Result window";
    // imshow( image_window, img_display );
    //imshow( result_window, result );
}

void MainWindow::on_actionCV_TM_CCORR_NORMED_triggered()
{
    Mat templ;
    Mat result;
    /* match_method只能取0~5之間的值，即：
      *method=CV_TM_SQDIFF_NORMED
        method=CV_TM_CCORR
        method=CV_TM_CCORR_NORMED
        method=CV_TM_CCOEFF
        method=CV_TM_CCOEFF_NORMED*/
    int match_method=3;
    char* image_window = "Source Image";
    char* result_window = "Result window";
    /***************************************開啟範本檔案*********************************************/
    QString filename = QFileDialog::getOpenFileName(this,tr("Open Image"),"",tr("Image File(*.bmp *.jpg *.jpeg *.png)"));
    QTextCodec *code = QTextCodec::codecForName("gb18030");
    std::string name = code->fromUnicode(filename).data();
    templ = cv::imread(name);
    if(!templ.data)
    {
        QMessageBox msgBox;
        msgBox.setText(tr("找不到資料"));
        msgBox.exec();
    }
    else
    {
        cv::cvtColor(templ,templ,CV_BGR2RGB);
        img = QImage((const unsigned char*)(templ.data),templ.cols,templ.rows, templ.cols*templ.channels(), QImage::Format_RGB888);
        ui->label3->clear();
        img=  img.scaled(ui->label3->width(), ui->label3->height());
        ui->label3->setPixmap(QPixmap::fromImage(img));
        //ui->processPushButton->setEnabled(true);
        //   ui->label1->resize(ui->label1->pixmap()->size());//設定目前標簽為圖形大小
        // ui->label1->resize(img.width(),img.height());

        //this->setWidget(label1);
    }
    /***************************************開啟範本檔案*********************************************/
    Mat img_display;

    srcImage.copyTo( img_display );

    /// Create the result matrix
    int result_cols =  srcImage.cols - templ.cols + 1;
    int result_rows = srcImage.rows - templ.rows + 1;
    /*
     * 需要注意，目的圖形的大小為int result_cols =  srcImage.cols - templ.cols + 1;
    int result_rows = srcImage.rows - templ.rows + 1;
    這是因為範本沿著原始圖形上的每一個點進行檢查，而產生一個目的圖形內的點，
    當圖形檢查到其右側時，只能檢查到其從右側數第 srcImage.cols - templ.cols + 1個點。
    當圖形檢查到其下側時，只能檢查到其從下側數第 srcImage.rows - templ.rows + 1個點。
    */
    result.create( result_cols, result_rows, CV_32FC1 );

    /// Do the Matching and Normalize
    cv::matchTemplate( srcImage, templ, result, match_method );
    normalize( result, result, 0, 1, NORM_MINMAX, -1, Mat() );

    /// Localizing the best match with minMaxLoc
    double minVal; double maxVal; Point minLoc; Point maxLoc;
    Point matchLoc;

    minMaxLoc( result, &minVal, &maxVal, &minLoc, &maxLoc, Mat() );

    /// For SQDIFF and SQDIFF_NORMED, the best matches are lower values. For all the other methods, the higher the better
    if( match_method  == CV_TM_SQDIFF || match_method == CV_TM_SQDIFF_NORMED )
    { matchLoc = minLoc; }
    else
    { matchLoc = maxLoc; }

    /// Show me what you got
    rectangle( img_display, matchLoc, Point( matchLoc.x + templ.cols , matchLoc.y + templ.rows ), Scalar::all(0), 2, 8, 0 );
    rectangle( result, matchLoc, Point( matchLoc.x + templ.cols , matchLoc.y + templ.rows ), Scalar::all(0), 2, 8, 0 );
    img_display.copyTo(dstImage);
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
    // imshow( image_window, img_display );
    //imshow( result_window, result );
}

void MainWindow::on_actionCV_TM_CCOEFF_triggered()
{
    Mat templ;
    Mat result;
    /* match_method只能取0~5之間的值，即：
      *method=CV_TM_SQDIFF_NORMED
        method=CV_TM_CCORR
        method=CV_TM_CCORR_NORMED
        method=CV_TM_CCOEFF
        method=CV_TM_CCOEFF_NORMED*/
    int match_method=4;
    char* image_window = "Source Image";
    char* result_window = "Result window";
    /***************************************開啟範本檔案*********************************************/
    QString filename = QFileDialog::getOpenFileName(this,tr("Open Image"),"",tr("Image File(*.bmp *.jpg *.jpeg *.png)"));
    QTextCodec *code = QTextCodec::codecForName("gb18030");
    std::string name = code->fromUnicode(filename).data();
    templ = cv::imread(name);
    if(!templ.data)
    {
        QMessageBox msgBox;
        msgBox.setText(tr("找不到資料"));
        msgBox.exec();
    }
    else
    {
        cv::cvtColor(templ,templ,CV_BGR2RGB);
        img = QImage((const unsigned char*)(templ.data),templ.cols,templ.rows, templ.cols*templ.channels(), QImage::Format_RGB888);
        ui->label3->clear();
        img=  img.scaled(ui->label3->width(), ui->label3->height());
        ui->label3->setPixmap(QPixmap::fromImage(img));
        //ui->processPushButton->setEnabled(true);
        //   ui->label1->resize(ui->label1->pixmap()->size());//設定目前標簽為圖形大小
        // ui->label1->resize(img.width(),img.height());

        //this->setWidget(label1);
    }
    /***************************************開啟範本檔案*********************************************/
    Mat img_display;

    srcImage.copyTo( img_display );

    /// Create the result matrix
    int result_cols =  srcImage.cols - templ.cols + 1;
    int result_rows = srcImage.rows - templ.rows + 1;
    /*
     * 需要注意，目的圖形的大小為int result_cols =  srcImage.cols - templ.cols + 1;
    int result_rows = srcImage.rows - templ.rows + 1;
    這是因為範本沿著原始圖形上的每一個點進行檢查，而產生一個目的圖形內的點，
    當圖形檢查到其右側時，只能檢查到其從右側數第 srcImage.cols - templ.cols + 1個點。
    當圖形檢查到其下側時，只能檢查到其從下側數第 srcImage.rows - templ.rows + 1個點。
    */
    result.create( result_cols, result_rows, CV_32FC1 );

    /// Do the Matching and Normalize
    cv::matchTemplate( srcImage, templ, result, match_method );
    normalize( result, result, 0, 1, NORM_MINMAX, -1, Mat() );

    /// Localizing the best match with minMaxLoc
    double minVal; double maxVal; Point minLoc; Point maxLoc;
    Point matchLoc;

    minMaxLoc( result, &minVal, &maxVal, &minLoc, &maxLoc, Mat() );

    /// For SQDIFF and SQDIFF_NORMED, the best matches are lower values. For all the other methods, the higher the better
    if( match_method  == CV_TM_SQDIFF || match_method == CV_TM_SQDIFF_NORMED )
    { matchLoc = minLoc; }
    else
    { matchLoc = maxLoc; }

    /// Show me what you got
    rectangle( img_display, matchLoc, Point( matchLoc.x + templ.cols , matchLoc.y + templ.rows ), Scalar::all(0), 2, 8, 0 );
    rectangle( result, matchLoc, Point( matchLoc.x + templ.cols , matchLoc.y + templ.rows ), Scalar::all(0), 2, 8, 0 );
    img_display.copyTo(dstImage);
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
    // imshow( image_window, img_display );
    //imshow( result_window, result );
}

void MainWindow::on_actionCV_TM_CCOEFF_NORMED_triggered()
{
    Mat templ;
    Mat result;
    /* match_method只能取0~5之間的值，即：
      *method=CV_TM_SQDIFF_NORMED
        method=CV_TM_CCORR
        method=CV_TM_CCORR_NORMED
        method=CV_TM_CCOEFF
        method=CV_TM_CCOEFF_NORMED*/
    int match_method=5;
    char* image_window = "Source Image";
    char* result_window = "Result window";
    /***************************************開啟範本檔案*********************************************/
    QString filename = QFileDialog::getOpenFileName(this,tr("Open Image"),"",tr("Image File(*.bmp *.jpg *.jpeg *.png)"));
    QTextCodec *code = QTextCodec::codecForName("gb18030");
    std::string name = code->fromUnicode(filename).data();
    templ = cv::imread(name);
    if(!templ.data)
    {
        QMessageBox msgBox;
        msgBox.setText(tr("找不到資料"));
        msgBox.exec();
    }
    else
    {
        cv::cvtColor(templ,templ,CV_BGR2RGB);
        img = QImage((const unsigned char*)(templ.data),templ.cols,templ.rows, templ.cols*templ.channels(), QImage::Format_RGB888);
        ui->label3->clear();
        img=  img.scaled(ui->label3->width(), ui->label3->height());
        ui->label3->setPixmap(QPixmap::fromImage(img));
        //ui->processPushButton->setEnabled(true);
        //   ui->label1->resize(ui->label1->pixmap()->size());//設定目前標簽為圖形大小
        // ui->label1->resize(img.width(),img.height());

        //this->setWidget(label1);
    }
    /***************************************開啟範本檔案*********************************************/
    Mat img_display;

    srcImage.copyTo( img_display );

    /// Create the result matrix
    int result_cols =  srcImage.cols - templ.cols + 1;
    int result_rows = srcImage.rows - templ.rows + 1;
    /*
     * 需要注意，目的圖形的大小為int result_cols =  srcImage.cols - templ.cols + 1;
    int result_rows = srcImage.rows - templ.rows + 1;
    這是因為範本沿著原始圖形上的每一個點進行檢查，而產生一個目的圖形內的點，
    當圖形檢查到其右側時，只能檢查到其從右側數第 srcImage.cols - templ.cols + 1個點。
    當圖形檢查到其下側時，只能檢查到其從下側數第 srcImage.rows - templ.rows + 1個點。
    */
    result.create( result_cols, result_rows, CV_32FC1 );

    /// Do the Matching and Normalize
    cv::matchTemplate( srcImage, templ, result, match_method );
    normalize( result, result, 0, 1, NORM_MINMAX, -1, Mat() );

    /// Localizing the best match with minMaxLoc
    double minVal; double maxVal; Point minLoc; Point maxLoc;
    Point matchLoc;

    minMaxLoc( result, &minVal, &maxVal, &minLoc, &maxLoc, Mat() );

    /// For SQDIFF and SQDIFF_NORMED, the best matches are lower values. For all the other methods, the higher the better
    if( match_method  == CV_TM_SQDIFF || match_method == CV_TM_SQDIFF_NORMED )
    { matchLoc = minLoc; }
    else
    { matchLoc = maxLoc; }

    /// Show me what you got
    rectangle( img_display, matchLoc, Point( matchLoc.x + templ.cols , matchLoc.y + templ.rows ), Scalar::all(0), 2, 8, 0 );
    rectangle( result, matchLoc, Point( matchLoc.x + templ.cols , matchLoc.y + templ.rows ), Scalar::all(0), 2, 8, 0 );
    img_display.copyTo(dstImage);
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
    // imshow( image_window, img_display );
    //imshow( result_window, result );
}

void MainWindow::on_resizeSmall_triggered()
{
    cv::resize(srcImage,dstImage,Size( srcImage.cols/4, srcImage.rows/4 ),0,0,3);
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    // img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_resizeBig_triggered()
{
    cv::resize(srcImage,dstImage,Size( srcImage.cols*4, srcImage.rows*4 ),0,0,3);
    //resize(srcImage,dstImage,Size( srcImage.cols*2, srcImage.rows*2 ),0,0,3);
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    // img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));

}

void MainWindow::on_mirrorHorizen_triggered()
{
    cv::flip(srcImage,dstImage,1);
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));

}

void MainWindow::on_mirrorVertical_triggered()
{
    cv::flip(srcImage,dstImage,0);
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_mirrorHorizenAndVertical_triggered()
{
    cv::flip(srcImage,dstImage,-1);
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_wrapAffine_triggered()
{
    //單純仿射
    Point2f srcTri[3];
    Point2f dstTri[3];
    Mat rot_mat( 2, 3, CV_32FC1 );
    Mat warp_mat( 2, 3, CV_32FC1 );
    Mat src, warp_dst, warp_rotate_dst;
    //讀入圖形
    srcImage.copyTo(src);
    warp_dst = Mat::zeros( src.rows, src.cols, src.type() );
    // 用3個點確定A仿射變換
    srcTri[0] = Point2f( 0,0 );
    srcTri[1] = Point2f( src.cols - 1, 0 );
    srcTri[2] = Point2f( 0, src.rows - 1 );
    dstTri[0] = Point2f( src.cols*0.0, src.rows*0.33 );
    dstTri[1] = Point2f( src.cols*0.85, src.rows*0.25 );
    dstTri[2] = Point2f( src.cols*0.15, src.rows*0.7 );
    warp_mat = getAffineTransform( srcTri, dstTri );
    warpAffine( src, warp_dst, warp_mat, warp_dst.size() );
    warp_dst.copyTo(dstImage);
    //顯示仿射結果
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_rotateWrapAffine_triggered()
{
    //旋轉仿射
    Point2f srcTri[3];
    Point2f dstTri[3];
    Mat rot_mat( 2, 3, CV_32FC1 );
    Mat warp_mat( 2, 3, CV_32FC1 );
    Mat src, warp_dst, warp_rotate_dst;
    //讀入圖形
    srcImage.copyTo(src);
    warp_dst = Mat::zeros( src.rows, src.cols, src.type() );
    // 用3個點確定A仿射變換
    srcTri[0] = Point2f( 0,0 );
    srcTri[1] = Point2f( src.cols - 1, 0 );
    srcTri[2] = Point2f( 0, src.rows - 1 );
    dstTri[0] = Point2f( src.cols*0.0, src.rows*0.33 );
    dstTri[1] = Point2f( src.cols*0.85, src.rows*0.25 );
    dstTri[2] = Point2f( src.cols*0.15, src.rows*0.7 );
    warp_mat = getAffineTransform( srcTri, dstTri );
    warpAffine( src, warp_dst, warp_mat, warp_dst.size() );
    // 旋轉矩陣
    Point center = Point( warp_dst.cols/2, warp_dst.rows/2 );
    double angle = -50.0;
    double scale = 0.6;
    rot_mat = getRotationMatrix2D( center, angle, scale );
    warpAffine( warp_dst, warp_rotate_dst, rot_mat, warp_dst.size() );
    ////OpenCV 1.0的形式
    //IplImage * img=cvLoadImage("baboon.jpg");
    //IplImage *img_rotate=cvCloneImage(img);
    //CvMat M =warp_mat;
    //cvWarpAffine(img,img_rotate, &M,CV_INTER_LINEAR+CV_WARP_FILL_OUTLIERS,cvScalarAll(0) );
    //cvShowImage("Wrap2",img_rotate);
    warp_rotate_dst.copyTo(dstImage);
    //顯示結果圖形
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}
void MainWindow::on_remapCopy_triggered()
{
    // 複製
    // 定義映射
    Mat  map_x, map_y;
    dstImage.create( srcImage.size(), srcImage.type() );
    map_x.create( srcImage.size(), CV_32FC1 );
    map_y.create( srcImage.size(), CV_32FC1 );
    for( int i = 0; i < srcImage.rows; i++ )
    {
        for( int j = 0; j < srcImage.cols; j++ )
        {
            map_x.at<float>(i,j) = j;
            map_y.at<float>(i,j) = i;
        }
    }
    //呼叫remap
    remap( srcImage, dstImage, map_x, map_y, CV_INTER_LINEAR, BORDER_CONSTANT, Scalar(0,0, 0) );
    //顯示圖形
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}
void MainWindow::on_remapX_triggered()
{
    //x軸
    //定義映射
    Mat  map_x, map_y;
    dstImage.create( srcImage.size(), srcImage.type() );
    map_x.create( srcImage.size(), CV_32FC1 );
    map_y.create( srcImage.size(), CV_32FC1 );
    for( int i = 0; i < srcImage.rows; i++ )
    {
        for( int j = 0; j < srcImage.cols; j++ )
        {
            map_x.at<float>(i,j) = srcImage.cols - j;
            map_y.at<float>(i,j) = i;
        }
    }
    //呼叫remap
    remap( srcImage, dstImage, map_x, map_y, CV_INTER_LINEAR, BORDER_CONSTANT, Scalar(0,0, 0) );
    //顯示圖形
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_remapY_triggered()
{
    //y軸
    //定義映射
    Mat  map_x, map_y;
    dstImage.create( srcImage.size(), srcImage.type() );
    map_x.create( srcImage.size(), CV_32FC1 );
    map_y.create( srcImage.size(), CV_32FC1 );
    for( int i = 0; i < srcImage.rows; i++ )
    {
        for( int j = 0; j < srcImage.cols; j++ )
        {
            map_x.at<float>(i,j) = j ;
            map_y.at<float>(i,j) = srcImage.rows -i ;
        }
    }
    //呼叫remap
    remap( srcImage, dstImage, map_x, map_y, CV_INTER_LINEAR, BORDER_CONSTANT, Scalar(0,0, 0) );
    //顯示圖形
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_remapSmall_triggered()
{
    //拉遠
    //定義映射
    Mat  map_x, map_y;
    dstImage.create( srcImage.size(), srcImage.type() );
    map_x.create( srcImage.size(), CV_32FC1 );
    map_y.create( srcImage.size(), CV_32FC1 );
    for( int i = 0; i < srcImage.rows; i++ )
    {
        for( int j = 0; j < srcImage.cols; j++ )
        {
            if( i > srcImage.rows*0.25 && i < srcImage.rows*0.75&&j > srcImage.cols*0.25 &&j < srcImage.cols*0.75  )
            {
                map_x.at<float>(i,j) = 2*( j - srcImage.cols*0.25 ) + 0.5 ;
                map_y.at<float>(i,j) = 2*( i - srcImage.rows*0.25 ) + 0.5 ;
            }
            else
            {
                map_x.at<float>(i,j) = 1 ;   //隨機選取
                map_y.at<float>(i,j) = 1 ;   //隨機選取
            }
        }
    }
    //呼叫remap
    remap( srcImage, dstImage, map_x, map_y, CV_INTER_LINEAR, BORDER_CONSTANT, Scalar(0,0, 0) );
    //顯示圖形
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_remapRotate_triggered()
{
    //旋轉
    //定義映射
    Mat  map_x, map_y;
    dstImage.create( srcImage.size(), srcImage.type() );
    map_x.create( srcImage.size(), CV_32FC1 );
    map_y.create( srcImage.size(), CV_32FC1 );
    for( int i = 0; i < srcImage.rows; i++ )
    {
        for( int j = 0; j < srcImage.cols; j++ )
        {
            map_x.at<float>(i,j) = srcImage.cols - j ;
            map_y.at<float>(i,j) = srcImage.rows -i ;
        }
    }
    //呼叫remap
    remap( srcImage, dstImage, map_x, map_y, CV_INTER_LINEAR, BORDER_CONSTANT, Scalar(0,0, 0) );
    //顯示圖形
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}


void MainWindow::on_remapDiagonal_triggered()
{
    //x、y互換
    //定義映射
    Mat  map_x, map_y;
    dstImage.create( srcImage.size(), srcImage.type() );
    map_x.create( srcImage.size(), CV_32FC1 );
    map_y.create( srcImage.size(), CV_32FC1 );
    for( int i = 0; i < srcImage.rows; i++ )
    {
        for( int j = 0; j < srcImage.cols; j++ )
        {
            map_x.at<float>(i,j) = i;
            map_y.at<float>(i,j) = j;
        }
    }
    //呼叫remap
    remap( srcImage, dstImage, map_x, map_y, CV_INTER_LINEAR, BORDER_CONSTANT, Scalar(0,0, 0) );
    //顯示圖形
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}


void MainWindow::on_clockwise_triggered()
{
    Point2f srcTri[3];
    Point2f dstTri[3];
    Mat rot_mat( 2, 3, CV_32FC1 );
    Mat warp_mat( 2, 3, CV_32FC1 );
    Mat src, warp_dst, warp_rotate_dst;
    //讀入圖形
    srcImage.copyTo(src);
    warp_dst = Mat::zeros( src.rows, src.cols, src.type() );
    // 用3個點確定A仿射變換
    Point center = Point( src.cols/2,src.rows/2 );
    double angle = -50.0;
    double scale = 1;
    rot_mat = getRotationMatrix2D( center, angle, scale );
    warpAffine(src, warp_rotate_dst, rot_mat, warp_dst.size() );
    ////OpenCV 1.0的形式
    //IplImage * img=cvLoadImage("baboon.jpg");
    //IplImage *img_rotate=cvCloneImage(img);
    //CvMat M =warp_mat;
    //cvWarpAffine(img,img_rotate, &M,CV_INTER_LINEAR+CV_WARP_FILL_OUTLIERS,cvScalarAll(0) );
    //cvShowImage("Wrap2",img_rotate);
    warp_rotate_dst.copyTo(dstImage);

    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_clockwiseResize_triggered()
{
    Point2f srcTri[3];
    Point2f dstTri[3];
    Mat rot_mat( 2, 3, CV_32FC1 );
    Mat warp_mat( 2, 3, CV_32FC1 );
    Mat src, warp_dst, warp_rotate_dst;
    //讀入圖形
    srcImage.copyTo(src);
    warp_dst = Mat::zeros( src.rows, src.cols, src.type() );
    // 用3個點確定A仿射變換
    Point center = Point( src.cols/2,src.rows/2 );
    double angle = -50.0;
    double scale = 0.6;
    rot_mat = getRotationMatrix2D( center, angle, scale );
    warpAffine(src, warp_rotate_dst, rot_mat, warp_dst.size() );
    ////OpenCV 1.0的形式
    //IplImage * img=cvLoadImage("baboon.jpg");
    //IplImage *img_rotate=cvCloneImage(img);
    //CvMat M =warp_mat;
    //cvWarpAffine(img,img_rotate, &M,CV_INTER_LINEAR+CV_WARP_FILL_OUTLIERS,cvScalarAll(0) );
    //cvShowImage("Wrap2",img_rotate);
    warp_rotate_dst.copyTo(dstImage);

    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_UNclockwise_triggered()
{
    Point2f srcTri[3];
    Point2f dstTri[3];
    Mat rot_mat( 2, 3, CV_32FC1 );
    Mat warp_mat( 2, 3, CV_32FC1 );
    Mat src, warp_dst, warp_rotate_dst;
    //讀入圖形
    srcImage.copyTo(src);
    warp_dst = Mat::zeros( src.rows, src.cols, src.type() );
    // 用3個點確定A仿射變換
    Point center = Point( src.cols/2,src.rows/2 );
    double angle = 50.0;
    double scale = 0.6;
    rot_mat = getRotationMatrix2D( center, angle, scale );
    warpAffine(src, warp_rotate_dst, rot_mat, warp_dst.size() );
    ////OpenCV 1.0的形式
    //IplImage * img=cvLoadImage("baboon.jpg");
    //IplImage *img_rotate=cvCloneImage(img);
    //CvMat M =warp_mat;
    //cvWarpAffine(img,img_rotate, &M,CV_INTER_LINEAR+CV_WARP_FILL_OUTLIERS,cvScalarAll(0) );
    //cvShowImage("Wrap2",img_rotate);
    warp_rotate_dst.copyTo(dstImage);

    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_zeroRotateResize_triggered()
{
    Point2f srcTri[3];
    Point2f dstTri[3];
    Mat rot_mat( 2, 3, CV_32FC1 );
    Mat warp_mat( 2, 3, CV_32FC1 );
    Mat src, warp_dst, warp_rotate_dst;
    //讀入圖形
    srcImage.copyTo(src);
    warp_dst = Mat::zeros( src.rows, src.cols, src.type() );
    // 用3個點確定A仿射變換
    Point center = Point( src.cols/2,src.rows/2 );
    double angle = 0;
    double scale = 0.6;
    rot_mat = getRotationMatrix2D( center, angle, scale );
    warpAffine(src, warp_rotate_dst, rot_mat, warp_dst.size() );
    ////OpenCV 1.0的形式
    //IplImage * img=cvLoadImage("baboon.jpg");
    //IplImage *img_rotate=cvCloneImage(img);
    //CvMat M =warp_mat;
    //cvWarpAffine(img,img_rotate, &M,CV_INTER_LINEAR+CV_WARP_FILL_OUTLIERS,cvScalarAll(0) );
    //cvShowImage("Wrap2",img_rotate);
    warp_rotate_dst.copyTo(dstImage);
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_actionTHRESH_BINARY_triggered()
{
    //選單：threshold=>THRESH_BINARY
    //定義Mat，用於儲存灰階圖形
    Mat srcGray;
    //調整大小
    cv::resize(srcImage,srcImage,Size(ui->label1->width(), ui->label1->height()),0,0,3);
    //色彩空間轉換
    cvtColor(srcImage,srcGray,COLOR_RGB2GRAY);
    //定義參數
    int threshold_value=128;
    int max_BINARY_value=255;
    int threshold_type=THRESH_BINARY;
    /***********同等於************/
    //int threshold_type=0;
    /***********同等於************/
    //呼叫threshold函數
    threshold(srcGray, dstImage, threshold_value, max_BINARY_value,threshold_type );
    // imshow("li",dstImage);    //測試效果
    //顯示圖形
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows, dstImage.cols*dstImage.channels(),QImage::Format_Indexed8);
    //img=img.scaled(ui->label1->size());   //縮放圖形
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_actionTHRESH_BINARY_INV_triggered()
{
    //選單：threshold=>THRESH_BINARY_INV;
    //定義Mat，用於儲存灰階圖形
    Mat srcGray;
    //調整大小
    cv::resize(srcImage,srcImage,Size(ui->label1->width(), ui->label1->height()),0,0,3);
    //色彩空間轉換
    cvtColor(srcImage,srcGray,COLOR_RGB2GRAY);
    //定義參數
    int threshold_value=128;
    int max_BINARY_value=255;
    int threshold_type=THRESH_BINARY_INV;
    /***********同等於************/
    //int threshold_type=0;
    /***********同等於************/
    //呼叫threshold函數
    threshold(srcGray, dstImage, threshold_value, max_BINARY_value,threshold_type );
    // imshow("li",dstImage);    //測試效果
    //顯示圖形
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows, dstImage.cols*dstImage.channels(),QImage::Format_Indexed8);
    //img=img.scaled(ui->label1->size());   //縮放圖形
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_actionTHRESH_TRUNC_triggered()
{
    //選單：threshold=>THRESH_TRUNC;
    //定義Mat，用於儲存灰階圖形
    Mat srcGray;
    //調整大小
    cv::resize(srcImage,srcImage,Size(ui->label1->width(), ui->label1->height()),0,0,3);
    //色彩空間轉換
    cvtColor(srcImage,srcGray,COLOR_RGB2GRAY);
    //定義參數
    int threshold_value=128;
    int max_BINARY_value=255;
    int threshold_type=THRESH_TRUNC;
    /***********同等於************/
    //int threshold_type=0;
    /***********同等於************/
    //呼叫threshold函數
    threshold(srcGray, dstImage, threshold_value, max_BINARY_value,threshold_type );
    // imshow("li",dstImage);    //測試效果
    //顯示圖形
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows, dstImage.cols*dstImage.channels(),QImage::Format_Indexed8);
    //img=img.scaled(ui->label1->size());   //縮放圖形
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_actionTHRESH_TOZERO_triggered()
{
    //選單：threshold=>THRESH_TOZERO;
    //定義Mat，用於儲存灰階圖形
    Mat srcGray;
    //調整大小
    cv::resize(srcImage,srcImage,Size(ui->label1->width(), ui->label1->height()),0,0,3);
    //色彩空間轉換
    cvtColor(srcImage,srcGray,COLOR_RGB2GRAY);
    //定義參數
    int threshold_value=128;
    int max_BINARY_value=255;
    int threshold_type=THRESH_TOZERO;
    /***********同等於************/
    //int threshold_type=0;
    /***********同等於************/
    //呼叫threshold函數
    threshold(srcGray, dstImage, threshold_value, max_BINARY_value,threshold_type );
    // imshow("li",dstImage);    //測試效果
    //顯示圖形
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows, dstImage.cols*dstImage.channels(),QImage::Format_Indexed8);
    //img=img.scaled(ui->label1->size());   //縮放圖形
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_actionTHRESH_TOZERO_INV_2_triggered()
{
    //選單：threshold=>THRESH_TOZERO_INV;
    //定義Mat，用於儲存灰階圖形
    Mat srcGray;
    //調整大小
    cv::resize(srcImage,srcImage,Size(ui->label1->width(), ui->label1->height()),0,0,3);
    //色彩空間轉換
    cvtColor(srcImage,srcGray,COLOR_RGB2GRAY);
    //定義參數
    int threshold_value=128;
    int max_BINARY_value=255;
    int threshold_type=THRESH_TOZERO_INV;
    /***********同等於************/
    //int threshold_type=0;
    /***********同等於************/
    //呼叫threshold函數
    threshold(srcGray, dstImage, threshold_value, max_BINARY_value,threshold_type );
    // imshow("li",dstImage);    //測試效果
    //顯示圖形
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows, dstImage.cols*dstImage.channels(),QImage::Format_Indexed8);
    //img=img.scaled(ui->label1->size());   //縮放圖形
    ui->label2->setPixmap(QPixmap::fromImage(img));
}



void MainWindow::on_actionTHRESH_BINARY_3_triggered()
{
    //選單：THRESH_OTST=>TRESH_BINARY
    //THRESH_BINARY+THRESH_OTSU;
    //定義灰階Mat，使用者儲存灰階圖形
    Mat srcGray;
    //調整下大小
    cv::resize(srcImage,srcImage,Size(ui->label1->width(), ui->label1->height()),0,0,3);
    //色彩空間轉換，彩色變灰階
    cvtColor(srcImage,srcGray,COLOR_RGB2GRAY);
    //定義參數值
    int threshold_value=128;
    int max_BINARY_value=255;
    int threshold_type=THRESH_BINARY+THRESH_OTSU;
    //呼叫threshold
    threshold(srcGray, dstImage, threshold_value, max_BINARY_value,threshold_type );
    // imshow("li",dstImage);    //測試一下
    //顯示圖形
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows, dstImage.cols*dstImage.channels(),QImage::Format_Indexed8);
    //  img=img.scaled(ui->label1->size());     //調整大小
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_actionTHRESH_BINARY_INV_3_triggered()
{   
    //選單：THRESH_OTST=>THRESH_BINARY_INV
    //THRESH_BINARY_INV+THRESH_OTSU;
    //定義灰階Mat，使用者儲存灰階圖形
    Mat srcGray;
    //調整下大小
    cv::resize(srcImage,srcImage,Size(ui->label1->width(), ui->label1->height()),0,0,3);
    //色彩空間轉換，彩色變灰階
    cvtColor(srcImage,srcGray,COLOR_RGB2GRAY);
    //定義參數值
    int threshold_value=128;
    int max_BINARY_value=255;
    int threshold_type=THRESH_BINARY_INV+THRESH_OTSU;
    //呼叫threshold
    threshold(srcGray, dstImage, threshold_value, max_BINARY_value,threshold_type );
    // imshow("li",dstImage);    //測試一下
    //顯示圖形
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows, dstImage.cols*dstImage.channels(),QImage::Format_Indexed8);
    //  img=img.scaled(ui->label1->size());     //調整大小
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_actionTHRESH_TRUNC_2_triggered()
{
    //選單：THRESH_OTST=>THRESH_TRUNC
    //THRESH_TRUNC+THRESH_OTSU;
    //定義灰階Mat，使用者儲存灰階圖形
    Mat srcGray;
    //調整下大小
    cv::resize(srcImage,srcImage,Size(ui->label1->width(), ui->label1->height()),0,0,3);
    //色彩空間轉換，彩色變灰階
    cvtColor(srcImage,srcGray,COLOR_RGB2GRAY);
    //定義參數值
    int threshold_value=128;
    int max_BINARY_value=255;
    int threshold_type=THRESH_TRUNC+THRESH_OTSU;
    //呼叫threshold
    threshold(srcGray, dstImage, threshold_value, max_BINARY_value,threshold_type );
    // imshow("li",dstImage);    //測試一下
    //顯示圖形
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows, dstImage.cols*dstImage.channels(),QImage::Format_Indexed8);
    //  img=img.scaled(ui->label1->size());     //調整大小
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_actionTHRESH_TOZERO_2_triggered()
{
    //選單：THRESH_OTST=>THRESH_TOZERO
    //THRESH_TOZERO+THRESH_OTSU;
    //定義灰階Mat，使用者儲存灰階圖形
    Mat srcGray;
    //調整下大小
    cv::resize(srcImage,srcImage,Size(ui->label1->width(), ui->label1->height()),0,0,3);
    //色彩空間轉換，彩色變灰階
    cvtColor(srcImage,srcGray,COLOR_RGB2GRAY);
    //定義參數值
    int threshold_value=128;
    int max_BINARY_value=255;
    int threshold_type=THRESH_TOZERO+THRESH_OTSU;
    //呼叫threshold
    threshold(srcGray, dstImage, threshold_value, max_BINARY_value,threshold_type );
    // imshow("li",dstImage);    //測試一下
    //顯示圖形
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows, dstImage.cols*dstImage.channels(),QImage::Format_Indexed8);
    //  img=img.scaled(ui->label1->size());     //調整大小
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_actionTHRESH_TOZERO_INV_triggered()
{
    //選單：THRESH_OTST=>THRESH_TOZERO_INV
    //THRESH_TOZERO_INV+THRESH_OTSU;
    //定義灰階Mat，使用者儲存灰階圖形
    Mat srcGray;
    //調整下大小
    cv::resize(srcImage,srcImage,Size(ui->label1->width(), ui->label1->height()),0,0,3);
    //色彩空間轉換，彩色變灰階
    cvtColor(srcImage,srcGray,COLOR_RGB2GRAY);
    //定義參數值
    int threshold_value=128;
    int max_BINARY_value=255;
    int threshold_type=THRESH_TOZERO_INV+THRESH_OTSU;
    //呼叫threshold
    threshold(srcGray, dstImage, threshold_value, max_BINARY_value,threshold_type );
    // imshow("li",dstImage);    //測試一下
    //顯示圖形
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows, dstImage.cols*dstImage.channels(),QImage::Format_Indexed8);
    //  img=img.scaled(ui->label1->size());     //調整大小
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_actionTHRESH_BINARY_INV_4_triggered()
{

}

void MainWindow::on_actionADAPTIVE_THRESH_MEAN_C_triggered()
{
    //選單:adaptiveThreshold=>THRESH_BINARY=>ADAPTIVE_THRESH_MEAN_C
    //定義一個Mat，用於儲存灰階圖形
    Mat srcGray;
    //調整大小
    cv::resize(srcImage,srcImage,Size(ui->label1->width(), ui->label1->height()),0,0,3);
    //色彩空間轉換
    cvtColor(srcImage,srcGray,COLOR_RGB2GRAY);
    //參數設定
    int maxValue=255;
    int adaptiveMethod=ADAPTIVE_THRESH_MEAN_C;
    int thresholdType=THRESH_BINARY;
    int blocksize=7;
    double C=1;
    //呼叫adaptiveThreshold函數
    adaptiveThreshold(srcGray, dstImage, maxValue,adaptiveMethod,thresholdType,blocksize,C );
    //顯示圖形
    // imshow("li",dstImage); //測試顯示情況
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows, dstImage.cols*dstImage.channels(),QImage::Format_Indexed8);
    //  img=img.scaled(ui->label1->size());   //調整大小
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_actionADAPTIVE_THRESH_GAUSSIAN_C_triggered()
{    
    //選單:adaptiveThreshold=>THRESH_BINARY=>ADAPTIVE_THRESH_GAUSSIAN_C
    //定義一個Mat，用於儲存灰階圖形
    Mat srcGray;
    //調整大小
    cv::resize(srcImage,srcImage,Size(ui->label1->width(), ui->label1->height()),0,0,3);
    //色彩空間轉換
    cvtColor(srcImage,srcGray,COLOR_RGB2GRAY);
    //參數設定
    int maxValue=255;
    int adaptiveMethod=ADAPTIVE_THRESH_GAUSSIAN_C;
    int thresholdType=THRESH_BINARY;
    int blocksize=7;
    double C=1;
    //呼叫adaptiveThreshold函數
    adaptiveThreshold(srcGray, dstImage, maxValue,adaptiveMethod,thresholdType,blocksize,C );
    //顯示圖形
    // imshow("li",dstImage); //測試顯示情況
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows, dstImage.cols*dstImage.channels(),QImage::Format_Indexed8);
    //  img=img.scaled(ui->label1->size());   //調整大小
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_actionADAPTIVE_THRESH_MEAN_C_2_triggered()
{
    //選單:adaptiveThreshold=>THRESH_BINARY_INV=>ADAPTIVE_THRESH_MEAN_C
    //定義一個Mat，用於儲存灰階圖形
    Mat srcGray;
    //調整大小
    cv::resize(srcImage,srcImage,Size(ui->label1->width(), ui->label1->height()),0,0,3);
    //色彩空間轉換
    cvtColor(srcImage,srcGray,COLOR_RGB2GRAY);
    //參數設定
    int maxValue=255;
    int adaptiveMethod=ADAPTIVE_THRESH_MEAN_C;
    int thresholdType=THRESH_BINARY_INV;
    int blocksize=7;
    double C=1;
    //呼叫adaptiveThreshold函數
    adaptiveThreshold(srcGray, dstImage, maxValue,adaptiveMethod,thresholdType,blocksize,C );
    //顯示圖形
    // imshow("li",dstImage); //測試顯示情況
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows, dstImage.cols*dstImage.channels(),QImage::Format_Indexed8);
    //  img=img.scaled(ui->label1->size());   //調整大小
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_actionADAPTIVE_THRESH_GAUSSIAN_C_2_triggered()
{
    //選單:adaptiveThreshold=>THRESH_BINARY_INV=>ADAPTIVE_THRESH_GAUSSIAN_C
    //定義一個Mat，用於儲存灰階圖形
    Mat srcGray;
    //調整大小
    cv::resize(srcImage,srcImage,Size(ui->label1->width(), ui->label1->height()),0,0,3);
    //色彩空間轉換
    cvtColor(srcImage,srcGray,COLOR_RGB2GRAY);
    //參數設定
    int maxValue=255;
    int adaptiveMethod=ADAPTIVE_THRESH_GAUSSIAN_C;
    int thresholdType=THRESH_BINARY_INV;
    int blocksize=7;
    double C=1;
    //呼叫adaptiveThreshold函數
    adaptiveThreshold(srcGray, dstImage, maxValue,adaptiveMethod,thresholdType,blocksize,C );
    //顯示圖形
    // imshow("li",dstImage); //測試顯示情況
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows, dstImage.cols*dstImage.channels(),QImage::Format_Indexed8);
    //  img=img.scaled(ui->label1->size());   //調整大小
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_action_triggered()
{
    //銳化
    //建構核
    Mat kernel(3,3,CV_32F,cv::Scalar(0));
    kernel.at<float>(1,1) = 5.0;
    kernel.at<float>(1,0) = -1.0;
    kernel.at<float>(1,2) = -1.0;
    //呼叫filter2D實現
    filter2D(srcImage,dstImage, srcImage.depth(), kernel);
    //顯示圖形
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_action_2_triggered()
{
    blur( srcImage, dstImage, Size( 7, 7 ), Point(-1,-1) );
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_action_3_triggered()
{
    GaussianBlur( srcImage, dstImage, Size( 7,7 ), 0, 0 );
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_action_4_triggered()
{
    medianBlur ( srcImage, dstImage, 7 );
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_action_5_triggered()
{
    bilateralFilter ( srcImage, dstImage, 31, 31*2, 31/2 );
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}
void MainWindow::on_actionTHRESH_BINARY_2_triggered()
{
    //選單：THRESH_TRIANGLE=>TRESH_BINARY
    //THRESH_BINARY+THRESH_TRIANGLE;
    //定義灰階Mat，使用者儲存灰階圖形
    Mat srcGray;
    //調整下大小
    cv::resize(srcImage,srcImage,Size(ui->label1->width(), ui->label1->height()),0,0,3);
    //色彩空間轉換，彩色變灰階
    cvtColor(srcImage,srcGray,COLOR_RGB2GRAY);
    //定義參數值
    int threshold_value=128;
    int max_BINARY_value=255;
    int threshold_type=THRESH_BINARY+THRESH_TRIANGLE;
    //呼叫threshold
    threshold(srcGray, dstImage, threshold_value, max_BINARY_value,threshold_type );
    // imshow("li",dstImage);    //測試一下
    //顯示圖形
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows, dstImage.cols*dstImage.channels(),QImage::Format_Indexed8);
    //  img=img.scaled(ui->label1->size());     //調整大小
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_actionTHRESH_BINARY_INV_2_triggered()
{
    //選單：THRESH_TRIANGLE=>THRESH_BINARY_INV
    //THRESH_BINARY_INV+THRESH_TRIANGLE;
    //定義灰階Mat，使用者儲存灰階圖形
    Mat srcGray;
    //調整下大小
    cv::resize(srcImage,srcImage,Size(ui->label1->width(), ui->label1->height()),0,0,3);
    //色彩空間轉換，彩色變灰階
    cvtColor(srcImage,srcGray,COLOR_RGB2GRAY);
    //定義參數值
    int threshold_value=128;
    int max_BINARY_value=255;
    int threshold_type=THRESH_BINARY_INV+THRESH_TRIANGLE;
    //呼叫threshold
    threshold(srcGray, dstImage, threshold_value, max_BINARY_value,threshold_type );
    // imshow("li",dstImage);    //測試一下
    //顯示圖形
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows, dstImage.cols*dstImage.channels(),QImage::Format_Indexed8);
    //  img=img.scaled(ui->label1->size());     //調整大小
    ui->label2->setPixmap(QPixmap::fromImage(img));
}




void MainWindow::on_actionTHRESH_TRUNC_3_triggered()
{
    //選單：THRESH_TRIANGLE=>THRESH_TRUNC
    //THRESH_TRUNC+THRESH_TRIANGLE;
    //定義灰階Mat，使用者儲存灰階圖形
    Mat srcGray;
    //調整下大小
    cv::resize(srcImage,srcImage,Size(ui->label1->width(), ui->label1->height()),0,0,3);
    //色彩空間轉換，彩色變灰階
    cvtColor(srcImage,srcGray,COLOR_RGB2GRAY);
    //定義參數值
    int threshold_value=128;
    int max_BINARY_value=255;
    int threshold_type=THRESH_TRUNC+THRESH_TRIANGLE;
    //呼叫threshold
    threshold(srcGray, dstImage, threshold_value, max_BINARY_value,threshold_type );
    // imshow("li",dstImage);    //測試一下
    //顯示圖形
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows, dstImage.cols*dstImage.channels(),QImage::Format_Indexed8);
    //  img=img.scaled(ui->label1->size());     //調整大小
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_actionTHRESH_TOZERO_3_triggered()
{
    //選單：THRESH_TRIANGLE=>THRESH_TOZERO
    //THRESH_TOZERO+THRESH_TRIANGLE;
    //定義灰階Mat，使用者儲存灰階圖形
    Mat srcGray;
    //調整下大小
    cv::resize(srcImage,srcImage,Size(ui->label1->width(), ui->label1->height()),0,0,3);
    //色彩空間轉換，彩色變灰階
    cvtColor(srcImage,srcGray,COLOR_RGB2GRAY);
    //定義參數值
    int threshold_value=128;
    int max_BINARY_value=255;
    int threshold_type=THRESH_TOZERO+THRESH_TRIANGLE;
    //呼叫threshold
    threshold(srcGray, dstImage, threshold_value, max_BINARY_value,threshold_type );
    // imshow("li",dstImage);    //測試一下
    //顯示圖形
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows, dstImage.cols*dstImage.channels(),QImage::Format_Indexed8);
    //  img=img.scaled(ui->label1->size());     //調整大小
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_actionTHRESH_TOZERO_INV_3_triggered()
{
    //選單：THRESH_TRIANGLE=>THRESH_TOZERO_INV
    //THRESH_TOZERO_INV+THRESH_TRIANGLE;
    //定義灰階Mat，使用者儲存灰階圖形
    Mat srcGray;
    //調整下大小
    cv::resize(srcImage,srcImage,Size(ui->label1->width(), ui->label1->height()),0,0,3);
    //色彩空間轉換，彩色變灰階
    cvtColor(srcImage,srcGray,COLOR_RGB2GRAY);
    //定義參數值
    int threshold_value=128;
    int max_BINARY_value=255;
    int threshold_type=THRESH_TOZERO_INV+THRESH_TRIANGLE;
    //呼叫threshold
    threshold(srcGray, dstImage, threshold_value, max_BINARY_value,threshold_type );
    // imshow("li",dstImage);    //測試一下
    //顯示圖形
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows, dstImage.cols*dstImage.channels(),QImage::Format_Indexed8);
    //  img=img.scaled(ui->label1->size());     //調整大小
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_Clear_triggered()
{
    //選單：檔案=>清除
    //清除標簽1的內容。
    ui->label1->clear();
    //清除標簽2的內容。
    ui->label2->clear();

}
