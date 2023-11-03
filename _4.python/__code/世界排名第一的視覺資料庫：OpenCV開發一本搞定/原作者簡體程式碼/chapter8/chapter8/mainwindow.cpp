#include "mainwindow.h"
#include "ui_mainwindow.h"
#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QString>
#include <QFileDialog>
#include <QMessageBox>
#include <opencv/cv.h>
#include <QTextCodec>
#include <math.h>
#include <QInputDialog>
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
        msgBox.setText(tr("默认的测试文件不存在，可以用以下两种方式的一种：1）复制一个文件到当前目录下，并命名为lena.jpg. 2)使用自定义方式打开一个自定义文件。"));
        msgBox.exec();
    }
    else
    {
        cv::cvtColor(srcImage,srcImage,COLOR_BGR2RGB);
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
        msgBox.setText(tr("未找到数据"));
        msgBox.exec();
    }
    else
    {
        cv::cvtColor(srcImage,srcImage,COLOR_BGR2RGB);
        img = QImage((const unsigned char*)(srcImage.data),srcImage.cols,srcImage.rows, srcImage.cols*srcImage.channels(), QImage::Format_RGB888);
        ui->label1->clear();
        img=  img.scaled(ui->label1->width(), ui->label1->height());
        ui->label1->setPixmap(QPixmap::fromImage(img));
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
    QMessageBox::information(this,"版权",tr("本软件版权所有者为：李立宗。如果使用，请联系：lilizong@gmail.com"));
}

void MainWindow::on_about_triggered()
{
    QMessageBox::information(this,"关于",tr("本软件当前版本为1.0，由李立宗等人开发。如果有问题，欢迎联系：lilizong@gmail.com"));
    return;
}

void MainWindow::on_action_triggered()
{

}
void MainWindow::showLabel(Mat m, QLabel *l)
{
    //在label上显示彩色图像
    //   cv::cvtColor(m,m,COLOR_BGR2RGB);
    img = QImage((const unsigned char*)(m.data),m.cols,m.rows,m.cols*m.channels(), QImage::Format_RGB888);
    l->clear();
    img=img.scaled(l->width(),l->height());
    l->setPixmap(QPixmap::fromImage(img));
}
void MainWindow::showLabelGray(Mat m, QLabel *l)
{
    //在label上显示灰度图像
    //   cv::cvtColor(m,m,COLOR_BGR2RGB);
    Size dsize = Size(l->width(),l->height());
    cv::resize(m, m,dsize);
    img = QImage((const unsigned char*)(m.data),m.cols,m.rows,m.cols*m.channels(), QImage::Format_Indexed8);
    l->clear();
    img=img.scaled(l->width(),l->height());
    l->setPixmap(QPixmap::fromImage(img));
}
void MainWindow::on_embed_triggered()
{
    //盲水印，最低有效位，嵌入过程
    //srcImage=imread("l64.jpg");//测试
    //读取载体图像
    QString filename = QFileDialog::getOpenFileName(this,tr("打开原始图像"),"",tr("Image File(*.bmp *.jpg *.jpeg *.png)"));
    QTextCodec *code = QTextCodec::codecForName("gb18030");
    std::string name = code->fromUnicode(filename).data();
    srcImage = cv::imread(name);
    if(!srcImage.data)
    {
        QMessageBox msgBox;
        msgBox.setText(tr("未找到数据"));
        msgBox.exec();
    }
    //获取图像大小
    int MM,NN;
    MM=srcImage.rows;
    NN=srcImage.cols;
    //拆分不同的色彩空间
    Mat bgr[3];
    split(srcImage, bgr);
    // cv::cvtColor(srcImage,srcImage,COLOR_BGR2RGB);
    //cvtColor( srcImage,srcImage, COLOR_RGB2GRAY );
    //读取水印图像
    filename = QFileDialog::getOpenFileName(this,tr("打开水印图像"),"",tr("Image File(*.bmp *.jpg *.jpeg *.png)"));
    //*code = QTextCodec::codecForName("gb18030");
    name = code->fromUnicode(filename).data();
    wmImage=imread(name,IMREAD_UNCHANGED );
    if(!wmImage.data)
    {
        QMessageBox msgBox;
        msgBox.setText(tr("未找到数据"));
        msgBox.exec();
    }
    //cvtColor( wmImage,wmImage, COLOR_RGB2GRAY );  //先转换成灰度图像
    Mat wmImageShow;  //该Mat专门用来显示用。
    // threshold(wmImage,wmImageShow, 127, 255, THRESH_BINARY );
    wmImage.copyTo(wmImageShow);
    //将图像转换为二值图像，即将图像内原来为255的像素点调整为1.
    threshold(wmImage,wmImage, 127, 1, THRESH_BINARY );   //保留最低位有效位LSB即可。
    //生成掩码图像，其值为254，即二进制的“1111 1110”。
    //Mat temp=Mat::ones(MM,NN,CV_8UC1);
    Mat t(MM,NN,CV_8UC1,254);
    t.copyTo(embedSrc);
    //将bgr[0]与t进行按位与，只保留bgr[0]的高7位，最低位置零
    cv::bitwise_and(bgr[0],t,embedSrc);
    //将水印图像嵌入到载体图像的最低位
    cv::bitwise_or(embedSrc,wmImage,embedSrc);
    //Mat t2(MM,NN,CV_8UC1,1);
    // cv::bitwise_and(embedSrc,t2,ExtractWM);
    //将含水印图像赋给bgr[0]
    embedSrc.copyTo(bgr[0]);
    //组合RGB图像
    merge(bgr,3, embedSrc);
    //  threshold(ExtractWM,ExtractWM, 0, 255, THRESH_BINARY );
    //完成色彩空间转换
    cv::cvtColor(srcImage,srcImage,COLOR_BGR2RGB);
    cv::cvtColor(embedSrc,embedSrc,COLOR_BGR2RGB);
    //cv::cvtColor(srcImage,srcImage,COLOR_BGR2RGB);
    //显示载体图像
    showLabel(srcImage,ui->label1);
    //显示水印图像
    showLabelGray(wmImageShow,ui->label2);
    //显示含水印图像
    showLabel(embedSrc,ui->label3);
    //保存含水印图像
    QString fileName = QFileDialog::getSaveFileName(this,
                                                    tr("保存含水印图像"),
                                                    "",
                                                    tr("image (*.bmp)"));  //需要保存为bmp格式，如果是其他格式，可能无法解密。
    Mat m(srcImage.size(),CV_8UC3);
    embedSrc.copyTo(m);
    img = QImage((const unsigned char*)(m.data),m.cols,m.rows,m.cols*m.channels(), QImage::Format_RGB888);
    img.save(fileName);
}

void MainWindow::on_extract_triggered()
{
    //盲水印，最低有效位，提取过程
    //读取含水印图像
    QString filename = QFileDialog::getOpenFileName(this,tr("打开含水印图像"),"",tr("Image File(*.bmp *.jpg *.jpeg *.png)"));
    QTextCodec *code = QTextCodec::codecForName("gb18030");
    std::string name = code->fromUnicode(filename).data();
    srcImage = cv::imread(name);
    if(!srcImage.data)
    {
        QMessageBox msgBox;
        msgBox.setText(tr("未找到数据"));
        msgBox.exec();
    }
    //srcImage=imread("a.bmp");  //测试用
    //获取图像大小
    int MM,NN;
    MM=srcImage.rows;
    NN=srcImage.cols;
    //分离图像色彩空间
    Mat bgr[3];
    split(srcImage, bgr);
    //定义掩码图像，该图像的值为1，即二进制的”0000 0001“
    Mat t(MM,NN,CV_8UC1,1);
    Mat embedSrcExtract;
    t.copyTo(embedSrcExtract);
    //将t与bgr[0]按位与，值保留rgb[0]的最低位
    cv::bitwise_and(bgr[0],t,ExtractWM);
    //定义一个t2，其值为254，即二进制的”1111 1110“
    Mat t2(MM,NN,CV_8UC1,254);
    //将bgr[0]与t2按位与，实现提取bgr[0]的高7位，即将水印剔除
    cv::bitwise_and(bgr[0],t2,bgr[0]);
    //合并RGB色彩空间
    merge(bgr,3, embedSrcExtract);
    //embedSrc色彩空间转换
    cv::cvtColor(embedSrcExtract,embedSrcExtract,COLOR_BGR2RGB);
    //将提取出来的水印图像，只有0和1两个值，将1转换为255.
    threshold(ExtractWM,ExtractWM, 0, 255, THRESH_BINARY );
    //显示读取的含水印图像
    showLabel(embedSrcExtract,ui->label4);
    //显示提取出来的水印图像
    showLabelGray(ExtractWM,ui->label5);
    /*
    //可以显示原始载体图像。
    //srcImage色彩空间转换
    cv::cvtColor(srcImage,srcImage,COLOR_BGR2RGB);
    //显示计算得到的不含水印的载体图像
    showLabel(embedSrc,ui->label4);
    */
}

void MainWindow::on_NEmbed_triggered()
{
    //非盲水印，最低有效位，嵌入过程
    srcImage=imread("l64.jpg");
    int MM,NN;
    MM=srcImage.rows;
    NN=srcImage.cols;
    Mat bgr[3];

    split(srcImage, bgr);


    // cv::cvtColor(srcImage,srcImage,COLOR_BGR2RGB);
    //cvtColor( srcImage,srcImage, COLOR_RGB2GRAY );
    wmImage=imread("watermark.bmp",IMREAD_UNCHANGED );

    //cvtColor( wmImage,wmImage, COLOR_RGB2GRAY );  //先转换成灰度图像
    Mat wmImageShow;  //该Mat专门用来显示用。
    // threshold(wmImage,wmImageShow, 127, 255, THRESH_BINARY );
    wmImage.copyTo(wmImageShow);
    threshold(wmImage,wmImage, 127, 1, THRESH_BINARY );   //保留最低位有效位LSB即可。


    //Mat temp=Mat::ones(MM,NN,CV_8UC1);
    Mat t(MM,NN,CV_8UC1,1);
    t.copyTo(embedSrc);
    cv::bitwise_and(bgr[0],t,embedSrc);
    cv::bitwise_xor(embedSrc,wmImage,embedSrc);

    Mat t2(MM,NN,CV_8UC1,254);
    Mat t3;
    t2.copyTo(t3);
    cv::bitwise_and(bgr[0],t2,t3);

    cv::bitwise_xor(t3,embedSrc,embedSrc);


    embedSrc.copyTo(bgr[0]);

    merge(bgr,3, embedSrc);


    cv::cvtColor(srcImage,srcImage,COLOR_BGR2RGB);
    cv::cvtColor(embedSrc,embedSrc,COLOR_BGR2RGB);
    //cv::cvtColor(srcImage,srcImage,COLOR_BGR2RGB);
    showLabel(srcImage,ui->label1);
    showLabelGray(wmImageShow,ui->label2);
    showLabel(embedSrc,ui->label3);

    QString fileName = QFileDialog::getSaveFileName(this,
                                                    tr("保存加密后的图像"),
                                                    "",
                                                    tr("image (*.bmp)"));  //需要保存为bmp格式，如果是其他格式，可能无法解密。
    Mat m(srcImage.size(),CV_8UC3);
    embedSrc.copyTo(m);
    img = QImage((const unsigned char*)(m.data),m.cols,m.rows,m.cols*m.channels(), QImage::Format_RGB888);
    img.save(fileName);

}

void MainWindow::on_NExtract_triggered()
{
    //非盲水印，最低有效位，提取过程
    //读入原始图像,提取其最低有效位
    srcImage=imread("l64.jpg");
    int MM,NN;
    MM=srcImage.rows;
    NN=srcImage.cols;
    Mat bgr[3];
    split(srcImage, bgr);
    Mat t(MM,NN,CV_8UC1,1);
    cv::bitwise_and(bgr[0],t,t);
    //读取含水印图像，提取其最低有效位
    embedSrc=imread("a.bmp");
    split(embedSrc, bgr);
    Mat t2(MM,NN,CV_8UC1,1);
    cv::bitwise_and(bgr[0],t2,t2);
    //将提取的两个最低有效位进行异或
    cv::bitwise_xor(t2,t,ExtractWM);
    threshold(ExtractWM,ExtractWM, 0, 255, THRESH_BINARY );
    //原始载体图像
    cv::cvtColor(srcImage,srcImage,COLOR_BGR2RGB);
    showLabel(srcImage,ui->label4);
    showLabelGray(ExtractWM,ui->label5);
}

void MainWindow::on_Rcolor_triggered()
{
    //分解出R通道
    //继续以RGB形式显示该通道
    //读取要分解的图像
    QString filename = QFileDialog::getOpenFileName(this,tr("打开原始图像"),"",tr("Image File(*.bmp *.jpg *.jpeg *.png)"));
    QTextCodec *code = QTextCodec::codecForName("gb18030");
    std::string name = code->fromUnicode(filename).data();
    srcImage = cv::imread(name);
    if(!srcImage.data)
    {
        QMessageBox msgBox;
        msgBox.setText(tr("未找到数据"));
        msgBox.exec();
    }
    //srcImage=imread("l64.jpg");  //用于测试
    //获取图像大小
    int MM,NN;
    MM=srcImage.rows;
    NN=srcImage.cols;
    //分离通道
    Mat bgr[3];
    split(srcImage, bgr);
    //将BG通道值置为0.
    Mat B(MM,NN,CV_8UC1, Scalar::all(0));
    Mat G(MM,NN,CV_8UC1, Scalar::all(0));
    B.copyTo(bgr[0]);
    G.copyTo(bgr[1]);
    srcImage.copyTo(dstImage);
    merge(bgr,3, dstImage);
    //转换颜色通道顺序，用于显示
    cv::cvtColor(dstImage,dstImage,COLOR_BGR2RGB);
    //显示图像
    showLabel(dstImage,ui->label6);
}

void MainWindow::on_Gcolor_triggered()
{
    //分解出G通道
    //继续以RGB形式显示该通道
    //读取要分解的图像
    QString filename = QFileDialog::getOpenFileName(this,tr("打开原始图像"),"",tr("Image File(*.bmp *.jpg *.jpeg *.png)"));
    QTextCodec *code = QTextCodec::codecForName("gb18030");
    std::string name = code->fromUnicode(filename).data();
    srcImage = cv::imread(name);
    if(!srcImage.data)
    {
        QMessageBox msgBox;
        msgBox.setText(tr("未找到数据"));
        msgBox.exec();
    }
    //srcImage=imread("l64.jpg");  //用于测试
    //获取图像大小
    int MM,NN;
    MM=srcImage.rows;
    NN=srcImage.cols;
    //分离通道
    Mat bgr[3];
    split(srcImage, bgr);
    //将BR通道值置为0.
    Mat B(MM,NN,CV_8UC1, Scalar::all(0));
    Mat R(MM,NN,CV_8UC1, Scalar::all(0));
    B.copyTo(bgr[0]);
    R.copyTo(bgr[2]);
    srcImage.copyTo(dstImage);
    merge(bgr,3, dstImage);
    //转换颜色通道顺序，用于显示
    cv::cvtColor(dstImage,dstImage,COLOR_BGR2RGB);
    //显示图像
    showLabel(dstImage,ui->label6);
}

void MainWindow::on_Bcolor_triggered()
{
    //分解出R通道
    //继续以RGB形式显示该通道
    //读取要分解的图像
    QString filename = QFileDialog::getOpenFileName(this,tr("打开原始图像"),"",tr("Image File(*.bmp *.jpg *.jpeg *.png)"));
    QTextCodec *code = QTextCodec::codecForName("gb18030");
    std::string name = code->fromUnicode(filename).data();
    srcImage = cv::imread(name);
    if(!srcImage.data)
    {
        QMessageBox msgBox;
        msgBox.setText(tr("未找到数据"));
        msgBox.exec();
    }
    //srcImage=imread("l64.jpg");  //用于测试
    //获取图像大小
    int MM,NN;
    MM=srcImage.rows;
    NN=srcImage.cols;
    //分离通道
    Mat bgr[3];
    split(srcImage, bgr);
    //将GR通道值置为0.
    Mat G(MM,NN,CV_8UC1, Scalar::all(0));
    Mat R(MM,NN,CV_8UC1, Scalar::all(0));
    G.copyTo(bgr[1]);
    R.copyTo(bgr[2]);
    srcImage.copyTo(dstImage);
    merge(bgr,3, dstImage);
    //转换颜色通道顺序，用于显示
    cv::cvtColor(dstImage,dstImage,COLOR_BGR2RGB);
    //显示图像
    showLabel(dstImage,ui->label6);
}

void MainWindow::on_Rgrey_triggered()
{
    //分解出R通道
    //继续以RGB形式显示该通道
    //读取要分解的图像
    QString filename = QFileDialog::getOpenFileName(this,tr("打开原始图像"),"",tr("Image File(*.bmp *.jpg *.jpeg *.png)"));
    QTextCodec *code = QTextCodec::codecForName("gb18030");
    std::string name = code->fromUnicode(filename).data();
    srcImage = cv::imread(name);
    if(!srcImage.data)
    {
        QMessageBox msgBox;
        msgBox.setText(tr("未找到数据"));
        msgBox.exec();
    }
    //srcImage=imread("l64.jpg");  //用于测试
    //分解图像
    Mat bgr[3];
    split(srcImage, bgr);
    //将分解出的图像以灰度图像形式显示
    showLabelGray(bgr[2],ui->label6);
}

void MainWindow::on_Ggrey_triggered()
{
    //分解出G通道
    //继续以RGB形式显示该通道
    //读取要分解的图像
    QString filename = QFileDialog::getOpenFileName(this,tr("打开原始图像"),"",tr("Image File(*.bmp *.jpg *.jpeg *.png)"));
    QTextCodec *code = QTextCodec::codecForName("gb18030");
    std::string name = code->fromUnicode(filename).data();
    srcImage = cv::imread(name);
    if(!srcImage.data)
    {
        QMessageBox msgBox;
        msgBox.setText(tr("未找到数据"));
        msgBox.exec();
    }
    //srcImage=imread("l64.jpg");  //用于测试
    //分解图像
    Mat bgr[3];
    split(srcImage, bgr);
    //将分解出的图像以灰度图像形式显示
    showLabelGray(bgr[1],ui->label6);
}

void MainWindow::on_Bgrey_triggered()
{
    //分解出B通道
    //继续以RGB形式显示该通道
    //读取要分解的图像
    QString filename = QFileDialog::getOpenFileName(this,tr("打开原始图像"),"",tr("Image File(*.bmp *.jpg *.jpeg *.png)"));
    QTextCodec *code = QTextCodec::codecForName("gb18030");
    std::string name = code->fromUnicode(filename).data();
    srcImage = cv::imread(name);
    if(!srcImage.data)
    {
        QMessageBox msgBox;
        msgBox.setText(tr("未找到数据"));
        msgBox.exec();
    }
    //srcImage=imread("l64.jpg");  //用于测试
    //分解图像
    Mat bgr[3];
    split(srcImage, bgr);
    //将分解出的图像以灰度图像形式显示
    showLabelGray(bgr[0],ui->label6);
}




void MainWindow::on_BRembed_triggered()
{
    //盲水印，随机位置嵌入水印信息
    //读取载体图像
    QString filename = QFileDialog::getOpenFileName(this,tr("打开原始载体图像"),"",tr("Image File(*.bmp *.jpg *.jpeg *.png)"));
    QTextCodec *code = QTextCodec::codecForName("gb18030");
    std::string name = code->fromUnicode(filename).data();
    srcImage = cv::imread(name);
    if(!srcImage.data)
    {
        QMessageBox msgBox;
        msgBox.setText(tr("未找到数据"));
        msgBox.exec();
    }
    // srcImage=imread("l64.jpg");
    //获取图像大小
    int M,N;
    M=srcImage.rows;
    N=srcImage.cols;
    //图像通道分解
    Mat bgr[3];
    split(srcImage, bgr);
    //读入水印图像；
    filename = QFileDialog::getOpenFileName(this,tr("打开水印图像"),"",tr("Image File(*.bmp *.jpg *.jpeg *.png)"));
    name = code->fromUnicode(filename).data();
    wmImage = cv::imread(name,IMREAD_UNCHANGED);
    if(!wmImage.data)
    {
        QMessageBox msgBox;
        msgBox.setText(tr("未找到数据"));
        msgBox.exec();
    }
    //wmImage=imread("watermark.bmp",IMREAD_UNCHANGED );
    //cvtColor( wmImage,wmImage, COLOR_RGB2GRAY );  //先转换成灰度图像
    Mat wmImageShow;  //该Mat专门用来显示用。
    wmImage.copyTo(wmImageShow);
    //调整二值水印图像，将其中的值由255调整为1
    threshold(wmImage,wmImage, 127, 1, THRESH_BINARY );   //保留最低位有效位LSB即可。
    //生成混沌序列，用来决定水印嵌入在哪一位。混沌序列chaoticInt的值为0~7
    float chaoticF[M*N];
    //混沌系统初始值
    double t;
    bool isOK;
    QString text=QInputDialog::getText(NULL, "混沌初始值",
                                       "请输入初始值",
                                       QLineEdit::Normal,
                                       "0.98",
                                       &isOK);
    if(isOK)
    {
        t=text.toDouble();
    }
    else
        t=0.98;
    chaoticF[0]=t;
    //chaoticF[0]=0.991;
    //生成混沌序列
    int i=0,j=0;
    for(i=1;i<M*N;i++)
        chaoticF[i]=1-2.0*chaoticF[i-1]*chaoticF[i-1];
    //生成嵌入位置序列，该序列内的值为[0,7)
    int chaoticInt[M*N];
    for(i=0;i<M*N;i++)
        chaoticInt[i]=abs((int)(chaoticF[i]*10000)%8);
    //chaoticInt[i]=abs((int)(chaoticF[i]*10000)%8)+1;   //位置从1开始计算。
    /*
    //测试一下值
    for(i=0;i<M*N;i=i+100)
       QMessageBox::about(NULL,"number",QString::number( chaoticInt[i]));
    */
    //m.at<uchar>(i,j)
    //嵌入水印
    //将特定位与水印信息进行比较。
    //相同则什么都不做。
    //如果不同，存在两种情况。
    //情况1：载体图像指定位置为1，将该位的1置为0，通过将该像素值减去2^n实现。
    //情况2：载体图像指定位置为0，将该位的0置为1，通过将该像素值加上2^n实现。
    int flag=0;   //flag用来标记嵌入位置序列中的元素位置
    int n;            //n用来标记要嵌入的是第几位
    for(i=0;i<M;i++)
        for(j=0;j<N;j++)
        {
            n=chaoticInt[flag];
            if(((bgr[0].at<uchar>(i,j)>>n)%2)!=wmImage.at<uchar>(i,j))
                if(((bgr[0].at<uchar>(i,j)>>n)%2)==1)
                    bgr[0].at<uchar>(i,j)=bgr[0].at<uchar>(i,j)-pow(2,n);
                else
                    bgr[0].at<uchar>(i,j)=bgr[0].at<uchar>(i,j)+pow(2,n);
            flag++;
        }
    //合并通道。
    merge(bgr,3, embedSrc);
    //通道顺序转换
    cv::cvtColor(srcImage,srcImage,COLOR_BGR2RGB);
    cv::cvtColor(embedSrc,embedSrc,COLOR_BGR2RGB);
    //显示原始载体图像
    showLabel(srcImage,ui->label1);
    //显示水印图像
    showLabelGray(wmImageShow,ui->label2);
    //显示完成嵌入后的水印
    showLabel(embedSrc,ui->label3);
    //保存图像
    QString fileName = QFileDialog::getSaveFileName(this,
                                                    tr("保存加密后的图像"),
                                                    "",
                                                    tr("image (*.bmp)"));  //需要保存为bmp格式，如果是其他格式，可能无法解密。
    Mat m(srcImage.size(),CV_8UC3);
    embedSrc.copyTo(m);
    img = QImage((const unsigned char*)(m.data),m.cols,m.rows,m.cols*m.channels(), QImage::Format_RGB888);
    img.save(fileName);
}

void MainWindow::on_BRextract_triggered()
{
    //盲水印，随机位置提取水印信息
    //读取载体图像
    QString filename = QFileDialog::getOpenFileName(this,tr("打开含水印图像"),"",tr("Image File(*.bmp *.jpg *.jpeg *.png)"));
    QTextCodec *code = QTextCodec::codecForName("gb18030");
    std::string name = code->fromUnicode(filename).data();
    srcImage = cv::imread(name);
    if(!srcImage.data)
    {
        QMessageBox msgBox;
        msgBox.setText(tr("未找到数据"));
        msgBox.exec();
    }
    //srcImage=imread("a.bmp");  //用于测试。
    //获取图像大小
    int M,N;
    M=srcImage.rows;
    N=srcImage.cols;
    //分解RGB通道
    Mat bgr[3];
    split(srcImage, bgr);
    //生成混沌序列，用来决定水印嵌入在哪一位。混沌序列chaoticInt的值为0~7
    float chaoticF[M*N];
    double t;
    bool isOK;
    //获取混沌初始值。
    QString text=QInputDialog::getText(NULL, "混沌初始值",
                                       "请输入初始值",
                                       QLineEdit::Normal,
                                       "0.98",
                                       &isOK);
    if(isOK)
    {
        t=text.toDouble();
    }
    else
        t=0.98;
    chaoticF[0]=t;
    //chaoticF[0]=0.991;   //测试
    int i=0,j=0;
    for(i=1;i<M*N;i++)
        chaoticF[i]=1-2.0*chaoticF[i-1]*chaoticF[i-1];
    int chaoticInt[M*N];
    //得到
    for(i=0;i<M*N;i++)
        chaoticInt[i]=abs((int)(chaoticF[i]*10000)%8);   //最低位是0位，最高位是7位。
    //chaoticInt[i]=abs((int)(chaoticF[i]*10000)%8)+1;   //最低位是1位，最高位是8位。
    /*
    //测试一下值
    for(i=0;i<M*N;i=i+100)
       QMessageBox::about(NULL,"number",QString::number( chaoticInt[i]));
    */
    //m.at<uchar>(i,j)
    //提取水印
    //将R通道赋给ExtractWM
    bgr[0].copyTo(ExtractWM);
    //flag是混沌序列的索引序号
    int flag=0;
    //n是chaoticInt内的值，用来表示需要提取的位置。
    int n;
    //提取水印
    for(i=0;i<M;i++)
        for(j=0;j<N;j++)
        {
            n=chaoticInt[flag];
            ExtractWM.at<uchar>(i,j)=(bgr[0].at<uchar>(i,j)>>n)%2;
            flag++;
        }
    //二进制值转换为0和255两个值。
    threshold(ExtractWM,ExtractWM, 0, 255, THRESH_BINARY );
    //显示提取出水印信息
    showLabelGray(ExtractWM,ui->label5);
    //进行色彩通道的顺序转换
    cv::cvtColor(srcImage,srcImage,COLOR_BGR2RGB);
    //显示读取的含水印载体图像
    showLabel(srcImage,ui->label4);
    //将提取出来的水印图像作为RGB图像保存
    QString fileName = QFileDialog::getSaveFileName(this,
                                                    tr("保存提取出来的水印图像"),
                                                    "",
                                                    tr("image (*.bmp)"));  //保存为bmp格式
    cvtColor(ExtractWM,ExtractWM,COLOR_GRAY2RGB);
    Mat m(ExtractWM.size(),CV_8UC3);
    ExtractWM.copyTo(m);
    img = QImage((const unsigned char*)(m.data),m.cols,m.rows,m.cols*m.channels(), QImage::Format_RGB888);
    img.save(fileName);
}

void MainWindow::on_NBRembed_triggered()
{
    //非盲水印，随机位置嵌入水印信息
    srcImage=imread("l64.jpg");
    int M,N;
    M=srcImage.rows;
    N=srcImage.cols;
    Mat bgr[3];

    split(srcImage, bgr);


    // cv::cvtColor(srcImage,srcImage,COLOR_BGR2RGB);
    //cvtColor( srcImage,srcImage, COLOR_RGB2GRAY );
    wmImage=imread("watermark.bmp",IMREAD_UNCHANGED );

    //cvtColor( wmImage,wmImage, COLOR_RGB2GRAY );  //先转换成灰度图像
    Mat wmImageShow;  //该Mat专门用来显示用。
    // threshold(wmImage,wmImageShow, 127, 255, THRESH_BINARY );
    wmImage.copyTo(wmImageShow);
    threshold(wmImage,wmImage, 127, 1, THRESH_BINARY );   //保留最低位有效位LSB即可。

    //生成混沌序列，用来决定水印嵌入在哪一位。混沌序列chaoticInt的值为0~7
    float chaoticF[M*N];
    chaoticF[0]=0.991;
    int i=0,j=0;
    for(i=1;i<M*N;i++)
        chaoticF[i]=1-2.0*chaoticF[i-1]*chaoticF[i-1];
    int chaoticInt[M*N];
    for(i=0;i<M*N;i++)
        chaoticInt[i]=abs((int)(chaoticF[i]*10000)%8);
    //chaoticInt[i]=abs((int)(chaoticF[i]*10000)%7)+1;

    /*
    //测试一下值
    for(i=0;i<M*N;i=i+100)
       QMessageBox::about(NULL,"number",QString::number( chaoticInt[i]));
    */
    //m.at<uchar>(i,j)
    //嵌入水印
    //将特定位与水印信息进行比较。
    int flag=0;
    int n;
    for(i=0;i<M;i++)
        for(j=0;j<N;j++)
        {
            n=chaoticInt[flag];
            if(((bgr[0].at<uchar>(i,j)>>n)%2)==1&&wmImage.at<uchar>(i,j)==1)
                bgr[0].at<uchar>(i,j)=bgr[0].at<uchar>(i,j)-pow(2,n);
            else if(((bgr[0].at<uchar>(i,j)>>n)%2)==0&&wmImage.at<uchar>(i,j)==1)    //必须使用else if，如果直接使用if，则会造成重复改变。
                bgr[0].at<uchar>(i,j)=bgr[0].at<uchar>(i,j)+pow(2,n);

            flag++;
        }


    merge(bgr,3, embedSrc);
    cv::cvtColor(srcImage,srcImage,COLOR_BGR2RGB);
    cv::cvtColor(embedSrc,embedSrc,COLOR_BGR2RGB);
    //cv::cvtColor(srcImage,srcImage,COLOR_BGR2RGB);
    showLabel(srcImage,ui->label1);
    showLabelGray(wmImageShow,ui->label2);
    showLabel(embedSrc,ui->label3);
    QString fileName = QFileDialog::getSaveFileName(this,
                                                    tr("保存加密后的图像"),
                                                    "",
                                                    tr("image (*.bmp)"));  //需要保存为bmp格式，如果是其他格式，可能无法解密。
    Mat m(srcImage.size(),CV_8UC3);
    embedSrc.copyTo(m);
    img = QImage((const unsigned char*)(m.data),m.cols,m.rows,m.cols*m.channels(), QImage::Format_RGB888);
    img.save(fileName);
}

void MainWindow::on_NBRextract_triggered()
{
    //非盲水印，随机位置提取水印信息
    srcImage=imread("l64.jpg");
    int M,N;
    M=srcImage.rows;
    N=srcImage.cols;
    Mat bgr[3];
    split(srcImage, bgr);
    embedSrc=imread("a.bmp");
    Mat bgrWM[3];

    split(embedSrc, bgrWM);
    //生成混沌序列，用来决定水印嵌入在哪一位。混沌序列chaoticInt的值为0~7
    float chaoticF[M*N];
    chaoticF[0]=0.991;
    int i=0,j=0;
    for(i=1;i<M*N;i++)
        chaoticF[i]=1-2.0*chaoticF[i-1]*chaoticF[i-1];
    int chaoticInt[M*N];
    for(i=0;i<M*N;i++)
        chaoticInt[i]=abs((int)(chaoticF[i]*10000)%8);
    //chaoticInt[i]=abs((int)(chaoticF[i]*10000)%7)+1;

    /*
    //测试一下值
    for(i=0;i<M*N;i=i+100)
       QMessageBox::about(NULL,"number",QString::number( chaoticInt[i]));
    */
    //m.at<uchar>(i,j)




    //提取水印
    bgr[0].copyTo(ExtractWM);
    int flag=0;
    int n;
    for(i=0;i<M;i++)
        for(j=0;j<N;j++)
        {
            n=chaoticInt[flag];
            ExtractWM.at<uchar>(i,j)=((bgr[0].at<uchar>(i,j)>>n)%2)^((bgrWM[0].at<uchar>(i,j)>>n)%2);
            flag++;
        }
    threshold(ExtractWM,ExtractWM, 0, 255, THRESH_BINARY );

    showLabelGray(ExtractWM,ui->label5);
    //显示读取的含水印载体图像
    cv::cvtColor( embedSrc, embedSrc,COLOR_BGR2RGB);
    showLabel( embedSrc,ui->label4);
    /*
    Mat t(MM,NN,CV_8UC1,1);
    t.copyTo(embedSrc);
    cv::bitwise_and(bgr[0],t,ExtractWM);
    Mat t2(MM,NN,CV_8UC1,254);
    cv::bitwise_and(bgr[0],t2,bgr[0]);
    merge(bgr,3, embedSrc);
    cv::cvtColor(embedSrc,embedSrc,COLOR_BGR2RGB);
    threshold(ExtractWM,ExtractWM, 0, 255, THRESH_BINARY );
    cv::cvtColor(srcImage,srcImage,COLOR_BGR2RGB);
    showLabel(embedSrc,ui->label4);
    showLabelGray(ExtractWM,ui->label5);
    */
}

void MainWindow::on_zero_triggered()
{
    //读入原始图像,提取其第0位（最低有效位）
    QString filename = QFileDialog::getOpenFileName(this,tr("打开原始图像"),"",tr("Image File(*.bmp *.jpg *.jpeg *.png)"));
    QTextCodec *code = QTextCodec::codecForName("gb18030");
    std::string name = code->fromUnicode(filename).data();
    srcImage = cv::imread(name);
    if(!srcImage.data)
    {
        QMessageBox msgBox;
        msgBox.setText(tr("未找到数据"));
        msgBox.exec();
    }
    //srcImage=imread("l64.jpg");  //用于测试
    //获取原始图像的大小
    int MM,NN;
    MM=srcImage.rows;
    NN=srcImage.cols;
    //分解图像
    Mat bgr[3];
    split(srcImage, bgr);
    //建立一个掩码图像，其值均为1,即二进制的“0000 0001”。
    Mat t(MM,NN,CV_8UC1,1);
    //将掩码图像与各个通道进行按位与，得到各个通道的第1位（最低有效位）
    cv::bitwise_and(bgr[0],t,bgr[0]);
    cv::bitwise_and(bgr[1],t,bgr[1]);
    cv::bitwise_and(bgr[2],t,bgr[2]);
    //阈值化，将大于0的值调整为255，以便于显示。
    threshold(bgr[0],bgr[0], 0, 255, THRESH_BINARY );
    threshold(bgr[1],bgr[1], 0, 255, THRESH_BINARY );
    threshold(bgr[2],bgr[2], 0, 255, THRESH_BINARY );
    //组合各个通道
    merge(bgr,3, dstImage);
    //threshold(dstImage,dstImage, 0, 255, THRESH_BINARY );
    //调整通道顺序
    cv::cvtColor(dstImage,dstImage,COLOR_BGR2RGB);
    //显示图像
    showLabel(dstImage,ui->label6);
}

void MainWindow::on_one_triggered()
{
    //读入原始图像,提取其第1位
    QString filename = QFileDialog::getOpenFileName(this,tr("打开原始图像"),"",tr("Image File(*.bmp *.jpg *.jpeg *.png)"));
    QTextCodec *code = QTextCodec::codecForName("gb18030");
    std::string name = code->fromUnicode(filename).data();
    srcImage = cv::imread(name);
    if(!srcImage.data)
    {
        QMessageBox msgBox;
        msgBox.setText(tr("未找到数据"));
        msgBox.exec();
    }
    //srcImage=imread("l64.jpg");  //用于测试
    //获取原始图像的大小
    int MM,NN;
    MM=srcImage.rows;
    NN=srcImage.cols;
    //分解图像
    Mat bgr[3];
    split(srcImage, bgr);
    //建立一个掩码图像，其值均为2,即为二进制的“0000 0010”。
    Mat t(MM,NN,CV_8UC1,2);
    //将掩码图像与各个通道进行按位与，得到各个通道的第2位
    cv::bitwise_and(bgr[0],t,bgr[0]);
    cv::bitwise_and(bgr[1],t,bgr[1]);
    cv::bitwise_and(bgr[2],t,bgr[2]);
    //阈值化，将大于0的值调整为255，以便于显示。
    threshold(bgr[0],bgr[0], 0, 255, THRESH_BINARY );
    threshold(bgr[1],bgr[1], 0, 255, THRESH_BINARY );
    threshold(bgr[2],bgr[2], 0, 255, THRESH_BINARY );
    //组合各个通道
    merge(bgr,3, dstImage);
    //threshold(dstImage,dstImage, 0, 255, THRESH_BINARY );
    //调整通道顺序
    cv::cvtColor(dstImage,dstImage,COLOR_BGR2RGB);
    //显示图像
    showLabel(dstImage,ui->label6);
}

void MainWindow::on_two_triggered()
{
    //读入原始图像,提取其第2位
    QString filename = QFileDialog::getOpenFileName(this,tr("打开原始图像"),"",tr("Image File(*.bmp *.jpg *.jpeg *.png)"));
    QTextCodec *code = QTextCodec::codecForName("gb18030");
    std::string name = code->fromUnicode(filename).data();
    srcImage = cv::imread(name);
    if(!srcImage.data)
    {
        QMessageBox msgBox;
        msgBox.setText(tr("未找到数据"));
        msgBox.exec();
    }
    //srcImage=imread("l64.jpg");  //用于测试
    //获取原始图像的大小
    int MM,NN;
    MM=srcImage.rows;
    NN=srcImage.cols;
    //分解图像
    Mat bgr[3];
    split(srcImage, bgr);
    //建立一个掩码图像，其值均为4,即为二进制的“0000 0100”。
    Mat t(MM,NN,CV_8UC1,4);
    //将掩码图像与各个通道进行按位与，得到各个通道的第3位
    cv::bitwise_and(bgr[0],t,bgr[0]);
    cv::bitwise_and(bgr[1],t,bgr[1]);
    cv::bitwise_and(bgr[2],t,bgr[2]);
    //阈值化，将大于0的值调整为255，以便于显示。
    threshold(bgr[0],bgr[0], 0, 255, THRESH_BINARY );
    threshold(bgr[1],bgr[1], 0, 255, THRESH_BINARY );
    threshold(bgr[2],bgr[2], 0, 255, THRESH_BINARY );
    //组合各个通道
    merge(bgr,3, dstImage);
    //threshold(dstImage,dstImage, 0, 255, THRESH_BINARY );
    //调整通道顺序
    cv::cvtColor(dstImage,dstImage,COLOR_BGR2RGB);
    //显示图像
    showLabel(dstImage,ui->label6);
}

void MainWindow::on_three_triggered()
{
    //读入原始图像,提取其第3位
    QString filename = QFileDialog::getOpenFileName(this,tr("打开原始图像"),"",tr("Image File(*.bmp *.jpg *.jpeg *.png)"));
    QTextCodec *code = QTextCodec::codecForName("gb18030");
    std::string name = code->fromUnicode(filename).data();
    srcImage = cv::imread(name);
    if(!srcImage.data)
    {
        QMessageBox msgBox;
        msgBox.setText(tr("未找到数据"));
        msgBox.exec();
    }
    //srcImage=imread("l64.jpg");  //用于测试
    //获取原始图像的大小
    int MM,NN;
    MM=srcImage.rows;
    NN=srcImage.cols;
    //分解图像
    Mat bgr[3];
    split(srcImage, bgr);
    //建立一个掩码图像，其值均为8,即为二进制的“0000 1000”。
    Mat t(MM,NN,CV_8UC1,8);
    //将掩码图像与各个通道进行按位与，得到各个通道的第4位
    cv::bitwise_and(bgr[0],t,bgr[0]);
    cv::bitwise_and(bgr[1],t,bgr[1]);
    cv::bitwise_and(bgr[2],t,bgr[2]);
    //阈值化，将大于0的值调整为255，以便于显示。
    threshold(bgr[0],bgr[0], 0, 255, THRESH_BINARY );
    threshold(bgr[1],bgr[1], 0, 255, THRESH_BINARY );
    threshold(bgr[2],bgr[2], 0, 255, THRESH_BINARY );
    //组合各个通道
    merge(bgr,3, dstImage);
    //threshold(dstImage,dstImage, 0, 255, THRESH_BINARY );
    //调整通道顺序
    cv::cvtColor(dstImage,dstImage,COLOR_BGR2RGB);
    //显示图像
    showLabel(dstImage,ui->label6);
}

void MainWindow::on_four_triggered()
{
    //读入原始图像,提取其第4位
    QString filename = QFileDialog::getOpenFileName(this,tr("打开原始图像"),"",tr("Image File(*.bmp *.jpg *.jpeg *.png)"));
    QTextCodec *code = QTextCodec::codecForName("gb18030");
    std::string name = code->fromUnicode(filename).data();
    srcImage = cv::imread(name);
    if(!srcImage.data)
    {
        QMessageBox msgBox;
        msgBox.setText(tr("未找到数据"));
        msgBox.exec();
    }
    //srcImage=imread("l64.jpg");  //用于测试
    //获取原始图像的大小
    int MM,NN;
    MM=srcImage.rows;
    NN=srcImage.cols;
    //分解图像
    Mat bgr[3];
    split(srcImage, bgr);
    //建立一个掩码图像，其值均为16,即为二进制的“0001 0000”。
    Mat t(MM,NN,CV_8UC1,16);
    //将掩码图像与各个通道进行按位与，得到各个通道的第5位
    cv::bitwise_and(bgr[0],t,bgr[0]);
    cv::bitwise_and(bgr[1],t,bgr[1]);
    cv::bitwise_and(bgr[2],t,bgr[2]);
    //阈值化，将大于0的值调整为255，以便于显示。
    threshold(bgr[0],bgr[0], 0, 255, THRESH_BINARY );
    threshold(bgr[1],bgr[1], 0, 255, THRESH_BINARY );
    threshold(bgr[2],bgr[2], 0, 255, THRESH_BINARY );
    //组合各个通道
    merge(bgr,3, dstImage);
    //threshold(dstImage,dstImage, 0, 255, THRESH_BINARY );
    //调整通道顺序
    cv::cvtColor(dstImage,dstImage,COLOR_BGR2RGB);
    //显示图像
    showLabel(dstImage,ui->label6);
}

void MainWindow::on_five_triggered()
{
    //读入原始图像,提取其第5位
    QString filename = QFileDialog::getOpenFileName(this,tr("打开原始图像"),"",tr("Image File(*.bmp *.jpg *.jpeg *.png)"));
    QTextCodec *code = QTextCodec::codecForName("gb18030");
    std::string name = code->fromUnicode(filename).data();
    srcImage = cv::imread(name);
    if(!srcImage.data)
    {
        QMessageBox msgBox;
        msgBox.setText(tr("未找到数据"));
        msgBox.exec();
    }
    //srcImage=imread("l64.jpg");  //用于测试
    //获取原始图像的大小
    int MM,NN;
    MM=srcImage.rows;
    NN=srcImage.cols;
    //分解图像
    Mat bgr[3];
    split(srcImage, bgr);
    //建立一个掩码图像，其值均为32,即为二进制的“0010 0000”。
    Mat t(MM,NN,CV_8UC1,32);
    //将掩码图像与各个通道进行按位与，得到各个通道的第6位
    cv::bitwise_and(bgr[0],t,bgr[0]);
    cv::bitwise_and(bgr[1],t,bgr[1]);
    cv::bitwise_and(bgr[2],t,bgr[2]);
    //阈值化，将大于0的值调整为255，以便于显示。
    threshold(bgr[0],bgr[0], 0, 255, THRESH_BINARY );
    threshold(bgr[1],bgr[1], 0, 255, THRESH_BINARY );
    threshold(bgr[2],bgr[2], 0, 255, THRESH_BINARY );
    //组合各个通道
    merge(bgr,3, dstImage);
    //threshold(dstImage,dstImage, 0, 255, THRESH_BINARY );
    //调整通道顺序
    cv::cvtColor(dstImage,dstImage,COLOR_BGR2RGB);
    //显示图像
    showLabel(dstImage,ui->label6);
}

void MainWindow::on_six_triggered()
{
    //读入原始图像,提取其第6位
    QString filename = QFileDialog::getOpenFileName(this,tr("打开原始图像"),"",tr("Image File(*.bmp *.jpg *.jpeg *.png)"));
    QTextCodec *code = QTextCodec::codecForName("gb18030");
    std::string name = code->fromUnicode(filename).data();
    srcImage = cv::imread(name);
    if(!srcImage.data)
    {
        QMessageBox msgBox;
        msgBox.setText(tr("未找到数据"));
        msgBox.exec();
    }
    //srcImage=imread("l64.jpg");  //用于测试
    //获取原始图像的大小
    int MM,NN;
    MM=srcImage.rows;
    NN=srcImage.cols;
    //分解图像
    Mat bgr[3];
    split(srcImage, bgr);
    //建立一个掩码图像，其值均为64,即为二进制的“0100 0000”。
    Mat t(MM,NN,CV_8UC1,64);
    //将掩码图像与各个通道进行按位与，得到各个通道的第7位
    cv::bitwise_and(bgr[0],t,bgr[0]);
    cv::bitwise_and(bgr[1],t,bgr[1]);
    cv::bitwise_and(bgr[2],t,bgr[2]);
    //阈值化，将大于0的值调整为255，以便于显示。
    threshold(bgr[0],bgr[0], 0, 255, THRESH_BINARY );
    threshold(bgr[1],bgr[1], 0, 255, THRESH_BINARY );
    threshold(bgr[2],bgr[2], 0, 255, THRESH_BINARY );
    //组合各个通道
    merge(bgr,3, dstImage);
    //threshold(dstImage,dstImage, 0, 255, THRESH_BINARY );
    //调整通道顺序
    cv::cvtColor(dstImage,dstImage,COLOR_BGR2RGB);
    //显示图像
    showLabel(dstImage,ui->label6);
}

void MainWindow::on_seven_triggered()
{
    //读入原始图像,提取其第7位
    QString filename = QFileDialog::getOpenFileName(this,tr("打开原始图像"),"",tr("Image File(*.bmp *.jpg *.jpeg *.png)"));
    QTextCodec *code = QTextCodec::codecForName("gb18030");
    std::string name = code->fromUnicode(filename).data();
    srcImage = cv::imread(name);
    if(!srcImage.data)
    {
        QMessageBox msgBox;
        msgBox.setText(tr("未找到数据"));
        msgBox.exec();
    }
    //srcImage=imread("l64.jpg");  //用于测试
    //获取原始图像的大小
    int MM,NN;
    MM=srcImage.rows;
    NN=srcImage.cols;
    //分解图像
    Mat bgr[3];
    split(srcImage, bgr);
    //建立一个掩码图像，其值均为128,即为二进制的“1000 0000”。
    Mat t(MM,NN,CV_8UC1,128);
    //将掩码图像与各个通道进行按位与，得到各个通道的第8位（最高位）
    cv::bitwise_and(bgr[0],t,bgr[0]);
    cv::bitwise_and(bgr[1],t,bgr[1]);
    cv::bitwise_and(bgr[2],t,bgr[2]);
    //阈值化，将大于0的值调整为255，以便于显示。
    threshold(bgr[0],bgr[0], 0, 255, THRESH_BINARY );
    threshold(bgr[1],bgr[1], 0, 255, THRESH_BINARY );
    threshold(bgr[2],bgr[2], 0, 255, THRESH_BINARY );
    //组合各个通道
    merge(bgr,3, dstImage);
    //threshold(dstImage,dstImage, 0, 255, THRESH_BINARY );
    //调整通道顺序
    cv::cvtColor(dstImage,dstImage,COLOR_BGR2RGB);
    //显示图像
    showLabel(dstImage,ui->label6);
}


//*******************调整序号前！***************************
void MainWindow::on_first_triggered()
{

}

void MainWindow::on_second_triggered()
{

}

void MainWindow::on_third_triggered()
{

}

void MainWindow::on_fourth_triggered()
{

}

void MainWindow::on_fifth_triggered()
{

}

void MainWindow::on_sixth_triggered()
{

}

void MainWindow::on_seventh_triggered()
{

}

void MainWindow::on_eighth_triggered()
{

}
//*******************调整序号前！***************************

void MainWindow::on_zeroGray_triggered()
{
    //当n=0时，掩码图像中的值即为二进制的“0000 0001”。
    //图像srcImage与掩码图像进行按位与运算，得到图像srcImage的第0层。
    GrayBitImage(0);
}

void MainWindow::on_oneGray_triggered()
{
    //当n=1时，掩码图像中的值即为二进制的“0000 0010”。
    //图像srcImage与掩码图像进行按位与运算，得到图像srcImage的第1层。
    GrayBitImage(1);
}

void MainWindow::on_twoGray_triggered()
{
    //当n=2时，掩码图像中的值即为二进制的“0000 0100”。
    //图像srcImage与掩码图像进行按位与运算，得到图像srcImage的第2层。
    GrayBitImage(2);
}

void MainWindow::on_threeGray_triggered()
{
    //当n=3时，掩码图像中的值即为二进制的“0000 1000”。
    //图像srcImage与掩码图像进行按位与运算，得到图像srcImage的第3层。
    GrayBitImage(3);
}

void MainWindow::on_fourGray_triggered()
{
    //当n=4时，掩码图像中的值即为二进制的“0001 0000”。
    //图像srcImage与掩码图像进行按位与运算，得到图像srcImage的第4位。
    GrayBitImage(4);
}

void MainWindow::on_fiveGray_triggered()
{
    //当n=5时，掩码图像中的值即为二进制的“0010 0000”。
    //图像srcImage与掩码图像进行按位与运算，得到图像srcImage的第5位。
    GrayBitImage(5);
}

void MainWindow::on_sixGray_triggered()
{
    //当n=6时，掩码图像中的值即为二进制的“0100 0000”。
    //图像srcImage与掩码图像进行按位与运算，得到图像srcImage的第7位。
    GrayBitImage(6);
}

void MainWindow::on_sevenGray_triggered()
{
    //当n=7时，掩码图像中的值即为二进制的“1000 0000”。
    //图像srcImage与掩码图像进行按位与运算，得到图像srcImage的第8位。
    GrayBitImage(7);
}
void MainWindow::GrayBitImage(int n)
{
    //先将图像转换为灰度图像，然后提取第1层
    QString filename = QFileDialog::getOpenFileName(this,tr("打开原始图像"),"",tr("Image File(*.bmp *.jpg *.jpeg *.png)"));
    QTextCodec *code = QTextCodec::codecForName("gb18030");
    std::string name = code->fromUnicode(filename).data();
    srcImage = cv::imread(name);
    if(!srcImage.data)
    {
        QMessageBox msgBox;
        msgBox.setText(tr("未找到数据"));
        msgBox.exec();
    }
    //srcImage=imread("l64.jpg");  //用于测试
    //获取原始图像的大小
    int MM,NN;
    MM=srcImage.rows;
    NN=srcImage.cols;
    //色彩空间转换
    cv::cvtColor(srcImage,srcImage,COLOR_BGR2GRAY);
    //建立一个掩码图像，其值均为2^n,
    //当n=0时，即为二进制的“0000 0001”。与掩码图像进行按位与运算，得到图像srcImage的第1层。
    //当n=1时，即为二进制的“0000 0010”。与掩码图像进行按位与运算，得到图像srcImage的第2层。
    //当n=2时，即为二进制的“0000 0100”。与掩码图像进行按位与运算，得到图像srcImage的第3层。
    //当n=3时，即为二进制的“0000 1000”。与掩码图像进行按位与运算，得到图像srcImage的第4层。
    //当n=4时，即为二进制的“0001 0000”。与掩码图像进行按位与运算，得到图像srcImage的第5位。
    //当n=5时，即为二进制的“0010 0000”。与掩码图像进行按位与运算，得到图像srcImage的第6位。
    //当n=6时，即为二进制的“0100 0000”。与掩码图像进行按位与运算，得到图像srcImage的第7位。
    //当n=7时，即为二进制的“1000 0000”。与掩码图像进行按位与运算，得到图像srcImage的第8位。
    Mat t(MM,NN,CV_8UC1,pow(2,n));
    //与掩码图像进行按位与运算，得到图像srcImage的第1位（最低有效位）。
    cv::bitwise_and(srcImage,t,dstImage);
    //将图像内非零值转换为255以方便显示。
    threshold(dstImage,dstImage, 0, 255, THRESH_BINARY );
    //显示图像。
    showLabelGray(dstImage,ui->label6);
}
//*********************调整序号前***********************************
void MainWindow::on_firstGray_triggered()
{

}

void MainWindow::on_secondGray_triggered()
{

}

void MainWindow::on_thirdGray_triggered()
{

}

void MainWindow::on_fourthGray_triggered()
{

}

void MainWindow::on_fifthGray_triggered()
{

}

void MainWindow::on_sixthGray_triggered()
{

}

void MainWindow::on_seventhGray_triggered()
{

}

void MainWindow::on_eighthGray_triggered()
{

}
//*********************调整序号前***********************************
