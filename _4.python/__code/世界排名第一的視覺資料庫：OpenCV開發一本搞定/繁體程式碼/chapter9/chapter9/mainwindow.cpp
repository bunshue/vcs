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
        cvtColor(srcImage,srcImage,CV_BGR2RGB);
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
    on_pushButton_clicked();
    /*
    //變更前：該函數為開啟自訂檔案。
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
    QMessageBox::information(this,"版權",tr("本軟體版權所有者為：天津職業技術師范大學。若果使用，請聯繫：lilizong@gmail.com"));
}

void MainWindow::on_about_triggered()
{
    QMessageBox::information(this,"關於",tr("本軟體目前版本為1.0，由李立宗等人開發。若果有問題，歡迎聯繫：lilizong@gmail.com"));
    return;
}

void MainWindow::on_pushButton_clicked()
{
    QString filename = QFileDialog::getOpenFileName(this,tr("開啟待檢索檔案"),"",tr("Image File(*.bmp *.jpg *.jpeg *.png)"));
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

void MainWindow::on_pushButton_3_clicked()
{
    Mat noImage = cv::imread("no.png");
    if(!noImage.data)
    {
        QMessageBox msgBox;
        msgBox.setText(tr("預設的測試檔案不存在，可以用以下兩種模式的一種：1）複製一個檔案到目前目錄下，並命名為lena.jpg. 2)使用自訂模式開啟一個自訂檔案。"));
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
        //   ui->label1->resize(ui->label1->pixmap()->size());//設定目前標簽為圖形大小
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
    //第1步：將圖形灰階化並拉遠尺寸，大小為mm*nn，這裡處理為mm=8,nn=8
    //因此，拉遠後的實際大小為8*8像素大小。
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
    //測試：看看拉遠後，圖形裡面的每個像素值是多少：
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

    //顯示目前拉遠圖形。
    //showLabelGray(Feature,ui->label2);
    //這裡顯示型態有問題，需要調整。
    //測試：看看拉遠後，圖形裡面的每個像素值是多少：
    /*
    for(i=0;i<mm;i++)
        for(j=0;j<nn;j++)
            printf("%d   ",Feature.at<int>(i,j));
    printf("end\n");
    */
    //第2步：簡化色彩。目前灰階級為8位，即256色，將其處理為cc色。
    //這裡設定cc=64
    //int cc=64;
    for(i=0;i<mm;i++)
        for(j=0;j<nn;j++)
            Feature.at<int>(i,j)/=(256/cc);
    //測試：看看簡化色彩後，圖形內裡面的每個像素值是多少：
    /*
    for(i=0;i<mm;i++)
        for(j=0;j<nn;j++)
            printf("%d   ",Feature.at<int>(i,j));
    */
    //第3步：計算圖形的平均值。
    double sum,aver;
    sum=0;
    for(i=0;i<mm;i++)
        for(j=0;j<nn;j++)
            sum+=Feature.at<int>(i,j);
    aver=sum/(mm*nn);
    //  printf("sum=%lf,aver=%lf",sum,aver);
    //第4步：計算像素值與平均值大小關系。同時得到特征矩陣FeatureResult，並傳回。
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
    //第1步：將圖形灰階化並拉遠尺寸，大小為mm*nn，這裡處理為mm=8,nn=8
    //因此，拉遠後的實際大小為8*8像素大小。
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
    //測試：看看拉遠後，圖形裡面的每個像素值是多少：
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

    //顯示目前拉遠圖形。
    //showLabelGray(Feature,ui->label2);
    //這裡顯示型態有問題，需要調整。
    //測試：看看拉遠後，圖形裡面的每個像素值是多少：
    /*
    for(i=0;i<mm;i++)
        for(j=0;j<nn;j++)
            printf("%d   ",Feature.at<int>(i,j));
    printf("end\n");
    */
    //第2步：簡化色彩。目前灰階級為8位，即256色，將其處理為cc色。
    //這裡設定cc=64

    for(i=0;i<mm;i++)
        for(j=0;j<nn;j++)
            Feature.at<int>(i,j)/=(256/cc);
    //測試：看看簡化色彩後，圖形內裡面的每個像素值是多少：
    /*
    for(i=0;i<mm;i++)
        for(j=0;j<nn;j++)
            printf("%d   ",Feature.at<int>(i,j));
    */
    //第3步：計算圖形的平均值。
    double sum,aver;
    sum=0;
    for(i=0;i<mm;i++)
        for(j=0;j<nn;j++)
            sum+=Feature.at<int>(i,j);
    aver=sum/(mm*nn);
    //  printf("sum=%lf,aver=%lf",sum,aver);
    //第4步：計算像素值與平均值大小關系。同時得到特征矩陣FeatureResult，並傳回。
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
    //分析特征！！！

    /*
    //測試：顯示下特征值是否能夠正確取得。
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
    //測試：顯示下特征值是否能夠正確取得。
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
    //讀取檔案到srcImage內，然後分析特征。
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
    //測試下特征分析情況。
    for(i=0;i<fileNumber;i++)
    {
        printf("\n%d:",i);
        for(j=0;j<featureNumber;j++)
            printf("%5d",FileFeature[i][j]);
    }
*/
    QMessageBox::about(NULL, "提示", "特征分析完畢！！！");//, QMessageBox::Yes | QMessageBox::No, QMessageBox::Yes);

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
    //設定路徑，這裡設定好要讀取的路徑，並且能夠將路徑下的圖片隨機地顯示在下面。
    QString path = QFileDialog::getExistingDirectory();
    //顯示目前選取的資料夾
    //  QMessageBox::information(NULL, "檔案路徑", path, QMessageBox::Yes | QMessageBox::No, QMessageBox::Yes);
    // QMessageBox::information(NULL, "檔案路徑", "設定完畢！！！", QMessageBox::Yes | QMessageBox::No, QMessageBox::Yes);


    QDir *dir=new QDir(path);
    //過濾掉檔名”.",和檔名"..".
    dir->setFilter(QDir::Files | QDir::NoSymLinks);
    QStringList filter;
    //filter<<"*.dat";
    //dir->setNameFilters(filter);
    //QList<QFileInfo> *fileInfo=new QList<QFileInfo>(dir->entryInfoList(filter));
    fileInfo=new QList<QFileInfo>(dir->entryInfoList(filter));
    // QString s;//=fileInfo->at(0).fileName();

    // QString dirS;  //包括一個目錄的路徑；
    total=fileInfo->count();
    //讀取目前目錄下檔案的個數
    //QMessageBox::information(NULL, "檔案路徑",QString::number(n), QMessageBox::Yes | QMessageBox::No, QMessageBox::Yes);
    // printf("%d",n);
    int i;
    /*
     //下面的想法是檢查圖形，然後在label內顯示。
     //這種想法不好在於label的名字處理困難。
    for(i=0;i<n;i++)
    {
        s=fileInfo->at(i).fileName();
        //呼叫發現，i需要從2開始，到n+2而結束。
        //這裡i=0時，檔名是”.“
        //i=1時，檔名是"..".
        //q強迫使用i從2開始，到n+2結束，不好用！
        // QMessageBox::information(NULL, "檔案路徑", QString::number(i).append(s), QMessageBox::Yes | QMessageBox::No, QMessageBox::Yes);
        dirS="image//";
        dirS=dirS.append(s);
        //測試檔名是否顯示正確。
       // QMessageBox::information(NULL, "檔案路徑", dirS, QMessageBox::Yes | QMessageBox::No, QMessageBox::Yes);
        QTextCodec *code = QTextCodec::codecForName("gb18030");
        std::string name = code->fromUnicode(dirS).data();
        srcImage = cv::imread(name);
         cv::cvtColor(srcImage,srcImage,CV_BGR2RGB);
       //測試是否能顯示圖形！
        //imshow("dd",srcImage);
        //waitKey();

        showLabel(srcImage,ui->label2);
    }
    //上面的想法是檢查圖形，然後在label內顯示。
    */
    //對每個label進行處理，隨機顯示一個目前確定目錄下的圖形
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
    //產生無重復的陣列；
    srand(time(NULL));
    int output[100]={0};
    int m;
    for(i=0; i<total; i++)
    {
        while(output[m=rand()%total])
            ;
        output[m] = i;
    }
    //上述處理過程中，不會出現值為0的陣列元素，下面隨機將0處理一下，放到某個陣列元素內。
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
    QString dirS;  //包括一個目錄的路徑；
    s=fileInfo->at(i).fileName();
    //呼叫發現，i需要從2開始，到n+2而結束。
    //這裡i=0時，檔名是”.“
    //i=1時，檔名是"..".
    //q強迫使用i從2開始，到n+2結束，不好用！
    // QMessageBox::information(NULL, "檔案路徑", QString::number(i).append(s), QMessageBox::Yes | QMessageBox::No, QMessageBox::Yes);
    dirS="image//";
    dirS=dirS.append(s);
    //測試檔名是否顯示正確。
    // QMessageBox::information(NULL, "檔案路徑", dirS, QMessageBox::Yes | QMessageBox::No, QMessageBox::Yes);
    QTextCodec *code = QTextCodec::codecForName("gb18030");
    std::string name = code->fromUnicode(dirS).data();
    srcImage = cv::imread(name);
    cv::cvtColor(srcImage,srcImage,CV_BGR2RGB);
}
//產生無重復的隨機數：
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
    //搜尋按鈕，主要完成檢索圖形的特征分析、特征比對、排序
    int t2[mm*nn];
    getFeature(srcImage,t2);
    /*
    //測試一下能否讀取特征值。
    for(int j=0;j<featureNumber;j++)
    {
            printf("%5d",t2[j]);
    }
    */
    /*
    //測試FileFeature是否正確讀取
    for(int i=0;i<fileNumber;i++)
    {
        printf("\n%d:",i);
        for(int j=0;j<featureNumber;j++)
            printf("%5d",FileFeature[i][j]);
    }
    */
    //相同特征值的數量。
    int sameCount[fileNumber]={0};//忘記起始化，罪過！！！
    //和目錄下圖片逐一比較，並得出相同的位數的個數。
    for(int i=0;i<fileNumber;i++)
        for(int j=0;j<featureNumber;j++)
        {
            sameCount[i]+=FileFeature[i][j]*t2[j];
            //犯了弱智錯誤，寫成了：sameCount[fileNumber]+=FileFeature[i][j]*t2[j];
            /*
            //c測試敘述，開始samecount內總是得到0，測試一下。
            if(FileFeature[i][j]*t2[j])
                printf("ok");
                */
        }
    /*
    for(int i=0;i<fileNumber;i++)
        printf("%d\n",sameCount[i]);
        */
    //將個數最多的fileNumber個找出來
    int maxi[8]={0};
    for(int i=0;i<8;i++)
    {
        int max=sameCount[0];
        for(int j=0;j<fileNumber;j++)
        {
            if(max<sameCount[j])
            {
                max=sameCount[j];
                // 犯了弱智錯誤，寫成了：maxi[fileNumber]=j;
                maxi[i]=j;
            }
        }
        sameCount[maxi[i]]=0;//避免重復計算最大值，將上次最大值置零，再次求最大值。

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
