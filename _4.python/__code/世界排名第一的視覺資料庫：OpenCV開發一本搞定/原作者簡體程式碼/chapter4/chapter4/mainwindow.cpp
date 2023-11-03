#include "mainwindow.h"
#include "ui_mainwindow.h"
#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QString>
#include <QFileDialog>
#include <QMessageBox>
#include <opencv/cv.h>
#include <QTextCodec>
#include <QInputDialog>
#include <QLineEdit>
#include <math.h>
#define M 64
#define N 64
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

void MainWindow::on_actionTest_triggered()
{
    /*  int M=512;
    int N=512;*/
    //不使用变量，使用define定义
    float chaoticF[M*N];
    chaoticF[0]=0.991;
    int i=0;
    int flag=0;   //这里出错了，因为int整数65536，超过了大小了。  用来遍历数组
    for(i=1;i<M*N;i++)
        chaoticF[i]=1-2.0*chaoticF[i-1]*chaoticF[i-1];
    /*
    for (int i=0; i<M*N; i++)
    {
            printf("%d %f\n",flag,chaoticF[flag]);
            flag++;
    }
    */
    for(i=0;i<M*N;i++)
        if(chaoticF[i]>0)
            chaoticF[i]=255;
        else
            chaoticF[i]=0;

    /*
    RNG rng;
       // int myRand=rng.uniform(0,256);
        //上述随机数没有起作用？？？？
    int myRand;
        srand(time(NULL));
    for(i=0;i<M*N;i++)
    {

            myRand=rand()%256;

            chaoticF[i]=myRand;
    }
    */
    /*
    for(i=0;i<512*512;i++)
        printf("%8f    ",chaoticF[i]);
*/
    Mat dst(M,N,CV_8UC3);

    flag=0;
    for (int i=0; i<dst.rows; i++)
    {
        uchar* dstR  = dst.ptr<uchar>(i);
        for (int j=0; j<dst.cols; j++)
        {
            dstR[3*j]=chaoticF[flag];
            dstR[3*j+1]=chaoticF[flag];
            dstR[3*j+2]=chaoticF[flag];
            flag=flag+1;
            // printf("%d %f\n",flag,chaoticF[flag]);

        }
    }
    printf("cols=%d\n",flag);
    printf("rows=%d\n",dst.rows);
    printf("cols=%d\n",dst.cols);
    showLabel(dst,ui->label2);
    showLabel(dst,ui->label1);
    //waitKey();
    /*

    double chaotic[512*512];

    int i;
    chaotic[0]=0.98;
    for(i=1;i<512*512;i++)
        chaotic[i]=1-2*chaotic[i-1]*chaotic[i-1];

    for(i=0;i<512*512;i++)
        if(chaotic[i]>0)
            chaotic[i]=255;
        else
            chaotic[i]=0;

    int flag=0;
*/
    /*
    Mat dst(512,512,CV_8UC3);

    dst.copyTo(srcImage);
    for (int i=0; i<srcImage.rows; i++)
    {
        uchar *p0 = srcImage.ptr<uchar>(i);

        for (int j=0; j<srcImage.cols; j++)
        {

            int dstR,dstG,dstB;
            dstR =chaotic[flag];
            dstG =chaotic[flag] ;
            dstB = chaotic[flag];

            p0[3*j]=dstR;
            p0[3*j+1]=dstG;
            p0[3*j+2]=dstB;
            flag++;
        }
    }
    showLabel(srcImage,ui->label2);
    imshow("li",srcImage);
    */
    /*
    Mat dst(512,512,CV_8UC1);


    for (int i=0; i<dst.rows; i++)
    {
        for (int j=0; j<dst.cols; j++)
        {
            dst.at<uchar>(i,j)=chaotic[flag];
            flag++;
        }
    }
    */
    // showLabel(dst,ui->label2);
    //  imshow("li",dst);

    /*
     * for(i=0;i<512*512;i++)
        printf("%8d",chaotic[i]);
        */


}
void MainWindow::showLabel(Mat m, QLabel *l)
{
    //   cv::cvtColor(m,m,COLOR_BGR2RGB);
    //   cv::cvtColor(m,m,CV_BGR2RGB);
    img = QImage((const unsigned char*)(m.data),m.cols,m.rows,m.cols*m.channels(), QImage::Format_RGB888);
    l->clear();
    img=img.scaled(l->width(),l->height());
    l->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_blackAndWhite_triggered()
{
    //黑白二色的混沌图像
    float chaotic[M*N];
    double t;
    bool isOK;
    QString text=QInputDialog::getText(NULL, "混沌初始值",
                                       "请输入初始值",
                                       QLineEdit::Normal,
                                       "0.98",
                                       &isOK);
    //混沌序列赋初值
    if(isOK)
    {
        t=text.toDouble();
    }
    else
        t=0.98;
    chaotic[0]=t;
    int i;
    //生成混沌序列
    for(i=1;i<M*N;i++)
        chaotic[i]=1-2*chaotic[i-1]*chaotic[i-1];
    //将混沌序列二值化，只有0和255两个值。
    for(i=0;i<M*N;i++)
        if(chaotic[i]>0)
            chaotic[i]=255;
        else
            chaotic[i]=0;
    //建立一个混沌图像
    Mat chaoticImg(M,N,CV_8UC1);
    //imshow("test",chaoticImg);
    int flag=0;
    /*
     * 用指针方式赋值。
    for (int y=0; y<M; y++)
    {
        uchar* chaoticImgR  = chaoticImg.ptr<uchar>(y);
        for (int x=0; x<N; x++)
        {
            chaoticImgR[x]=chaotic[flag];
            flag++;
        }
    }
    imshow("test1",chaoticImg);
    */
    //将混沌序列赋值给混沌图像
    for(int y=0;y<M;y++)
        for(int x=0;x<N;x++)
        {
            chaoticImg.at<uchar>(y,x)=chaotic[flag];
            flag++;
        }
    //调用函数 showLabelGray 显示混沌图像
    showLabelGray(chaoticImg,ui->label2);
    /*
     * 自定义显示函数
    Size dsize = Size(ui->label2->width(),ui->label2->height());
    cv::resize(chaoticImg,chaoticImg,dsize,0,0,CV_INTER_AREA);
    Mat m;
    chaoticImg.copyTo(m);
    img = QImage((const unsigned char*)(m.data),m.cols,m.rows,m.cols*m.channels(), QImage::Format_Indexed8);
    ui->label2->clear();
    //img=img.scaled(ui->label2->width(),ui->label2->height());
    ui->label2->setPixmap(QPixmap::fromImage(img));
    */
}

void MainWindow::on_myGray_triggered()
{
    //灰度混沌图像。
    float chaotic[M*N];
    double t;
    bool isOK;
    QString text=QInputDialog::getText(NULL, "混沌初始值",
                                       "请输入初始值",
                                       QLineEdit::Normal,
                                       "0.98",
                                       &isOK);
    //混沌赋初始值
    if(isOK)
    {
        t=text.toDouble();
    }
    else
        t=0.98;
    chaotic[0]=t;
    int i;
    //给整个混沌序列赋值
    for(i=1;i<M*N;i++)
        chaotic[i]=1-2*chaotic[i-1]*chaotic[i-1];
    int tmp;
    //处理为256个灰度级
    for(i=0;i<M*N;i++)
    {
        tmp=chaotic[i]*1000000;
        chaotic[i]=tmp%256;
    }
    //定义一个灰度图像
    Mat chaoticImg(M,N,CV_8UC1);
    int flag=0;
    //将混沌序列的值赋给灰度图像
    for (int y=0; y<M; y++)
    {
        uchar* chaoticImgR  = chaoticImg.ptr<uchar>(y);
        for (int x=0; x<N; x++)
        {
            chaoticImgR[x]=chaotic[flag];
            flag++;
        }
    }
    //调用函数showLabelGray,显示混沌图像
    showLabelGray(chaoticImg,ui->label2);
}

void MainWindow::on_myColor_triggered()
{
    //彩色混沌图像
    //定义一个数组，用来存储混沌序列
    float chaotic[M*N*3];
    double t;
    bool isOK;
    QString text=QInputDialog::getText(NULL, "混沌初始值",
                                       "请输入初始值",
                                       QLineEdit::Normal,
                                       "0.98",
                                       &isOK);
    //混沌赋初始值
    if(isOK)
    {
        t=text.toDouble();
    }
    else
        t=0.98;
    chaotic[0]=t;
    int i;
    //混沌序列赋值
    for(i=1;i<M*N*3;i++)
        chaotic[i]=1-2*chaotic[i-1]*chaotic[i-1];
    int tmp;
    //混沌序列处理为256级
    for(i=0;i<M*N*3;i++)
    {
        tmp=chaotic[i]*10000;
        chaotic[i]=tmp%256;
    }
    //定义混沌图像
    Mat chaoticImg(M,N,CV_8UC3);
    //将混沌序列的值赋给混沌图像
    int flag=0;
    for (int y=0; y<M; y++)
    {
        uchar* chaoticImgR  = chaoticImg.ptr<uchar>(y);
        for (int x=0; x<N; x++)
        {
            chaoticImgR[3*x]=chaotic[flag];
            chaoticImgR[3*x+1]=chaotic[flag+M*N];
            chaoticImgR[3*x+2]=chaotic[flag+2*M*N];
            flag=flag+1;
        }
    }
    //定义一个专门用于显示的图像
    Mat chaoticImgShow;
    chaoticImg.copyTo(chaoticImgShow);
    //色彩空间转换
    cv::cvtColor(chaoticImgShow,chaoticImgShow,COLOR_BGR2RGB);
    //cv::cvtColor(chaoticImgShow,chaoticImgShow,CV_BGR2RGB);
    //cvtColor中使用参数CV_BGR2RGB，也可以，其是OpenCV2.0的标准。
    //调用函数showLabel显示混沌图像。
    showLabel(chaoticImgShow,ui->label2);
}
void MainWindow::creatChaoticImage(float init)
{
    //获取原始图像的大小
    int MM,NN;
    MM=srcImage.rows;
    NN=srcImage.cols;
    //定义一个数组，从初混沌值
    float chaotic[MM*NN*3];
    //混沌系统赋初始值
    chaotic[0]=init;
    int i;
    //计算混沌序列的值
    for(i=1;i<MM*NN*3;i++)
        chaotic[i]=1-2*chaotic[i-1]*chaotic[i-1];
    int tmp;
    //将混沌序列的值调整为8位像素值区间即：[0,255]
    for(i=0;i<MM*NN*3;i++)
    {
        tmp=chaotic[i]*10000;
        chaotic[i]=tmp%256;
    }
    //定义一个混沌图像
    Mat chaoticImgT(MM,NN,CV_8UC3);
    //给混沌图像赋初始值
    int flag=0;
    for (int y=0; y<MM; y++)
    {
        uchar* chaoticImgR  = chaoticImgT.ptr<uchar>(y);
        for (int x=0; x<NN; x++)
        {
            chaoticImgR[3*x]=chaotic[flag];
            chaoticImgR[3*x+1]=chaotic[flag+MM*NN];
            chaoticImgR[3*x+2]=chaotic[flag+2*MM*NN];
            flag=flag+1;
        }
    }
    //将计算得到的值赋给全局图像变量，chaoticImg
    chaoticImgT.copyTo(chaoticImg);
}

void MainWindow::on_cryp_triggered()
{

}

void MainWindow::on_deCryp_triggered()
{
    //读入需要解密的图像
    QString filename = QFileDialog::getOpenFileName(this,tr("打开要解密的图像"),"",tr("Image File(*.bmp *.jpg *.jpeg *.png)"));
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
    }
    //读取混沌初始值，用于生成混沌图像
    double t;
    bool isOK;
    QString text=QInputDialog::getText(NULL, "混沌初始值",
                                       "请输入初始值",
                                       QLineEdit::Normal,
                                       "0.98",
                                       &isOK);
    //将读取的值赋给变量t，如果没有读到，令t=0.98
    if(isOK)
    {
        t=text.toDouble();
    }
    else
        t=0.98;
    //调用函数creatChaoticImage生成混沌图像chaoticImg，参数为t。
    creatChaoticImage(t);
    //用混沌图像(chaoticImg)与加密图像（srcImage)进行异或，实现解密
    bitwise_xor(srcImage,chaoticImg,dstImage);
    //将解密结果的图像显示在label2上
    showLabel(dstImage,ui->label2);
    //保存解密后图像
    QString fileName = QFileDialog::getSaveFileName(this,
                                                    tr("保存解密后的图像"),
                                                    "",
                                                    tr("image (*.bmp)"));
    Mat m(srcImage.size(),CV_8UC3);
    dstImage.copyTo(m);
    img = QImage((const unsigned char*)(m.data),m.cols,m.rows,m.cols*m.channels(), QImage::Format_RGB888);
    img.save(fileName);
    /*  不使用异或函数bitwise_xor完成异或操作。
    int MM,NN;
    MM=srcImage.rows;
    NN=srcImage.cols;
    float chaotic[MM*NN];
    Mat deCrypImage(srcImage.size(),CV_8UC3);
    //解密图像，大小与加密图像srcImage一致。
    //这里首先选取加密图像，经过on_openCustomeFile_triggered()加载后，其名称为srcImage，需要注意名字不是dstImage。
    // srcImage.copyTo(dstImage);  //这里给dstImage赋值，为的是能够确保其大小 与srcImage一致。
    for (int i=0; i<MM; i++)
    {
        uchar *p0 = srcImage.ptr<uchar>(i);
        uchar *q0 = chaoticImg.ptr<uchar>(i);
        uchar *r0=deCrypImage.ptr<uchar>(i);
        for (int j=0; j<NN; j++)
        {
            int srcR=p0[3*j];
            int srcG=p0[3*j+1];
            int srcB=p0[3*j+2];

            int dstR=q0[3*j];
            int dstG=q0[3*j+1];
            int dstB=q0[3*j+2];


            r0[3*j]=srcR^dstR;
            r0[3*j+1]=srcG^dstG;
            r0[3*j+2]=srcB^dstB;
        }
    }
    showLabel(deCrypImage,ui->label2);
    */
}

void MainWindow::on_encryp_triggered()
{
    //读入原始需要加密图像
    QString filename = QFileDialog::getOpenFileName(this,tr("打开要加密图像"),"",tr("Image File(*.bmp *.jpg *.jpeg *.png)"));
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
        //cv::cvtColor(srcImage,srcImage,CV_BGR2RGB);
        cv::cvtColor(srcImage,srcImage,COLOR_BGR2RGB);
        img = QImage((const unsigned char*)(srcImage.data),srcImage.cols,srcImage.rows, srcImage.cols*srcImage.channels(), QImage::Format_RGB888);
        ui->label1->clear();
        img=  img.scaled(ui->label1->width(), ui->label1->height());
        ui->label1->setPixmap(QPixmap::fromImage(img));
    }
    //读取混沌初始值，用来生成混沌图像
    double t;
    bool isOK;
    QString text=QInputDialog::getText(NULL, "混沌初始值",
                                       "请输入初始值",
                                       QLineEdit::Normal,
                                       "0.98",
                                       &isOK);
    //获取刚刚输入的值，作为混沌赋初始值
    if(isOK)
    {
        t=text.toDouble();
    }
    else
        t=0.98;
    //调用函数creatChaoticImage,用t作为混沌初始值，生成混沌图像chaoticImg。
    creatChaoticImage(t);
    //完成图像异或加密
    bitwise_xor(srcImage,chaoticImg,dstImage);
    //显示加密后的图像
    showLabel(dstImage,ui->label2);
    //保存加密后图像
    QString fileName = QFileDialog::getSaveFileName(this,
                                                    tr("保存加密后的图像"),
                                                    "",
                                                    tr("image (*.bmp)"));  //需要保存为bmp格式，如果是其他格式，可能无法解密。
    Mat m(srcImage.size(),CV_8UC3);
    dstImage.copyTo(m);
    img = QImage((const unsigned char*)(m.data),m.cols,m.rows,m.cols*m.channels(), QImage::Format_RGB888);
    img.save(fileName);

    /*
     *CxXor函数是低版本的，如果使用OpenCV3.0以下版本，请使用该函数实现。
    void cvXor	(	const CvArr * 	src1,
    const CvArr * 	src2,
    CvArr * 	dst,
    const CvArr * 	mask = NULL
    )
    */
    /*
    //imshow("li",chaoticImg);
    const  CvArr* s=(CvArr*)&srcImage;
    //const  CvArr* t=(CvArr*)&chaoticImg;
    const  CvArr* t=(CvArr*)&srcImage;
    CvArr* r=(CvArr*)&srcImage;  //不能使const类型
    // cvXor(s,t,r);
    */
    //====================================================================================
    /*  不使用异或函数bitwise_xor完成异或操作。
    int MM,NN;
    MM=srcImage.rows;
    NN=srcImage.cols;
    float chaotic[MM*NN];
    // Mat dstImage(srcImage.size(),CV_8UC3);
    srcImage.copyTo(dstImage);  //这里给dstImage赋值，为的是能够确保其大小 与srcImage一致。
    for (int i=0; i<MM; i++)
    {
        uchar *p0 = srcImage.ptr<uchar>(i);
        uchar *q0 = chaoticImg.ptr<uchar>(i);
        uchar *r0=dstImage.ptr<uchar>(i);
        for (int j=0; j<NN; j++)
        {
            int srcR=p0[3*j];
            int srcG=p0[3*j+1];
            int srcB=p0[3*j+2];

            int dstR=q0[3*j];
            int dstG=q0[3*j+1];
            int dstB=q0[3*j+2];


            r0[3*j]=srcR^dstR;
            r0[3*j+1]=srcG^dstG;
            r0[3*j+2]=srcB^dstB;
        }
    }
    showLabel(dstImage,ui->label2);

    QString fileName = QFileDialog::getSaveFileName(this,
                                                    tr("保存加密后的图像"),
                                                    "",
                                                    tr("image (*.bmp)"));  //需要保存为bmp格式，如果是其他格式，可能无法解密。
    Mat m(srcImage.size(),CV_8UC3);
    dstImage.copyTo(m);
    img = QImage((const unsigned char*)(m.data),m.cols,m.rows,m.cols*m.channels(), QImage::Format_RGB888);
    img.save(fileName);
    */
}

void MainWindow::on_Sencryp_triggered()
{

    //导入原始需要加密图像
    QString filename = QFileDialog::getOpenFileName(this,tr("打开要加密图像"),"",tr("Image File(*.bmp *.jpg *.jpeg *.png)"));
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
    }
    //读取混沌初始值，用于生成混沌图像
    double t;
    bool isOK;
    QString text=QInputDialog::getText(NULL, "混沌初始值",
                                       "请输入初始值",
                                       QLineEdit::Normal,
                                       "0.98",
                                       &isOK);
    //获取输入的初始值，将其赋给t。
    if(isOK)
    {
        t=text.toDouble();
    }
    else
        t=0.98;
    //获取原始图像的长和宽
    int MM,NN;
    int i,j;
    MM=srcImage.rows;
    NN=srcImage.cols;
    //定义一个混沌序列
    double *chaotic=new double[MM*NN*3];
    //定义一个混沌有序序列
    double *chaoticSort=new double[MM*NN*3];
    //定义一个索引序列
    int *chaoticIndex=new int[MM*NN*3];
    //混沌初始值赋值
    chaotic[0]=t;
    //生成混沌序列
    for(i=1;i<MM*NN*3;i++)
        chaotic[i]=1-2*chaotic[i-1]*chaotic[i-1];
    //初始化chaoticSort
    memcpy(chaoticSort,chaotic,MM*NN*3*sizeof(double));
    //memcpy(chaoticSort,chaotic,MM*NN*3*8);
    //double类型占8个字节
    //对chaoticSort进行排序
    std::sort(chaoticSort,chaoticSort+MM*NN*3);
    /*   测试
    for(i=4000;i<4090;i++)
        QMessageBox::about(NULL,"number",QString::number(chaoticSort[i]));
    */
    //生成索引序列，计算chaoticSort在chaotic内的位置信息
    for(i=0;i<MM*NN*3;i++)
    {
        for(j=0;j<MM*NN*3;j++)
            if(chaoticSort[i]==chaotic[j])
                chaoticIndex[i]=j;
    }
    // int *test=new int[MM*NN*3];
    /*
    * 测试。用于将原图像整体逆序排列,即实现图像的旋转。
    for(i=0;i<MM*NN*3;i++)
    {
        chaoticIndex[i]=MM*NN*3-1-i;
    }
    */
    /*
     * 测试chaoticIndex内的数据
    for(i=0;i<100;i++)
        QMessageBox::about(NULL,"number",QString::number(chaoticIndex[i]));
    */

    int flag=0;
    srcImage.copyTo(dstImage);
    //这里给dstImage赋值，为的是能够确保其大小 与srcImage一致。
    /*
    * 测试一下
    for (int i=0; i<MM; i++)
    {
      uchar  *r0=dstImage.ptr<uchar>(i);
        for (int j=0; j<NN*3; j++)
        {
           r0[j]=255;
        }
    }
     showLabel(dstImage,ui->label2);
     QMessageBox::about(NULL,"number",QString::number(2));
     */
    /*
     * 测试chaoticIndex内的数据
    for(i=500;i<1000;i=i+500)
        QMessageBox::about(NULL,"number",QString::number(chaoticIndex[i]));
    */
    for (int i=0; i<MM; i++)
    {
        uchar  *r0=dstImage.ptr<uchar>(i);
        //    uchar *p0 = srcImage.ptr<uchar>(i);
        for (int j=0; j<NN*3; j++)
        {

            //  uchar  *r0=dstImage.ptr<uchar>(i);
            uchar *p0 = srcImage.ptr<uchar>(chaoticIndex[flag]/(NN*3));
            r0[j]=p0[chaoticIndex[flag]%(NN*3)];
            flag++;
            // uchar *p0 = srcImage.ptr<uchar>(chaoticIndex[i*NN+j]/NN);
            /*
             * 其他可能的计算方式
            uchar *p0 = srcImage.ptr<uchar>(chaoticIndex[flag]/(NN*3));

            r0[3*j]=p0[3*(chaoticIndex[flag]%NN)];
            r0[3*j+1]=p0[3*(chaoticIndex[flag]%NN)];
            r0[3*j+2]=p0[3*(chaoticIndex[flag]%NN)];
            */
            //  uchar *p0 = srcImage.ptr<uchar>(test[flag]/(NN*3));
            // r0[3*j]=p0[3*j];
            // r0[3*j+1]=p0[3*j+1];
            // r0[3*j+2]=p0[3*j+2];
            /*
             r0[3*j]=p0[3*(test[flag]%(NN*3))];
             r0[3*j+1]=p0[3*(test[flag]%(NN*3))+1];
             r0[3*j+2]=p0[3*(test[flag]%(NN*3))+2];
            */
            // r0[3*j+1]=p0[3*(chaoticIndex[flag]%NN)+1];
            //  r0[3*j+2]=p0[3*(chaoticIndex[flag]%NN)+2];
            //r0[3*j]=p0[3*(chaoticIndex[flag]%NN)];
            //r0[3*j+1]=255;
            // r0[3*j+2]=55;
            //   r0[3*j]=p0[3*(chaoticIndex[flag]%NN)];
            //r0[3*j]=p0[3*(chaoticIndex[i*NN+j]%NN)];
            //  r0[3*j+1]=p0[3*(chaoticIndex[i*NN+j]%NN)+1];
            //r0[3*j+2]=p0[3*(chaoticIndex[i*NN+j]%NN)+2];
            //flag++;
        }
    }
    //显示加密图像
    showLabel(dstImage,ui->label2);
    //保存图像。
    //需要保存为bmp格式，如果是其他格式，可能无法解密。
    QString fileName = QFileDialog::getSaveFileName(this,
                                                    tr("保存加密后的图像"),
                                                    "",
                                                    tr("image (*.bmp)"));

    Mat m(srcImage.size(),CV_8UC3);
    dstImage.copyTo(m);
    img = QImage((const unsigned char*)(m.data),m.cols,m.rows,m.cols*m.channels(), QImage::Format_RGB888);
    img.save(fileName);
}

void MainWindow::on_Sdecryp_triggered()
{
    //导入原始需要加密图像
    QString filename = QFileDialog::getOpenFileName(this,tr("打开要解密图像"),"",tr("Image File(*.bmp *.jpg *.jpeg *.png)"));
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
    }
    //输入混沌初始值，生成混沌图像
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
    //获取读入图像大小，用于构建混沌数组使用
    int MM,NN;
    int i,j;
    MM=srcImage.rows;
    NN=srcImage.cols;
    //定义一个混沌序列
    double *chaotic=new double[MM*NN*3];
    //定义一个混沌有序序列
    double *chaoticSort=new double[MM*NN*3];
    //定义一个索引序列
    int *chaoticIndex=new int[MM*NN*3];
    //混沌数组赋初值
    chaotic[0]=t;
    //生成混沌序列
    for(i=1;i<MM*NN*3;i++)
        chaotic[i]=1-2*chaotic[i-1]*chaotic[i-1];
    memcpy(chaoticSort,chaotic,MM*NN*3*sizeof(double));
    // memcpy(chaoticSort,chaotic,MM*NN*3*8);
    //double类型占8个字节
    //对chaoticSort进行排序
    std::sort(chaoticSort,chaoticSort+MM*NN*3);
    /*
    for(i=4000;i<4090;i++)
        QMessageBox::about(NULL,"number",QString::number(chaoticSort[i]));
    */
    //生成索引序列，计算chaoticSort在chaotic内的位置信息
    for(i=0;i<MM*NN*3;i++)
    {
        for(j=0;j<MM*NN*3;j++)
            if(chaoticSort[i]==chaotic[j])
                chaoticIndex[i]=j;
    }
    //int *test=new int[MM*NN*3];
    /*
     * 测试。用于将原图像整体逆序排列

     for(i=0;i<MM*NN*3;i++)
     {
         chaoticIndex[i]=MM*NN*3-1-i;
     }
    */

    /*
    for(i=0;i<100;i++)
        QMessageBox::about(NULL,"number",QString::number(chaoticIndex[i]));
    */
    int flag=0;
    srcImage.copyTo(dstImage);  //这里给dstImage赋值，为的是能够确保其大小 与srcImage一致。
    /*
     * 测试一下
    for (int i=0; i<MM; i++)
    {
      uchar  *r0=dstImage.ptr<uchar>(i);
        for (int j=0; j<NN*3; j++)
        {

           r0[j]=255;

        }
    }
     showLabel(dstImage,ui->label2);
     QMessageBox::about(NULL,"number",QString::number(2));
     */
    /*
    for(i=500;i<0、1000;i=i+500)
        QMessageBox::about(NULL,"number",QString::number(chaoticIndex[i]));
    */
    //解密过程
    for (int i=0; i<MM; i++)
    {
        //    uchar *p0 = srcImage.ptr<uchar>(i);
        for (int j=0; j<NN*3; j++)
        {
            //  uchar  *r0=dstImage.ptr<uchar>(i);
            uchar *p0 = srcImage.ptr<uchar>(i);
            uchar  *r0=dstImage.ptr<uchar>(chaoticIndex[flag]/(NN*3));
            r0[chaoticIndex[flag]%(NN*3)]=p0[j];
            flag++;
            // uchar *p0 = srcImage.ptr<uchar>(chaoticIndex[i*NN+j]/NN);
            /*
             * 其他可能计算方式
            uchar *p0 = srcImage.ptr<uchar>(chaoticIndex[flag]/(NN*3));

            r0[3*j]=p0[3*(chaoticIndex[flag]%NN)];
            r0[3*j+1]=p0[3*(chaoticIndex[flag]%NN)];
            r0[3*j+2]=p0[3*(chaoticIndex[flag]%NN)];
            */

            //  uchar *p0 = srcImage.ptr<uchar>(test[flag]/(NN*3));

            // r0[3*j]=p0[3*j];
            // r0[3*j+1]=p0[3*j+1];
            // r0[3*j+2]=p0[3*j+2];
            /*
              r0[3*j]=p0[3*(test[flag]%(NN*3))];
              r0[3*j+1]=p0[3*(test[flag]%(NN*3))+1];
              r0[3*j+2]=p0[3*(test[flag]%(NN*3))+2];
            */

            // r0[3*j+1]=p0[3*(chaoticIndex[flag]%NN)+1];
            //  r0[3*j+2]=p0[3*(chaoticIndex[flag]%NN)+2];
            //r0[3*j]=p0[3*(chaoticIndex[flag]%NN)];
            //r0[3*j+1]=255;
            // r0[3*j+2]=55;
            //   r0[3*j]=p0[3*(chaoticIndex[flag]%NN)];

            //r0[3*j]=p0[3*(chaoticIndex[i*NN+j]%NN)];

            //  r0[3*j+1]=p0[3*(chaoticIndex[i*NN+j]%NN)+1];
            //r0[3*j+2]=p0[3*(chaoticIndex[i*NN+j]%NN)+2];
            //flag++;
        }
    }
    //显示解密图像
    showLabel(dstImage,ui->label2);
    //需要保存为bmp格式，如果是其他格式，可能无法解密。
    QString fileName = QFileDialog::getSaveFileName(this,
                                                    tr("保存解密后的图像"),
                                                    "",
                                                    tr("image (*.bmp)"));
    //用于保存
    Mat m(srcImage.size(),CV_8UC3);
    dstImage.copyTo(m);
    img = QImage((const unsigned char*)(m.data),m.cols,m.rows,m.cols*m.channels(), QImage::Format_RGB888);
    img.save(fileName);
}

void MainWindow::showLabelGray(Mat m, QLabel *l)
{
    //   cv::cvtColor(m,m,CV_BGR2RGB);
    Size dsize = Size(l->width(),l->height());
    cv::resize(m, m,dsize,0,0,CV_INTER_AREA);
    //注意插值方式，如果采用默认方式：cv::resize(m, m,dsize),图像缩小后的图像失真严重。
    img = QImage((const unsigned char*)(m.data),m.cols,m.rows,m.cols*m.channels(), QImage::Format_Indexed8);
    l->clear();
    //  img=img.scaled(l->width(),l->height());
    l->setPixmap(QPixmap::fromImage(img));
}
