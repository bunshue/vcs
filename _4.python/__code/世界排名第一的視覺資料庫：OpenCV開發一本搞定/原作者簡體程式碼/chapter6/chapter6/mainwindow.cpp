#include "mainwindow.h"
#include "ui_mainwindow.h"
#include "mainwindow.h"
#include "ui_mainwindow.h"
#include "time.h"
#include "math.h"
#include <QString>
#include <QFileDialog>
#include <QMessageBox>
#include <opencv/cv.h>
#include <QTextCodec>
#include "windows.h"
using namespace cv;
//  版权信息：  lilizong[at]gmail.com
MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    int T[10][3][3]={
        //如果不希望再次处理，可以直接在建立数组时，将1改为255即可。
        //0个白点
        {0,0,0,
         0,0,0,
         0,0,0},
        //1个白点
        {0,0,0,
         0,1,0,
         0,0,0},
        //2个白点
        {1,0,0,
         0,0,0,
         0,0,1},
        //3个白点
        {1,0,0,
         0,1,0,
         0,0,1},
        //4个白点
        {1,0,1,
         0,0,0,
         1,0,1},
        //5个白点
        {1,0,1,
         0,1,0,
         1,0,1},
        //6个白点
        {1,1,1,
         0,0,0,
         1,1,1},
        //7个白点
        {1,0,1,
         1,1,1,
         1,0,1},
        //8个白点
        {1,1,1,
         1,0,1,
         1,1,1},
        //9个白点
        {1,1,1,
         1,1,1,
         1,1,1},
    };
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::on_openLenaJpg_triggered()
//打开当前目录下的lena.jpg图像。
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
        //将当前打开的图像显示在左侧的标签内。
        //先进行图像转换
        cv::cvtColor(srcImage,srcImage,CV_BGR2RGB);
        //将转换后的图像赋给img
        img = QImage((const unsigned char*)(srcImage.data),srcImage.cols,srcImage.rows, srcImage.cols*srcImage.channels(), QImage::Format_RGB888);
        //label1清空
        ui->label1->clear();
        //调整图像大小以适应标签大小。
        img=  img.scaled(ui->label1->width(), ui->label1->height());
        //让img显示在label1内
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

void MainWindow::on_actionTest_triggered()
{
    //这里是测试函数，开始在【帮助】菜单下实现，后来菜单删除，该函数保留。
    int i,j;
    // Mat Feature(cv::Size((srcImage.rows+2)/3,(srcImage.cols+2)/3), CV_8UC3);

    int X,Y;

    //srcImage=imread("e:\\a.jpg");
    Y=srcImage.cols;
    X=srcImage.rows;
    Mat Feature((X+2)/3,(Y+2)/3,CV_8UC(1), Scalar::all(0));
    Mat dstImage(X,Y,CV_8UC(1), Scalar::all(0));
    // srcImage.copyTo(Feature);
    cvtColor(srcImage,srcImage,CV_BGR2GRAY);
    /*
    for(i=0;i<111;i++)
        for(j=0;j<111;j++)
            Feature.at<uchar>(i/3,j/3)=111;
    */

    for(i=0;i<X;i++)
        for(j=0;j<Y;j++)
            Feature.at<uchar>(i/3,j/3)+=srcImage.at<uchar>(i,j)/9;

    // imshow("fea",Feature);
    for(i=0;i<X/3;i++)
        for(j=0;j<Y/3;j++)
            Feature.at<uchar>(i,j)/=1;
    for(i=0;i<X/3;i++)
        for(j=0;j<Y/3;j++)
            Feature.at<uchar>(i,j)/=(255/6);


    int T[6][3][3]={
        //如果不希望再次处理，可以直接在建立数组时，将1改为255即可。
        {0,0,0,
         0,0,0,
         0,0,0},
        {0,0,0,
         0,1,0,
         0,0,0},
        {1,0,0,
         0,0,0,
         0,0,1},
        {1,0,0,
         0,1,0,
         0,0,1},
        {1,0,1,
         0,0,0,
         1,0,1},
        {1,0,1,
         1,1,1,
         1,0,1}
    };

    for(i=0;i<dstImage.rows;i++)
        for(j=0;j<dstImage.cols;j++)
            dstImage.at<uchar>(i,j)=T[Feature.at<uchar>(i/3,j/3)][i%3][j%3];
    threshold(dstImage,dstImage,0.5, 255,   THRESH_BINARY );
    imshow("ad",dstImage);


    // imshow("aaa",Feature);
    /* cv::Mat image;
    cv::Mat resizedImage;	// to contain resized image
    image=imread("e:\\a.jpg");
    namedWindow("image", CV_WINDOW_AUTOSIZE);
    imshow("image",image);
    cv::resize(image,resizedImage,
            cv::Size(image.cols/5, image.rows/5),0,0,4);	// 1/3 resizing
    imshow("asdf",resizedImage);
    */

    /* Mat myFeature;
    cv::cvtColor(srcImage,srcImage,CV_RGB2BGR);
    cv::resize(srcImage,myFeature,cv::Size(srcImage.rows/3,srcImage.cols/3),0,0,INTER_LINEAR);

    imshow(",",myFeature);
    Mat myFeature,test;
    Size size(100,100);
    cv::cvtColor(srcImage,myFeature,CV_BGR2GRAY);
    cv::resize(myFeature,test,cv::Size(512/3,512/3),0,0,3);
    imshow("li",test);

*/
    // int i,j;
    // int X,Y;
    //  int M,N;
    //  int label2M,label2N;
    /*  int T[6][3][3]={
        {0,0,0,
         0,0,0,
         0,0,0},
        {0,0,0,
         0,1,0,
         0,0,0},
        {1,0,0,
         0,0,0,
         0,0,1},
        {1,0,0,
         0,1,0,
         0,0,1},
        {1,0,1,
         0,0,0,
         1,0,1},
        {1,0,1,
         1,1,1,
         1,0,1}
    };
    */
    //注意，确保是二值图像，否则不能显示。或者把1更改为255也可。



    // Mat Feature;
    // cv::cvtColor(srcImage,srcImage,CV_RGB2GRAY);
    /*
    X=srcImage.rows;
    Y=srcImage.cols;
    //cv::resize(dstImage,dstImage,ui->label2->size());
    M=dstImage.rows;
    N=dstImage.cols;
    label2M=ui->label2->width();
    label2N=ui->label2->height();
    M=100;
    N=100;
    */
    //   cv::resize(Feature,Feature,cv::Size(ui->label2->width()/3,ui->label2->height()/3));  //Size的获取，需要注意格式，从Qsize转换为cv::size
    //  imshow(",",Feature);
    //自己计算的，可以使用resize直接计算Feature。
    /*for(i=0;i<X;i++)
        for(j=0;j<Y;j++)
            Feature.at<uchar>(X/(M/3),Y/(N/3))+=srcImage.at<uchar>(i,j);
            */
    //cv::resize(Feature,Feature,Size(ui->label2->height()+1,ui->label2->width()+1)); //都加上1，确保能够都有特征
    // imshow(",",Feature);
    /*
    img = QImage((const unsigned char*)
                 (Feature.data),Feature.cols,Feature.rows,Feature.cols*Feature.channels(),
                 QImage::Format_RGB888);
    img=img.scaled(ui->label2->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
    */
    //   imshow(",2",Feature);
    // cv::resize(Feature,Feature,cv::Size((Feature.rows+2)/3,(Feature.cols+2)/3),0,0,3);  //加上2确保每个都有特征！！！前面加1不对
    //  imshow(",",Feature);
    //imshow("dd",srcImage);
    //cv::Size dsize=cv::Size((srcImage.rows+2)/3,(srcImage.cols+2)/3);
    //cv::Size dsize=cv::Size(111,111);
    //cv::resize(srcImage,srcImage,dsize,0,0,CV_INTER_LINEAR);  //加上2确保每个都有特征！！！前面加1不对
    //cv::cvtColor(Feature,Feature,CV_RGB2GRAY);
    /*  for(i=0;i<Feature.rows;i++)
        for(j=0;j<Feature.cols;j++)
            Feature.at<uchar>(i,j)=Feature.at<uchar>(i,j)/(255/6);
            */
    //threshold(Feature,Feature, 128, 255,   THRESH_BINARY );
    //imshow("d",srcImage);
    //  Mat r(cv::Size(Feature.cols*3,Feature.rows*3));
    /*
cv::cvtColor(srcImage,Feature,CV_RGB2GRAY);
     for(i=0;i<dstImage.rows;i++)
         for(j=0;j<dstImage.cols;j++)
             dstImage.at<uchar>(i,j)=T[Feature.at<uchar>(i/3,j/3)][i%3][j%3];
     imshow("ad",dstImage);
     */
    /*
    img = QImage((const unsigned char*)
                 (Feature.data),Feature.cols,Feature.rows,Feature.cols*Feature.channels(),
                 QImage::Format_Indexed8);
    //QImage::Format_Indexed8的格式一定注意！！！！

   // img=img.scaled(ui->label2->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
*/

    /*
    for(i=0;i<label2M-3;i++)
        for(j=0;j<label2N-3;j++)
            dstImage.at<uchar>(i,j)=T[Feature.at<uchar>(i/3,j/3)][i%3][j%3];
    img = QImage((const unsigned char*)
                 (Feature.data),Feature.cols,Feature.rows,Feature.cols*Feature.channels(),
                 QImage::Format_Indexed8);
    //QImage::Format_Indexed8的格式一定注意！！！！

   // img=img.scaled(ui->label2->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
    */
}

void MainWindow::on_myDefine_triggered()
{
    int i,j;
    int X,Y;
    Y=srcImage.cols;
    X=srcImage.rows;
    //定义特征矩阵
    Mat Feature((X+2)/3,(Y+2)/3,CV_8UC(1), Scalar::all(0));
    //定义目标图像（骰子画）
    Mat dstImage(X,Y,CV_8UC(1), Scalar::all(0));
    Mat srcImage2;
    //灰度化
    cvtColor(srcImage,srcImage2,CV_BGR2GRAY);
    //自己计算Feature。
    //也可以定义一个数组，先求和，然后再求平均值。
    for(i=0;i<X;i++)
        for(j=0;j<Y;j++)
            Feature.at<uchar>(i/3,j/3)+=srcImage2.at<uchar>(i,j)/9;
    /*
     * 看下特征图像什么样
    namedWindow( "fea", CV_WINDOW_AUTOSIZE );
    imshow("fea",Feature);
    */
    for(i=0;i<X/3;i++)
        for(j=0;j<Y/3;j++)
            Feature.at<uchar>(i,j)/=((255/9)*9)/9;
    //定义用来表示骰子的数组
    int T[10][3][3]={
        //如果不希望再次处理，可以直接在建立数组时，将1改为255即可。
        //0个白点
        {0,0,0,
         0,0,0,
         0,0,0},
        //1个白点
        {0,0,0,
         0,1,0,
         0,0,0},
        //2个白点
        {1,0,0,
         0,0,0,
         0,0,1},
        //3个白点
        {1,0,0,
         0,1,0,
         0,0,1},
        //4个白点
        {1,0,1,
         0,0,0,
         1,0,1},
        //5个白点
        {1,0,1,
         0,1,0,
         1,0,1},
        //6个白点
        {1,1,1,
         0,0,0,
         1,1,1},
        //7个白点
        {1,0,1,
         1,1,1,
         1,0,1},
        //8个白点
        {1,1,1,
         1,0,1,
         1,1,1},
        //9个白点
        {1,1,1,
         1,1,1,
         1,1,1},
    };
    //映射
    for(i=0;i<dstImage.rows;i++)
        for(j=0;j<dstImage.cols;j++)
            dstImage.at<uchar>(i,j)=T[Feature.at<uchar>(i/3,j/3)][i%3][j%3];
    //阈值化处理
    threshold(dstImage,dstImage,0.5, 255,   THRESH_BINARY );
    cv::Size dsize=Size(ui->label2->width(),ui->label2->height());
    //缩放目标图像
    cv::resize(dstImage,dstImage,dsize);
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.step,  QImage::Format_Indexed8);
    ui->label2->clear();
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_windowShow_triggered()
{
    int i,j;
    int X,Y;
    Y=srcImage.cols;
    X=srcImage.rows;
    //特征图像
    Mat Feature((X+2)/3,(Y+2)/3,CV_8UC(1), Scalar::all(0));
    //骰子图
    Mat dstImage(X,Y,CV_8UC(1), Scalar::all(0));
    //原始图像的灰度图像
    Mat srcImage2;
    //灰度化
    cvtColor(srcImage,srcImage2,CV_BGR2GRAY);
    for(i=0;i<X;i++)
        for(j=0;j<Y;j++)
            Feature.at<uchar>(i/3,j/3)+=srcImage2.at<uchar>(i,j)/9;
    //显示下特征图像
    // imshow("fea",Feature);
    //提取特征
    for(i=0;i<X/3;i++)
        for(j=0;j<Y/3;j++)
            Feature.at<uchar>(i,j)/=(255/10+1);  //或者...=((255/9)*9)/9;
    //骰子状子块
    int T[10][3][3]={
        //如果不希望再次处理，可以直接在建立数组时，将1改为255即可。
        //0个白点
        {0,0,0,
         0,0,0,
         0,0,0},
        //1个白点
        {0,0,0,
         0,1,0,
         0,0,0},
        //2个白点
        {1,0,0,
         0,0,0,
         0,0,1},
        //3个白点
        {1,0,0,
         0,1,0,
         0,0,1},
        //4个白点
        {1,0,1,
         0,0,0,
         1,0,1},
        //5个白点
        {1,0,1,
         0,1,0,
         1,0,1},
        //6个白点
        {1,1,1,
         0,0,0,
         1,1,1},
        //7个白点
        {1,0,1,
         1,1,1,
         1,0,1},
        //8个白点
        {1,1,1,
         1,0,1,
         1,1,1},
        //9个白点
        {1,1,1,
         1,1,1,
         1,1,1},
    };
    //映射
    for(i=0;i<dstImage.rows;i++)
        for(j=0;j<dstImage.cols;j++)
            dstImage.at<uchar>(i,j)=T[Feature.at<uchar>(i/3,j/3)][i%3][j%3];
    //阈值化处理
    threshold(dstImage,dstImage,0.5, 255,   THRESH_BINARY );
    //显示
    cv::imshow("chapter5",dstImage);
}
void MainWindow::showLabel(Mat m, QLabel *l)
{
    //   cv::cvtColor(m,m,CV_BGR2RGB);
    img = QImage((const unsigned char*)(m.data),m.cols,m.rows,m.cols*m.channels(), QImage::Format_RGB888);
    //l.clear();
    l->clear();
    //img=  img.scaled(l.width(),l.height());
    img=img.scaled(l->width(),l->height());
    //l.setPixmap(QPixmap::fromImage(img));
    l->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_useResize_triggered()
{
    int i,j;
    int X,Y;
    X=srcImage.rows;
    Y=srcImage.cols;
    //定义特征矩阵
    Mat Feature((X+2)/3,(Y+2)/3,CV_8UC(1), Scalar::all(0));
    //定义目标图像（骰子画）
    Mat dstImage(X,Y,CV_8UC(1), Scalar::all(0));
    Mat srcImage2;
    //灰度化
    cvtColor(srcImage,srcImage2,CV_BGR2GRAY);
    //使用resize计算得到特征矩阵Feature。
    cv::Size dsize=Size(Feature.cols,Feature.rows);
    cv::resize(srcImage2,Feature,dsize);
    for(i=0;i<X/3;i++)
        for(j=0;j<Y/3;j++)
            Feature.at<uchar>(i,j)/=(255/9);
    //定义骰子
    int T[10][3][3]={
        //如果不希望再次处理，可以直接在建立数组时，将1改为255即可。
        //0个白点
        {0,0,0,
         0,0,0,
         0,0,0},
        //1个白点
        {0,0,0,
         0,1,0,
         0,0,0},
        //2个白点
        {1,0,0,
         0,0,0,
         0,0,1},
        //3个白点
        {1,0,0,
         0,1,0,
         0,0,1},
        //4个白点
        {1,0,1,
         0,0,0,
         1,0,1},
        //5个白点
        {1,0,1,
         0,1,0,
         1,0,1},
        //6个白点
        {1,1,1,
         0,0,0,
         1,1,1},
        //7个白点
        {1,0,1,
         1,1,1,
         1,0,1},
        //8个白点
        {1,1,1,
         1,0,1,
         1,1,1},
        //9个白点
        {1,1,1,
         1,1,1,
         1,1,1},
    };
    //映射
    for(i=0;i<dstImage.rows;i++)
        for(j=0;j<dstImage.cols;j++)
            dstImage.at<uchar>(i,j)=T[Feature.at<uchar>(i/3,j/3)][i%3][j%3];
    //阈值化处理
    threshold(dstImage,dstImage,0.5, 255,   THRESH_BINARY );
    //窗口测试显示
    // imshow("dst",dstImage);
    dsize=Size(ui->label2->width(),ui->label2->height());
    //缩放
    cv::resize(dstImage,dstImage,dsize);
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.step,  QImage::Format_Indexed8);
    ui->label2->clear();
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_horizen_triggered()
{
    //建立一个dsize，与label2相等
    cv::Size dsize=Size(ui->label2->width(),ui->label2->height());
    //定义h用于存储label2的高度
    int h;
    //将label2的高度赋给h
    h=ui->label2->height();
    //定义目标图像dstImage
    Mat dstImage(dsize,CV_8UC(1), Scalar::all(0));
    int i,j;
    //对dstImage内像素进行赋值
    for(i=0;i<dstImage.rows;i++)
        for(j=0;j<dstImage.cols;j++)
            dstImage.at<uchar>(i,j)=(i*255/h);
    //将img赋值
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.step,  QImage::Format_Indexed8);
    //清空label2
    ui->label2->clear();
    //将img赋给label2
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_action_2_triggered()
{

}
void MainWindow::on_action_4_triggered()
{

}
void MainWindow::on_vertical_triggered()
{
    //建立一个dsize，与label2相等
    cv::Size dsize=Size(ui->label2->width(),ui->label2->height());
    //定义w用于存储label2的宽度
    int w;
    //将label2的高度赋给w
    w=ui->label2->height();
    //定义目标图像dstImage
    Mat dstImage(dsize,CV_8UC(1), Scalar::all(0));
    int i,j;
    //对dstImage内像素进行赋值
    for(i=0;i<dstImage.rows;i++)
        for(j=0;j<dstImage.cols;j++)
            dstImage.at<uchar>(i,j)=(j*255/w);
    //将img赋值
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.step,  QImage::Format_Indexed8);
    //清空label2
    ui->label2->clear();
    //将img赋给label2
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_circle_triggered()
{
    //建立一个dsize，与label2相等
    cv::Size dsize=Size(ui->label2->width(),ui->label2->height());
    //定义目标图像dstImage
    Mat dstImage(dsize,CV_8UC(1), Scalar::all(0));
    int i,j;
    //对dstImage内像素进行赋值
    for(i=0;i<dstImage.rows;i++)
        for(j=0;j<dstImage.cols;j++)
            dstImage.at<uchar>(i,j)=int(sqrt(i*i+j*j))%255;
    //将img赋值
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.step,  QImage::Format_Indexed8);
    //清空label2
    ui->label2->clear();
    //将img赋给label2
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_mySum_triggered()
{
    //建立一个dsize，与label2相等
    cv::Size dsize=Size(ui->label2->width(),ui->label2->height());
    //定义目标图像dstImage
    Mat dstImage(dsize,CV_8UC(1), Scalar::all(0));
    int i,j;
    //对dstImage内像素进行赋值
    for(i=0;i<dstImage.rows;i++)
        for(j=0;j<dstImage.cols;j++)
            dstImage.at<uchar>(i,j)=(i+j)%255;
    //将img赋值
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.step,  QImage::Format_Indexed8);
    //清空label2
    ui->label2->clear();
    //将img赋给label2
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_myAbstrct_triggered()
{
    //建立一个dsize，与label2相等
    cv::Size dsize=Size(ui->label2->width(),ui->label2->height());
    //定义目标图像dstImage
    Mat dstImage(dsize,CV_8UC(1), Scalar::all(0));
    int i,j;
    //对dstImage内像素进行赋值
    for(i=0;i<dstImage.rows;i++)
        for(j=0;j<dstImage.cols;j++)
            dstImage.at<uchar>(i,j)=abs(i-j)%255;
    //将img赋值
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.step,  QImage::Format_Indexed8);
    //清空label2
    ui->label2->clear();
    //将img赋给label2
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_myTriple_triggered(bool checked)
{
    //建立一个dsize，与label2相等
    cv::Size dsize=Size(ui->label2->width(),ui->label2->height());
    //定义目标图像dstImage
    Mat dstImage(dsize,CV_8UC(1), Scalar::all(0));
    int i,j;
    //对dstImage内像素进行赋值
    for(i=0;i<dstImage.rows;i++)
        for(j=0;j<dstImage.cols;j++)
            dstImage.at<uchar>(i,j)=i<j?i:j;
    //将img赋值
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.step,  QImage::Format_Indexed8);
    //清空label2
    ui->label2->clear();
    //将img赋给label2
    ui->label2->setPixmap(QPixmap::fromImage(img));
}


void MainWindow::on_myRand_triggered()
{
    //定义随机数
    int key=0;
    srand(time(NULL));
    //赋值
    key=abs(rand()*10090%8);
    //得到label2的大小
    cv::Size dsize=Size(ui->label2->width(),ui->label2->height());
    //定义目标图像
    Mat dstImage(dsize,CV_8UC(1), Scalar::all(0));
    int i,j;
    //生成随机图像
    switch(key)
    {
    case 0:
        for(i=0;i<dstImage.rows;i++)
            for(j=0;j<dstImage.cols;j++)
                dstImage.at<uchar>(i,j)=(i*i)%255;
        break;
    case 1:
        for(i=0;i<dstImage.rows;i++)
            for(j=0;j<dstImage.cols;j++)
                dstImage.at<uchar>(i,j)=(i*i+j*j)%255;
        break;
    case 2:
        for(i=0;i<dstImage.rows;i++)
            for(j=0;j<dstImage.cols;j++)
                dstImage.at<uchar>(i,j)=(i*i*i+j*j*j)%255;
        break;
    case 3:
        for(i=0;i<dstImage.rows;i++)
            for(j=0;j<dstImage.cols;j++)
                dstImage.at<uchar>(i,j)=((i+j)*(i+j))%255;
        break;
    case 4:
        for(i=0;i<dstImage.rows;i++)
            for(j=0;j<dstImage.cols;j++)
                dstImage.at<uchar>(i,j)=((i*i)+j)%255;
        break;
    case 5:
        for(i=0;i<dstImage.rows;i++)
            for(j=0;j<dstImage.cols;j++)
                dstImage.at<uchar>(i,j)=(i*255+j)%255;
        break;
    case 6:
        for(i=0;i<dstImage.rows;i++)
            for(j=0;j<dstImage.cols;j++)
                dstImage.at<uchar>(i,j)=(i+j*j*j)%255;
        break;
    case 7:
        for(i=0;i<dstImage.rows;i++)
            for(j=0;j<dstImage.cols;j++)
                dstImage.at<uchar>(i,j)=(i*i*i+j)%255;
        break;
    default:
        for(i=0;i<dstImage.rows;i++)
            for(j=0;j<dstImage.cols;j++)
                dstImage.at<uchar>(i,j)=(2*i*5*j*j)%255;
    }
    //img赋值
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.step,  QImage::Format_Indexed8);
    //label2清空
    ui->label2->clear();
    //在label内显示img
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_myIndex_triggered()
{
    //此部分的注释可以参考前面的骰子画部分
    int i,j;
    cv::Size dsize=Size(9,9);
    //cv::resize(dstImage,dstImage,dsize);
    Mat dstImage(dsize,CV_8UC(1), Scalar::all(0));
    int n=0;
    // srcImage.copyTo(Feature);

    /*
    for(i=0;i<111;i++)
        for(j=0;j<111;j++)
            Feature.at<uchar>(i/3,j/3)=111;
    */
    /*
    for(i=0;i<X;i++)
        for(j=0;j<Y;j++)
            Feature.at<uchar>(i/3,j/3)+=srcImage2.at<uchar>(i,j)/9;
*/


    //cv::imshow("fea",Feature);
    //不知道什么原因：使用imshow显示resize后的图像总是错的，但是后续计算是正确的！待解！！！！
    int T[10][3][3]={
        //如果不希望再次处理，可以直接在建立数组时，将1改为255即可。
        //0个白点
        {0,0,0,
         0,0,0,
         0,0,0},
        //1个白点
        {0,0,0,
         0,1,0,
         0,0,0},
        //2个白点
        {1,0,0,
         0,0,0,
         0,0,1},
        //3个白点
        {1,0,0,
         0,1,0,
         0,0,1},
        //4个白点
        {1,0,1,
         0,0,0,
         1,0,1},
        //5个白点
        {1,0,1,
         0,1,0,
         1,0,1},
        //6个白点
        {1,1,1,
         0,0,0,
         1,1,1},
        //7个白点
        {1,0,1,
         1,1,1,
         1,0,1},
        //8个白点
        {1,1,1,
         1,0,1,
         1,1,1},
        //9个白点
        {1,1,1,
         1,1,1,
         1,1,1},
    };

    for(i=0;i<dstImage.rows;i++)
        for(j=0;j<dstImage.cols;j++)
            dstImage.at<uchar>(i,j)=T[j/3+i/3][i%3][j%3];
    threshold(dstImage,dstImage,0.5, 255,   THRESH_BINARY );
    // imshow("ad",dstImage);    //窗口显示
    dsize=Size(ui->label2->width(),ui->label2->height());
    cv::resize(dstImage,dstImage,dsize,0,0,0);
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.step,  QImage::Format_Indexed8);
    // img = QImage(dstImage,dstImage.cols,dstImage.rows,dstImage.step,  QImage::Format_RGB888);
    ui->label2->clear();
    // img=img.scaled(ui->label2->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
    cv::imshow("DPLS",dstImage);
    /*
    Sleep(10000);

    for(i=0;i<dstImage.rows;i++)
        for(j=0;j<dstImage.cols;j++)
            dstImage.at<uchar>(i,j)=T[1][i%3][j%3];
    threshold(dstImage,dstImage,0.5, 255,   THRESH_BINARY );
    // imshow("ad",dstImage);    //窗口显示
    dsize=Size(ui->label2->width(),ui->label2->height());
    cv::resize(dstImage,dstImage,dsize);
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.step,  QImage::Format_Indexed8);
    // img = QImage(dstImage,dstImage.cols,dstImage.rows,dstImage.step,  QImage::Format_RGB888);
    ui->label2->clear();
    // img=img.scaled(ui->label2->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
    Sleep(1000);

    for(i=0;i<dstImage.rows;i++)
        for(j=0;j<dstImage.cols;j++)
            dstImage.at<uchar>(i,j)=T[2][i%3][j%3];
    threshold(dstImage,dstImage,0.5, 255,   THRESH_BINARY );
    // imshow("ad",dstImage);    //窗口显示
    dsize=Size(ui->label2->width(),ui->label2->height());
    cv::resize(dstImage,dstImage,dsize);
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.step,  QImage::Format_Indexed8);
    // img = QImage(dstImage,dstImage.cols,dstImage.rows,dstImage.step,  QImage::Format_RGB888);
    ui->label2->clear();
    // img=img.scaled(ui->label2->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
     Sleep(1000);


    for(i=0;i<dstImage.rows;i++)
        for(j=0;j<dstImage.cols;j++)
            dstImage.at<uchar>(i,j)=T[3][i%3][j%3];
    threshold(dstImage,dstImage,0.5, 255,   THRESH_BINARY );
    // imshow("ad",dstImage);    //窗口显示
    dsize=Size(ui->label2->width(),ui->label2->height());
    cv::resize(dstImage,dstImage,dsize);
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.step,  QImage::Format_Indexed8);
    // img = QImage(dstImage,dstImage.cols,dstImage.rows,dstImage.step,  QImage::Format_RGB888);
    ui->label2->clear();
    // img=img.scaled(ui->label2->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
     Sleep(1000);



    for(i=0;i<dstImage.rows;i++)
        for(j=0;j<dstImage.cols;j++)
            dstImage.at<uchar>(i,j)=T[4][i%3][j%3];
    threshold(dstImage,dstImage,0.5, 255,   THRESH_BINARY );
    // imshow("ad",dstImage);    //窗口显示
    dsize=Size(ui->label2->width(),ui->label2->height());
    cv::resize(dstImage,dstImage,dsize);
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.step,  QImage::Format_Indexed8);
    // img = QImage(dstImage,dstImage.cols,dstImage.rows,dstImage.step,  QImage::Format_RGB888);
    ui->label2->clear();
    // img=img.scaled(ui->label2->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
     Sleep(1000);


    for(i=0;i<dstImage.rows;i++)
        for(j=0;j<dstImage.cols;j++)
            dstImage.at<uchar>(i,j)=T[5][i%3][j%3];
    threshold(dstImage,dstImage,0.5, 255,   THRESH_BINARY );
    // imshow("ad",dstImage);    //窗口显示
    dsize=Size(ui->label2->width(),ui->label2->height());
    cv::resize(dstImage,dstImage,dsize);
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.step,  QImage::Format_Indexed8);
    // img = QImage(dstImage,dstImage.cols,dstImage.rows,dstImage.step,  QImage::Format_RGB888);
    ui->label2->clear();
    // img=img.scaled(ui->label2->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
    */

}

void MainWindow::on_myRand2_triggered()
{
    //此部分的注释可以参考前面的骰子画部分
    int i,j;
    cv::Size dsize=Size(ui->label2->width(),ui->label2->height());
    //cv::resize(dstImage,dstImage,dsize);
    Mat dstImage(dsize,CV_8UC(1), Scalar::all(0));

    // srcImage.copyTo(Feature);

    /*
    for(i=0;i<111;i++)
        for(j=0;j<111;j++)
            Feature.at<uchar>(i/3,j/3)=111;
    */
    /*
    for(i=0;i<X;i++)
        for(j=0;j<Y;j++)
            Feature.at<uchar>(i/3,j/3)+=srcImage2.at<uchar>(i,j)/9;
*/


    //cv::imshow("fea",Feature);
    //不知道什么原因：使用imshow显示resize后的图像总是错的，但是后续计算是正确的！待解！！！！
    int T[10][3][3]={
        //如果不希望再次处理，可以直接在建立数组时，将1改为255即可。
        //0个白点
        {0,0,0,
         0,0,0,
         0,0,0},
        //1个白点
        {0,0,0,
         0,1,0,
         0,0,0},
        //2个白点
        {1,0,0,
         0,0,0,
         0,0,1},
        //3个白点
        {1,0,0,
         0,1,0,
         0,0,1},
        //4个白点
        {1,0,1,
         0,0,0,
         1,0,1},
        //5个白点
        {1,0,1,
         0,1,0,
         1,0,1},
        //6个白点
        {1,1,1,
         0,0,0,
         1,1,1},
        //7个白点
        {1,0,1,
         1,1,1,
         1,0,1},
        //8个白点
        {1,1,1,
         1,0,1,
         1,1,1},
        //9个白点
        {1,1,1,
         1,1,1,
         1,1,1},
    };
    int key=0;
    srand(time(NULL));
    key=abs((rand()*100000)%10);
    /* QMessageBox msgBox;
    msgBox.setText(QString::number(key));
    msgBox.setText(tr("lili"));
    */
    // QMessageBox::information(NULL, "Title", QString::number(key), QMessageBox::Yes | QMessageBox::No, QMessageBox::Yes);
    //该语句用于测试key的值，开始总是不能出现key的正确值，原来key可能为负值
    //msgbox不能显示。
    for(i=0;i<dstImage.rows;i++)
        for(j=0;j<dstImage.cols;j++)
            dstImage.at<uchar>(i,j)=T[key][i%3][j%3];
    threshold(dstImage,dstImage,0.5, 255,   THRESH_BINARY );
    // imshow("ad",dstImage);    //窗口显示
    dsize=Size(ui->label2->width(),ui->label2->height());
    cv::resize(dstImage,dstImage,dsize);
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.step,  QImage::Format_Indexed8);
    // img = QImage(dstImage,dstImage.cols,dstImage.rows,dstImage.step,  QImage::Format_RGB888);
    ui->label2->clear();
    // img=img.scaled(ui->label2->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));

}

void MainWindow::on_myRand3_triggered()
{
    //此部分的注释可以参考前面的骰子画部分
    int i,j;
    cv::Size dsize=Size(3,3);
    //cv::resize(dstImage,dstImage,dsize);
    Mat dstImage(dsize,CV_8UC(1), Scalar::all(0));

    // srcImage.copyTo(Feature);

    /*
    for(i=0;i<111;i++)
        for(j=0;j<111;j++)
            Feature.at<uchar>(i/3,j/3)=111;
    */
    /*
    for(i=0;i<X;i++)
        for(j=0;j<Y;j++)
            Feature.at<uchar>(i/3,j/3)+=srcImage2.at<uchar>(i,j)/9;
*/


    //cv::imshow("fea",Feature);
    //不知道什么原因：使用imshow显示resize后的图像总是错的，但是后续计算是正确的！待解！！！！
    int T[10][3][3]={
        //如果不希望再次处理，可以直接在建立数组时，将1改为255即可。
        //0个白点
        {0,0,0,
         0,0,0,
         0,0,0},
        //1个白点
        {0,0,0,
         0,1,0,
         0,0,0},
        //2个白点
        {1,0,0,
         0,0,0,
         0,0,1},
        //3个白点
        {1,0,0,
         0,1,0,
         0,0,1},
        //4个白点
        {1,0,1,
         0,0,0,
         1,0,1},
        //5个白点
        {1,0,1,
         0,1,0,
         1,0,1},
        //6个白点
        {1,1,1,
         0,0,0,
         1,1,1},
        //7个白点
        {1,0,1,
         1,1,1,
         1,0,1},
        //8个白点
        {1,1,1,
         1,0,1,
         1,1,1},
        //9个白点
        {1,1,1,
         1,1,1,
         1,1,1},
    };
    int key=0;
    srand(time(NULL));
    key=abs((rand()*100000)%10);
    /* QMessageBox msgBox;
    msgBox.setText(QString::number(key));
    msgBox.setText(tr("lili"));
    */
    // QMessageBox::information(NULL, "Title", QString::number(key), QMessageBox::Yes | QMessageBox::No, QMessageBox::Yes);
    //该语句用于测试key的值，开始总是不能出现key的正确值，原来key可能为负值
    //msgbox不能显示。
    for(i=0;i<dstImage.rows;i++)
        for(j=0;j<dstImage.cols;j++)
            dstImage.at<uchar>(i,j)=T[key][i%3][j%3];
    threshold(dstImage,dstImage,0.5, 255,   THRESH_BINARY );
    // imshow("ad",dstImage);    //窗口显示
    dsize=Size(ui->label2->width(),ui->label2->height());
    cv::resize(dstImage,dstImage,dsize,0,0,0);
    threshold(dstImage,dstImage,40, 255,   THRESH_BINARY );
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.step,  QImage::Format_Indexed8);
    // img = QImage(dstImage,dstImage.cols,dstImage.rows,dstImage.step,  QImage::Format_RGB888);
    ui->label2->clear();
    // img=img.scaled(ui->label2->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
}
//原型0
void MainWindow::on_number0_triggered()
{
    showNumber(0);
}
//原型1
void MainWindow::on_number1_triggered()
{
    showNumber(1);
}
//原型2
void MainWindow::on_number2_triggered()
{
    showNumber(2);
}
//原型3
void MainWindow::on_number3_triggered()
{
    showNumber(3);
}
//原型4
void MainWindow::on_number4_triggered()
{
    showNumber(4);
}
//原型5
void MainWindow::on_number5_triggered()
{
    showNumber(5);
}
//原型6
void MainWindow::on_number6_triggered()
{
    showNumber(6);
}
//原型7
void MainWindow::on_number7_triggered()
{
    showNumber(7);
}
//原型8
void MainWindow::on_number8_triggered()
{
    showNumber(8);
}
//原型9
void MainWindow::on_number9_triggered()
{
    showNumber(9);
}
void MainWindow::showNumber(int n)
{
    //此部分的注释可以参考前面的骰子画部分
    int i,j;
    cv::Size dsize=Size(3,3);
    Mat dstImage(dsize,CV_8UC(1), Scalar::all(0));
    //骰子状子块
    int T[10][3][3]={
        //如果不希望再次处理，可以直接在建立数组时，将1改为255即可。
        //0个白点
        {0,0,0,
         0,0,0,
         0,0,0},
        //1个白点
        {0,0,0,
         0,1,0,
         0,0,0},
        //2个白点
        {1,0,0,
         0,0,0,
         0,0,1},
        //3个白点
        {1,0,0,
         0,1,0,
         0,0,1},
        //4个白点
        {1,0,1,
         0,0,0,
         1,0,1},
        //5个白点
        {1,0,1,
         0,1,0,
         1,0,1},
        //6个白点
        {1,1,1,
         0,0,0,
         1,1,1},
        //7个白点
        {1,0,1,
         1,1,1,
         1,0,1},
        //8个白点
        {1,1,1,
         1,0,1,
         1,1,1},
        //9个白点
        {1,1,1,
         1,1,1,
         1,1,1},
    };
    int key=n;
    //映射
    for(i=0;i<dstImage.rows;i++)
        for(j=0;j<dstImage.cols;j++)
            dstImage.at<uchar>(i,j)=T[key][i%3][j%3];
    //阈值化
    threshold(dstImage,dstImage,0.5, 255,   THRESH_BINARY );
    //窗口显示
    // imshow("dst",dstImage);
    dsize=Size(ui->label2->width(),ui->label2->height());
    //调整大小
    cv::resize(dstImage,dstImage,dsize,0,0,0);
    //阈值化
    threshold(dstImage,dstImage,40, 255,   THRESH_BINARY );
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.step,  QImage::Format_Indexed8);
    ui->label2->clear();
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_aboutMe_triggered()
{
    QMessageBox::information(this,"关于",tr("本软件为骰子作画学习系统，当前版本为1.0，由李立宗等人开发。"));
    return;
}

void MainWindow::on_contactUs_triggered()
{
    QMessageBox::information(this,"联系我们",tr("如有问题请联系：lilizong(at)Gmail。QQ群：QT+OpenCV，群号：107416004"));
    return;
}



void MainWindow::on_myTriple_triggered()
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
