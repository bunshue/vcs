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
        msgBox.setWindowTitle(tr("警示"));
        msgBox.setText(tr("預設的測試檔案不存在，可以用以下兩種模式的一種：1）複製一個檔案到目前目錄下，並命名為lena.jpg. 2)使用自訂模式開啟一個自訂檔案。"));
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

void MainWindow::on_actionSobel_triggered()
{
    //選單：邊緣檢驗=>Sobel
    //sobel邊緣檢驗，具有預設值的采用預設參數值
    Sobel(srcImage,dstImage,srcImage.depth(),0,1);
    //顯示處理結果
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_actionCanny_triggered()
{
    //選單：邊緣檢驗=>Canny
    //canny邊緣檢驗，具有預設值的采用預設參數值
    Mat dstImage2;
    //先調整到與標簽等大小。
    cv::resize(srcImage,srcImage,Size(ui->label1->width(), ui->label1->height()),0,0,3);
    //色彩空間轉換
    cvtColor(srcImage,dstImage2,CV_BGR2GRAY);
    //呼叫canny，預設參數
    Canny(dstImage2,dstImage2,30,100);
    //顯示處理結果
    img = QImage((const unsigned char*)(dstImage2.data),dstImage2.cols,dstImage2.rows,dstImage2.step,  QImage::Format_Indexed8);
    //  img=img.scaled(ui->label2->size());  //說明：若果經由canny變換後再調整圖形大小，顯示時會顯示全黑，無法觀看。
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_actionLaplacian_triggered()
{
    //選單：邊緣檢驗=>Laplacian
    //Laplacian邊緣檢驗，具有預設值的采用預設參數值
    Laplacian(srcImage,dstImage,srcImage.depth());
    //顯示處理結果
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}
void MainWindow::on_actionScharr_triggered()
{
    //選單：邊緣檢驗=>Scharr
    //Scharr邊緣檢驗，具有預設值的采用預設參數值
    Scharr(srcImage,dstImage,srcImage.depth(),0,1);
    //顯示處理結果
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}
void MainWindow::on_actionDx_triggered()
{
    //選單：Soble=>方向=>dx
    //呼叫Sobel在x軸方向上動作
    Sobel(srcImage,dstImage,srcImage.depth(),1,0);
    //顯示圖形
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_actionDy_triggered()
{
    //選單：Soble=>方向=>dy
    //呼叫Sobel在y軸方向上動作
    Sobel(srcImage,dstImage,srcImage.depth(),0,1);
    //顯示圖形
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_actionDx_dy_triggered()
{
    //選單：Soble=>方向=>dx&dy
    //呼叫Sobel在x軸&y軸方向上動作
    Sobel(srcImage,dstImage,srcImage.depth(),1,1);
    //顯示圖形
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_action1_triggered()
{
    //選單：Sobel=>ksize大小=>size=1
    //呼叫soble實現，size大小等於1。
    Sobel(srcImage,dstImage,srcImage.depth(),1,1,1);
    //顯示處理結果
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
    //選單：sobel=>scale縮放因子=>scale=1
    //呼叫sobel，設定scale參數值為1
    Sobel(srcImage,dstImage,srcImage.depth(),1,1,7,1);
    //顯示處理效果
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
    //選單：sobel=>delta值=>delta=50
    //soble檢驗、delta=50.
    Sobel(srcImage,dstImage,srcImage.depth(),1,1,7,1,50);
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_actionDelta_0_triggered()
{
    //選單：sobel=>delta值=>delta=0
    //soble檢驗、delta采用預設值0.
    Sobel(srcImage,dstImage,srcImage.depth(),1,1,7,1,0);
    //顯示處理結果圖形
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_actionDelta_2_triggered()
{
    //選單：sobel=>delta值=>delta=100
    Sobel(srcImage,dstImage,srcImage.depth(),1,1,7,1,100);
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
    //  imshow("test",dstImage);
}

void MainWindow::on_action50_triggered()
{
    //選單：canny=>threshold1=>t1=50
    //設定參數threshold1=50的情況下呼叫canny
    Mat srcImage2;   //用於儲存轉換後圖形，直接轉換srcImage發生變換，影響srcImage的後續使用
    //調整大小
    cv::resize(srcImage,srcImage2,Size(ui->label1->width(), ui->label1->height()),0,0,3);
    //色彩空間轉換，彩色=>灰階
    cvtColor(srcImage2,srcImage2,CV_BGR2GRAY);
    //canny檢驗
    Canny(srcImage2,dstImage,50,150);
    //顯示圖形
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.step,  QImage::Format_Indexed8);
    //  img=img.scaled(ui->label2->size());  //說明：若果重設圖形大小會導致全黑，無法觀看。提前將原始圖形進行了縮放。
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_action100_triggered()
{
    //選單：canny=>threshold1=>t1=100
    //設定參數threshold1=100的情況下呼叫canny
    Mat srcImage2;   //用於儲存轉換後圖形，直接轉換srcImage發生變換，影響srcImage的後續使用
    //調整大小
    cv::resize(srcImage,srcImage2,Size(ui->label1->width(), ui->label1->height()),0,0,3);
    //色彩空間轉換，彩色=>灰階
    cvtColor(srcImage2,srcImage2,CV_BGR2GRAY);
    //canny檢驗
    Canny(srcImage2,dstImage,100,150);
    //顯示圖形
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.step,  QImage::Format_Indexed8);
    //  img=img.scaled(ui->label2->size());  //說明：若果重設圖形大小會導致全黑，無法觀看。提前將原始圖形進行了縮放。
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_action150_triggered()
{
    //選單：canny=>threshold2=>t2=150
    //設定參數threshold2=150的情況下呼叫canny
    Mat srcImage2;   //用於儲存轉換後圖形，直接轉換srcImage發生變換，影響srcImage的後續使用
    //調整大小
    cv::resize(srcImage,srcImage2,Size(ui->label1->width(), ui->label1->height()),0,0,3);
    //色彩空間轉換，彩色=>灰階
    cvtColor(srcImage2,srcImage2,CV_BGR2GRAY);
    //canny檢驗
    Canny(srcImage2,dstImage,10,150);
    //顯示圖形
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.step,  QImage::Format_Indexed8);
    //  img=img.scaled(ui->label2->size());  //說明：若果重設圖形大小會導致全黑，無法觀看。提前將原始圖形進行了縮放。
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_action200_triggered()
{
    //選單：canny=>threshold2=>t2=200
    //設定參數threshold2=200的情況下呼叫canny
    Mat srcImage2;   //用於儲存轉換後圖形，直接轉換srcImage發生變換，影響srcImage的後續使用
    //調整大小
    cv::resize(srcImage,srcImage2,Size(ui->label1->width(), ui->label1->height()),0,0,3);
    //色彩空間轉換，彩色=>灰階
    cvtColor(srcImage2,srcImage2,CV_BGR2GRAY);
    //canny檢驗
    Canny(srcImage2,dstImage,10,200);
    //顯示圖形
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.step,  QImage::Format_Indexed8);
    //  img=img.scaled(ui->label2->size());  //說明：若果重設圖形大小會導致全黑，無法觀看。提前將原始圖形進行了縮放。
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_actionAs_1_triggered()
{
    //選單：canny=>apertureSize=>as=5
    //調整大小
    cv::resize(srcImage,dstImage,Size(ui->label1->width(), ui->label1->height()),0,0,3);
    //色彩空間轉換，轉為灰階圖形
    cvtColor(dstImage,dstImage,CV_BGR2GRAY);
    //呼叫canny，apertureSize設定為5.
    Canny(dstImage,dstImage,50,150,5);
    //顯示圖形處理效果
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.step,  QImage::Format_Indexed8);
    //  img=img.scaled(ui->label2->size());  //說明：若果重設圖形大小會導致全黑，無法觀看。提前將原始圖形進行了縮放。
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_actionAs_3_triggered()
{
    //選單：canny=>apertureSize=>as=7
    //調整大小
    cv::resize(srcImage,dstImage,Size(ui->label1->width(), ui->label1->height()),0,0,3);
    //色彩空間轉換，轉為灰階圖形
    cvtColor(dstImage,dstImage,CV_BGR2GRAY);
    //呼叫canny，apertureSize設定為7.
    Canny(dstImage,dstImage,50,150,7);
    //顯示圖形處理效果
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.step,  QImage::Format_Indexed8);
    //  img=img.scaled(ui->label2->size());  //說明：若果重設圖形大小會導致全黑，無法觀看。提前將原始圖形進行了縮放。
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_actionAs_4_triggered()
{
    //選單：canny=>apertureSize=>as=3
    //調整大小
    cv::resize(srcImage,dstImage,Size(ui->label1->width(), ui->label1->height()),0,0,3);
    //色彩空間轉換，轉為灰階圖形
    cvtColor(dstImage,dstImage,CV_BGR2GRAY);
    //呼叫canny，apertureSize設定為3.
    Canny(dstImage,dstImage,50,150,3);
    //顯示圖形處理效果
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.step,  QImage::Format_Indexed8);
    //  img=img.scaled(ui->label2->size());  //說明：若果重設圖形大小會導致全黑，無法觀看。提前將原始圖形進行了縮放。
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_actionFalse_triggered()
{
    //選單： canny=>L2gradient=>false
    //調整大小
    cv::resize(srcImage,dstImage,Size(ui->label1->width(), ui->label1->height()),0,0,3);
    //轉為灰階圖形
    cvtColor(dstImage,dstImage,CV_BGR2GRAY);
    //呼叫Canny函數
    Canny(dstImage,dstImage,50,150);
    //顯示圖形
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.step,  QImage::Format_Indexed8);
    //  img=img.scaled(ui->label2->size());   //說明：若果重設圖形大小會導致全黑，無法觀看。提前將原始圖形進行了縮放。
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_actionTrue_triggered()
{
    //選單： canny=>L2gradient=>true
    //調整大小
    cv::resize(srcImage,dstImage,Size(ui->label1->width(), ui->label1->height()),0,0,3);
    //轉為灰階圖形
    cvtColor(dstImage,dstImage,CV_BGR2GRAY);
    //呼叫Canny函數
    Canny(dstImage,dstImage,50,150,3,true);
    //顯示圖形
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.step,  QImage::Format_Indexed8);
    //  img=img.scaled(ui->label2->size());   //說明：若果重設圖形大小會導致全黑，無法觀看。提前將原始圖形進行了縮放。
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_actionKsize_1_triggered()
{
    //選單：Laplacian=>ksize=>ksize=1
    //呼叫Laplacian函數，使用預設的ksize值
    Laplacian(srcImage,dstImage,srcImage.depth());
    //顯示處理結果
    img = QImage((const unsigned char*)
                 (dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),
                 QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_actionKsize_3_triggered()
{
    //選單：Laplacian=>ksize=>ksize=3
    //呼叫Laplacian函數，顯性設定：ksize=3
    Laplacian(srcImage,dstImage,srcImage.depth(),3);
    //顯示處理結果
    img = QImage((const unsigned char*)
                 (dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),
                 QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_actionKsize_5_triggered()
{
    //選單：Laplacian=>ksize=>ksize=5
    //呼叫Laplacian函數，顯性設定：ksize=5
    Laplacian(srcImage,dstImage,srcImage.depth(),5);
    //顯示處理結果
    img = QImage((const unsigned char*)
                 (dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),
                 QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_actionScale_1_triggered()
{
    //選單：Laplacian=>scale=>lsacle=1
    //呼叫Laplacian函數，使用預設的scale值
    Laplacian(srcImage,dstImage,srcImage.depth());
    //顯示處理結果
    img = QImage((const unsigned char*)
                 (dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),
                 QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_actionScale_0_5_triggered()
{
    //選單：Laplacian=>scale=>lsacle=0.5
    //呼叫Laplacian函數，設定：scale=0.5
    Laplacian(srcImage,dstImage,srcImage.depth(),1,0.5);
    //顯示處理結果
    img = QImage((const unsigned char*)
                 (dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),
                 QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_actionScale_3_triggered()
{
    //選單：Laplacian=>scale=>lsacle=2
    //呼叫Laplacian函數，設定：scale=2
    Laplacian(srcImage,dstImage,srcImage.depth(),1,2);
    //顯示處理結果
    img = QImage((const unsigned char*)
                 (dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),
                 QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_actionDelta_4_triggered()
{
    //選單：Laplacian=>delta=>ldelta=0
    //呼叫Laplacian函數，使用delta的預設值
    Laplacian(srcImage,dstImage,srcImage.depth());
    //顯示處理結果
    img = QImage((const unsigned char*)
                 (dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),
                 QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_actionDelta_50_triggered()
{
    //選單：Laplacian=>delta=>ldelta=50
    //呼叫Laplacian函數，設定：delt=50
    Laplacian(srcImage,dstImage,srcImage.depth(),1,1,50);
    //顯示圖形處理結果
    img = QImage((const unsigned char*)
                 (dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),
                 QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_actionDelta_100_triggered()
{
    //選單：Laplacian=>delta=>ldelta=100
    //呼叫Laplacian函數，設定：delt=100
    Laplacian(srcImage,dstImage,srcImage.depth(),1,1,100);
    //顯示圖形處理結果
    img = QImage((const unsigned char*)
                 (dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),
                 QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_actionX_triggered()
{
    //選單：Scharr=>方向=>x
    //    呼叫Scharr實現邊緣檢驗，計算x方向的導數
    Scharr(srcImage,dstImage,srcImage.depth(),1,0);
    //    顯示處理結果圖形
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_actionY_triggered()
{
    //選單：Scharr=>方向=>y
    //    呼叫Scharr實現邊緣檢驗，計算y方向的導數
    Scharr(srcImage,dstImage,srcImage.depth(),0,1);
    //    顯示處理結果圖形
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
    //選單：Scharr=>scale=>sscale=1
    //    呼叫Scharr實現邊緣檢驗，scale設定為1.
    Scharr(srcImage,dstImage,srcImage.depth(),0,1,1);
    //    顯示處理結果圖形
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_actionSscale_0_5_triggered()
{
    //選單：Scharr=>scale=>sscale=0.5
    //    呼叫Scharr實現邊緣檢驗，scale設定為0.5.
    Scharr(srcImage,dstImage,srcImage.depth(),0,1,0.5);
    //    顯示處理結果圖形
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_actionSscale_2_triggered()
{
    //選單：Scharr=>scale=>sscale=2
    //    呼叫Scharr實現邊緣檢驗，scale設定為2.
    Scharr(srcImage,dstImage,srcImage.depth(),0,1,2);
    //    顯示處理結果圖形
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_actionSdelta_0_triggered()
{
    //選單：Scharr=>delta=>sdelta=0
    //    呼叫Scharr實現邊緣檢驗，delta采用預設值，為0.
    Scharr(srcImage,dstImage,srcImage.depth(),0,1,1);
    //    顯示處理結果圖形
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_actionSdelta_50_triggered()
{
    //選單：Scharr=>delta=>sdelta=50
    //    呼叫Scharr實現邊緣檢驗，delta=50.
    Scharr(srcImage,dstImage,srcImage.depth(),0,1,1,50);
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_actionSdelta_100_triggered()
{
    //選單：Scharr=>delta=>sdelta=100
    //    呼叫Scharr實現邊緣檢驗，delta=100.
    Scharr(srcImage,dstImage,srcImage.depth(),0,1,1,100);
    //顯示處理結果圖形
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),  QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}



void MainWindow::on_action_triggered()
{

}

void MainWindow::on_Clear_triggered()
{
    //選單：檔案=>清除
    //清除標簽1的內容。
    ui->label1->clear();
    //清除標簽2的內容。
    ui->label2->clear();
}
