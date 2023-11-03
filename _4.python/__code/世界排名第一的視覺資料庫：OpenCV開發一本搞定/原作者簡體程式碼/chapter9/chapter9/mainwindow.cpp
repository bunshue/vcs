#include "mainwindow.h"
#include "ui_mainwindow.h"
#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QString>
#include <QFileDialog>
#include <QMessageBox>
#include <opencv/cv.h>
#include <QTextCodec>
#include <stdio.h>
#include <qdir.h>
#include <stdlib.h>
#include <time.h>
#include <opencv/cv.h>
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
        cvtColor(srcImage,srcImage,CV_BGR2RGB);
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
    on_pushButton_clicked();
    /*
    //更改前：该函数为打开自定义文件。
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
    */
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

void MainWindow::on_pushButton_clicked()
{
    QString filename = QFileDialog::getOpenFileName(this,tr("打开待检索文件"),"",tr("Image File(*.bmp *.jpg *.jpeg *.png)"));
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

void MainWindow::on_pushButton_3_clicked()
{
    Mat noImage = cv::imread("no.png");
    if(!noImage.data)
    {
        QMessageBox msgBox;
        msgBox.setText(tr("默认的测试文件不存在，可以用以下两种方式的一种：1）复制一个文件到当前目录下，并命名为lena.jpg. 2)使用自定义方式打开一个自定义文件。"));
        msgBox.exec();
    }
    else
    {
        cv::cvtColor(noImage,noImage,CV_BGR2RGB);
        img = QImage((const unsigned char*)(noImage.data),noImage.cols,noImage.rows, noImage.cols*noImage.channels(), QImage::Format_RGB888);
        ui->label1->clear();
        img=  img.scaled(ui->label1->width(), ui->label1->height());
        ui->label1->setPixmap(QPixmap::fromImage(img));
        //ui->processPushButton->setEnabled(true);
        //   ui->label1->resize(ui->label1->pixmap()->size());//设置当前标签为图像大小
        // ui->label1->resize(img.width(),img.height());

        //this->setWidget(label1);
    }


    noImage.copyTo(dstImage);
    img = QImage((const unsigned char*)
                 (dstImage.data),dstImage.cols,dstImage.rows,dstImage.cols*dstImage.channels(),
                 QImage::Format_RGB888);
    img=img.scaled(ui->label1->size());
    ui->label1->setPixmap(QPixmap::fromImage(img));
    showLabel(noImage,ui->label2);
    showLabel(noImage,ui->label3);
    showLabel(noImage,ui->label4);
    showLabel(noImage,ui->label5);
    showLabel(noImage,ui->label6);
    showLabel(noImage,ui->label7);
    showLabel(noImage,ui->label8);
    showLabel(noImage,ui->label9);



}

void MainWindow::on_pushButton_4_clicked()
{
    exit(0);
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


void MainWindow::getFeature(cv::Mat m,int t[])
{
    //第1步：将图像灰度化并缩小尺寸，大小为mm*nn，这里处理为mm=8,nn=8
    //因此，缩小后的实际大小为8*8像素大小。
    int M=m.rows;
    int N=m.cols;

    //  printf("%d,%d\n",M,N);
    cv::cvtColor(m,m,CV_BGR2GRAY);
    // imshow("test",m);
    //  printf("%d\n",m.at<uchar>(123,123));
    int i,j;
    /*
    for(i=0;i<M;i++)
        for(j=0;j<N;j++)
        {
            printf("%d   \n",m.at<uchar>(i,j));
            // Feature.at<uchar>(i/(M/8),j/(N/8))+=m.at<uchar>(i,j);
        }
        */


    // mm=8;
    //nn=8;
    int FeatureResult[mm*nn];
    Mat Feature(mm,nn,CV_32SC1, Scalar::all(0));

    for(i=0;i<M;i++)
        for(j=0;j<N;j++)
        {
            Feature.at<int>(i/(M/mm),j/(N/nn))=Feature.at<int>(i/(M/mm),j/(N/nn))+m.at<uchar>(i,j);
            // Feature.at<uchar>(i/(M/8),j/(N/8))+=m.at<uchar>(i,j);
        }
    //测试：看看缩小后，图像里面的每个像素值是多少：
    /*
    for(i=0;i<mm;i++)
        for(j=0;j<nn;j++)
            printf("%d   ",Feature.at<int>(i,j));
    printf("end\n");
*/

    for(i=0;i<mm;i++)
        for(j=0;j<nn;j++)
            Feature.at<int>(i,j)=Feature.at<int>(i,j)/((M/mm)*(N/nn));

    // imshow("original",m);
    // imshow("resize Image:8*8",Feature);

    //显示当前缩小图像。
    //showLabelGray(Feature,ui->label2);
    //这里显示类型有问题，需要调整。
    //测试：看看缩小后，图像里面的每个像素值是多少：
    /*
    for(i=0;i<mm;i++)
        for(j=0;j<nn;j++)
            printf("%d   ",Feature.at<int>(i,j));
    printf("end\n");
    */
    //第2步：简化色彩。当前灰度级为8位，即256色，将其处理为cc色。
    //这里设置cc=64
    //int cc=64;
    for(i=0;i<mm;i++)
        for(j=0;j<nn;j++)
            Feature.at<int>(i,j)/=(256/cc);
    //测试：看看简化色彩后，图像内里面的每个像素值是多少：
    /*
    for(i=0;i<mm;i++)
        for(j=0;j<nn;j++)
            printf("%d   ",Feature.at<int>(i,j));
    */
    //第3步：计算图像的平均值。
    double sum,aver;
    sum=0;
    for(i=0;i<mm;i++)
        for(j=0;j<nn;j++)
            sum+=Feature.at<int>(i,j);
    aver=sum/(mm*nn);
    //  printf("sum=%lf,aver=%lf",sum,aver);
    //第4步：计算像素值与平均值大小关系。同时得到特征矩阵FeatureResult，并返回。
    int flag=0;
    for(i=0;i<mm;i++)
        for(j=0;j<nn;j++)
            if(Feature.at<int>(i,j)>aver)
                t[flag++]=1;
            else
                t[flag++]=0;
    /*
    for(i=0;i<mm*nn;i++)
        printf("%d",t[i]);
    printf("\n");
    */
    /*
    int *t;
    t=FeatureResult;
    return t;

*/
}

int* MainWindow::getFeature2(cv::Mat m)
{
    //第1步：将图像灰度化并缩小尺寸，大小为mm*nn，这里处理为mm=8,nn=8
    //因此，缩小后的实际大小为8*8像素大小。
    int M=m.rows;
    int N=m.cols;

    //  printf("%d,%d\n",M,N);
    //cv::cvtColor(m,m,CV_BGR2GRAY);
    cv::cvtColor(m,m,CV_RGB2GRAY);
    // imshow("test",m);
    //  printf("%d\n",m.at<uchar>(123,123));
    int i,j;
    /*
    for(i=0;i<M;i++)
        for(j=0;j<N;j++)
        {
            printf("%d   \n",m.at<uchar>(i,j));
            // Feature.at<uchar>(i/(M/8),j/(N/8))+=m.at<uchar>(i,j);
        }
        */


    // mm=8;
    // nn=8;
    int FeatureResult[mm*nn];
    Mat Feature(mm,nn,CV_32SC1, Scalar::all(0));

    for(i=0;i<M;i++)
        for(j=0;j<N;j++)
        {
            Feature.at<int>(i/(M/mm),j/(N/nn))=Feature.at<int>(i/(M/mm),j/(N/nn))+m.at<uchar>(i,j);
            // Feature.at<uchar>(i/(M/8),j/(N/8))+=m.at<uchar>(i,j);
        }
    //测试：看看缩小后，图像里面的每个像素值是多少：
    /*
    for(i=0;i<mm;i++)
        for(j=0;j<nn;j++)
            printf("%d   ",Feature.at<int>(i,j));
    printf("end\n");
*/

    for(i=0;i<mm;i++)
        for(j=0;j<nn;j++)
            Feature.at<int>(i,j)=Feature.at<int>(i,j)/((M/mm)*(N/nn));

    // imshow("original",m);
    // imshow("resize Image:8*8",Feature);

    //显示当前缩小图像。
    //showLabelGray(Feature,ui->label2);
    //这里显示类型有问题，需要调整。
    //测试：看看缩小后，图像里面的每个像素值是多少：
    /*
    for(i=0;i<mm;i++)
        for(j=0;j<nn;j++)
            printf("%d   ",Feature.at<int>(i,j));
    printf("end\n");
    */
    //第2步：简化色彩。当前灰度级为8位，即256色，将其处理为cc色。
    //这里设置cc=64

    for(i=0;i<mm;i++)
        for(j=0;j<nn;j++)
            Feature.at<int>(i,j)/=(256/cc);
    //测试：看看简化色彩后，图像内里面的每个像素值是多少：
    /*
    for(i=0;i<mm;i++)
        for(j=0;j<nn;j++)
            printf("%d   ",Feature.at<int>(i,j));
    */
    //第3步：计算图像的平均值。
    double sum,aver;
    sum=0;
    for(i=0;i<mm;i++)
        for(j=0;j<nn;j++)
            sum+=Feature.at<int>(i,j);
    aver=sum/(mm*nn);
    //  printf("sum=%lf,aver=%lf",sum,aver);
    //第4步：计算像素值与平均值大小关系。同时得到特征矩阵FeatureResult，并返回。
    int flag=0;
    // int FeatureResult[mm*nn];
    for(i=0;i<mm;i++)
        for(j=0;j<nn;j++)
            if(Feature.at<int>(i,j)>aver)
                FeatureResult[flag++]=1;
            else
                FeatureResult[flag++]=0;
    /*
    for(i=0;i<mm*nn;i++)
        printf("%d",t[i]);
    printf("\n");
    */

    int *t;
    t=FeatureResult;
    return t;


}
void MainWindow::on_pushButton_6_clicked()
{
    //提取特征！！！

    /*
    //测试：显示下特征值是否能够正确获取。
    //mm=8;
    //nn=8;
    int t[mm*nn];
    getFeature(srcImage,t);
    int i;
    for(i=0;i<mm*nn;i++)
        //  printf("%d,%d\n",i,*(t+i));
        printf("%d,%d\t",i,t[i]);
    printf("\n===========\n");
    int *t2;
    t2=getFeature2(srcImage);
    for(i=0;i<mm*nn;i++)
        //  printf("%d,%d\n",i,*(t+i));
        printf("%d,%d\t",i,t[i]);
    //测试：显示下特征值是否能够正确获取。
    */
    /*
    string fileName;
    int i=0;
    for(i=0;i<16;i++)
    {
        fileName=file+i;
        FileFeature[i]=getFeature2(fileName);
    }
    for(i=0;i<16;i++)
    {
        printf("\n");
        for(j=0;j<mm*nn;j++)
            printf("%d,%d",i,FileFeature[i][j]);
    }
    */
    //读取文件到srcImage内，然后提取特征。
    int i,j;
    for(i=0;i<total;i++)
    {
        getImage(fileInfo,i);
        int t2[mm*nn];
        getFeature(srcImage,t2);
        for(j=0;j<featureNumber;j++)
        {
            FileFeature[i][j]=t2[j];
            //   printf("%5d",t2[j]);
        }
        // printf("end:%d\n",i);
    }
    /*
    //测试下特征提取情况。
    for(i=0;i<fileNumber;i++)
    {
        printf("\n%d:",i);
        for(j=0;j<featureNumber;j++)
            printf("%5d",FileFeature[i][j]);
    }
*/
    QMessageBox::about(NULL, "提示", "特征提取完毕！！！");//, QMessageBox::Yes | QMessageBox::No, QMessageBox::Yes);

}
void MainWindow::showLabelGray(Mat m, QLabel *l)
{

    cv::Size dsize=Size(l->width(),l->height());
    cv::resize(m,m,dsize);
    img = QImage((const unsigned char*)(m.data),m.cols,m.rows,m.step,  QImage::Format_Indexed8);
    // img = QImage(dstImage,dstImage.cols,dstImage.rows,dstImage.step,  QImage::Format_RGB888);
    // img = QImage((const unsigned char*)(m.data),m.cols,m.rows,m.step,  QImage::Format_RGB32);
    l->clear();
    // img=img.scaled(ui->label2->size());
    l->setPixmap(QPixmap::fromImage(img));

}


void MainWindow::on_pushButton_5_clicked()
{
    //设定路径，这里设置好要读取的路径，并且能够将路径下的图片随机地显示在下面。
    QString path = QFileDialog::getExistingDirectory();
    //显示当前选取的文件夹
    //  QMessageBox::information(NULL, "文件路径", path, QMessageBox::Yes | QMessageBox::No, QMessageBox::Yes);
    // QMessageBox::information(NULL, "文件路径", "设定完毕！！！", QMessageBox::Yes | QMessageBox::No, QMessageBox::Yes);


    QDir *dir=new QDir(path);
    //过滤掉文件名”.",和文件名"..".
    dir->setFilter(QDir::Files | QDir::NoSymLinks);
    QStringList filter;
    //filter<<"*.dat";
    //dir->setNameFilters(filter);
    //QList<QFileInfo> *fileInfo=new QList<QFileInfo>(dir->entryInfoList(filter));
    fileInfo=new QList<QFileInfo>(dir->entryInfoList(filter));
    // QString s;//=fileInfo->at(0).fileName();

    // QString dirS;  //包含一个目录的路径；
    total=fileInfo->count();
    //读取当前目录下文件的个数
    //QMessageBox::information(NULL, "文件路径",QString::number(n), QMessageBox::Yes | QMessageBox::No, QMessageBox::Yes);
    // printf("%d",n);
    int i;
    /*
     //下面的思路是遍历图像，然后在label内显示。
     //这种思路不好在于label的名字处理困难。
    for(i=0;i<n;i++)
    {
        s=fileInfo->at(i).fileName();
        //调用发现，i需要从2开始，到n+2而结束。
        //这里i=0时，文件名是”.“
        //i=1时，文件名是"..".
        //q强迫使用i从2开始，到n+2结束，不好用！
        // QMessageBox::information(NULL, "文件路径", QString::number(i).append(s), QMessageBox::Yes | QMessageBox::No, QMessageBox::Yes);
        dirS="image//";
        dirS=dirS.append(s);
        //测试文件名是否显示正确。
       // QMessageBox::information(NULL, "文件路径", dirS, QMessageBox::Yes | QMessageBox::No, QMessageBox::Yes);
        QTextCodec *code = QTextCodec::codecForName("gb18030");
        std::string name = code->fromUnicode(dirS).data();
        srcImage = cv::imread(name);
         cv::cvtColor(srcImage,srcImage,CV_BGR2RGB);
       //测试是否能显示图像！
        //imshow("dd",srcImage);
        //waitKey();

        showLabel(srcImage,ui->label2);
    }
    //上面的思路是遍历图像，然后在label内显示。
    */
    //对每个label进行处理，随机显示一个当前确定目录下的图像
    /*
    int k;
    srand(time(NULL));
    k=rand()%n;
    getImage(fileInfo,k);
    showLabel(srcImage,ui->label2);
    k=rand()%n;
    getImage(fileInfo,k);
    showLabel(srcImage,ui->label3);
    k=rand()%n;
    getImage(fileInfo,k);
    showLabel(srcImage,ui->label4);
    k=rand()%n;
    getImage(fileInfo,k);
    showLabel(srcImage,ui->label5);
    k=rand()%n;
    getImage(fileInfo,k);
    showLabel(srcImage,ui->label6);
    k=rand()%n;
    getImage(fileInfo,k);
    showLabel(srcImage,ui->label7);
    k=rand()%n;
    getImage(fileInfo,k);
    showLabel(srcImage,ui->label8);
    k=rand()%n;
    getImage(fileInfo,k);
    showLabel(srcImage,ui->label9);
    */
    //产生无重复的数组；
    srand(time(NULL));
    int output[100]={0};
    int m;
    for(i=0; i<total; i++)
    {
        while(output[m=rand()%total])
            ;
        output[m] = i;
    }
    //上述处理过程中，不会出现值为0的数组元素，下面随机将0处理一下，放到某个数组元素内。
    m=rand()%total;
    output[m]=0;
    getImage(fileInfo,output[0]);
    showLabel(srcImage,ui->label2);
    getImage(fileInfo,output[1]);
    showLabel(srcImage,ui->label3);
    getImage(fileInfo,output[2]);
    showLabel(srcImage,ui->label4);
    getImage(fileInfo,output[3]);
    showLabel(srcImage,ui->label5);
    getImage(fileInfo,output[4]);
    showLabel(srcImage,ui->label6);
    getImage(fileInfo,output[5]);
    showLabel(srcImage,ui->label7);
    getImage(fileInfo,output[6]);
    showLabel(srcImage,ui->label8);
    getImage(fileInfo,output[7]);
    showLabel(srcImage,ui->label9);


}
void MainWindow::getImage(QList<QFileInfo> *fileInfo,int i)
{
    QString s;//=fileInfo->at(0).fileName();
    QString dirS;  //包含一个目录的路径；
    s=fileInfo->at(i).fileName();
    //调用发现，i需要从2开始，到n+2而结束。
    //这里i=0时，文件名是”.“
    //i=1时，文件名是"..".
    //q强迫使用i从2开始，到n+2结束，不好用！
    // QMessageBox::information(NULL, "文件路径", QString::number(i).append(s), QMessageBox::Yes | QMessageBox::No, QMessageBox::Yes);
    dirS="image//";
    dirS=dirS.append(s);
    //测试文件名是否显示正确。
    // QMessageBox::information(NULL, "文件路径", dirS, QMessageBox::Yes | QMessageBox::No, QMessageBox::Yes);
    QTextCodec *code = QTextCodec::codecForName("gb18030");
    std::string name = code->fromUnicode(dirS).data();
    srcImage = cv::imread(name);
    cv::cvtColor(srcImage,srcImage,CV_BGR2RGB);
}
//产生无重复的随机数：
/*
public static int[] MainWindow::GetRandomSequence0(int total)
{
    int[] hashtable = new int[total];
    int[] output = new int[total];

    Random random = new Random();
    for (int i = 0; i < total; i++)
    {
        int num = random.Next(0, total);
        while (hashtable[num] > 0)
        {
            num = random.Next(0, total);
        }

        output[i] = num;
        hashtable[num] = 1;
    }

    return output;
}
*/

void MainWindow::on_pushButton_2_clicked()
{
    //搜索按钮，主要完成检索图像的特征提取、特征比对、排序
    int t2[mm*nn];
    getFeature(srcImage,t2);
    /*
    //测试一下能否读取特征值。
    for(int j=0;j<featureNumber;j++)
    {
            printf("%5d",t2[j]);
    }
    */
    /*
    //测试FileFeature是否正确读取
    for(int i=0;i<fileNumber;i++)
    {
        printf("\n%d:",i);
        for(int j=0;j<featureNumber;j++)
            printf("%5d",FileFeature[i][j]);
    }
    */
    //相同特征值的数量。
    int sameCount[fileNumber]={0};//忘记初始化，罪过！！！
    //和目录下图片挨个比较，并得出相同的位数的个数。
    for(int i=0;i<fileNumber;i++)
        for(int j=0;j<featureNumber;j++)
        {
            sameCount[i]+=FileFeature[i][j]*t2[j];
            //犯了弱智错误，写成了：sameCount[fileNumber]+=FileFeature[i][j]*t2[j];
            /*
            //c测试语句，开始samecount内总是得到0，测试一下。
            if(FileFeature[i][j]*t2[j])
                printf("ok");
                */
        }
    /*
    for(int i=0;i<fileNumber;i++)
        printf("%d\n",sameCount[i]);
        */
    //将个数最多的fileNumber个找出来
    int maxi[8]={0};
    for(int i=0;i<8;i++)
    {
        int max=sameCount[0];
        for(int j=0;j<fileNumber;j++)
        {
            if(max<sameCount[j])
            {
                max=sameCount[j];
                // 犯了弱智错误，写成了：maxi[fileNumber]=j;
                maxi[i]=j;
            }
        }
        sameCount[maxi[i]]=0;//避免重复计算最大值，将上次最大值置零，再次求最大值。

    }
    /*
                for(int i=0;i<8;i++)
                printf("%d\n",maxi[i]);
    */
    getImage(fileInfo,maxi[0]);
    showLabel(srcImage,ui->label2);
    getImage(fileInfo,maxi[1]);
    showLabel(srcImage,ui->label3);
    getImage(fileInfo,maxi[2]);
    showLabel(srcImage,ui->label4);
    getImage(fileInfo,maxi[3]);
    showLabel(srcImage,ui->label5);
    getImage(fileInfo,maxi[4]);
    showLabel(srcImage,ui->label6);
    getImage(fileInfo,maxi[5]);
    showLabel(srcImage,ui->label7);
    getImage(fileInfo,maxi[6]);
    showLabel(srcImage,ui->label8);
    getImage(fileInfo,maxi[7]);
    showLabel(srcImage,ui->label9);







}

void MainWindow::on_action_triggered()
{
    on_pushButton_5_clicked();
}

void MainWindow::on_action_2_triggered()
{
    on_pushButton_2_clicked();
}

void MainWindow::on_action_3_triggered()
{
    on_pushButton_6_clicked();
}
