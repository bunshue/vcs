#include "mainwindow.h"
#include "ui_mainwindow.h"
#include "mainwindow.h"
#include "ui_mainwindow.h"
#include "time.h"
#include <QString>
#include <QFileDialog>
#include <QMessageBox>
#include <opencv/cv.h>
#include <QTextCodec>
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
        img = QImage((const unsigned char*)(srcImage.data),srcImage.cols,srcImage.rows, srcImage.cols*srcImage.channels(), QImage::Format_RGB888);
        ui->label1->clear();
        img=  img.scaled(ui->label1->width(), ui->label1->height());
        ui->label1->setPixmap(QPixmap::fromImage(img));
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
    }
}

void MainWindow::on_restoreFile_triggered()
//復原功能
{
    //將srcImage賦給dstImage
    srcImage.copyTo(dstImage);
    //將dst賦給img
    img = QImage((const unsigned char*)
                 (dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),
                 QImage::Format_RGB888);
    //調整img大小
    img=img.scaled(ui->label1->size());
    //在label2內顯示img
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

void MainWindow::on_actionTest_triggered()
{


}

void MainWindow::on_tu1_triggered()
{
    //注意一點即可，雕刻中，浮雕（凸雕）是右下角的點減去左上角的點
    //雕刻，凹雕，是左上角的點減去右下角的點。
    //嘗試使用多種模式去看雕刻的效果。
    //改變的模式內含：最後加的像素值不同；右上角、左上角點選取不同
    Mat dst(srcImage.size(),CV_8UC3);
    for (int i=1; i<srcImage.rows-1; i++)
    {
        uchar *current = srcImage.ptr<uchar>(i);
        uchar *currentBefore = srcImage.ptr<uchar>(i-1);
        //   uchar *currentNext = srcImage.ptr<uchar>(i+1);
        uchar *dstLine = dst.ptr<uchar>(i);
        for (int j=1; j<srcImage.cols-1; j++)
        {
            for (int k=0; k<3; k++)
            {
                int tmp0 = current[3*j+k]-currentBefore[3*(j-1)+k]+128;//此處與其他不同，浮雕1
                if (tmp0<0)
                    dstLine[3*j+k]=0;
                else if(tmp0>255)
                    dstLine[3*j+k]=255;
                else
                    dstLine[3*j+k]=tmp0;
            }
        }
    }
    dst.copyTo(dstImage);
    showLabel(dstImage,ui->label2);
}
void MainWindow::showLabel(Mat m, QLabel *l)
//在標簽l內顯示m
{
    //將m賦給img
    img = QImage((const unsigned char*)(m.data),m.cols,m.rows,m.cols*m.channels(), QImage::Format_RGB888);
    //清理用於顯示的標簽
    l->clear();
    //調整img大小
    img=img.scaled(l->width(),l->height());
    //顯示
    l->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_tu2_triggered()
{
    //注意一點即可，雕刻中，浮雕（凸雕）是右下角的點減去左上角的點
    //雕刻，凹雕，是左上角的點減去右下角的點。
    //嘗試使用多種模式去看雕刻的效果。
    //改變的模式內含：最後加的像素值不同；右上角、左上角點選取不同
    Mat dst(srcImage.size(),CV_8UC3);
    for (int i=1; i<srcImage.rows-1; i++)
    {
        //    uchar *current = srcImage.ptr<uchar>(i);
        uchar *currentBefore = srcImage.ptr<uchar>(i-1);
        uchar *currentNext = srcImage.ptr<uchar>(i+1);
        uchar *dstLine = dst.ptr<uchar>(i);
        for (int j=1; j<srcImage.cols-1; j++)
        {
            for (int k=0; k<3; k++)
            {
                int tmp0 = currentNext[3*(j+1)+k]-currentBefore[3*(j-1)+k]+128;//此處與其他不同，浮雕2
                if (tmp0<0)
                    dstLine[3*j+k]=0;
                else if(tmp0>255)
                    dstLine[3*j+k]=255;
                else
                    dstLine[3*j+k]=tmp0;
            }
        }
    }
    dst.copyTo(dstImage);
    showLabel(dstImage,ui->label2);
}

void MainWindow::on_tu3_triggered()
{
    //注意一點即可，雕刻中，浮雕（凸雕）是右下角的點減去左上角的點
    //雕刻，凹雕，是左上角的點減去右下角的點。
    //嘗試使用多種模式去看雕刻的效果。
    //改變的模式內含：最後加的像素值不同；右上角、左上角點選取不同
    Mat dst(srcImage.size(),CV_8UC3);
    for (int i=1; i<srcImage.rows-1; i++)
    {
        //      uchar *current = srcImage.ptr<uchar>(i);
        uchar *currentBefore = srcImage.ptr<uchar>(i-1);
        uchar *currentNext = srcImage.ptr<uchar>(i+1);
        uchar *dstLine = dst.ptr<uchar>(i);
        for (int j=1; j<srcImage.cols-1; j++)
        {
            for (int k=0; k<3; k++)
            {
                int tmp0 = currentNext[3*(j+1)+k]-currentBefore[3*(j-1)+k]+200;//此處與其他不同，浮雕3
                if (tmp0<0)
                    dstLine[3*j+k]=0;
                else if(tmp0>255)
                    dstLine[3*j+k]=255;
                else
                    dstLine[3*j+k]=tmp0;
            }
        }
    }
    dst.copyTo(dstImage);
    showLabel(dstImage,ui->label2);
}

void MainWindow::on_tu4_triggered()
{
    //注意一點即可，雕刻中，浮雕（凸雕）是右下角的點減去左上角的點
    //雕刻，凹雕，是左上角的點減去右下角的點。
    //嘗試使用多種模式去看雕刻的效果。
    //改變的模式內含：最後加的像素值不同；右上角、左上角點選取不同
    Mat dst(srcImage.size(),CV_8UC3);
    for (int i=1; i<srcImage.rows-1; i++)
    {
        //     uchar *current = srcImage.ptr<uchar>(i);
        uchar *currentBefore = srcImage.ptr<uchar>(i-1);
        uchar *currentNext = srcImage.ptr<uchar>(i+1);
        uchar *dstLine = dst.ptr<uchar>(i);
        for (int j=1; j<srcImage.cols-1; j++)
        {
            for (int k=0; k<3; k++)
            {
                int tmp0 = currentNext[3*(j+1)+k]-currentBefore[3*(j-1)+k]+80;//此處與其他不同，浮雕4
                if (tmp0<0)
                    dstLine[3*j+k]=0;
                else if(tmp0>255)
                    dstLine[3*j+k]=255;
                else
                    dstLine[3*j+k]=tmp0;
            }
        }
    }
    dst.copyTo(dstImage);
    showLabel(dstImage,ui->label2);
}

void MainWindow::on_aoA_triggered()
{
    //注意一點即可，雕刻中，浮雕（凸雕）是右下角的點減去左上角的點
    //雕刻，凹雕，是左上角的點減去右下角的點。
    //嘗試使用多種模式去看雕刻的效果。
    //改變的模式內含：最後加的像素值不同；右上角、左上角點選取不同
    Mat dst(srcImage.size(),CV_8UC3);
    for (int i=1; i<srcImage.rows-1; i++)
    {
        uchar *current = srcImage.ptr<uchar>(i);
        uchar *currentBefore = srcImage.ptr<uchar>(i-1);
        //   uchar *currentNext = srcImage.ptr<uchar>(i+1);
        uchar *dstLine = dst.ptr<uchar>(i);
        for (int j=1; j<srcImage.cols-1; j++)
        {
            for (int k=0; k<3; k++)
            {
                int tmp0 = currentBefore[3*(j-1)+k]-current[3*j+k]+128;//此處與其他不同，凹雕1
                if (tmp0<0)
                    dstLine[3*j+k]=0;
                else if(tmp0>255)
                    dstLine[3*j+k]=255;
                else
                    dstLine[3*j+k]=tmp0;
            }
        }
    }
    dst.copyTo(dstImage);
    showLabel(dstImage,ui->label2);
}

void MainWindow::on_aoB_triggered()
{
    //注意一點即可，雕刻中，浮雕（凸雕）是右下角的點減去左上角的點
    //雕刻，凹雕，是左上角的點減去右下角的點。
    //嘗試使用多種模式去看雕刻的效果。
    //改變的模式內含：最後加的像素值不同；右上角、左上角點選取不同
    Mat dst(srcImage.size(),CV_8UC3);
    for (int i=1; i<srcImage.rows-1; i++)
    {
        //       uchar *current = srcImage.ptr<uchar>(i);
        uchar *currentBefore = srcImage.ptr<uchar>(i-1);
        uchar *currentNext = srcImage.ptr<uchar>(i+1);
        uchar *dstLine = dst.ptr<uchar>(i);
        for (int j=1; j<srcImage.cols-1; j++)
        {
            for (int k=0; k<3; k++)
            {
                int tmp0 = currentBefore[3*(j-1)+k]-currentNext[3*(j+1)+k]+128;//此處與其他不同，凹雕2
                if (tmp0<0)
                    dstLine[3*j+k]=0;
                else if(tmp0>255)
                    dstLine[3*j+k]=255;
                else
                    dstLine[3*j+k]=tmp0;
            }
        }
    }
    dst.copyTo(dstImage);
    showLabel(dstImage,ui->label2);
}

void MainWindow::on_aoC_triggered()
{
    //注意一點即可，雕刻中，浮雕（凸雕）是右下角的點減去左上角的點
    //雕刻，凹雕，是左上角的點減去右下角的點。
    //嘗試使用多種模式去看雕刻的效果。
    //改變的模式內含：最後加的像素值不同；右上角、左上角點選取不同
    Mat dst(srcImage.size(),CV_8UC3);
    for (int i=1; i<srcImage.rows-1; i++)
    {
        uchar *current = srcImage.ptr<uchar>(i);
        uchar *currentBefore = srcImage.ptr<uchar>(i-1);
        //     uchar *currentNext = srcImage.ptr<uchar>(i+1);
        uchar *dstLine = dst.ptr<uchar>(i);
        for (int j=1; j<srcImage.cols-1; j++)
        {
            for (int k=0; k<3; k++)
            {
                int tmp0 = currentBefore[3*(j+1)+k]-current[3*(j-1)+k]+128;//此處與其他不同，凹雕3
                if (tmp0<0)
                    dstLine[3*j+k]=0;
                else if(tmp0>255)
                    dstLine[3*j+k]=255;
                else
                    dstLine[3*j+k]=tmp0;
            }
        }
    }
    dst.copyTo(dstImage);
    showLabel(dstImage,ui->label2);
}

void MainWindow::on_aoD_triggered()
{
    //注意一點即可，雕刻中，浮雕（凸雕）是右下角的點減去左上角的點
    //雕刻，凹雕，是左上角的點減去右下角的點。
    //嘗試使用多種模式去看雕刻的效果。
    //改變的模式內含：最後加的像素值不同；右上角、左上角點選取不同
    Mat dst(srcImage.size(),CV_8UC3);
    for (int i=1; i<srcImage.rows-1; i++)
    {
        uchar *current = srcImage.ptr<uchar>(i);
        uchar *currentBefore = srcImage.ptr<uchar>(i-1);
        //      uchar *currentNext = srcImage.ptr<uchar>(i+1);
        uchar *dstLine = dst.ptr<uchar>(i);
        for (int j=1; j<srcImage.cols-1; j++)
        {
            for (int k=0; k<3; k++)
            {
                int tmp0 = currentBefore[3*(j)+k]-current[3*(j-1)+k]+128;//此處與其他不同，凹雕4
                if (tmp0<0)
                    dstLine[3*j+k]=0;
                else if(tmp0>255)
                    dstLine[3*j+k]=255;
                else
                    dstLine[3*j+k]=tmp0;
            }
        }
    }
    dst.copyTo(dstImage);
    showLabel(dstImage,ui->label2);
}

void MainWindow::on_action_triggered()
//老照片效果
{
    Mat dstImage(srcImage.size(),CV_8UC3);
    //定義一個圖形，用來儲存最後的處理效果，內定變數
    for (int i=1; i<srcImage.rows-1; i++)
    {
        uchar *p0 = srcImage.ptr<uchar>(i);
        uchar *q0 = dstImage.ptr<uchar>(i);
        for (int j=1; j<srcImage.cols-1; j++)
        {
            int srcB=p0[3*j];
            int srcG=p0[3*j+1];
            int srcR=p0[3*j+2];
            int dstR,dstG,dstB;
            dstR = (101 * srcR + 197 * srcG + 48 * srcB) >> 8;
            dstG = (89 * srcR + 176 * srcG + 43 * srcB) >> 8;
            dstB = (70 * srcR + 137 * srcG + 34 * srcB) >> 8;
            dstR=dstR>255?255:dstR;
            dstG=dstG>255?255:dstG;
            dstB=dstB>255?255:dstB;
            q0[3*j]=dstB;
            q0[3*j+1]=dstG;
            q0[3*j+2]=dstR;
        }
    }
    showLabel(dstImage,ui->label2);
}

void MainWindow::on_action_2_triggered()
{
    //這裡指的是，老照片的紅綠互換。
    Mat dstImage(srcImage.size(),CV_8UC3);   //做個重定義，內定變數
    for (int i=1; i<srcImage.rows-1; i++)
    {
        uchar *p0 = srcImage.ptr<uchar>(i);
        uchar *q0 = dstImage.ptr<uchar>(i);
        for (int j=1; j<srcImage.cols-1; j++)
        {
            int srcR=p0[3*j];
            int srcG=p0[3*j+1];
            int srcB=p0[3*j+2];
            int dstR,dstG,dstB;
            dstR = (101 * srcR + 197 * srcG + 48 * srcB) >> 8;
            dstG = (89 * srcR + 176 * srcG + 43 * srcB) >> 8;
            dstB = (70 * srcR + 137 * srcG + 34 * srcB) >> 8;
            dstR=dstR>255?255:dstR;
            dstG=dstG>255?255:dstG;
            dstB=dstB>255?255:dstB;
            q0[3*j]=dstR;
            q0[3*j+1]=dstG;
            q0[3*j+2]=dstB;
        }
    }
    cvtColor(dstImage,dstImage,CV_RGB2BGR);
    showLabel(dstImage,ui->label2);
}

void MainWindow::on_action_3_triggered()
{
    cvtColor(srcImage,dstImage,CV_RGB2GRAY);
    /*  imshow(",",dstImage);
    showLabel(dstImage,ui->label2);
    */
    //因為是灰階圖形，不能使用ShowLabel
    cv::Size    dsize=Size(ui->label2->width(),ui->label2->height());
    cv::resize(dstImage,dstImage,dsize);
    //   cv::cvtColor(m,m,CV_BGR2RGB);
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(), QImage::Format_Indexed8);
    //l.clear();
    ui->label2->clear();
    //img=  img.scaled(l.width(),l.height());
    // img=img.scaled(ui->label2->width(),ui->label2->height());
    //l.setPixmap(QPixmap::fromImage(img));
    ui->label2->setPixmap(QPixmap::fromImage(img));
    //imshow(",",dstImage);
}

void MainWindow::on_action_4_triggered()
{
    cvtColor(srcImage,dstImage,CV_RGB2GRAY);
    /*  imshow(",",dstImage);
    showLabel(dstImage,ui->label2);
    */
    //因為是灰階圖形，不能使用ShowLabel
    threshold(dstImage,dstImage,128,255,0);
    cv::Size    dsize=Size(ui->label2->width(),ui->label2->height());
    cv::resize(dstImage,dstImage,dsize);
    //   cv::cvtColor(m,m,CV_BGR2RGB);
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(), QImage::Format_Indexed8);
    //l.clear();
    ui->label2->clear();
    //img=  img.scaled(l.width(),l.height());
    // img=img.scaled(ui->label2->width(),ui->label2->height());
    //l.setPixmap(QPixmap::fromImage(img));
    ui->label2->setPixmap(QPixmap::fromImage(img));
    //imshow(",",dstImage);
}

void MainWindow::on_woodCarving_triggered()
{
    //木雕效果
    //若果目前點的像素值與臨近任意一點的像素值大於設定值（這裡設定為30），置白色；否則，置黑色
    Mat dst(srcImage.rows,srcImage.cols,CV_8UC1);
    Mat src;
    cvtColor(srcImage,src,CV_RGB2GRAY);
    for (int i=1; i<src.rows-1; i++)
    {
     
        //像素點
        uchar *dstLine = dst.ptr<uchar>(i);
        for (int j=1; j<src.cols-1; j++)
        {
            int a,b,c,d,e,f,g,h;
            a=abs(current[j]-currentBefore[(j-1)]);
            b=abs(current[j]-currentBefore[j]);
            c=abs(current[j]-currentBefore[(j+1)]);
            d=abs(current[j]-currentNext[(j-1)]);
            e=abs(current[j]-currentNext[(j)]);
            f=abs(current[j]-currentNext[(j+1)]);
            g=abs(current[j]-current[(j-1)]);
            h=abs(current[j]-current[(j+1)]);
            /*
            //若果不先進行灰階處理，可以采用如下模式。對每一個RGB分量進行處理。
            for(int k=0;k<3;k++)
            {
                sum+=abs(current[3*j+k]-currentBefore[3*(j-1)+k]);
                sum+=abs(current[3*j+k]-currentBefore[3*j+k]);
                sum+=abs(current[3*j+k]-currentBefore[3*(j+1)+k]);
                sum+=abs(current[3*j+k]-currentNext[3*(j-1)+k]);
                sum+=abs(current[3*j+k]-currentNext[3*(j)+k]);
                sum+=abs(current[3*j+k]-currentNext[3*(j+1)+k]);
                sum+=abs(current[3*j+k]-current[3*(j-1)+k]);
                sum+=abs(current[3*j+k]-current[3*(j+1)+k]);
            }
            */
            if(a>30||b>30||c>30||d>30||e>30||f>30||g>30||h>30)
                dstLine[j]=255;
            else
                dstLine[j]=0;
        }
    }
    cv::Size dsize=Size(ui->label2->width(),ui->label2->height());
    cv::resize(dst,dst,dsize);
    img = QImage((const unsigned char*)(dst.data),dst.cols,dst.rows,dst.cols*dst.channels(), QImage::Format_Indexed8);
    ui->label2->clear();
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_pencil_triggered()
{
    //鉛筆畫
    //若果目前點的像素值與臨近任意一點的像素值大於設定值（這裡設定為30），置黑色；否則，置白色
    //這裡和木雕是相反的動作。
    Mat dst(srcImage.rows,srcImage.cols,CV_8UC1);
    Mat src;
    cvtColor(srcImage,src,CV_RGB2GRAY);
    for (int i=1; i<src.rows-1; i++)
    {
        uchar *current = src.ptr<uchar>(i);
        uchar *currentBefore = src.ptr<uchar>(i-1);
        uchar *currentNext = src.ptr<uchar>(i+1);
        //   uchar *currentNext = srcImage.ptr<uchar>(i+1);
        uchar *dstLine = dst.ptr<uchar>(i);
        for (int j=1; j<src.cols-1; j++)
        {
            int a,b,c,d,e,f,g,h;
            a=abs(current[j]-currentBefore[(j-1)]);
            b=abs(current[j]-currentBefore[j]);
            c=abs(current[j]-currentBefore[(j+1)]);
            d=abs(current[j]-currentNext[(j-1)]);
            e=abs(current[j]-currentNext[(j)]);
            f=abs(current[j]-currentNext[(j+1)]);
            g=abs(current[j]-current[(j-1)]);
            h=abs(current[j]-current[(j+1)]);
            /*
            //若果不先進行灰階處理，可以采用如下模式。對每一個RGB分量進行處理。
            for(int k=0;k<3;k++)
            {
                sum+=abs(current[3*j+k]-currentBefore[3*(j-1)+k]);
                sum+=abs(current[3*j+k]-currentBefore[3*j+k]);
                sum+=abs(current[3*j+k]-currentBefore[3*(j+1)+k]);
                sum+=abs(current[3*j+k]-currentNext[3*(j-1)+k]);
                sum+=abs(current[3*j+k]-currentNext[3*(j)+k]);
                sum+=abs(current[3*j+k]-currentNext[3*(j+1)+k]);
                sum+=abs(current[3*j+k]-current[3*(j-1)+k]);
                sum+=abs(current[3*j+k]-current[3*(j+1)+k]);
            }
            */
            if(a>30||b>30||c>30||d>30||e>30||f>30||g>30||h>30)
                dstLine[j]=0;
            else
                dstLine[j]=255;
        }
    }
    cv::Size    dsize=Size(ui->label2->width(),ui->label2->height());
    cv::resize(dst,dst,dsize);
    img = QImage((const unsigned char*)(dst.data),dst.cols,dst.rows,dst.cols*dst.channels(), QImage::Format_Indexed8);
    ui->label2->clear();
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_sketch_triggered()
{
    //素描
    Mat src;
    srcImage.copyTo(src);
    int width=src.cols;
    int heigh=src.rows;
    Mat gray0,gray1;
    cvtColor(src,gray0,CV_RGB2GRAY);   //灰階處理
    addWeighted(gray0,-1,NULL,0,255,gray1);    //反色
    //threshold(gray0,gray1,128,255,THRESH_BINARY_INV);
    GaussianBlur(gray1,gray1,Size(11,11),0);   //高斯處理一下
    Mat dst(gray1.size(),CV_8UC1);
    for (int y=0; y<heigh; y++)
    {
        uchar* P0  = gray0.ptr<uchar>(y);
        uchar* P1  = gray1.ptr<uchar>(y);
        uchar* P  = dst.ptr<uchar>(y);
        for (int x=0; x<width; x++)
        {
            int tmp0=P0[x];
            int tmp1=P1[x];
            P[x] =(uchar) min((tmp0+(tmp0*tmp1)/(256-tmp1)),255);   //計算
        }
    }
    cv::Size dsize=Size(ui->label2->width(),ui->label2->height());
    cv::resize(dst,dstImage,dsize);
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(), QImage::Format_Indexed8);
    ui->label2->clear();
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_diffuse_triggered()
{
    //擴散，用週邊的一個像素點代替目前的點。
    Mat dst(srcImage.size(),CV_8UC3);
    RNG rng;
    for (int y=1; y<srcImage.rows-1; y++)
    {
        uchar* srcR  = srcImage.ptr<uchar>(y);
        uchar* dstR  = dst.ptr<uchar>(y);
        for (int x=1; x<srcImage.cols-1; x++)
        {
            int myRand=rng.uniform(0,9);
            srand(time(NULL));
            myRand=rand()%9;
            dstR[3*x]=srcImage.at<uchar>(y-1+myRand/3,3*(x-1+myRand%3));
            dstR[3*x+1]=srcImage.at<uchar>(y-1+myRand/3,3*(x-1+myRand%3)+1);
            dstR[3*x+2]=srcImage.at<uchar>(y-1+myRand/3,3*(x-1+myRand%3)+2);
        }
    }
    dst.copyTo(dstImage);
    showLabel(dstImage,ui->label2);
}

void MainWindow::on_blur_triggered()
{
    //模糊
    Mat dst(srcImage.size(),CV_8UC3);
    int tem[3][3] = {1, 2, 1, 2, 4, 2, 1, 2, 1};	//變換陣 * 16
    for (int y=1; y<srcImage.rows-1; y++)
    {
        uchar* srcR  = srcImage.ptr<uchar>(y);
        uchar* dstR  = dst.ptr<uchar>(y);
        int br,bg,bb;
        for (int x=1; x<srcImage.cols-1; x++)
        {
            br=0;
            bg=0;
            bb=0;
            for(int i=-1;i<2;i++)
            {
                for(int j=-1;j<2;j++)
                {
                    br+=srcImage.at<uchar>(y+i,3*(x+j))* tem[i + 1][j + 1];
                    bg+=srcImage.at<uchar>(y+i,3*(x+j)+1)* tem[i + 1][j + 1];
                    bb+=srcImage.at<uchar>(y+i,3*(x+j)+2)* tem[i + 1][j + 1];
                }
            }
            dstR[3*x]=br>>4;
            dstR[3*x+1]= bg>>4;
            dstR[3*x+2]= bb>>4;
        }
    }
    dst.copyTo(dstImage);
    showLabel(dstImage,ui->label2);
}

void MainWindow::on_soft_triggered()
{
    //柔化
    Mat dst(srcImage.size(),CV_8UC3);
    for (int y=2; y<srcImage.rows-2; y++)
    {
        uchar* srcR  = srcImage.ptr<uchar>(y);
        uchar* dstR  = dst.ptr<uchar>(y);
        int br,bg,bb;
        for (int x=2; x<srcImage.cols-2; x++)
        {
            br=0;
            bg=0;
            bb=0;
            for(int i=-2;i<=2;i++)
            {
                for(int j=-2;j<=2;j++)
                {
                    br+=srcImage.at<uchar>(y+i,3*(x+j));
                    bg+=srcImage.at<uchar>(y+i,3*(x+j)+1);
                    bb+=srcImage.at<uchar>(y+i,3*(x+j)+2);
                }
            }
            dstR[3*x]=br/ (4 * 2 * 2 + 4 * 2 + 1);
            dstR[3*x+1]= bg/(4 * 2 * 2 + 4 * 2 + 1);
            dstR[3*x+2]= bb/(4 * 2 * 2 + 4 * 2 + 1);
        }
    }
    dst.copyTo(dstImage);
    showLabel(dstImage,ui->label2);
}

void MainWindow::on_sharp_triggered()
{
    //銳化
    //銳化，搜尋周圍半徑為R範圍內的點，
    //差值 = 目前像素點 - 周圍像素點的平均值
    //本點 = 目前像素點 + 差值 * 銳化系數S
    int R;
    int S;
    R=2;
    S=2;
    Mat dst(srcImage.size(),CV_8UC3);
    for (int y=2; y<srcImage.rows-2; y++)
    {
        uchar* srcR  = srcImage.ptr<uchar>(y);
        uchar* dstR  = dst.ptr<uchar>(y);
        int br,bg,bb;
        for (int x=2; x<srcImage.cols-2; x++)
        {
            br=0;
            bg=0;
            bb=0;
            for(int i=-2;i<=2;i++)
            {
                for(int j=-2;j<=2;j++)
                {
                    if(i == 0 && j == 0) continue;
                    br+=srcImage.at<uchar>(y+i,3*(x+j));
                    bg+=srcImage.at<uchar>(y+i,3*(x+j)+1);
                    bb+=srcImage.at<uchar>(y+i,3*(x+j)+2);
                }
            }
            br=srcImage.at<uchar>(y,3*x)* (1 + S) - br * S / (4 * R * R + 4 * R+1);
            bg=srcImage.at<uchar>(y,3*x+1) * (1 + S) - bg * S / (4 * R * R + 4 * R+1);
            bb=srcImage.at<uchar>(y,3*x+2) * (1 + S) - bb * S / (4 * R * R + 4 * R+1);
            br = br > 255? 255 : br;
            bg = bg > 255? 255 : bg;
            bb = bb > 255? 255 : bb;
            br = br < 0? 0 : br;
            bg = bg < 0? 0 : bg;
            bb = bb < 0? 0 : bb;
            dstR[3*x]=br;
            dstR[3*x+1]= bg;
            dstR[3*x+2]= bb;
        }
    }
    dst.copyTo(dstImage);
    showLabel(dstImage,ui->label2);
}

void MainWindow::on_filterMax_triggered()
{
    //濾鏡，取得周圍點的最大值。
    Mat dst(srcImage.size(),CV_8UC3);
    for (int y=1; y<srcImage.rows-1; y++)
    {
        uchar* srcR  = srcImage.ptr<uchar>(y);
        uchar* dstR  = dst.ptr<uchar>(y);
        int br,bg,bb;
        for (int x=1; x<srcImage.cols-1; x++)
        {
            br=srcR[3*x];
            bg=srcR[3*x+1];
            bb=srcR[3*x+2];
            for(int i=-1;i<=1;i++)
            {
                for(int j=-1;j<=1;j++)
                {
                    br=br>srcImage.at<uchar>(y+i,3*(x+j)+1)?br:srcImage.at<uchar>(y+i,3*(x+j)+1);
                    bg=bg>srcImage.at<uchar>(y+i,3*(x+j)+1)?bg:srcImage.at<uchar>(y+i,3*(x+j)+1);
                    bb=bb>srcImage.at<uchar>(y+i,3*(x+j)+1)?bb:srcImage.at<uchar>(y+i,3*(x+j)+1);
                }
            }
            dstR[3*x]=br;
            dstR[3*x+1]= bg;
            dstR[3*x+2]= bb;
        }
    }
    dst.copyTo(dstImage);
    showLabel(dstImage,ui->label2);
}

void MainWindow::on_filterMin_triggered()
{
    //濾鏡，取得周圍點的最小值。
    //使用lena圖形，結果看起來很像灰階圖形。
    Mat dst(srcImage.size(),CV_8UC3);
    for (int y=2; y<srcImage.rows-2; y++)
    {
        uchar* srcR  = srcImage.ptr<uchar>(y);
        uchar* dstR  = dst.ptr<uchar>(y);
        int br,bg,bb;
        for (int x=2; x<srcImage.cols-2; x++)
        {
            br=srcR[3*x];
            bg=srcR[3*x+1];
            bb=srcR[3*x+2];
            for(int i=-1;i<=1;i++)
            {
                for(int j=-1;j<=1;j++)
                {
                    br=br<srcImage.at<uchar>(y+i,3*(x+j)+1)?br:srcImage.at<uchar>(y+i,3*(x+j)+1);
                    bg=bg<srcImage.at<uchar>(y+i,3*(x+j)+1)?bg:srcImage.at<uchar>(y+i,3*(x+j)+1);
                    bb=bb<srcImage.at<uchar>(y+i,3*(x+j)+1)?bb:srcImage.at<uchar>(y+i,3*(x+j)+1);
                }
            }
            dstR[3*x]=br;
            dstR[3*x+1]= bg;
            dstR[3*x+2]= bb;
        }
    }
    dst.copyTo(dstImage);
    showLabel(dstImage,ui->label2);
}

void MainWindow::on_picBook_triggered()
{
    //連環畫效果。比灰階亮度更明顯。
    /*
     * R = |g – b + g + r| * r / 256
     G = |b – g + b + r| * r / 256;
    B = |b – g + b + r| * g / 256;
    完成後再次進行灰階化處理。
    */
    Mat dst(srcImage.size(),CV_8UC3);
    for (int y=0; y<srcImage.rows; y++)
    {
        uchar* srcR  = srcImage.ptr<uchar>(y);
        uchar* dstR  = dst.ptr<uchar>(y);
        int br,bg,bb;
        float brF,bgF,bbF;
        for (int x=0; x<srcImage.cols; x++)
        {
            br=srcR[3*x];
            bg=srcR[3*x+1];
            bb=srcR[3*x+2];

            brF= (abs(bg - bb + bg + br) * br) >> 8;
            bgF= (abs(bb - bg + bb + br) * br) >> 8;
            bbF= (abs(bb - bg + bb + br) * bg) >> 8;
            brF = brF > 255? 255 : brF;
            bgF = bgF > 255? 255 : bgF;
            bbF = bbF > 255? 255 : bbF;
            brF = brF < 0? 0 : brF;
            bgF = bgF < 0? 0 : bgF;
            bbF = bbF < 0? 0 : bbF;
            dstR[3*x]=(uchar)brF;
            dstR[3*x+1]= (uchar)bgF;
            dstR[3*x+2]= (uchar)bbF;
        }
    }
    //Mat gray;
    cvtColor(dst,dst,CV_BGR2GRAY);
    normalize(dst,dst,255,0,CV_MINMAX);
    cv::Size dsize=Size(ui->label2->width(),ui->label2->height());
    cv::resize(dst,dstImage,dsize);
    //   cv::cvtColor(m,m,CV_BGR2RGB);
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(), QImage::Format_Indexed8);
    ui->label2->clear();
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_colorMap_triggered()
//彩色變換
{
    /*
        enum  	cv::ColormapTypes {
          cv::COLORMAP_AUTUMN = 0,
          cv::COLORMAP_BONE = 1,
          cv::COLORMAP_JET = 2,
          cv::COLORMAP_WINTER = 3,
          cv::COLORMAP_RAINBOW = 4,
          cv::COLORMAP_OCEAN = 5,
          cv::COLORMAP_SUMMER = 6,
          cv::COLORMAP_SPRING = 7,
          cv::COLORMAP_COOL = 8,
          cv::COLORMAP_HSV = 9,
          cv::COLORMAP_PINK = 10,
          cv::COLORMAP_HOT = 11,
          cv::COLORMAP_PARULA = 12
        }
    */
    //定義隨機數
    int myRand;
    srand(time(NULL));
    myRand=rand()%13;
    //定義目的圖形img
    Mat img(srcImage.size(),CV_8UC3);
    //套用函數applyColorMap
    applyColorMap(srcImage,img,myRand);
    //需要包括：#include "opencv2/contrib/contrib.hpp"
    //在label2內顯示img
    showLabel(img,ui->label2);
}

void MainWindow::on_rChanel_triggered()
//分析R通道
//在開啟srcImage時，已經將通道轉為RGB。
{
    //用來儲存三個通道
    Mat dst[3];
    //儲存分析結果
    Mat dstR(srcImage.rows,srcImage.cols,CV_8UC1);
    //分離
    split(srcImage,dst);
    //給予值
    dst[0].copyTo(dstR);
    //這裡需要把分解後的dst[0]賦給dstR。
    //直接定義mat dst[3]，然後分別分析即可。
    cv::Size dsize=Size(ui->label2->width(),ui->label2->height());
    cv::resize(dstR,dstR,dsize);
    img = QImage((const unsigned char*)(dstR.data),dstR.cols,dstR.rows,dstR.cols*dstR.channels(), QImage::Format_Indexed8);
    ui->label2->clear();
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_gChanel_triggered()
//G通道
{
    //定義dst用來儲存三個通道
    Mat dst[3];
    //定義dstG，用來儲存G通道
    Mat dstG(srcImage.rows,srcImage.cols,CV_8UC1);
    split(srcImage,dst);
    dst[1].copyTo(dstG);
    //這裡需要把分解後的dst[1]賦給dstG。
    //直接定義mat dst[3]，然後分別分析即可。
    cv::Size dsize=Size(ui->label2->width(),ui->label2->height());
    cv::resize(dstG,dstG,dsize);
    img = QImage((const unsigned char*)(dstG.data),dstG.cols,dstG.rows,dstG.cols*dstG.channels(), QImage::Format_Indexed8);
    ui->label2->clear();
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_bChanel_triggered()
//B通道
{
    //定義dst用來儲存三個通道
    Mat dst[3];
    //定義dstB用來儲存目的圖形
    Mat dstB(srcImage.rows,srcImage.cols,CV_8UC1);
    split(srcImage,dst);
    dst[2].copyTo(dstB);
    //這裡需要把分解後的dst[2]賦給dstB。
    //直接定義mat dst[3]，然後分別分析即可。
    cv::Size dsize=Size(ui->label2->width(),ui->label2->height());
    cv::resize(dstB,dstB,dsize);
    img = QImage((const unsigned char*)(dstB.data),dstB.cols,dstB.rows,dstB.cols*dstB.channels(), QImage::Format_Indexed8);
    ui->label2->clear();
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_inverse_triggered()
{
    //反相，將每一個像素都用255去減
    Mat dst(srcImage.size(),CV_8UC3);
    for (int y=0; y<srcImage.rows; y++)
    {
        uchar* srcR  = srcImage.ptr<uchar>(y);
        uchar* dstR  = dst.ptr<uchar>(y);
        int br,bg,bb;
        for (int x=0; x<srcImage.cols; x++)
        {
            br=srcR[3*x];
            bg=srcR[3*x+1];
            bb=srcR[3*x+2];

            dstR[3*x]=255-br;
            dstR[3*x+1]= 255-bg;
            dstR[3*x+2]=255-bb;
        }
    }
    showLabel(dst,ui->label2);
}

void MainWindow::on_highLight_triggered()
{
    //強光效果
   
    Mat dst(srcImage.size(),CV_8UC3);
    for (int y=0; y<srcImage.rows; y++)
    {
        uchar* srcR  = srcImage.ptr<uchar>(y);
        uchar* dstR  = dst.ptr<uchar>(y);
        int br,bg,bb;
        for (int x=0; x<srcImage.cols; x++)
        {
            br=srcR[3*x];
            bg=srcR[3*x+1];
            bb=srcR[3*x+2];
            br=br>127.5? br+(255-br)*(br-127.5)/127.5:br*br/127.5;
            br=br>255?255:br;
            br=br<0?0:br;
            bg=bg>127.5? bg+(255-bg)*(bg-127.5)/127.5:bg*bg/127.5;
            bg=bg>255?255:bg;
            bg=bg<0?0:bg;
            bb=bb>127.5? bb+(255-bb)*(bb-127.5)/127.5:bb*bb/127.5;
            bb=bb>255?255:bb;
            bb=bb<0?0:bb;
            dstR[3*x]=br;
            dstR[3*x+1]= bg;
            dstR[3*x+2]=bb;
        }
    }
    showLabel(dst,ui->label2);
}

void MainWindow::on_blackAndWhiteInverse_triggered()
{
    //黑白底片
    Mat dst(srcImage.size(),CV_8UC3);
    for (int y=0; y<srcImage.rows; y++)
    {
        uchar* srcR  = srcImage.ptr<uchar>(y);
        uchar* dstR  = dst.ptr<uchar>(y);
        int br,bg,bb;
        for (int x=0; x<srcImage.cols; x++)
        {
            br=srcR[3*x];
            bg=srcR[3*x+1];
            bb=srcR[3*x+2];

            dstR[3*x]=255-br;
            dstR[3*x+1]= 255-bg;
            dstR[3*x+2]=255-bb;
        }
    }
    cv::cvtColor(dst,dstImage,CV_RGB2GRAY);
    cv::Size    dsize=Size(ui->label2->width(),ui->label2->height());
    cv::resize(dstImage,dstImage,dsize);
    //   cv::cvtColor(m,m,CV_BGR2RGB);
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(), QImage::Format_Indexed8);
    ui->label2->clear();
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_casting_triggered()
{
    //熔鑄
   
    Mat dst(srcImage.size(),CV_8UC3);
    for (int y=0; y<srcImage.rows; y++)
    {
        uchar* srcR  = srcImage.ptr<uchar>(y);
        uchar* dstR  = dst.ptr<uchar>(y);
        int br,bg,bb;
        for (int x=0; x<srcImage.cols; x++)
        {
            br=srcR[3*x];
            bg=srcR[3*x+1];
            bb=srcR[3*x+2];

            br=br*128/(bg+bb +1);
            bg= bg*128/(br+bb +1);
            bb=bb*128/(bg+br +1);

            br = br > 255? 255 : br;
            bg = bg > 255? 255 : bg;
            bb = bb > 255? 255 : bb;

            br = br < 0? 0 : br;
            bg = bg < 0? 0 : bg;
            bb = bb < 0? 0 : bb;

            dstR[3*x]=br;
            dstR[3*x+1]= bg;
            dstR[3*x+2]= bb;
        }
    }
    showLabel(dst,ui->label2);
}

void MainWindow::on_freezing_triggered()
{
    //冰凍
  
    Mat dst(srcImage.size(),CV_8UC3);
    for (int y=0; y<srcImage.rows; y++)
    {
        uchar* srcR  = srcImage.ptr<uchar>(y);
        uchar* dstR  = dst.ptr<uchar>(y);
        float br,bg,bb;
        for (int x=0; x<srcImage.cols; x++)
        {
            br=srcR[3*x];
            bg=srcR[3*x+1];
            bb=srcR[3*x+2];

            br=(br-bg-bb)*3/2;
            bg= (bg-br-bb)*3/2;
            bb=(bb-bg-br)*3/2;

            br = br > 255? 255 : br;
            bg = bg > 255? 255 : bg;
            bb = bb > 255? 255 : bb;

            br = br < 0? -br : br;
            bg = bg < 0? -bg : bg;
            bb = bb < 0? -bb : bb;

            dstR[3*x]=(uchar)br;
            dstR[3*x+1]= (uchar)bg;
            dstR[3*x+2]= (uchar)bb;
        }
    }
    showLabel(dst,ui->label2);
}

void MainWindow::on_oldPic_triggered()
//老照片效果，注意通道順序
//在開啟圖形時已經進行了通道轉換，srcImage內已經是RGB順序呢
{
    //srcImage是讀取的原始圖形
    Mat dstImage(srcImage.size(),CV_8UC3);
    //定義一個圖形，用來儲存最後的處理效果，內定變數
    for (int i=1; i<srcImage.rows-1; i++)
    {
        uchar *p0 = srcImage.ptr<uchar>(i);
        uchar *q0 = dstImage.ptr<uchar>(i);
        for (int j=1; j<srcImage.cols-1; j++)
        {
            int srcR=p0[3*j];
            int srcG=p0[3*j+1];
            int srcB=p0[3*j+2];
            int dstR,dstG,dstB;
            dstR = (101 * srcR + 197 * srcG + 48 * srcB) >> 8;
            dstG = (89 * srcR + 176 * srcG + 43 * srcB) >> 8;
            dstB = (70 * srcR + 137 * srcG + 34 * srcB) >> 8;
            dstR=dstR>255?255:dstR;
            dstG=dstG>255?255:dstG;
            dstB=dstB>255?255:dstB;
            q0[3*j]=dstR;
            q0[3*j+1]=dstG;
            q0[3*j+2]=dstB;
        }
    }
    //自訂函數showLabel
    showLabel(dstImage,ui->label2);
}

void MainWindow::on_exchangeRG_triggered()
//紅綠通道互換,這裡指的是老照片的紅綠互換。
{
    //srcImage是原始圖形，開啟照片時已經將通道進行了調整
    //定義一個目的圖形
    Mat dstImage(srcImage.size(),CV_8UC3);
    for (int i=1; i<srcImage.rows-1; i++)
    {
        uchar *p0 = srcImage.ptr<uchar>(i);
        uchar *q0 = dstImage.ptr<uchar>(i);
        for (int j=1; j<srcImage.cols-1; j++)
        {
            int srcR=p0[3*j];
            int srcG=p0[3*j+1];
            int srcB=p0[3*j+2];
            int dstR,dstG,dstB;
            dstR = (101 * srcR + 197 * srcG + 48 * srcB) >> 8;
            dstG = (89 * srcR + 176 * srcG + 43 * srcB) >> 8;
            dstB = (70 * srcR + 137 * srcG + 34 * srcB) >> 8;
            dstR=dstR>255?255:dstR;
            dstG=dstG>255?255:dstG;
            dstB=dstB>255?255:dstB;
            q0[3*j]=dstR;
            q0[3*j+1]=dstG;
            q0[3*j+2]=dstB;
        }
    }
    //使用cvtColor完成通道交換
    cvtColor(dstImage,dstImage,CV_RGB2BGR);
    showLabel(dstImage,ui->label2);
}

void MainWindow::on_toGray_triggered()
//圖形灰階化
{
    //srcImage是原始圖形
    //dstImage是目的圖形
    cvtColor(srcImage,dstImage,CV_RGB2GRAY);
    //定義dsize，取得label2的大小後將值賦給dsize
    cv::Size dsize=Size(ui->label2->width(),ui->label2->height());
    //調整dstImage大小
    cv::resize(dstImage,dstImage,dsize);
    //給imge給予值
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(), QImage::Format_Indexed8);
    //label2清理
    ui->label2->clear();
    //label2顯示圖形
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_toBin_triggered()
//圖形二值化
{
    //首先進行灰階化處理srcImage是原始圖形，dstImage是處理後圖形
    cvtColor(srcImage,dstImage,CV_RGB2GRAY);
    //設定值處理，二值化
    threshold(dstImage,dstImage,128,255,0);
    //定義dsize，與label2，即右側的標簽大小相等
    cv::Size dsize=Size(ui->label2->width(),ui->label2->height());
    //調整dst圖形大小為dsize
    cv::resize(dstImage,dstImage,dsize);
    //將dstImage賦給imge
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(), QImage::Format_Indexed8);
    //清理label2
    ui->label2->clear();
    //填充label2
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
