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

void MainWindow::on_actionTest_triggered()
{
    /*  int M=512;
    int N=512;*/
    //不使用變數，使用define定義
    float chaoticF[M*N];
    chaoticF[0]=0.991;
    int i=0;
    int flag=0;   //這裡出錯了，因為int整數65536，超過了大小了。  用來檢查陣列
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
        //上述隨機數沒有起作用？？？？
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
    //黑白二色的混沌圖形
    float chaotic[M*N];
    double t;
    bool isOK;
    QString text=QInputDialog::getText(NULL, "混沌初值",
                                       "請輸入初值",
                                       QLineEdit::Normal,
                                       "0.98",
                                       &isOK);
    //混沌序列賦初值
    if(isOK)
    {
        t=text.toDouble();
    }
    else
        t=0.98;
    chaotic[0]=t;
    int i;
    //產生混沌序列
    for(i=1;i<M*N;i++)
        chaotic[i]=1-2*chaotic[i-1]*chaotic[i-1];
    //將混沌序列二值化，只有0和255兩個值。
    for(i=0;i<M*N;i++)
        if(chaotic[i]>0)
            chaotic[i]=255;
        else
            chaotic[i]=0;
    //建立一個混沌圖形
    Mat chaoticImg(M,N,CV_8UC1);
    //imshow("test",chaoticImg);
    int flag=0;
    /*
     * 用指標模式給予值。
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
    //將混沌序列給予值給混沌圖形
    for(int y=0;y<M;y++)
        for(int x=0;x<N;x++)
        {
            chaoticImg.at<uchar>(y,x)=chaotic[flag];
            flag++;
        }
    //呼叫函數 showLabelGray 顯示混沌圖形
    showLabelGray(chaoticImg,ui->label2);
    /*
     * 自訂顯示函數
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
    //灰階混沌圖形。
    float chaotic[M*N];
    double t;
    bool isOK;
    QString text=QInputDialog::getText(NULL, "混沌初值",
                                       "請輸入初值",
                                       QLineEdit::Normal,
                                       "0.98",
                                       &isOK);
    //混沌賦初值
    if(isOK)
    {
        t=text.toDouble();
    }
    else
        t=0.98;
    chaotic[0]=t;
    int i;
    //給整個混沌序列給予值
    for(i=1;i<M*N;i++)
        chaotic[i]=1-2*chaotic[i-1]*chaotic[i-1];
    int tmp;
    //處理為256個灰階級
    for(i=0;i<M*N;i++)
    {
        tmp=chaotic[i]*1000000;
        chaotic[i]=tmp%256;
    }
    //定義一個灰階圖形
    Mat chaoticImg(M,N,CV_8UC1);
    int flag=0;
    //將混沌序列的值賦給灰階圖形
    for (int y=0; y<M; y++)
    {
        uchar* chaoticImgR  = chaoticImg.ptr<uchar>(y);
        for (int x=0; x<N; x++)
        {
            chaoticImgR[x]=chaotic[flag];
            flag++;
        }
    }
    //呼叫函數showLabelGray,顯示混沌圖形
    showLabelGray(chaoticImg,ui->label2);
}

void MainWindow::on_myColor_triggered()
{
    //彩色混沌圖形
    //定義一個陣列，用來儲存混沌序列
    float chaotic[M*N*3];
    double t;
    bool isOK;
    QString text=QInputDialog::getText(NULL, "混沌初值",
                                       "請輸入初值",
                                       QLineEdit::Normal,
                                       "0.98",
                                       &isOK);
    //混沌賦初值
    if(isOK)
    {
        t=text.toDouble();
    }
    else
        t=0.98;
    chaotic[0]=t;
    int i;
    //混沌序列給予值
    for(i=1;i<M*N*3;i++)
        chaotic[i]=1-2*chaotic[i-1]*chaotic[i-1];
    int tmp;
    //混沌序列處理為256級
    for(i=0;i<M*N*3;i++)
    {
        tmp=chaotic[i]*10000;
        chaotic[i]=tmp%256;
    }
    //定義混沌圖形
    Mat chaoticImg(M,N,CV_8UC3);
    //將混沌序列的值賦給混沌圖形
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
    //定義一個專門用於顯示的圖形
    Mat chaoticImgShow;
    chaoticImg.copyTo(chaoticImgShow);
    //色彩空間轉換
    cv::cvtColor(chaoticImgShow,chaoticImgShow,COLOR_BGR2RGB);
    //cv::cvtColor(chaoticImgShow,chaoticImgShow,CV_BGR2RGB);
    //cvtColor中使用參數CV_BGR2RGB，也可以，其是OpenCV2.0的標准。
    //呼叫函數showLabel顯示混沌圖形。
    showLabel(chaoticImgShow,ui->label2);
}
void MainWindow::creatChaoticImage(float init)
{
    //取得原始圖形的大小
    int MM,NN;
    MM=srcImage.rows;
    NN=srcImage.cols;
    //定義一個陣列，從初混沌值
    float chaotic[MM*NN*3];
    //混沌系統賦初值
    chaotic[0]=init;
    int i;
    //計算混沌序列的值
    for(i=1;i<MM*NN*3;i++)
        chaotic[i]=1-2*chaotic[i-1]*chaotic[i-1];
    int tmp;
    //將混沌序列的值調整為8位像素值區間即：[0,255]
    for(i=0;i<MM*NN*3;i++)
    {
        tmp=chaotic[i]*10000;
        chaotic[i]=tmp%256;
    }
    //定義一個混沌圖形
    Mat chaoticImgT(MM,NN,CV_8UC3);
    //給混沌圖形賦初值
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
    //將計算得到的值賦給全局圖形變數，chaoticImg
    chaoticImgT.copyTo(chaoticImg);
}

void MainWindow::on_cryp_triggered()
{

}

void MainWindow::on_deCryp_triggered()
{
    //讀入需要解密的圖形
    QString filename = QFileDialog::getOpenFileName(this,tr("開啟要解密的圖形"),"",tr("Image File(*.bmp *.jpg *.jpeg *.png)"));
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
    //讀取混沌初值，用於產生混沌圖形
    double t;
    bool isOK;
    QString text=QInputDialog::getText(NULL, "混沌初值",
                                       "請輸入初值",
                                       QLineEdit::Normal,
                                       "0.98",
                                       &isOK);
    //將讀取的值賦給變數t，若果沒有讀到，令t=0.98
    if(isOK)
    {
        t=text.toDouble();
    }
    else
        t=0.98;
    //呼叫函數creatChaoticImage產生混沌圖形chaoticImg，參數為t。
    creatChaoticImage(t);
    //用混沌圖形(chaoticImg)與加密圖形（srcImage)進行互斥，實現解密
    bitwise_xor(srcImage,chaoticImg,dstImage);
    //將解密結果的圖形顯示在label2上
    showLabel(dstImage,ui->label2);
    //儲存解密後圖形
    QString fileName = QFileDialog::getSaveFileName(this,
                                                    tr("儲存解密後的圖形"),
                                                    "",
                                                    tr("image (*.bmp)"));
    Mat m(srcImage.size(),CV_8UC3);
    dstImage.copyTo(m);
    img = QImage((const unsigned char*)(m.data),m.cols,m.rows,m.cols*m.channels(), QImage::Format_RGB888);
    img.save(fileName);
    /*  不使用互斥函數bitwise_xor完成互斥動作。
    int MM,NN;
    MM=srcImage.rows;
    NN=srcImage.cols;
    float chaotic[MM*NN];
    Mat deCrypImage(srcImage.size(),CV_8UC3);
    //解密圖形，大小與加密圖形srcImage一致。
    //這裡首先選取加密圖形，經由on_openCustomeFile_triggered()載入後，其名稱為srcImage，需要注意名字不是dstImage。
    // srcImage.copyTo(dstImage);  //這裡給dstImage給予值，為的是能夠確保其大小 與srcImage一致。
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
    //讀入原始需要加密圖形
    QString filename = QFileDialog::getOpenFileName(this,tr("開啟要加密圖形"),"",tr("Image File(*.bmp *.jpg *.jpeg *.png)"));
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
        //cv::cvtColor(srcImage,srcImage,CV_BGR2RGB);
        cv::cvtColor(srcImage,srcImage,COLOR_BGR2RGB);
        img = QImage((const unsigned char*)(srcImage.data),srcImage.cols,srcImage.rows, srcImage.cols*srcImage.channels(), QImage::Format_RGB888);
        ui->label1->clear();
        img=  img.scaled(ui->label1->width(), ui->label1->height());
        ui->label1->setPixmap(QPixmap::fromImage(img));
    }
    //讀取混沌初值，用來產生混沌圖形
    double t;
    bool isOK;
    QString text=QInputDialog::getText(NULL, "混沌初值",
                                       "請輸入初值",
                                       QLineEdit::Normal,
                                       "0.98",
                                       &isOK);
    //取得剛剛輸入的值，作為混沌賦初值
    if(isOK)
    {
        t=text.toDouble();
    }
    else
        t=0.98;
    //呼叫函數creatChaoticImage,用t作為混沌初值，產生混沌圖形chaoticImg。
    creatChaoticImage(t);
    //完成圖形互斥加密
    bitwise_xor(srcImage,chaoticImg,dstImage);
    //顯示加密後的圖形
    showLabel(dstImage,ui->label2);
    //儲存加密後圖形
    QString fileName = QFileDialog::getSaveFileName(this,
                                                    tr("儲存加密後的圖形"),
                                                    "",
                                                    tr("image (*.bmp)"));  //需要儲存為bmp格式，若果是其他格式，可能無法解密。
    Mat m(srcImage.size(),CV_8UC3);
    dstImage.copyTo(m);
    img = QImage((const unsigned char*)(m.data),m.cols,m.rows,m.cols*m.channels(), QImage::Format_RGB888);
    img.save(fileName);

    /*
     *CxXor函數是低版本的，若果使用OpenCV3.0以下版本，請使用該函數實現。
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
    CvArr* r=(CvArr*)&srcImage;  //不能使const型態
    // cvXor(s,t,r);
    */
    //====================================================================================
    /*  不使用互斥函數bitwise_xor完成互斥動作。
    int MM,NN;
    MM=srcImage.rows;
    NN=srcImage.cols;
    float chaotic[MM*NN];
    // Mat dstImage(srcImage.size(),CV_8UC3);
    srcImage.copyTo(dstImage);  //這裡給dstImage給予值，為的是能夠確保其大小 與srcImage一致。
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
                                                    tr("儲存加密後的圖形"),
                                                    "",
                                                    tr("image (*.bmp)"));  //需要儲存為bmp格式，若果是其他格式，可能無法解密。
    Mat m(srcImage.size(),CV_8UC3);
    dstImage.copyTo(m);
    img = QImage((const unsigned char*)(m.data),m.cols,m.rows,m.cols*m.channels(), QImage::Format_RGB888);
    img.save(fileName);
    */
}

void MainWindow::on_Sencryp_triggered()
{

    //匯入原始需要加密圖形
    QString filename = QFileDialog::getOpenFileName(this,tr("開啟要加密圖形"),"",tr("Image File(*.bmp *.jpg *.jpeg *.png)"));
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
    //讀取混沌初值，用於產生混沌圖形
    double t;
    bool isOK;
    QString text=QInputDialog::getText(NULL, "混沌初值",
                                       "請輸入初值",
                                       QLineEdit::Normal,
                                       "0.98",
                                       &isOK);
    //取得輸入的初值，將其賦給t。
    if(isOK)
    {
        t=text.toDouble();
    }
    else
        t=0.98;
    //取得原始圖形的長和寬
    int MM,NN;
    int i,j;
    MM=srcImage.rows;
    NN=srcImage.cols;
    //定義一個混沌序列
    double *chaotic=new double[MM*NN*3];
    //定義一個混沌有序序列
    double *chaoticSort=new double[MM*NN*3];
    //定義一個索引序列
    int *chaoticIndex=new int[MM*NN*3];
    //混沌初值給予值
    chaotic[0]=t;
    //產生混沌序列
    for(i=1;i<MM*NN*3;i++)
        chaotic[i]=1-2*chaotic[i-1]*chaotic[i-1];
    //起始化chaoticSort
    memcpy(chaoticSort,chaotic,MM*NN*3*sizeof(double));
    //memcpy(chaoticSort,chaotic,MM*NN*3*8);
    //double型態占8個位元組
    //對chaoticSort進行排序
    std::sort(chaoticSort,chaoticSort+MM*NN*3);
    /*   測試
    for(i=4000;i<4090;i++)
        QMessageBox::about(NULL,"number",QString::number(chaoticSort[i]));
    */
    //產生索引序列，計算chaoticSort在chaotic內的位置訊息
    for(i=0;i<MM*NN*3;i++)
    {
        for(j=0;j<MM*NN*3;j++)
            if(chaoticSort[i]==chaotic[j])
                chaoticIndex[i]=j;
    }
    // int *test=new int[MM*NN*3];
    /*
    * 測試。用於將原圖形整體反向排序,即實現圖形的旋轉。
    for(i=0;i<MM*NN*3;i++)
    {
        chaoticIndex[i]=MM*NN*3-1-i;
    }
    */
    /*
     * 測試chaoticIndex內的資料
    for(i=0;i<100;i++)
        QMessageBox::about(NULL,"number",QString::number(chaoticIndex[i]));
    */

    int flag=0;
    srcImage.copyTo(dstImage);
    //這裡給dstImage給予值，為的是能夠確保其大小 與srcImage一致。
    /*
    * 測試一下
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
     * 測試chaoticIndex內的資料
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
             * 其他可能的計算模式
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
    //顯示加密圖形
    showLabel(dstImage,ui->label2);
    //儲存圖形。
    //需要儲存為bmp格式，若果是其他格式，可能無法解密。
    QString fileName = QFileDialog::getSaveFileName(this,
                                                    tr("儲存加密後的圖形"),
                                                    "",
                                                    tr("image (*.bmp)"));

    Mat m(srcImage.size(),CV_8UC3);
    dstImage.copyTo(m);
    img = QImage((const unsigned char*)(m.data),m.cols,m.rows,m.cols*m.channels(), QImage::Format_RGB888);
    img.save(fileName);
}

void MainWindow::on_Sdecryp_triggered()
{
    //匯入原始需要加密圖形
    QString filename = QFileDialog::getOpenFileName(this,tr("開啟要解密圖形"),"",tr("Image File(*.bmp *.jpg *.jpeg *.png)"));
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
    //輸入混沌初值，產生混沌圖形
    double t;
    bool isOK;
    QString text=QInputDialog::getText(NULL, "混沌初值",
                                       "請輸入初值",
                                       QLineEdit::Normal,
                                       "0.98",
                                       &isOK);
    if(isOK)
    {
        t=text.toDouble();
    }
    else
        t=0.98;
    //取得讀入圖形大小，用於建構混沌陣列使用
    int MM,NN;
    int i,j;
    MM=srcImage.rows;
    NN=srcImage.cols;
    //定義一個混沌序列
    double *chaotic=new double[MM*NN*3];
    //定義一個混沌有序序列
    double *chaoticSort=new double[MM*NN*3];
    //定義一個索引序列
    int *chaoticIndex=new int[MM*NN*3];
    //混沌陣列賦初值
    chaotic[0]=t;
    //產生混沌序列
    for(i=1;i<MM*NN*3;i++)
        chaotic[i]=1-2*chaotic[i-1]*chaotic[i-1];
    memcpy(chaoticSort,chaotic,MM*NN*3*sizeof(double));
    // memcpy(chaoticSort,chaotic,MM*NN*3*8);
    //double型態占8個位元組
    //對chaoticSort進行排序
    std::sort(chaoticSort,chaoticSort+MM*NN*3);
    /*
    for(i=4000;i<4090;i++)
        QMessageBox::about(NULL,"number",QString::number(chaoticSort[i]));
    */
    //產生索引序列，計算chaoticSort在chaotic內的位置訊息
    for(i=0;i<MM*NN*3;i++)
    {
        for(j=0;j<MM*NN*3;j++)
            if(chaoticSort[i]==chaotic[j])
                chaoticIndex[i]=j;
    }
    //int *test=new int[MM*NN*3];
    /*
     * 測試。用於將原圖形整體反向排序

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
    srcImage.copyTo(dstImage);  //這裡給dstImage給予值，為的是能夠確保其大小 與srcImage一致。
    /*
     * 測試一下
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
    //解密過程
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
             * 其他可能計算模式
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
    //顯示解密圖形
    showLabel(dstImage,ui->label2);
    //需要儲存為bmp格式，若果是其他格式，可能無法解密。
    QString fileName = QFileDialog::getSaveFileName(this,
                                                    tr("儲存解密後的圖形"),
                                                    "",
                                                    tr("image (*.bmp)"));
    //用於儲存
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
    //注意插值模式，若果采用預設模式：cv::resize(m, m,dsize),圖形拉遠後的圖形失真嚴重。
    img = QImage((const unsigned char*)(m.data),m.cols,m.rows,m.cols*m.channels(), QImage::Format_Indexed8);
    l->clear();
    //  img=img.scaled(l->width(),l->height());
    l->setPixmap(QPixmap::fromImage(img));
}
