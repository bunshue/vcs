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
//  版权信息：  lilizong[at]gmail.com
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
        msgBox.setText(tr("默认的测试文件不存在，可以用以下两种方式的一种：1）复制一个文件到当前目录下，并命名为lena.jpg. 2)使用自定义方式打开一个自定义文件。"));
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
        //   ui->label1->resize(ui->label1->pixmap()->size());//设置当前标签为图像大小
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
        msgBox.setText(tr("未找到数据"));
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
        //   ui->label1->resize(ui->label1->pixmap()->size());//设置当前标签为图像大小
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
    QMessageBox::information(this,"版权",tr("本软件版权所有者为：天津职业技术师范大学。如果使用，请联系：lilizong@gmail.com"));
}

void MainWindow::on_about_triggered()
{
    QMessageBox::information(this,"关于",tr("本软件当前版本为1.0，由李立宗等人开发。如果有问题，欢迎联系：lilizong@gmail.com"));
    return;
}

void MainWindow::on_HistEqualize_triggered()
{
    //直方图均衡化
    //定义一个数组，用来存储各通道图片的向量
    vector<Mat> splitBGR(srcImage.channels());
    //分割通道，存储到splitBGR中
    split(srcImage,splitBGR);
    //对各个通道分别进行直方图均衡化
    for(int i=0; i<srcImage.channels(); i++)
        equalizeHist(splitBGR[i],splitBGR[i]);
    Mat mergeImg;//合并后的图像
    //合并通道
    merge(splitBGR,mergeImg);
    //复制图像
    mergeImg.copyTo(dstImage);
    // cv::cvtColor(dstImage,dstImage,CV_BGR2RGB);  //打开文件时已经完成BRG到RGB的转换
    //显示图像
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_contrast_triggered()
{
    //调节对比度
    //这里仅仅调整alpha的值，beta默认为0.
    srcImage.convertTo(dstImage,-1,2);
    //显示图像
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_light_triggered()
{
    //调节亮度
    //这里仅仅调整beta的值，alpha设置为1.
    srcImage.convertTo(dstImage,-1,1,80);
    //显示图像
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_filter2D1_triggered()
{
    //算子1
    //建立核
    Mat kernel = (Mat_<float>(3, 3) << 0, -1, 0, -1, 5, -1, 0, -1, 0);
    //应用函数filter2D处理。
    filter2D(srcImage,dstImage, srcImage.depth(), kernel);
    //显示图像
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
    //调用函数filter2D处理
    filter2D(srcImage,dstImage, srcImage.depth(), kernel);
    //显示图像
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_filter2D3_triggered()
{
    //算子3
    //构造核
    Mat kernel(3,3,CV_32F,Scalar(-1));
    kernel.at<float>(1,1) = 8.9;
    //调用filter2D函数
    filter2D(srcImage,dstImage, srcImage.depth(), kernel);
    //显示图像
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
    //调用filter2D
    filter2D(srcImage,dstImage, srcImage.depth(), kernel);
    //显示图像
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
    //调用filter2D
    filter2D(srcImage,dstImage, srcImage.depth(), kernel);
    //显示图像
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_filter2D6_triggered()
{
    //算子6
    Mat kernel = (Mat_<float>(3, 3) << 0, -1, 0, -1, 6, -1, 0, -1, 0);
    filter2D(srcImage,dstImage, srcImage.depth(), kernel);
    //显示图像
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_contrastAndLight_triggered()
{
    //同时调节亮度、对比度
    //同时调整参数alpha、beta
    srcImage.convertTo(dstImage,-1,2,80);
    //显示图像
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_actionCV_TM_SQDIFF_triggered()
{
    //SQDIFF效果
    //定义模板、结果
    Mat templ;
    Mat result;
    /* match_method只能取0~5之中的某一个值，即：
      * method=TM_SQDIFF             （0）
      * method=TM_SQDIFF_NORMED      （1）
        method=TM_CCORR              （2）
        method=TM_CCORR_NORMED       （3）
        method=TM_CCOEFF ·           （4）
        method=TM_CCOEFF_NORMED      （5）
    */
    //设置匹配方法
    int match_method=0;
    /***************************************打开模板文件*********************************************/
    //注意这里在主界面的左上角添加了一个标签，专门用于显示模板图像
    QString filename = QFileDialog::getOpenFileName(this,tr("打开模板图像"),"",tr("Image File(*.bmp *.jpg *.jpeg *.png)"));
    QTextCodec *code = QTextCodec::codecForName("gb18030");
    std::string name = code->fromUnicode(filename).data();
    templ = cv::imread(name);
    if(!templ.data)
    {
        QMessageBox msgBox;
        msgBox.setText(tr("未找到数据"));
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
    /***************************************打开模板文件*********************************************/
    //用于显示的图像
    Mat img_display;
    //复制图像srcImage到img_display
    srcImage.copyTo( img_display );
    //生成结果
    int result_cols =  srcImage.cols - templ.cols + 1;
    int result_rows = srcImage.rows - templ.rows + 1;
    /*
     * 需要注意，目标图像的大小为int result_cols =  srcImage.cols - templ.cols + 1;
    int result_rows = srcImage.rows - templ.rows + 1;
    这是因为模板沿着原始图像上的每一个点进行遍历，而产生一个目标图像内的点，
    当图像遍历到其右侧时，只能遍历到其从左侧数第 srcImage.cols - templ.cols + 1个点。
    当图像遍历到其下侧时，只能遍历到其从上侧数第 srcImage.rows - templ.rows + 1个点。
    */
    result.create( result_cols, result_rows, CV_32FC1 );
    //进行模板匹配操作
    cv::matchTemplate( srcImage, templ, result, match_method );
    normalize( result, result, 0, 1, NORM_MINMAX, -1, Mat() );
    //使用minMaxLoc对匹配结果进行定位
    double minVal;
    double maxVal;
    Point minLoc;
    Point maxLoc;
    Point matchLoc;
    minMaxLoc( result, &minVal, &maxVal, &minLoc, &maxLoc, Mat() );
    //对于SQDIFF和SQDIFF_NORMED，最好的匹配时最小值，其他的是最大值。
    if( match_method  == TM_SQDIFF || match_method == TM_SQDIFF_NORMED )
        matchLoc = minLoc;
    else
        matchLoc = maxLoc;
    //处理结果
    rectangle( img_display, matchLoc, Point( matchLoc.x + templ.cols , matchLoc.y + templ.rows ), Scalar::all(0), 2, 8, 0 );
    rectangle( result, matchLoc, Point( matchLoc.x + templ.cols , matchLoc.y + templ.rows ), Scalar::all(0), 2, 8, 0 );
    img_display.copyTo(dstImage);
    //显示结果
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
    //窗口显示测试
    //char* image_window = "Source Image";
    // char* result_window = "Result window";
    // imshow( image_window, img_display );
    //imshow( result_window, result );
}

void MainWindow::on_actionCV_TM_SQDIFF_NORMED_triggered()
{
    Mat templ;
    Mat result;
    /* match_method只能取0~5之间的值，即：
      *method=CV_TM_SQDIFF_NORMED
        method=CV_TM_CCORR
        method=CV_TM_CCORR_NORMED
        method=CV_TM_CCOEFF
        method=CV_TM_CCOEFF_NORMED*/
    int match_method=1;
    char* image_window = "Source Image";
    char* result_window = "Result window";
    /***************************************打开模板文件*********************************************/
    QString filename = QFileDialog::getOpenFileName(this,tr("Open Image"),"",tr("Image File(*.bmp *.jpg *.jpeg *.png)"));
    QTextCodec *code = QTextCodec::codecForName("gb18030");
    std::string name = code->fromUnicode(filename).data();
    templ = cv::imread(name);
    if(!templ.data)
    {
        QMessageBox msgBox;
        msgBox.setText(tr("未找到数据"));
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
        //   ui->label1->resize(ui->label1->pixmap()->size());//设置当前标签为图像大小
        // ui->label1->resize(img.width(),img.height());

        //this->setWidget(label1);
    }
    /***************************************打开模板文件*********************************************/
    Mat img_display;

    srcImage.copyTo( img_display );

    /// Create the result matrix
    int result_cols =  srcImage.cols - templ.cols + 1;
    int result_rows = srcImage.rows - templ.rows + 1;
    /*
     * 需要注意，目标图像的大小为int result_cols =  srcImage.cols - templ.cols + 1;
    int result_rows = srcImage.rows - templ.rows + 1;
    这是因为模板沿着原始图像上的每一个点进行遍历，而产生一个目标图像内的点，
    当图像遍历到其右侧时，只能遍历到其从右侧数第 srcImage.cols - templ.cols + 1个点。
    当图像遍历到其下侧时，只能遍历到其从下侧数第 srcImage.rows - templ.rows + 1个点。
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
    //定义模板、结果
    Mat templ;
    Mat result;
    /* match_method只能取0~5之中的某一个值，即：
      * method=TM_SQDIFF             （0）
      * method=TM_SQDIFF_NORMED      （1）
        method=TM_CCORR              （2）
        method=TM_CCORR_NORMED       （3）
        method=TM_CCOEFF ·           （4）
        method=TM_CCOEFF_NORMED      （5）
    */
    //设置匹配方法
    int match_method=2;
    /***************************************打开模板文件*********************************************/
    //注意这里在主界面的左上角添加了一个标签，专门用于显示模板图像
    QString filename = QFileDialog::getOpenFileName(this,tr("打开模板图像"),"",tr("Image File(*.bmp *.jpg *.jpeg *.png)"));
    QTextCodec *code = QTextCodec::codecForName("gb18030");
    std::string name = code->fromUnicode(filename).data();
    templ = cv::imread(name);
    if(!templ.data)
    {
        QMessageBox msgBox;
        msgBox.setText(tr("未找到数据"));
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
    /***************************************打开模板文件*********************************************/
    //用于显示的图像
    Mat img_display;
    //复制图像srcImage到img_display
    srcImage.copyTo( img_display );
    //生成结果
    int result_cols =  srcImage.cols - templ.cols + 1;
    int result_rows = srcImage.rows - templ.rows + 1;
    /*
     * 需要注意，目标图像的大小为int result_cols =  srcImage.cols - templ.cols + 1;
    int result_rows = srcImage.rows - templ.rows + 1;
    这是因为模板沿着原始图像上的每一个点进行遍历，而产生一个目标图像内的点，
    当图像遍历到其右侧时，只能遍历到其从左侧数第 srcImage.cols - templ.cols + 1个点。
    当图像遍历到其下侧时，只能遍历到其从上侧数第 srcImage.rows - templ.rows + 1个点。
    */
    result.create( result_cols, result_rows, CV_32FC1 );
    //进行模板匹配操作
    cv::matchTemplate( srcImage, templ, result, match_method );
    normalize( result, result, 0, 1, NORM_MINMAX, -1, Mat() );
    //使用minMaxLoc对匹配结果进行定位
    double minVal;
    double maxVal;
    Point minLoc;
    Point maxLoc;
    Point matchLoc;
    minMaxLoc( result, &minVal, &maxVal, &minLoc, &maxLoc, Mat() );
    //对于SQDIFF和SQDIFF_NORMED，最好的匹配时最小值，其他的是最大值。
    if( match_method  == TM_SQDIFF || match_method == TM_SQDIFF_NORMED )
        matchLoc = minLoc;
    else
        matchLoc = maxLoc;
    //处理结果
    rectangle( img_display, matchLoc, Point( matchLoc.x + templ.cols , matchLoc.y + templ.rows ), Scalar::all(0), 2, 8, 0 );
    rectangle( result, matchLoc, Point( matchLoc.x + templ.cols , matchLoc.y + templ.rows ), Scalar::all(0), 2, 8, 0 );
    img_display.copyTo(dstImage);
    //显示结果
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
    //窗口显示测试
    //char* image_window = "Source Image";
    // char* result_window = "Result window";
    // imshow( image_window, img_display );
    //imshow( result_window, result );
}

void MainWindow::on_actionCV_TM_CCORR_NORMED_triggered()
{
    Mat templ;
    Mat result;
    /* match_method只能取0~5之间的值，即：
      *method=CV_TM_SQDIFF_NORMED
        method=CV_TM_CCORR
        method=CV_TM_CCORR_NORMED
        method=CV_TM_CCOEFF
        method=CV_TM_CCOEFF_NORMED*/
    int match_method=3;
    char* image_window = "Source Image";
    char* result_window = "Result window";
    /***************************************打开模板文件*********************************************/
    QString filename = QFileDialog::getOpenFileName(this,tr("Open Image"),"",tr("Image File(*.bmp *.jpg *.jpeg *.png)"));
    QTextCodec *code = QTextCodec::codecForName("gb18030");
    std::string name = code->fromUnicode(filename).data();
    templ = cv::imread(name);
    if(!templ.data)
    {
        QMessageBox msgBox;
        msgBox.setText(tr("未找到数据"));
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
        //   ui->label1->resize(ui->label1->pixmap()->size());//设置当前标签为图像大小
        // ui->label1->resize(img.width(),img.height());

        //this->setWidget(label1);
    }
    /***************************************打开模板文件*********************************************/
    Mat img_display;

    srcImage.copyTo( img_display );

    /// Create the result matrix
    int result_cols =  srcImage.cols - templ.cols + 1;
    int result_rows = srcImage.rows - templ.rows + 1;
    /*
     * 需要注意，目标图像的大小为int result_cols =  srcImage.cols - templ.cols + 1;
    int result_rows = srcImage.rows - templ.rows + 1;
    这是因为模板沿着原始图像上的每一个点进行遍历，而产生一个目标图像内的点，
    当图像遍历到其右侧时，只能遍历到其从右侧数第 srcImage.cols - templ.cols + 1个点。
    当图像遍历到其下侧时，只能遍历到其从下侧数第 srcImage.rows - templ.rows + 1个点。
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
    /* match_method只能取0~5之间的值，即：
      *method=CV_TM_SQDIFF_NORMED
        method=CV_TM_CCORR
        method=CV_TM_CCORR_NORMED
        method=CV_TM_CCOEFF
        method=CV_TM_CCOEFF_NORMED*/
    int match_method=4;
    char* image_window = "Source Image";
    char* result_window = "Result window";
    /***************************************打开模板文件*********************************************/
    QString filename = QFileDialog::getOpenFileName(this,tr("Open Image"),"",tr("Image File(*.bmp *.jpg *.jpeg *.png)"));
    QTextCodec *code = QTextCodec::codecForName("gb18030");
    std::string name = code->fromUnicode(filename).data();
    templ = cv::imread(name);
    if(!templ.data)
    {
        QMessageBox msgBox;
        msgBox.setText(tr("未找到数据"));
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
        //   ui->label1->resize(ui->label1->pixmap()->size());//设置当前标签为图像大小
        // ui->label1->resize(img.width(),img.height());

        //this->setWidget(label1);
    }
    /***************************************打开模板文件*********************************************/
    Mat img_display;

    srcImage.copyTo( img_display );

    /// Create the result matrix
    int result_cols =  srcImage.cols - templ.cols + 1;
    int result_rows = srcImage.rows - templ.rows + 1;
    /*
     * 需要注意，目标图像的大小为int result_cols =  srcImage.cols - templ.cols + 1;
    int result_rows = srcImage.rows - templ.rows + 1;
    这是因为模板沿着原始图像上的每一个点进行遍历，而产生一个目标图像内的点，
    当图像遍历到其右侧时，只能遍历到其从右侧数第 srcImage.cols - templ.cols + 1个点。
    当图像遍历到其下侧时，只能遍历到其从下侧数第 srcImage.rows - templ.rows + 1个点。
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
    /* match_method只能取0~5之间的值，即：
      *method=CV_TM_SQDIFF_NORMED
        method=CV_TM_CCORR
        method=CV_TM_CCORR_NORMED
        method=CV_TM_CCOEFF
        method=CV_TM_CCOEFF_NORMED*/
    int match_method=5;
    char* image_window = "Source Image";
    char* result_window = "Result window";
    /***************************************打开模板文件*********************************************/
    QString filename = QFileDialog::getOpenFileName(this,tr("Open Image"),"",tr("Image File(*.bmp *.jpg *.jpeg *.png)"));
    QTextCodec *code = QTextCodec::codecForName("gb18030");
    std::string name = code->fromUnicode(filename).data();
    templ = cv::imread(name);
    if(!templ.data)
    {
        QMessageBox msgBox;
        msgBox.setText(tr("未找到数据"));
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
        //   ui->label1->resize(ui->label1->pixmap()->size());//设置当前标签为图像大小
        // ui->label1->resize(img.width(),img.height());

        //this->setWidget(label1);
    }
    /***************************************打开模板文件*********************************************/
    Mat img_display;

    srcImage.copyTo( img_display );

    /// Create the result matrix
    int result_cols =  srcImage.cols - templ.cols + 1;
    int result_rows = srcImage.rows - templ.rows + 1;
    /*
     * 需要注意，目标图像的大小为int result_cols =  srcImage.cols - templ.cols + 1;
    int result_rows = srcImage.rows - templ.rows + 1;
    这是因为模板沿着原始图像上的每一个点进行遍历，而产生一个目标图像内的点，
    当图像遍历到其右侧时，只能遍历到其从右侧数第 srcImage.cols - templ.cols + 1个点。
    当图像遍历到其下侧时，只能遍历到其从下侧数第 srcImage.rows - templ.rows + 1个点。
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
    //单纯仿射
    Point2f srcTri[3];
    Point2f dstTri[3];
    Mat rot_mat( 2, 3, CV_32FC1 );
    Mat warp_mat( 2, 3, CV_32FC1 );
    Mat src, warp_dst, warp_rotate_dst;
    //读入图像
    srcImage.copyTo(src);
    warp_dst = Mat::zeros( src.rows, src.cols, src.type() );
    // 用3个点确定A仿射变换
    srcTri[0] = Point2f( 0,0 );
    srcTri[1] = Point2f( src.cols - 1, 0 );
    srcTri[2] = Point2f( 0, src.rows - 1 );
    dstTri[0] = Point2f( src.cols*0.0, src.rows*0.33 );
    dstTri[1] = Point2f( src.cols*0.85, src.rows*0.25 );
    dstTri[2] = Point2f( src.cols*0.15, src.rows*0.7 );
    warp_mat = getAffineTransform( srcTri, dstTri );
    warpAffine( src, warp_dst, warp_mat, warp_dst.size() );
    warp_dst.copyTo(dstImage);
    //显示仿射结果
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_rotateWrapAffine_triggered()
{
    //旋转仿射
    Point2f srcTri[3];
    Point2f dstTri[3];
    Mat rot_mat( 2, 3, CV_32FC1 );
    Mat warp_mat( 2, 3, CV_32FC1 );
    Mat src, warp_dst, warp_rotate_dst;
    //读入图像
    srcImage.copyTo(src);
    warp_dst = Mat::zeros( src.rows, src.cols, src.type() );
    // 用3个点确定A仿射变换
    srcTri[0] = Point2f( 0,0 );
    srcTri[1] = Point2f( src.cols - 1, 0 );
    srcTri[2] = Point2f( 0, src.rows - 1 );
    dstTri[0] = Point2f( src.cols*0.0, src.rows*0.33 );
    dstTri[1] = Point2f( src.cols*0.85, src.rows*0.25 );
    dstTri[2] = Point2f( src.cols*0.15, src.rows*0.7 );
    warp_mat = getAffineTransform( srcTri, dstTri );
    warpAffine( src, warp_dst, warp_mat, warp_dst.size() );
    // 旋转矩阵
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
    //显示结果图像
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}
void MainWindow::on_remapCopy_triggered()
{
    // 复制
    // 定义映射
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
    //调用remap
    remap( srcImage, dstImage, map_x, map_y, CV_INTER_LINEAR, BORDER_CONSTANT, Scalar(0,0, 0) );
    //显示图像
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}
void MainWindow::on_remapX_triggered()
{
    //x轴
    //定义映射
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
    //调用remap
    remap( srcImage, dstImage, map_x, map_y, CV_INTER_LINEAR, BORDER_CONSTANT, Scalar(0,0, 0) );
    //显示图像
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_remapY_triggered()
{
    //y轴
    //定义映射
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
    //调用remap
    remap( srcImage, dstImage, map_x, map_y, CV_INTER_LINEAR, BORDER_CONSTANT, Scalar(0,0, 0) );
    //显示图像
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_remapSmall_triggered()
{
    //缩小
    //定义映射
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
                map_x.at<float>(i,j) = 1 ;   //随机选取
                map_y.at<float>(i,j) = 1 ;   //随机选取
            }
        }
    }
    //调用remap
    remap( srcImage, dstImage, map_x, map_y, CV_INTER_LINEAR, BORDER_CONSTANT, Scalar(0,0, 0) );
    //显示图像
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_remapRotate_triggered()
{
    //旋转
    //定义映射
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
    //调用remap
    remap( srcImage, dstImage, map_x, map_y, CV_INTER_LINEAR, BORDER_CONSTANT, Scalar(0,0, 0) );
    //显示图像
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}


void MainWindow::on_remapDiagonal_triggered()
{
    //x、y互换
    //定义映射
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
    //调用remap
    remap( srcImage, dstImage, map_x, map_y, CV_INTER_LINEAR, BORDER_CONSTANT, Scalar(0,0, 0) );
    //显示图像
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
    //读入图像
    srcImage.copyTo(src);
    warp_dst = Mat::zeros( src.rows, src.cols, src.type() );
    // 用3个点确定A仿射变换
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
    //读入图像
    srcImage.copyTo(src);
    warp_dst = Mat::zeros( src.rows, src.cols, src.type() );
    // 用3个点确定A仿射变换
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
    //读入图像
    srcImage.copyTo(src);
    warp_dst = Mat::zeros( src.rows, src.cols, src.type() );
    // 用3个点确定A仿射变换
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
    //读入图像
    srcImage.copyTo(src);
    warp_dst = Mat::zeros( src.rows, src.cols, src.type() );
    // 用3个点确定A仿射变换
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
    //菜单：threshold=>THRESH_BINARY
    //定义Mat，用于存储灰度图像
    Mat srcGray;
    //调整大小
    cv::resize(srcImage,srcImage,Size(ui->label1->width(), ui->label1->height()),0,0,3);
    //色彩空间转换
    cvtColor(srcImage,srcGray,COLOR_RGB2GRAY);
    //定义参数
    int threshold_value=128;
    int max_BINARY_value=255;
    int threshold_type=THRESH_BINARY;
    /***********等价于************/
    //int threshold_type=0;
    /***********等价于************/
    //调用threshold函数
    threshold(srcGray, dstImage, threshold_value, max_BINARY_value,threshold_type );
    // imshow("li",dstImage);    //测试效果
    //显示图像
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows, dstImage.cols*dstImage.channels(),QImage::Format_Indexed8);
    //img=img.scaled(ui->label1->size());   //缩放图像
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_actionTHRESH_BINARY_INV_triggered()
{
    //菜单：threshold=>THRESH_BINARY_INV;
    //定义Mat，用于存储灰度图像
    Mat srcGray;
    //调整大小
    cv::resize(srcImage,srcImage,Size(ui->label1->width(), ui->label1->height()),0,0,3);
    //色彩空间转换
    cvtColor(srcImage,srcGray,COLOR_RGB2GRAY);
    //定义参数
    int threshold_value=128;
    int max_BINARY_value=255;
    int threshold_type=THRESH_BINARY_INV;
    /***********等价于************/
    //int threshold_type=0;
    /***********等价于************/
    //调用threshold函数
    threshold(srcGray, dstImage, threshold_value, max_BINARY_value,threshold_type );
    // imshow("li",dstImage);    //测试效果
    //显示图像
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows, dstImage.cols*dstImage.channels(),QImage::Format_Indexed8);
    //img=img.scaled(ui->label1->size());   //缩放图像
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_actionTHRESH_TRUNC_triggered()
{
    //菜单：threshold=>THRESH_TRUNC;
    //定义Mat，用于存储灰度图像
    Mat srcGray;
    //调整大小
    cv::resize(srcImage,srcImage,Size(ui->label1->width(), ui->label1->height()),0,0,3);
    //色彩空间转换
    cvtColor(srcImage,srcGray,COLOR_RGB2GRAY);
    //定义参数
    int threshold_value=128;
    int max_BINARY_value=255;
    int threshold_type=THRESH_TRUNC;
    /***********等价于************/
    //int threshold_type=0;
    /***********等价于************/
    //调用threshold函数
    threshold(srcGray, dstImage, threshold_value, max_BINARY_value,threshold_type );
    // imshow("li",dstImage);    //测试效果
    //显示图像
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows, dstImage.cols*dstImage.channels(),QImage::Format_Indexed8);
    //img=img.scaled(ui->label1->size());   //缩放图像
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_actionTHRESH_TOZERO_triggered()
{
    //菜单：threshold=>THRESH_TOZERO;
    //定义Mat，用于存储灰度图像
    Mat srcGray;
    //调整大小
    cv::resize(srcImage,srcImage,Size(ui->label1->width(), ui->label1->height()),0,0,3);
    //色彩空间转换
    cvtColor(srcImage,srcGray,COLOR_RGB2GRAY);
    //定义参数
    int threshold_value=128;
    int max_BINARY_value=255;
    int threshold_type=THRESH_TOZERO;
    /***********等价于************/
    //int threshold_type=0;
    /***********等价于************/
    //调用threshold函数
    threshold(srcGray, dstImage, threshold_value, max_BINARY_value,threshold_type );
    // imshow("li",dstImage);    //测试效果
    //显示图像
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows, dstImage.cols*dstImage.channels(),QImage::Format_Indexed8);
    //img=img.scaled(ui->label1->size());   //缩放图像
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_actionTHRESH_TOZERO_INV_2_triggered()
{
    //菜单：threshold=>THRESH_TOZERO_INV;
    //定义Mat，用于存储灰度图像
    Mat srcGray;
    //调整大小
    cv::resize(srcImage,srcImage,Size(ui->label1->width(), ui->label1->height()),0,0,3);
    //色彩空间转换
    cvtColor(srcImage,srcGray,COLOR_RGB2GRAY);
    //定义参数
    int threshold_value=128;
    int max_BINARY_value=255;
    int threshold_type=THRESH_TOZERO_INV;
    /***********等价于************/
    //int threshold_type=0;
    /***********等价于************/
    //调用threshold函数
    threshold(srcGray, dstImage, threshold_value, max_BINARY_value,threshold_type );
    // imshow("li",dstImage);    //测试效果
    //显示图像
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows, dstImage.cols*dstImage.channels(),QImage::Format_Indexed8);
    //img=img.scaled(ui->label1->size());   //缩放图像
    ui->label2->setPixmap(QPixmap::fromImage(img));
}



void MainWindow::on_actionTHRESH_BINARY_3_triggered()
{
    //菜单：THRESH_OTST=>TRESH_BINARY
    //THRESH_BINARY+THRESH_OTSU;
    //定义灰度Mat，用户存储灰度图像
    Mat srcGray;
    //调整下大小
    cv::resize(srcImage,srcImage,Size(ui->label1->width(), ui->label1->height()),0,0,3);
    //色彩空间转换，彩色变灰度
    cvtColor(srcImage,srcGray,COLOR_RGB2GRAY);
    //定义参数值
    int threshold_value=128;
    int max_BINARY_value=255;
    int threshold_type=THRESH_BINARY+THRESH_OTSU;
    //调用threshold
    threshold(srcGray, dstImage, threshold_value, max_BINARY_value,threshold_type );
    // imshow("li",dstImage);    //测试一下
    //显示图像
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows, dstImage.cols*dstImage.channels(),QImage::Format_Indexed8);
    //  img=img.scaled(ui->label1->size());     //调整大小
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_actionTHRESH_BINARY_INV_3_triggered()
{   
    //菜单：THRESH_OTST=>THRESH_BINARY_INV
    //THRESH_BINARY_INV+THRESH_OTSU;
    //定义灰度Mat，用户存储灰度图像
    Mat srcGray;
    //调整下大小
    cv::resize(srcImage,srcImage,Size(ui->label1->width(), ui->label1->height()),0,0,3);
    //色彩空间转换，彩色变灰度
    cvtColor(srcImage,srcGray,COLOR_RGB2GRAY);
    //定义参数值
    int threshold_value=128;
    int max_BINARY_value=255;
    int threshold_type=THRESH_BINARY_INV+THRESH_OTSU;
    //调用threshold
    threshold(srcGray, dstImage, threshold_value, max_BINARY_value,threshold_type );
    // imshow("li",dstImage);    //测试一下
    //显示图像
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows, dstImage.cols*dstImage.channels(),QImage::Format_Indexed8);
    //  img=img.scaled(ui->label1->size());     //调整大小
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_actionTHRESH_TRUNC_2_triggered()
{
    //菜单：THRESH_OTST=>THRESH_TRUNC
    //THRESH_TRUNC+THRESH_OTSU;
    //定义灰度Mat，用户存储灰度图像
    Mat srcGray;
    //调整下大小
    cv::resize(srcImage,srcImage,Size(ui->label1->width(), ui->label1->height()),0,0,3);
    //色彩空间转换，彩色变灰度
    cvtColor(srcImage,srcGray,COLOR_RGB2GRAY);
    //定义参数值
    int threshold_value=128;
    int max_BINARY_value=255;
    int threshold_type=THRESH_TRUNC+THRESH_OTSU;
    //调用threshold
    threshold(srcGray, dstImage, threshold_value, max_BINARY_value,threshold_type );
    // imshow("li",dstImage);    //测试一下
    //显示图像
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows, dstImage.cols*dstImage.channels(),QImage::Format_Indexed8);
    //  img=img.scaled(ui->label1->size());     //调整大小
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_actionTHRESH_TOZERO_2_triggered()
{
    //菜单：THRESH_OTST=>THRESH_TOZERO
    //THRESH_TOZERO+THRESH_OTSU;
    //定义灰度Mat，用户存储灰度图像
    Mat srcGray;
    //调整下大小
    cv::resize(srcImage,srcImage,Size(ui->label1->width(), ui->label1->height()),0,0,3);
    //色彩空间转换，彩色变灰度
    cvtColor(srcImage,srcGray,COLOR_RGB2GRAY);
    //定义参数值
    int threshold_value=128;
    int max_BINARY_value=255;
    int threshold_type=THRESH_TOZERO+THRESH_OTSU;
    //调用threshold
    threshold(srcGray, dstImage, threshold_value, max_BINARY_value,threshold_type );
    // imshow("li",dstImage);    //测试一下
    //显示图像
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows, dstImage.cols*dstImage.channels(),QImage::Format_Indexed8);
    //  img=img.scaled(ui->label1->size());     //调整大小
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_actionTHRESH_TOZERO_INV_triggered()
{
    //菜单：THRESH_OTST=>THRESH_TOZERO_INV
    //THRESH_TOZERO_INV+THRESH_OTSU;
    //定义灰度Mat，用户存储灰度图像
    Mat srcGray;
    //调整下大小
    cv::resize(srcImage,srcImage,Size(ui->label1->width(), ui->label1->height()),0,0,3);
    //色彩空间转换，彩色变灰度
    cvtColor(srcImage,srcGray,COLOR_RGB2GRAY);
    //定义参数值
    int threshold_value=128;
    int max_BINARY_value=255;
    int threshold_type=THRESH_TOZERO_INV+THRESH_OTSU;
    //调用threshold
    threshold(srcGray, dstImage, threshold_value, max_BINARY_value,threshold_type );
    // imshow("li",dstImage);    //测试一下
    //显示图像
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows, dstImage.cols*dstImage.channels(),QImage::Format_Indexed8);
    //  img=img.scaled(ui->label1->size());     //调整大小
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_actionTHRESH_BINARY_INV_4_triggered()
{

}

void MainWindow::on_actionADAPTIVE_THRESH_MEAN_C_triggered()
{
    //菜单:adaptiveThreshold=>THRESH_BINARY=>ADAPTIVE_THRESH_MEAN_C
    //定义一个Mat，用于存储灰度图像
    Mat srcGray;
    //调整大小
    cv::resize(srcImage,srcImage,Size(ui->label1->width(), ui->label1->height()),0,0,3);
    //色彩空间转换
    cvtColor(srcImage,srcGray,COLOR_RGB2GRAY);
    //参数设定
    int maxValue=255;
    int adaptiveMethod=ADAPTIVE_THRESH_MEAN_C;
    int thresholdType=THRESH_BINARY;
    int blocksize=7;
    double C=1;
    //调用adaptiveThreshold函数
    adaptiveThreshold(srcGray, dstImage, maxValue,adaptiveMethod,thresholdType,blocksize,C );
    //显示图像
    // imshow("li",dstImage); //测试显示情况
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows, dstImage.cols*dstImage.channels(),QImage::Format_Indexed8);
    //  img=img.scaled(ui->label1->size());   //调整大小
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_actionADAPTIVE_THRESH_GAUSSIAN_C_triggered()
{    
    //菜单:adaptiveThreshold=>THRESH_BINARY=>ADAPTIVE_THRESH_GAUSSIAN_C
    //定义一个Mat，用于存储灰度图像
    Mat srcGray;
    //调整大小
    cv::resize(srcImage,srcImage,Size(ui->label1->width(), ui->label1->height()),0,0,3);
    //色彩空间转换
    cvtColor(srcImage,srcGray,COLOR_RGB2GRAY);
    //参数设定
    int maxValue=255;
    int adaptiveMethod=ADAPTIVE_THRESH_GAUSSIAN_C;
    int thresholdType=THRESH_BINARY;
    int blocksize=7;
    double C=1;
    //调用adaptiveThreshold函数
    adaptiveThreshold(srcGray, dstImage, maxValue,adaptiveMethod,thresholdType,blocksize,C );
    //显示图像
    // imshow("li",dstImage); //测试显示情况
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows, dstImage.cols*dstImage.channels(),QImage::Format_Indexed8);
    //  img=img.scaled(ui->label1->size());   //调整大小
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_actionADAPTIVE_THRESH_MEAN_C_2_triggered()
{
    //菜单:adaptiveThreshold=>THRESH_BINARY_INV=>ADAPTIVE_THRESH_MEAN_C
    //定义一个Mat，用于存储灰度图像
    Mat srcGray;
    //调整大小
    cv::resize(srcImage,srcImage,Size(ui->label1->width(), ui->label1->height()),0,0,3);
    //色彩空间转换
    cvtColor(srcImage,srcGray,COLOR_RGB2GRAY);
    //参数设定
    int maxValue=255;
    int adaptiveMethod=ADAPTIVE_THRESH_MEAN_C;
    int thresholdType=THRESH_BINARY_INV;
    int blocksize=7;
    double C=1;
    //调用adaptiveThreshold函数
    adaptiveThreshold(srcGray, dstImage, maxValue,adaptiveMethod,thresholdType,blocksize,C );
    //显示图像
    // imshow("li",dstImage); //测试显示情况
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows, dstImage.cols*dstImage.channels(),QImage::Format_Indexed8);
    //  img=img.scaled(ui->label1->size());   //调整大小
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_actionADAPTIVE_THRESH_GAUSSIAN_C_2_triggered()
{
    //菜单:adaptiveThreshold=>THRESH_BINARY_INV=>ADAPTIVE_THRESH_GAUSSIAN_C
    //定义一个Mat，用于存储灰度图像
    Mat srcGray;
    //调整大小
    cv::resize(srcImage,srcImage,Size(ui->label1->width(), ui->label1->height()),0,0,3);
    //色彩空间转换
    cvtColor(srcImage,srcGray,COLOR_RGB2GRAY);
    //参数设定
    int maxValue=255;
    int adaptiveMethod=ADAPTIVE_THRESH_GAUSSIAN_C;
    int thresholdType=THRESH_BINARY_INV;
    int blocksize=7;
    double C=1;
    //调用adaptiveThreshold函数
    adaptiveThreshold(srcGray, dstImage, maxValue,adaptiveMethod,thresholdType,blocksize,C );
    //显示图像
    // imshow("li",dstImage); //测试显示情况
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows, dstImage.cols*dstImage.channels(),QImage::Format_Indexed8);
    //  img=img.scaled(ui->label1->size());   //调整大小
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_action_triggered()
{
    //锐化
    //构造核
    Mat kernel(3,3,CV_32F,cv::Scalar(0));
    kernel.at<float>(1,1) = 5.0;
    kernel.at<float>(1,0) = -1.0;
    kernel.at<float>(1,2) = -1.0;
    //调用filter2D实现
    filter2D(srcImage,dstImage, srcImage.depth(), kernel);
    //显示图像
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
    //菜单：THRESH_TRIANGLE=>TRESH_BINARY
    //THRESH_BINARY+THRESH_TRIANGLE;
    //定义灰度Mat，用户存储灰度图像
    Mat srcGray;
    //调整下大小
    cv::resize(srcImage,srcImage,Size(ui->label1->width(), ui->label1->height()),0,0,3);
    //色彩空间转换，彩色变灰度
    cvtColor(srcImage,srcGray,COLOR_RGB2GRAY);
    //定义参数值
    int threshold_value=128;
    int max_BINARY_value=255;
    int threshold_type=THRESH_BINARY+THRESH_TRIANGLE;
    //调用threshold
    threshold(srcGray, dstImage, threshold_value, max_BINARY_value,threshold_type );
    // imshow("li",dstImage);    //测试一下
    //显示图像
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows, dstImage.cols*dstImage.channels(),QImage::Format_Indexed8);
    //  img=img.scaled(ui->label1->size());     //调整大小
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_actionTHRESH_BINARY_INV_2_triggered()
{
    //菜单：THRESH_TRIANGLE=>THRESH_BINARY_INV
    //THRESH_BINARY_INV+THRESH_TRIANGLE;
    //定义灰度Mat，用户存储灰度图像
    Mat srcGray;
    //调整下大小
    cv::resize(srcImage,srcImage,Size(ui->label1->width(), ui->label1->height()),0,0,3);
    //色彩空间转换，彩色变灰度
    cvtColor(srcImage,srcGray,COLOR_RGB2GRAY);
    //定义参数值
    int threshold_value=128;
    int max_BINARY_value=255;
    int threshold_type=THRESH_BINARY_INV+THRESH_TRIANGLE;
    //调用threshold
    threshold(srcGray, dstImage, threshold_value, max_BINARY_value,threshold_type );
    // imshow("li",dstImage);    //测试一下
    //显示图像
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows, dstImage.cols*dstImage.channels(),QImage::Format_Indexed8);
    //  img=img.scaled(ui->label1->size());     //调整大小
    ui->label2->setPixmap(QPixmap::fromImage(img));
}




void MainWindow::on_actionTHRESH_TRUNC_3_triggered()
{
    //菜单：THRESH_TRIANGLE=>THRESH_TRUNC
    //THRESH_TRUNC+THRESH_TRIANGLE;
    //定义灰度Mat，用户存储灰度图像
    Mat srcGray;
    //调整下大小
    cv::resize(srcImage,srcImage,Size(ui->label1->width(), ui->label1->height()),0,0,3);
    //色彩空间转换，彩色变灰度
    cvtColor(srcImage,srcGray,COLOR_RGB2GRAY);
    //定义参数值
    int threshold_value=128;
    int max_BINARY_value=255;
    int threshold_type=THRESH_TRUNC+THRESH_TRIANGLE;
    //调用threshold
    threshold(srcGray, dstImage, threshold_value, max_BINARY_value,threshold_type );
    // imshow("li",dstImage);    //测试一下
    //显示图像
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows, dstImage.cols*dstImage.channels(),QImage::Format_Indexed8);
    //  img=img.scaled(ui->label1->size());     //调整大小
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_actionTHRESH_TOZERO_3_triggered()
{
    //菜单：THRESH_TRIANGLE=>THRESH_TOZERO
    //THRESH_TOZERO+THRESH_TRIANGLE;
    //定义灰度Mat，用户存储灰度图像
    Mat srcGray;
    //调整下大小
    cv::resize(srcImage,srcImage,Size(ui->label1->width(), ui->label1->height()),0,0,3);
    //色彩空间转换，彩色变灰度
    cvtColor(srcImage,srcGray,COLOR_RGB2GRAY);
    //定义参数值
    int threshold_value=128;
    int max_BINARY_value=255;
    int threshold_type=THRESH_TOZERO+THRESH_TRIANGLE;
    //调用threshold
    threshold(srcGray, dstImage, threshold_value, max_BINARY_value,threshold_type );
    // imshow("li",dstImage);    //测试一下
    //显示图像
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows, dstImage.cols*dstImage.channels(),QImage::Format_Indexed8);
    //  img=img.scaled(ui->label1->size());     //调整大小
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_actionTHRESH_TOZERO_INV_3_triggered()
{
    //菜单：THRESH_TRIANGLE=>THRESH_TOZERO_INV
    //THRESH_TOZERO_INV+THRESH_TRIANGLE;
    //定义灰度Mat，用户存储灰度图像
    Mat srcGray;
    //调整下大小
    cv::resize(srcImage,srcImage,Size(ui->label1->width(), ui->label1->height()),0,0,3);
    //色彩空间转换，彩色变灰度
    cvtColor(srcImage,srcGray,COLOR_RGB2GRAY);
    //定义参数值
    int threshold_value=128;
    int max_BINARY_value=255;
    int threshold_type=THRESH_TOZERO_INV+THRESH_TRIANGLE;
    //调用threshold
    threshold(srcGray, dstImage, threshold_value, max_BINARY_value,threshold_type );
    // imshow("li",dstImage);    //测试一下
    //显示图像
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows, dstImage.cols*dstImage.channels(),QImage::Format_Indexed8);
    //  img=img.scaled(ui->label1->size());     //调整大小
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_Clear_triggered()
{
    //菜单：文件=>清除
    //清除标签1的内容。
    ui->label1->clear();
    //清除标签2的内容。
    ui->label2->clear();

}
