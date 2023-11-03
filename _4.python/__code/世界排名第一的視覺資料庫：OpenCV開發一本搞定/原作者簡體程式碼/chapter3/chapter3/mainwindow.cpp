#include "mainwindow.h"
#include "ui_mainwindow.h"
#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QString>
#include <QFileDialog>
#include <QMessageBox>
#include <opencv/cv.h>
#include <QTextCodec>
using namespace cv;
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
        msgBox.setWindowTitle(tr("警告"));
        msgBox.setText(tr("默认的测试文件不存在，可以用以下两种方式的一种：1）复制一个文件到当前目录下，并命名为lena.jpg. 2)使用自定义方式打开一个自定义文件。"));
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

void MainWindow::on_actionSobel_triggered()
{
    //菜单：边缘检测=>Sobel
    //sobel边缘检测，具有默认值的采用默认参数值
    Sobel(srcImage,dstImage,srcImage.depth(),0,1);
    //显示处理结果
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_actionCanny_triggered()
{
    //菜单：边缘检测=>Canny
    //canny边缘检测，具有默认值的采用默认参数值
    Mat dstImage2;
    //先调整到与标签等大小。
    cv::resize(srcImage,srcImage,Size(ui->label1->width(), ui->label1->height()),0,0,3);
    //色彩空间转换
    cvtColor(srcImage,dstImage2,CV_BGR2GRAY);
    //调用canny，默认参数
    Canny(dstImage2,dstImage2,30,100);
    //显示处理结果
    img = QImage((const unsigned char*)(dstImage2.data),dstImage2.cols,dstImage2.rows,dstImage2.step,  QImage::Format_Indexed8);
    //  img=img.scaled(ui->label2->size());  //说明：如果经过canny变换后再调整图像大小，显示时会显示全黑，无法观看。
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_actionLaplacian_triggered()
{
    //菜单：边缘检测=>Laplacian
    //Laplacian边缘检测，具有默认值的采用默认参数值
    Laplacian(srcImage,dstImage,srcImage.depth());
    //显示处理结果
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}
void MainWindow::on_actionScharr_triggered()
{
    //菜单：边缘检测=>Scharr
    //Scharr边缘检测，具有默认值的采用默认参数值
    Scharr(srcImage,dstImage,srcImage.depth(),0,1);
    //显示处理结果
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}
void MainWindow::on_actionDx_triggered()
{
    //菜单：Soble=>方向=>dx
    //调用Sobel在x轴方向上操作
    Sobel(srcImage,dstImage,srcImage.depth(),1,0);
    //显示图像
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_actionDy_triggered()
{
    //菜单：Soble=>方向=>dy
    //调用Sobel在y轴方向上操作
    Sobel(srcImage,dstImage,srcImage.depth(),0,1);
    //显示图像
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_actionDx_dy_triggered()
{
    //菜单：Soble=>方向=>dx&dy
    //调用Sobel在x轴&y轴方向上操作
    Sobel(srcImage,dstImage,srcImage.depth(),1,1);
    //显示图像
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_action1_triggered()
{
    //菜单：Sobel=>ksize大小=>size=1
    //调用soble实现，size大小等于1。
    Sobel(srcImage,dstImage,srcImage.depth(),1,1,1);
    //显示处理结果
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_action3_triggered()
{
    //Sobel(srcImage,dstImage,srcImage.depth(),1,1);
    Sobel(srcImage,dstImage,srcImage.depth(),1,1,3);
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_action5_triggered()
{
    //Sobel(srcImage,dstImage,srcImage.depth(),1,1);
    Sobel(srcImage,dstImage,srcImage.depth(),1,1,5);
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_action7_triggered()
{
    //Sobel(srcImage,dstImage,srcImage.depth(),1,1);
    Sobel(srcImage,dstImage,srcImage.depth(),1,1,7,1);
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
    //  Mat dstImage2;
    //   Sobel(srcImage,dstImage2,srcImage.depth(),1,1,7,5);
    //imshow("li",dstImage);
    //imshow("li2",dstImage2);
}

void MainWindow::on_action1_2_triggered()
{
    //菜单：sobel=>scale缩放因子=>scale=1
    //调用sobel，设置scale参数值为1
    Sobel(srcImage,dstImage,srcImage.depth(),1,1,7,1);
    //显示处理效果
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_action0_5_triggered()
{
    Sobel(srcImage,dstImage,srcImage.depth(),1,1,7,0.5);
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_action2_triggered()
{
    Sobel(srcImage,dstImage,srcImage.depth(),1,1,7,2);
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_actionDelta_1_triggered()
{
    //菜单：sobel=>delta值=>delta=50
    //soble检测、delta=50.
    Sobel(srcImage,dstImage,srcImage.depth(),1,1,7,1,50);
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_actionDelta_0_triggered()
{
    //菜单：sobel=>delta值=>delta=0
    //soble检测、delta采用默认值0.
    Sobel(srcImage,dstImage,srcImage.depth(),1,1,7,1,0);
    //显示处理结果图像
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_actionDelta_2_triggered()
{
    //菜单：sobel=>delta值=>delta=100
    Sobel(srcImage,dstImage,srcImage.depth(),1,1,7,1,100);
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
    //  imshow("test",dstImage);
}

void MainWindow::on_action50_triggered()
{
    //菜单：canny=>threshold1=>t1=50
    //设置参数threshold1=50的情况下调用canny
    Mat srcImage2;   //用于存储转换后图像，直接转换srcImage发生变换，影响srcImage的后续使用
    //调整大小
    cv::resize(srcImage,srcImage2,Size(ui->label1->width(), ui->label1->height()),0,0,3);
    //色彩空间转换，彩色=>灰度
    cvtColor(srcImage2,srcImage2,CV_BGR2GRAY);
    //canny检测
    Canny(srcImage2,dstImage,50,150);
    //显示图像
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.step,  QImage::Format_Indexed8);
    //  img=img.scaled(ui->label2->size());  //说明：如果重置图像大小会导致全黑，无法观看。提前将原始图像进行了缩放。
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_action100_triggered()
{
    //菜单：canny=>threshold1=>t1=100
    //设置参数threshold1=100的情况下调用canny
    Mat srcImage2;   //用于存储转换后图像，直接转换srcImage发生变换，影响srcImage的后续使用
    //调整大小
    cv::resize(srcImage,srcImage2,Size(ui->label1->width(), ui->label1->height()),0,0,3);
    //色彩空间转换，彩色=>灰度
    cvtColor(srcImage2,srcImage2,CV_BGR2GRAY);
    //canny检测
    Canny(srcImage2,dstImage,100,150);
    //显示图像
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.step,  QImage::Format_Indexed8);
    //  img=img.scaled(ui->label2->size());  //说明：如果重置图像大小会导致全黑，无法观看。提前将原始图像进行了缩放。
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_action150_triggered()
{
    //菜单：canny=>threshold2=>t2=150
    //设置参数threshold2=150的情况下调用canny
    Mat srcImage2;   //用于存储转换后图像，直接转换srcImage发生变换，影响srcImage的后续使用
    //调整大小
    cv::resize(srcImage,srcImage2,Size(ui->label1->width(), ui->label1->height()),0,0,3);
    //色彩空间转换，彩色=>灰度
    cvtColor(srcImage2,srcImage2,CV_BGR2GRAY);
    //canny检测
    Canny(srcImage2,dstImage,10,150);
    //显示图像
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.step,  QImage::Format_Indexed8);
    //  img=img.scaled(ui->label2->size());  //说明：如果重置图像大小会导致全黑，无法观看。提前将原始图像进行了缩放。
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_action200_triggered()
{
    //菜单：canny=>threshold2=>t2=200
    //设置参数threshold2=200的情况下调用canny
    Mat srcImage2;   //用于存储转换后图像，直接转换srcImage发生变换，影响srcImage的后续使用
    //调整大小
    cv::resize(srcImage,srcImage2,Size(ui->label1->width(), ui->label1->height()),0,0,3);
    //色彩空间转换，彩色=>灰度
    cvtColor(srcImage2,srcImage2,CV_BGR2GRAY);
    //canny检测
    Canny(srcImage2,dstImage,10,200);
    //显示图像
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.step,  QImage::Format_Indexed8);
    //  img=img.scaled(ui->label2->size());  //说明：如果重置图像大小会导致全黑，无法观看。提前将原始图像进行了缩放。
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_actionAs_1_triggered()
{
    //菜单：canny=>apertureSize=>as=5
    //调整大小
    cv::resize(srcImage,dstImage,Size(ui->label1->width(), ui->label1->height()),0,0,3);
    //色彩空间转换，转换为灰度图像
    cvtColor(dstImage,dstImage,CV_BGR2GRAY);
    //调用canny，apertureSize设置为5.
    Canny(dstImage,dstImage,50,150,5);
    //显示图像处理效果
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.step,  QImage::Format_Indexed8);
    //  img=img.scaled(ui->label2->size());  //说明：如果重置图像大小会导致全黑，无法观看。提前将原始图像进行了缩放。
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_actionAs_3_triggered()
{
    //菜单：canny=>apertureSize=>as=7
    //调整大小
    cv::resize(srcImage,dstImage,Size(ui->label1->width(), ui->label1->height()),0,0,3);
    //色彩空间转换，转换为灰度图像
    cvtColor(dstImage,dstImage,CV_BGR2GRAY);
    //调用canny，apertureSize设置为7.
    Canny(dstImage,dstImage,50,150,7);
    //显示图像处理效果
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.step,  QImage::Format_Indexed8);
    //  img=img.scaled(ui->label2->size());  //说明：如果重置图像大小会导致全黑，无法观看。提前将原始图像进行了缩放。
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_actionAs_4_triggered()
{
    //菜单：canny=>apertureSize=>as=3
    //调整大小
    cv::resize(srcImage,dstImage,Size(ui->label1->width(), ui->label1->height()),0,0,3);
    //色彩空间转换，转换为灰度图像
    cvtColor(dstImage,dstImage,CV_BGR2GRAY);
    //调用canny，apertureSize设置为3.
    Canny(dstImage,dstImage,50,150,3);
    //显示图像处理效果
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.step,  QImage::Format_Indexed8);
    //  img=img.scaled(ui->label2->size());  //说明：如果重置图像大小会导致全黑，无法观看。提前将原始图像进行了缩放。
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_actionFalse_triggered()
{
    //菜单： canny=>L2gradient=>false
    //调整大小
    cv::resize(srcImage,dstImage,Size(ui->label1->width(), ui->label1->height()),0,0,3);
    //转换为灰度图像
    cvtColor(dstImage,dstImage,CV_BGR2GRAY);
    //调用Canny函数
    Canny(dstImage,dstImage,50,150);
    //显示图像
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.step,  QImage::Format_Indexed8);
    //  img=img.scaled(ui->label2->size());   //说明：如果重置图像大小会导致全黑，无法观看。提前将原始图像进行了缩放。
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_actionTrue_triggered()
{
    //菜单： canny=>L2gradient=>true
    //调整大小
    cv::resize(srcImage,dstImage,Size(ui->label1->width(), ui->label1->height()),0,0,3);
    //转换为灰度图像
    cvtColor(dstImage,dstImage,CV_BGR2GRAY);
    //调用Canny函数
    Canny(dstImage,dstImage,50,150,3,true);
    //显示图像
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.step,  QImage::Format_Indexed8);
    //  img=img.scaled(ui->label2->size());   //说明：如果重置图像大小会导致全黑，无法观看。提前将原始图像进行了缩放。
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_actionKsize_1_triggered()
{
    //菜单：Laplacian=>ksize=>ksize=1
    //调用Laplacian函数，使用默认的ksize值
    Laplacian(srcImage,dstImage,srcImage.depth());
    //显示处理结果
    img = QImage((const unsigned char*)
                 (dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),
                 QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_actionKsize_3_triggered()
{
    //菜单：Laplacian=>ksize=>ksize=3
    //调用Laplacian函数，显式设置：ksize=3
    Laplacian(srcImage,dstImage,srcImage.depth(),3);
    //显示处理结果
    img = QImage((const unsigned char*)
                 (dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),
                 QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_actionKsize_5_triggered()
{
    //菜单：Laplacian=>ksize=>ksize=5
    //调用Laplacian函数，显式设置：ksize=5
    Laplacian(srcImage,dstImage,srcImage.depth(),5);
    //显示处理结果
    img = QImage((const unsigned char*)
                 (dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),
                 QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_actionScale_1_triggered()
{
    //菜单：Laplacian=>scale=>lsacle=1
    //调用Laplacian函数，使用默认的scale值
    Laplacian(srcImage,dstImage,srcImage.depth());
    //显示处理结果
    img = QImage((const unsigned char*)
                 (dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),
                 QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_actionScale_0_5_triggered()
{
    //菜单：Laplacian=>scale=>lsacle=0.5
    //调用Laplacian函数，设置：scale=0.5
    Laplacian(srcImage,dstImage,srcImage.depth(),1,0.5);
    //显示处理结果
    img = QImage((const unsigned char*)
                 (dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),
                 QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_actionScale_3_triggered()
{
    //菜单：Laplacian=>scale=>lsacle=2
    //调用Laplacian函数，设置：scale=2
    Laplacian(srcImage,dstImage,srcImage.depth(),1,2);
    //显示处理结果
    img = QImage((const unsigned char*)
                 (dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),
                 QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_actionDelta_4_triggered()
{
    //菜单：Laplacian=>delta=>ldelta=0
    //调用Laplacian函数，使用delta的默认值
    Laplacian(srcImage,dstImage,srcImage.depth());
    //显示处理结果
    img = QImage((const unsigned char*)
                 (dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),
                 QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_actionDelta_50_triggered()
{
    //菜单：Laplacian=>delta=>ldelta=50
    //调用Laplacian函数，设置：delt=50
    Laplacian(srcImage,dstImage,srcImage.depth(),1,1,50);
    //显示图像处理结果
    img = QImage((const unsigned char*)
                 (dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),
                 QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_actionDelta_100_triggered()
{
    //菜单：Laplacian=>delta=>ldelta=100
    //调用Laplacian函数，设置：delt=100
    Laplacian(srcImage,dstImage,srcImage.depth(),1,1,100);
    //显示图像处理结果
    img = QImage((const unsigned char*)
                 (dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),
                 QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_actionX_triggered()
{
    //菜单：Scharr=>方向=>x
    //    调用Scharr实现边缘检测，计算x方向的导数
    Scharr(srcImage,dstImage,srcImage.depth(),1,0);
    //    显示处理结果图像
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_actionY_triggered()
{
    //菜单：Scharr=>方向=>y
    //    调用Scharr实现边缘检测，计算y方向的导数
    Scharr(srcImage,dstImage,srcImage.depth(),0,1);
    //    显示处理结果图像
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_actionX_y_triggered()
{
    Scharr(srcImage,dstImage,srcImage.depth(),0,0);
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_actionSscale_1_triggered()
{
    //菜单：Scharr=>scale=>sscale=1
    //    调用Scharr实现边缘检测，scale设置为1.
    Scharr(srcImage,dstImage,srcImage.depth(),0,1,1);
    //    显示处理结果图像
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_actionSscale_0_5_triggered()
{
    //菜单：Scharr=>scale=>sscale=0.5
    //    调用Scharr实现边缘检测，scale设置为0.5.
    Scharr(srcImage,dstImage,srcImage.depth(),0,1,0.5);
    //    显示处理结果图像
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_actionSscale_2_triggered()
{
    //菜单：Scharr=>scale=>sscale=2
    //    调用Scharr实现边缘检测，scale设置为2.
    Scharr(srcImage,dstImage,srcImage.depth(),0,1,2);
    //    显示处理结果图像
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_actionSdelta_0_triggered()
{
    //菜单：Scharr=>delta=>sdelta=0
    //    调用Scharr实现边缘检测，delta采用默认值，为0.
    Scharr(srcImage,dstImage,srcImage.depth(),0,1,1);
    //    显示处理结果图像
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_actionSdelta_50_triggered()
{
    //菜单：Scharr=>delta=>sdelta=50
    //    调用Scharr实现边缘检测，delta=50.
    Scharr(srcImage,dstImage,srcImage.depth(),0,1,1,50);
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_actionSdelta_100_triggered()
{
    //菜单：Scharr=>delta=>sdelta=100
    //    调用Scharr实现边缘检测，delta=100.
    Scharr(srcImage,dstImage,srcImage.depth(),0,1,1,100);
    //显示处理结果图像
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}



void MainWindow::on_action_triggered()
{

}

void MainWindow::on_Clear_triggered()
{
    //菜单：文件=>清除
    //清除标签1的内容。
    ui->label1->clear();
    //清除标签2的内容。
    ui->label2->clear();
}
