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
//  版權訊息：  lilizong[at]gmail.com
MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    int T[10][3][3]={
        //若果不希望再次處理，可以直接在建立陣列時，將1改為255即可。
        //0個白點
        {0,0,0,
         0,0,0,
         0,0,0},
        //1個白點
        {0,0,0,
         0,1,0,
         0,0,0},
        //2個白點
        {1,0,0,
         0,0,0,
         0,0,1},
        //3個白點
        {1,0,0,
         0,1,0,
         0,0,1},
        //4個白點
        {1,0,1,
         0,0,0,
         1,0,1},
        //5個白點
        {1,0,1,
         0,1,0,
         1,0,1},
        //6個白點
        {1,1,1,
         0,0,0,
         1,1,1},
        //7個白點
        {1,0,1,
         1,1,1,
         1,0,1},
        //8個白點
        {1,1,1,
         1,0,1,
         1,1,1},
        //9個白點
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
//開啟目前目錄下的lena.jpg圖形。
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
        //將目前開啟的圖形顯示在左側的標簽內。
        //先進行圖形轉換
        cv::cvtColor(srcImage,srcImage,CV_BGR2RGB);
        //將轉換後的圖形賦給img
        img = QImage((const unsigned char*)(srcImage.data),srcImage.cols,srcImage.rows, srcImage.cols*srcImage.channels(), QImage::Format_RGB888);
        //label1清理
        ui->label1->clear();
        //調整圖形大小以適應標簽大小。
        img=  img.scaled(ui->label1->width(), ui->label1->height());
        //讓img顯示在label1內
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

void MainWindow::on_actionTest_triggered()
{
    //這裡是測試函數，開始在【幫助】選單下實現，後來選單移除，該函數保留。
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
        //若果不希望再次處理，可以直接在建立陣列時，將1改為255即可。
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
    //注意，確保是二值圖形，否則不能顯示。或是把1變更為255也可。



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
    //   cv::resize(Feature,Feature,cv::Size(ui->label2->width()/3,ui->label2->height()/3));  //Size的取得，需要注意格式，從Qsize轉為cv::size
    //  imshow(",",Feature);
    //自己計算的，可以使用resize直接計算Feature。
    /*for(i=0;i<X;i++)
        for(j=0;j<Y;j++)
            Feature.at<uchar>(X/(M/3),Y/(N/3))+=srcImage.at<uchar>(i,j);
            */
    //cv::resize(Feature,Feature,Size(ui->label2->height()+1,ui->label2->width()+1)); //都加上1，確保能夠都有特征
    // imshow(",",Feature);
    /*
    img = QImage((const unsigned char*)
                 (Feature.data),Feature.cols,Feature.rows,Feature.cols*Feature.channels(),
                 QImage::Format_RGB888);
    img=img.scaled(ui->label2->size());
    ui->label2->setPixmap(QPixmap::fromImage(img));
    */
    //   imshow(",2",Feature);
    // cv::resize(Feature,Feature,cv::Size((Feature.rows+2)/3,(Feature.cols+2)/3),0,0,3);  //加上2確保每個都有特征！！！前面加1不對
    //  imshow(",",Feature);
    //imshow("dd",srcImage);
    //cv::Size dsize=cv::Size((srcImage.rows+2)/3,(srcImage.cols+2)/3);
    //cv::Size dsize=cv::Size(111,111);
    //cv::resize(srcImage,srcImage,dsize,0,0,CV_INTER_LINEAR);  //加上2確保每個都有特征！！！前面加1不對
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
    //定義特征矩陣
    Mat Feature((X+2)/3,(Y+2)/3,CV_8UC(1), Scalar::all(0));
    //定義目的圖形（骰子畫）
    Mat dstImage(X,Y,CV_8UC(1), Scalar::all(0));
    Mat srcImage2;
    //灰階化
    cvtColor(srcImage,srcImage2,CV_BGR2GRAY);
    //自己計算Feature。
    //也可以定義一個陣列，先求和，然後再求平均值。
    for(i=0;i<X;i++)
        for(j=0;j<Y;j++)
            Feature.at<uchar>(i/3,j/3)+=srcImage2.at<uchar>(i,j)/9;
    /*
     * 看下特征圖形什麼樣
    namedWindow( "fea", CV_WINDOW_AUTOSIZE );
    imshow("fea",Feature);
    */
    for(i=0;i<X/3;i++)
        for(j=0;j<Y/3;j++)
            Feature.at<uchar>(i,j)/=((255/9)*9)/9;
    //定義用來表示骰子的陣列
    int T[10][3][3]={
        //若果不希望再次處理，可以直接在建立陣列時，將1改為255即可。
        //0個白點
        {0,0,0,
         0,0,0,
         0,0,0},
        //1個白點
        {0,0,0,
         0,1,0,
         0,0,0},
        //2個白點
        {1,0,0,
         0,0,0,
         0,0,1},
        //3個白點
        {1,0,0,
         0,1,0,
         0,0,1},
        //4個白點
        {1,0,1,
         0,0,0,
         1,0,1},
        //5個白點
        {1,0,1,
         0,1,0,
         1,0,1},
        //6個白點
        {1,1,1,
         0,0,0,
         1,1,1},
        //7個白點
        {1,0,1,
         1,1,1,
         1,0,1},
        //8個白點
        {1,1,1,
         1,0,1,
         1,1,1},
        //9個白點
        {1,1,1,
         1,1,1,
         1,1,1},
    };
    //映射
    for(i=0;i<dstImage.rows;i++)
        for(j=0;j<dstImage.cols;j++)
            dstImage.at<uchar>(i,j)=T[Feature.at<uchar>(i/3,j/3)][i%3][j%3];
    //設定值化處理
    threshold(dstImage,dstImage,0.5, 255,   THRESH_BINARY );
    cv::Size dsize=Size(ui->label2->width(),ui->label2->height());
    //縮放目的圖形
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
    //特征圖形
    Mat Feature((X+2)/3,(Y+2)/3,CV_8UC(1), Scalar::all(0));
    //骰子圖
    Mat dstImage(X,Y,CV_8UC(1), Scalar::all(0));
    //原始圖形的灰階圖形
    Mat srcImage2;
    //灰階化
    cvtColor(srcImage,srcImage2,CV_BGR2GRAY);
    for(i=0;i<X;i++)
        for(j=0;j<Y;j++)
            Feature.at<uchar>(i/3,j/3)+=srcImage2.at<uchar>(i,j)/9;
    //顯示下特征圖形
    // imshow("fea",Feature);
    //分析特征
    for(i=0;i<X/3;i++)
        for(j=0;j<Y/3;j++)
            Feature.at<uchar>(i,j)/=(255/10+1);  //或是...=((255/9)*9)/9;
    //骰子狀子塊
    int T[10][3][3]={
        //若果不希望再次處理，可以直接在建立陣列時，將1改為255即可。
        //0個白點
        {0,0,0,
         0,0,0,
         0,0,0},
        //1個白點
        {0,0,0,
         0,1,0,
         0,0,0},
        //2個白點
        {1,0,0,
         0,0,0,
         0,0,1},
        //3個白點
        {1,0,0,
         0,1,0,
         0,0,1},
        //4個白點
        {1,0,1,
         0,0,0,
         1,0,1},
        //5個白點
        {1,0,1,
         0,1,0,
         1,0,1},
        //6個白點
        {1,1,1,
         0,0,0,
         1,1,1},
        //7個白點
        {1,0,1,
         1,1,1,
         1,0,1},
        //8個白點
        {1,1,1,
         1,0,1,
         1,1,1},
        //9個白點
        {1,1,1,
         1,1,1,
         1,1,1},
    };
    //映射
    for(i=0;i<dstImage.rows;i++)
        for(j=0;j<dstImage.cols;j++)
            dstImage.at<uchar>(i,j)=T[Feature.at<uchar>(i/3,j/3)][i%3][j%3];
    //設定值化處理
    threshold(dstImage,dstImage,0.5, 255,   THRESH_BINARY );
    //顯示
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
    //定義特征矩陣
    Mat Feature((X+2)/3,(Y+2)/3,CV_8UC(1), Scalar::all(0));
    //定義目的圖形（骰子畫）
    Mat dstImage(X,Y,CV_8UC(1), Scalar::all(0));
    Mat srcImage2;
    //灰階化
    cvtColor(srcImage,srcImage2,CV_BGR2GRAY);
    //使用resize計算得到特征矩陣Feature。
    cv::Size dsize=Size(Feature.cols,Feature.rows);
    cv::resize(srcImage2,Feature,dsize);
    for(i=0;i<X/3;i++)
        for(j=0;j<Y/3;j++)
            Feature.at<uchar>(i,j)/=(255/9);
    //定義骰子
    int T[10][3][3]={
        //若果不希望再次處理，可以直接在建立陣列時，將1改為255即可。
        //0個白點
        {0,0,0,
         0,0,0,
         0,0,0},
        //1個白點
        {0,0,0,
         0,1,0,
         0,0,0},
        //2個白點
        {1,0,0,
         0,0,0,
         0,0,1},
        //3個白點
        {1,0,0,
         0,1,0,
         0,0,1},
        //4個白點
        {1,0,1,
         0,0,0,
         1,0,1},
        //5個白點
        {1,0,1,
         0,1,0,
         1,0,1},
        //6個白點
        {1,1,1,
         0,0,0,
         1,1,1},
        //7個白點
        {1,0,1,
         1,1,1,
         1,0,1},
        //8個白點
        {1,1,1,
         1,0,1,
         1,1,1},
        //9個白點
        {1,1,1,
         1,1,1,
         1,1,1},
    };
    //映射
    for(i=0;i<dstImage.rows;i++)
        for(j=0;j<dstImage.cols;j++)
            dstImage.at<uchar>(i,j)=T[Feature.at<uchar>(i/3,j/3)][i%3][j%3];
    //設定值化處理
    threshold(dstImage,dstImage,0.5, 255,   THRESH_BINARY );
    //視窗測試顯示
    // imshow("dst",dstImage);
    dsize=Size(ui->label2->width(),ui->label2->height());
    //縮放
    cv::resize(dstImage,dstImage,dsize);
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.step,  QImage::Format_Indexed8);
    ui->label2->clear();
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_horizen_triggered()
{
    //建立一個dsize，與label2相等
    cv::Size dsize=Size(ui->label2->width(),ui->label2->height());
    //定義h用於儲存label2的高度
    int h;
    //將label2的高度賦給h
    h=ui->label2->height();
    //定義目的圖形dstImage
    Mat dstImage(dsize,CV_8UC(1), Scalar::all(0));
    int i,j;
    //對dstImage內像素進行給予值
    for(i=0;i<dstImage.rows;i++)
        for(j=0;j<dstImage.cols;j++)
            dstImage.at<uchar>(i,j)=(i*255/h);
    //將img給予值
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.step,  QImage::Format_Indexed8);
    //清理label2
    ui->label2->clear();
    //將img賦給label2
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
    //建立一個dsize，與label2相等
    cv::Size dsize=Size(ui->label2->width(),ui->label2->height());
    //定義w用於儲存label2的寬度
    int w;
    //將label2的高度賦給w
    w=ui->label2->height();
    //定義目的圖形dstImage
    Mat dstImage(dsize,CV_8UC(1), Scalar::all(0));
    int i,j;
    //對dstImage內像素進行給予值
    for(i=0;i<dstImage.rows;i++)
        for(j=0;j<dstImage.cols;j++)
            dstImage.at<uchar>(i,j)=(j*255/w);
    //將img給予值
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.step,  QImage::Format_Indexed8);
    //清理label2
    ui->label2->clear();
    //將img賦給label2
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_circle_triggered()
{
    //建立一個dsize，與label2相等
    cv::Size dsize=Size(ui->label2->width(),ui->label2->height());
    //定義目的圖形dstImage
    Mat dstImage(dsize,CV_8UC(1), Scalar::all(0));
    int i,j;
    //對dstImage內像素進行給予值
    for(i=0;i<dstImage.rows;i++)
        for(j=0;j<dstImage.cols;j++)
            dstImage.at<uchar>(i,j)=int(sqrt(i*i+j*j))%255;
    //將img給予值
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.step,  QImage::Format_Indexed8);
    //清理label2
    ui->label2->clear();
    //將img賦給label2
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_mySum_triggered()
{
    //建立一個dsize，與label2相等
    cv::Size dsize=Size(ui->label2->width(),ui->label2->height());
    //定義目的圖形dstImage
    Mat dstImage(dsize,CV_8UC(1), Scalar::all(0));
    int i,j;
    //對dstImage內像素進行給予值
    for(i=0;i<dstImage.rows;i++)
        for(j=0;j<dstImage.cols;j++)
            dstImage.at<uchar>(i,j)=(i+j)%255;
    //將img給予值
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.step,  QImage::Format_Indexed8);
    //清理label2
    ui->label2->clear();
    //將img賦給label2
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_myAbstrct_triggered()
{
    //建立一個dsize，與label2相等
    cv::Size dsize=Size(ui->label2->width(),ui->label2->height());
    //定義目的圖形dstImage
    Mat dstImage(dsize,CV_8UC(1), Scalar::all(0));
    int i,j;
    //對dstImage內像素進行給予值
    for(i=0;i<dstImage.rows;i++)
        for(j=0;j<dstImage.cols;j++)
            dstImage.at<uchar>(i,j)=abs(i-j)%255;
    //將img給予值
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.step,  QImage::Format_Indexed8);
    //清理label2
    ui->label2->clear();
    //將img賦給label2
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_myTriple_triggered(bool checked)
{
    //建立一個dsize，與label2相等
    cv::Size dsize=Size(ui->label2->width(),ui->label2->height());
    //定義目的圖形dstImage
    Mat dstImage(dsize,CV_8UC(1), Scalar::all(0));
    int i,j;
    //對dstImage內像素進行給予值
    for(i=0;i<dstImage.rows;i++)
        for(j=0;j<dstImage.cols;j++)
            dstImage.at<uchar>(i,j)=i<j?i:j;
    //將img給予值
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.step,  QImage::Format_Indexed8);
    //清理label2
    ui->label2->clear();
    //將img賦給label2
    ui->label2->setPixmap(QPixmap::fromImage(img));
}


void MainWindow::on_myRand_triggered()
{
    //定義隨機數
    int key=0;
    srand(time(NULL));
    //給予值
    key=abs(rand()*10090%8);
    //得到label2的大小
    cv::Size dsize=Size(ui->label2->width(),ui->label2->height());
    //定義目的圖形
    Mat dstImage(dsize,CV_8UC(1), Scalar::all(0));
    int i,j;
    //產生隨機圖形
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
    //img給予值
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.step,  QImage::Format_Indexed8);
    //label2清理
    ui->label2->clear();
    //在label內顯示img
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_myIndex_triggered()
{
    //此部分的注解可以參考前面的骰子畫部分
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
    //不知道什麼原因：使用imshow顯示resize後的圖形總是錯的，但是後續計算是正確的！待解！！！！
    int T[10][3][3]={
        //若果不希望再次處理，可以直接在建立陣列時，將1改為255即可。
        //0個白點
        {0,0,0,
         0,0,0,
         0,0,0},
        //1個白點
        {0,0,0,
         0,1,0,
         0,0,0},
        //2個白點
        {1,0,0,
         0,0,0,
         0,0,1},
        //3個白點
        {1,0,0,
         0,1,0,
         0,0,1},
        //4個白點
        {1,0,1,
         0,0,0,
         1,0,1},
        //5個白點
        {1,0,1,
         0,1,0,
         1,0,1},
        //6個白點
        {1,1,1,
         0,0,0,
         1,1,1},
        //7個白點
        {1,0,1,
         1,1,1,
         1,0,1},
        //8個白點
        {1,1,1,
         1,0,1,
         1,1,1},
        //9個白點
        {1,1,1,
         1,1,1,
         1,1,1},
    };

    for(i=0;i<dstImage.rows;i++)
        for(j=0;j<dstImage.cols;j++)
            dstImage.at<uchar>(i,j)=T[j/3+i/3][i%3][j%3];
    threshold(dstImage,dstImage,0.5, 255,   THRESH_BINARY );
    // imshow("ad",dstImage);    //視窗顯示
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
    // imshow("ad",dstImage);    //視窗顯示
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
    // imshow("ad",dstImage);    //視窗顯示
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
    // imshow("ad",dstImage);    //視窗顯示
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
    // imshow("ad",dstImage);    //視窗顯示
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
    // imshow("ad",dstImage);    //視窗顯示
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
    //此部分的注解可以參考前面的骰子畫部分
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
    //不知道什麼原因：使用imshow顯示resize後的圖形總是錯的，但是後續計算是正確的！待解！！！！
    int T[10][3][3]={
        //若果不希望再次處理，可以直接在建立陣列時，將1改為255即可。
        //0個白點
        {0,0,0,
         0,0,0,
         0,0,0},
        //1個白點
        {0,0,0,
         0,1,0,
         0,0,0},
        //2個白點
        {1,0,0,
         0,0,0,
         0,0,1},
        //3個白點
        {1,0,0,
         0,1,0,
         0,0,1},
        //4個白點
        {1,0,1,
         0,0,0,
         1,0,1},
        //5個白點
        {1,0,1,
         0,1,0,
         1,0,1},
        //6個白點
        {1,1,1,
         0,0,0,
         1,1,1},
        //7個白點
        {1,0,1,
         1,1,1,
         1,0,1},
        //8個白點
        {1,1,1,
         1,0,1,
         1,1,1},
        //9個白點
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
    //該敘述用於測試key的值，開始總是不能出現key的正確值，原來key可能為負值
    //msgbox不能顯示。
    for(i=0;i<dstImage.rows;i++)
        for(j=0;j<dstImage.cols;j++)
            dstImage.at<uchar>(i,j)=T[key][i%3][j%3];
    threshold(dstImage,dstImage,0.5, 255,   THRESH_BINARY );
    // imshow("ad",dstImage);    //視窗顯示
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
    //此部分的注解可以參考前面的骰子畫部分
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
    //不知道什麼原因：使用imshow顯示resize後的圖形總是錯的，但是後續計算是正確的！待解！！！！
    int T[10][3][3]={
        //若果不希望再次處理，可以直接在建立陣列時，將1改為255即可。
        //0個白點
        {0,0,0,
         0,0,0,
         0,0,0},
        //1個白點
        {0,0,0,
         0,1,0,
         0,0,0},
        //2個白點
        {1,0,0,
         0,0,0,
         0,0,1},
        //3個白點
        {1,0,0,
         0,1,0,
         0,0,1},
        //4個白點
        {1,0,1,
         0,0,0,
         1,0,1},
        //5個白點
        {1,0,1,
         0,1,0,
         1,0,1},
        //6個白點
        {1,1,1,
         0,0,0,
         1,1,1},
        //7個白點
        {1,0,1,
         1,1,1,
         1,0,1},
        //8個白點
        {1,1,1,
         1,0,1,
         1,1,1},
        //9個白點
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
    //該敘述用於測試key的值，開始總是不能出現key的正確值，原來key可能為負值
    //msgbox不能顯示。
    for(i=0;i<dstImage.rows;i++)
        for(j=0;j<dstImage.cols;j++)
            dstImage.at<uchar>(i,j)=T[key][i%3][j%3];
    threshold(dstImage,dstImage,0.5, 255,   THRESH_BINARY );
    // imshow("ad",dstImage);    //視窗顯示
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
    //此部分的注解可以參考前面的骰子畫部分
    int i,j;
    cv::Size dsize=Size(3,3);
    Mat dstImage(dsize,CV_8UC(1), Scalar::all(0));
    //骰子狀子塊
    int T[10][3][3]={
        //若果不希望再次處理，可以直接在建立陣列時，將1改為255即可。
        //0個白點
        {0,0,0,
         0,0,0,
         0,0,0},
        //1個白點
        {0,0,0,
         0,1,0,
         0,0,0},
        //2個白點
        {1,0,0,
         0,0,0,
         0,0,1},
        //3個白點
        {1,0,0,
         0,1,0,
         0,0,1},
        //4個白點
        {1,0,1,
         0,0,0,
         1,0,1},
        //5個白點
        {1,0,1,
         0,1,0,
         1,0,1},
        //6個白點
        {1,1,1,
         0,0,0,
         1,1,1},
        //7個白點
        {1,0,1,
         1,1,1,
         1,0,1},
        //8個白點
        {1,1,1,
         1,0,1,
         1,1,1},
        //9個白點
        {1,1,1,
         1,1,1,
         1,1,1},
    };
    int key=n;
    //映射
    for(i=0;i<dstImage.rows;i++)
        for(j=0;j<dstImage.cols;j++)
            dstImage.at<uchar>(i,j)=T[key][i%3][j%3];
    //設定值化
    threshold(dstImage,dstImage,0.5, 255,   THRESH_BINARY );
    //視窗顯示
    // imshow("dst",dstImage);
    dsize=Size(ui->label2->width(),ui->label2->height());
    //調整大小
    cv::resize(dstImage,dstImage,dsize,0,0,0);
    //設定值化
    threshold(dstImage,dstImage,40, 255,   THRESH_BINARY );
    img = QImage((const unsigned char*)(dstImage.data),dstImage.cols,dstImage.rows,dstImage.step,  QImage::Format_Indexed8);
    ui->label2->clear();
    ui->label2->setPixmap(QPixmap::fromImage(img));
}

void MainWindow::on_aboutMe_triggered()
{
    QMessageBox::information(this,"關於",tr("本軟體為骰子作畫研讀系統，目前版本為1.0，由李立宗等人開發。"));
    return;
}

void MainWindow::on_contactUs_triggered()
{
    QMessageBox::information(this,"聯繫我們",tr("如有問題請聯繫：lilizong(at)Gmail。QQ群：QT+OpenCV，群號：107416004"));
    return;
}



void MainWindow::on_myTriple_triggered()
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
