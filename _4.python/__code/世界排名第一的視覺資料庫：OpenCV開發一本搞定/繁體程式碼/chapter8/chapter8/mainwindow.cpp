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
        msgBox.setText(tr("找不到資料"));
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
    QMessageBox::information(this,"版權",tr("本軟體版權所有者為：李立宗。若果使用，請聯繫：lilizong@gmail.com"));
}

void MainWindow::on_about_triggered()
{
    QMessageBox::information(this,"關於",tr("本軟體目前版本為1.0，由李立宗等人開發。若果有問題，歡迎聯繫：lilizong@gmail.com"));
    return;
}

void MainWindow::on_action_triggered()
{

}
void MainWindow::showLabel(Mat m, QLabel *l)
{
    //在label上顯示彩色圖形
    //   cv::cvtColor(m,m,COLOR_BGR2RGB);
    img = QImage((const unsigned char*)(m.data),m.cols,m.rows,m.cols*m.channels(), QImage::Format_RGB888);
    l->clear();
    img=img.scaled(l->width(),l->height());
    l->setPixmap(QPixmap::fromImage(img));
}
void MainWindow::showLabelGray(Mat m, QLabel *l)
{
    //在label上顯示灰階圖形
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
    //盲水印，最低有效位，內嵌過程
    //srcImage=imread("l64.jpg");//測試
    //讀取載體圖形
    QString filename = QFileDialog::getOpenFileName(this,tr("開啟原始圖形"),"",tr("Image File(*.bmp *.jpg *.jpeg *.png)"));
    QTextCodec *code = QTextCodec::codecForName("gb18030");
    std::string name = code->fromUnicode(filename).data();
    srcImage = cv::imread(name);
    if(!srcImage.data)
    {
        QMessageBox msgBox;
        msgBox.setText(tr("找不到資料"));
        msgBox.exec();
    }
    //取得圖形大小
    int MM,NN;
    MM=srcImage.rows;
    NN=srcImage.cols;
    //分割不同的色彩空間
    Mat bgr[3];
    split(srcImage, bgr);
    // cv::cvtColor(srcImage,srcImage,COLOR_BGR2RGB);
    //cvtColor( srcImage,srcImage, COLOR_RGB2GRAY );
    //讀取水印圖形
    filename = QFileDialog::getOpenFileName(this,tr("開啟水印圖形"),"",tr("Image File(*.bmp *.jpg *.jpeg *.png)"));
    //*code = QTextCodec::codecForName("gb18030");
    name = code->fromUnicode(filename).data();
    wmImage=imread(name,IMREAD_UNCHANGED );
    if(!wmImage.data)
    {
        QMessageBox msgBox;
        msgBox.setText(tr("找不到資料"));
        msgBox.exec();
    }
    //cvtColor( wmImage,wmImage, COLOR_RGB2GRAY );  //先轉換成灰階圖形
    Mat wmImageShow;  //該Mat專門用來顯示用。
    // threshold(wmImage,wmImageShow, 127, 255, THRESH_BINARY );
    wmImage.copyTo(wmImageShow);
    //將圖形轉為二值圖形，即將圖形內原來為255的像素點調整為1.
    threshold(wmImage,wmImage, 127, 1, THRESH_BINARY );   //保留最低位有效位LSB即可。
    //產生遮罩圖形，其值為254，即二進位的“1111 1110”。
    //Mat temp=Mat::ones(MM,NN,CV_8UC1);
    Mat t(MM,NN,CV_8UC1,254);
    t.copyTo(embedSrc);
    //將bgr[0]與t進行逐位元與，只保留bgr[0]的高7位，最低位置零
    cv::bitwise_and(bgr[0],t,embedSrc);
    //將水印圖形內嵌到載體圖形的最低位
    cv::bitwise_or(embedSrc,wmImage,embedSrc);
    //Mat t2(MM,NN,CV_8UC1,1);
    // cv::bitwise_and(embedSrc,t2,ExtractWM);
    //將含水印圖形賦給bgr[0]
    embedSrc.copyTo(bgr[0]);
    //群組合RGB圖形
    merge(bgr,3, embedSrc);
    //  threshold(ExtractWM,ExtractWM, 0, 255, THRESH_BINARY );
    //完成色彩空間轉換
    cv::cvtColor(srcImage,srcImage,COLOR_BGR2RGB);
    cv::cvtColor(embedSrc,embedSrc,COLOR_BGR2RGB);
    //cv::cvtColor(srcImage,srcImage,COLOR_BGR2RGB);
    //顯示載體圖形
    showLabel(srcImage,ui->label1);
    //顯示水印圖形
    showLabelGray(wmImageShow,ui->label2);
    //顯示含水印圖形
    showLabel(embedSrc,ui->label3);
    //儲存含水印圖形
    QString fileName = QFileDialog::getSaveFileName(this,
                                                    tr("儲存含水印圖形"),
                                                    "",
                                                    tr("image (*.bmp)"));  //需要儲存為bmp格式，若果是其他格式，可能無法解密。
    Mat m(srcImage.size(),CV_8UC3);
    embedSrc.copyTo(m);
    img = QImage((const unsigned char*)(m.data),m.cols,m.rows,m.cols*m.channels(), QImage::Format_RGB888);
    img.save(fileName);
}

void MainWindow::on_extract_triggered()
{
    //盲水印，最低有效位，分析過程
    //讀取含水印圖形
    QString filename = QFileDialog::getOpenFileName(this,tr("開啟含水印圖形"),"",tr("Image File(*.bmp *.jpg *.jpeg *.png)"));
    QTextCodec *code = QTextCodec::codecForName("gb18030");
    std::string name = code->fromUnicode(filename).data();
    srcImage = cv::imread(name);
    if(!srcImage.data)
    {
        QMessageBox msgBox;
        msgBox.setText(tr("找不到資料"));
        msgBox.exec();
    }
    //srcImage=imread("a.bmp");  //測試用
    //取得圖形大小
    int MM,NN;
    MM=srcImage.rows;
    NN=srcImage.cols;
    //分離圖形色彩空間
    Mat bgr[3];
    split(srcImage, bgr);
    //定義遮罩圖形，該圖形的值為1，即二進位的”0000 0001“
    Mat t(MM,NN,CV_8UC1,1);
    Mat embedSrcExtract;
    t.copyTo(embedSrcExtract);
    //將t與bgr[0]逐位元與，值保留rgb[0]的最低位
    cv::bitwise_and(bgr[0],t,ExtractWM);
    //定義一個t2，其值為254，即二進位的”1111 1110“
    Mat t2(MM,NN,CV_8UC1,254);
    //將bgr[0]與t2逐位元與，實現分析bgr[0]的高7位，即將水印剔除
    cv::bitwise_and(bgr[0],t2,bgr[0]);
    //合並RGB色彩空間
    merge(bgr,3, embedSrcExtract);
    //embedSrc色彩空間轉換
    cv::cvtColor(embedSrcExtract,embedSrcExtract,COLOR_BGR2RGB);
    //將分析出來的水印圖形，只有0和1兩個值，將1轉為255.
    threshold(ExtractWM,ExtractWM, 0, 255, THRESH_BINARY );
    //顯示讀取的含水印圖形
    showLabel(embedSrcExtract,ui->label4);
    //顯示分析出來的水印圖形
    showLabelGray(ExtractWM,ui->label5);
    /*
    //可以顯示原始載體圖形。
    //srcImage色彩空間轉換
    cv::cvtColor(srcImage,srcImage,COLOR_BGR2RGB);
    //顯示計算得到的不含水印的載體圖形
    showLabel(embedSrc,ui->label4);
    */
}

void MainWindow::on_NEmbed_triggered()
{
    //非盲水印，最低有效位，內嵌過程
    srcImage=imread("l64.jpg");
    int MM,NN;
    MM=srcImage.rows;
    NN=srcImage.cols;
    Mat bgr[3];

    split(srcImage, bgr);


    // cv::cvtColor(srcImage,srcImage,COLOR_BGR2RGB);
    //cvtColor( srcImage,srcImage, COLOR_RGB2GRAY );
    wmImage=imread("watermark.bmp",IMREAD_UNCHANGED );

    //cvtColor( wmImage,wmImage, COLOR_RGB2GRAY );  //先轉換成灰階圖形
    Mat wmImageShow;  //該Mat專門用來顯示用。
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
                                                    tr("儲存加密後的圖形"),
                                                    "",
                                                    tr("image (*.bmp)"));  //需要儲存為bmp格式，若果是其他格式，可能無法解密。
    Mat m(srcImage.size(),CV_8UC3);
    embedSrc.copyTo(m);
    img = QImage((const unsigned char*)(m.data),m.cols,m.rows,m.cols*m.channels(), QImage::Format_RGB888);
    img.save(fileName);

}

void MainWindow::on_NExtract_triggered()
{
    //非盲水印，最低有效位，分析過程
    //讀入原始圖形,分析其最低有效位
    srcImage=imread("l64.jpg");
    int MM,NN;
    MM=srcImage.rows;
    NN=srcImage.cols;
    Mat bgr[3];
    split(srcImage, bgr);
    Mat t(MM,NN,CV_8UC1,1);
    cv::bitwise_and(bgr[0],t,t);
    //讀取含水印圖形，分析其最低有效位
    embedSrc=imread("a.bmp");
    split(embedSrc, bgr);
    Mat t2(MM,NN,CV_8UC1,1);
    cv::bitwise_and(bgr[0],t2,t2);
    //將分析的兩個最低有效位進行互斥
    cv::bitwise_xor(t2,t,ExtractWM);
    threshold(ExtractWM,ExtractWM, 0, 255, THRESH_BINARY );
    //原始載體圖形
    cv::cvtColor(srcImage,srcImage,COLOR_BGR2RGB);
    showLabel(srcImage,ui->label4);
    showLabelGray(ExtractWM,ui->label5);
}

void MainWindow::on_Rcolor_triggered()
{
    //分解出R通道
    //繼續以RGB形式顯示該通道
    //讀取要分解的圖形
    QString filename = QFileDialog::getOpenFileName(this,tr("開啟原始圖形"),"",tr("Image File(*.bmp *.jpg *.jpeg *.png)"));
    QTextCodec *code = QTextCodec::codecForName("gb18030");
    std::string name = code->fromUnicode(filename).data();
    srcImage = cv::imread(name);
    if(!srcImage.data)
    {
        QMessageBox msgBox;
        msgBox.setText(tr("找不到資料"));
        msgBox.exec();
    }
    //srcImage=imread("l64.jpg");  //用於測試
    //取得圖形大小
    int MM,NN;
    MM=srcImage.rows;
    NN=srcImage.cols;
    //分離通道
    Mat bgr[3];
    split(srcImage, bgr);
    //將BG通道值置為0.
    Mat B(MM,NN,CV_8UC1, Scalar::all(0));
    Mat G(MM,NN,CV_8UC1, Scalar::all(0));
    B.copyTo(bgr[0]);
    G.copyTo(bgr[1]);
    srcImage.copyTo(dstImage);
    merge(bgr,3, dstImage);
    //轉換彩色通道順序，用於顯示
    cv::cvtColor(dstImage,dstImage,COLOR_BGR2RGB);
    //顯示圖形
    showLabel(dstImage,ui->label6);
}

void MainWindow::on_Gcolor_triggered()
{
    //分解出G通道
    //繼續以RGB形式顯示該通道
    //讀取要分解的圖形
    QString filename = QFileDialog::getOpenFileName(this,tr("開啟原始圖形"),"",tr("Image File(*.bmp *.jpg *.jpeg *.png)"));
    QTextCodec *code = QTextCodec::codecForName("gb18030");
    std::string name = code->fromUnicode(filename).data();
    srcImage = cv::imread(name);
    if(!srcImage.data)
    {
        QMessageBox msgBox;
        msgBox.setText(tr("找不到資料"));
        msgBox.exec();
    }
    //srcImage=imread("l64.jpg");  //用於測試
    //取得圖形大小
    int MM,NN;
    MM=srcImage.rows;
    NN=srcImage.cols;
    //分離通道
    Mat bgr[3];
    split(srcImage, bgr);
    //將BR通道值置為0.
    Mat B(MM,NN,CV_8UC1, Scalar::all(0));
    Mat R(MM,NN,CV_8UC1, Scalar::all(0));
    B.copyTo(bgr[0]);
    R.copyTo(bgr[2]);
    srcImage.copyTo(dstImage);
    merge(bgr,3, dstImage);
    //轉換彩色通道順序，用於顯示
    cv::cvtColor(dstImage,dstImage,COLOR_BGR2RGB);
    //顯示圖形
    showLabel(dstImage,ui->label6);
}

void MainWindow::on_Bcolor_triggered()
{
    //分解出R通道
    //繼續以RGB形式顯示該通道
    //讀取要分解的圖形
    QString filename = QFileDialog::getOpenFileName(this,tr("開啟原始圖形"),"",tr("Image File(*.bmp *.jpg *.jpeg *.png)"));
    QTextCodec *code = QTextCodec::codecForName("gb18030");
    std::string name = code->fromUnicode(filename).data();
    srcImage = cv::imread(name);
    if(!srcImage.data)
    {
        QMessageBox msgBox;
        msgBox.setText(tr("找不到資料"));
        msgBox.exec();
    }
    //srcImage=imread("l64.jpg");  //用於測試
    //取得圖形大小
    int MM,NN;
    MM=srcImage.rows;
    NN=srcImage.cols;
    //分離通道
    Mat bgr[3];
    split(srcImage, bgr);
    //將GR通道值置為0.
    Mat G(MM,NN,CV_8UC1, Scalar::all(0));
    Mat R(MM,NN,CV_8UC1, Scalar::all(0));
    G.copyTo(bgr[1]);
    R.copyTo(bgr[2]);
    srcImage.copyTo(dstImage);
    merge(bgr,3, dstImage);
    //轉換彩色通道順序，用於顯示
    cv::cvtColor(dstImage,dstImage,COLOR_BGR2RGB);
    //顯示圖形
    showLabel(dstImage,ui->label6);
}

void MainWindow::on_Rgrey_triggered()
{
    //分解出R通道
    //繼續以RGB形式顯示該通道
    //讀取要分解的圖形
    QString filename = QFileDialog::getOpenFileName(this,tr("開啟原始圖形"),"",tr("Image File(*.bmp *.jpg *.jpeg *.png)"));
    QTextCodec *code = QTextCodec::codecForName("gb18030");
    std::string name = code->fromUnicode(filename).data();
    srcImage = cv::imread(name);
    if(!srcImage.data)
    {
        QMessageBox msgBox;
        msgBox.setText(tr("找不到資料"));
        msgBox.exec();
    }
    //srcImage=imread("l64.jpg");  //用於測試
    //分解圖形
    Mat bgr[3];
    split(srcImage, bgr);
    //將分解出的圖形以灰階圖形形式顯示
    showLabelGray(bgr[2],ui->label6);
}

void MainWindow::on_Ggrey_triggered()
{
    //分解出G通道
    //繼續以RGB形式顯示該通道
    //讀取要分解的圖形
    QString filename = QFileDialog::getOpenFileName(this,tr("開啟原始圖形"),"",tr("Image File(*.bmp *.jpg *.jpeg *.png)"));
    QTextCodec *code = QTextCodec::codecForName("gb18030");
    std::string name = code->fromUnicode(filename).data();
    srcImage = cv::imread(name);
    if(!srcImage.data)
    {
        QMessageBox msgBox;
        msgBox.setText(tr("找不到資料"));
        msgBox.exec();
    }
    //srcImage=imread("l64.jpg");  //用於測試
    //分解圖形
    Mat bgr[3];
    split(srcImage, bgr);
    //將分解出的圖形以灰階圖形形式顯示
    showLabelGray(bgr[1],ui->label6);
}

void MainWindow::on_Bgrey_triggered()
{
    //分解出B通道
    //繼續以RGB形式顯示該通道
    //讀取要分解的圖形
    QString filename = QFileDialog::getOpenFileName(this,tr("開啟原始圖形"),"",tr("Image File(*.bmp *.jpg *.jpeg *.png)"));
    QTextCodec *code = QTextCodec::codecForName("gb18030");
    std::string name = code->fromUnicode(filename).data();
    srcImage = cv::imread(name);
    if(!srcImage.data)
    {
        QMessageBox msgBox;
        msgBox.setText(tr("找不到資料"));
        msgBox.exec();
    }
    //srcImage=imread("l64.jpg");  //用於測試
    //分解圖形
    Mat bgr[3];
    split(srcImage, bgr);
    //將分解出的圖形以灰階圖形形式顯示
    showLabelGray(bgr[0],ui->label6);
}




void MainWindow::on_BRembed_triggered()
{
    //盲水印，隨機位置內嵌水印訊息
    //讀取載體圖形
    QString filename = QFileDialog::getOpenFileName(this,tr("開啟原始載體圖形"),"",tr("Image File(*.bmp *.jpg *.jpeg *.png)"));
    QTextCodec *code = QTextCodec::codecForName("gb18030");
    std::string name = code->fromUnicode(filename).data();
    srcImage = cv::imread(name);
    if(!srcImage.data)
    {
        QMessageBox msgBox;
        msgBox.setText(tr("找不到資料"));
        msgBox.exec();
    }
    // srcImage=imread("l64.jpg");
    //取得圖形大小
    int M,N;
    M=srcImage.rows;
    N=srcImage.cols;
    //圖形通道分解
    Mat bgr[3];
    split(srcImage, bgr);
    //讀入水印圖形；
    filename = QFileDialog::getOpenFileName(this,tr("開啟水印圖形"),"",tr("Image File(*.bmp *.jpg *.jpeg *.png)"));
    name = code->fromUnicode(filename).data();
    wmImage = cv::imread(name,IMREAD_UNCHANGED);
    if(!wmImage.data)
    {
        QMessageBox msgBox;
        msgBox.setText(tr("找不到資料"));
        msgBox.exec();
    }
    //wmImage=imread("watermark.bmp",IMREAD_UNCHANGED );
    //cvtColor( wmImage,wmImage, COLOR_RGB2GRAY );  //先轉換成灰階圖形
    Mat wmImageShow;  //該Mat專門用來顯示用。
    wmImage.copyTo(wmImageShow);
    //調整二值水印圖形，將其中的值由255調整為1
    threshold(wmImage,wmImage, 127, 1, THRESH_BINARY );   //保留最低位有效位LSB即可。
    //產生混沌序列，用來決定水印內嵌在哪一位。混沌序列chaoticInt的值為0~7
    float chaoticF[M*N];
    //混沌系統初值
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
    chaoticF[0]=t;
    //chaoticF[0]=0.991;
    //產生混沌序列
    int i=0,j=0;
    for(i=1;i<M*N;i++)
        chaoticF[i]=1-2.0*chaoticF[i-1]*chaoticF[i-1];
    //產生內嵌位置序列，該序列內的值為[0,7)
    int chaoticInt[M*N];
    for(i=0;i<M*N;i++)
        chaoticInt[i]=abs((int)(chaoticF[i]*10000)%8);
    //chaoticInt[i]=abs((int)(chaoticF[i]*10000)%8)+1;   //位置從1開始計算。
    /*
    //測試一下值
    for(i=0;i<M*N;i=i+100)
       QMessageBox::about(NULL,"number",QString::number( chaoticInt[i]));
    */
    //m.at<uchar>(i,j)
    //內嵌水印
    //將特定位與水印訊息進行比較。
    //相同則什麼都不做。
    //若果不同，存在兩種情況。
    //情況1：載體圖形指定位置為1，將該位的1置為0，透過將該像素值減去2^n實現。
    //情況2：載體圖形指定位置為0，將該位的0置為1，透過將該像素值加上2^n實現。
    int flag=0;   //flag用來標示內嵌位置序列中的元素位置
    int n;            //n用來標示要內嵌的是第幾位
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
    //合並通道。
    merge(bgr,3, embedSrc);
    //通道順序轉換
    cv::cvtColor(srcImage,srcImage,COLOR_BGR2RGB);
    cv::cvtColor(embedSrc,embedSrc,COLOR_BGR2RGB);
    //顯示原始載體圖形
    showLabel(srcImage,ui->label1);
    //顯示水印圖形
    showLabelGray(wmImageShow,ui->label2);
    //顯示完成內嵌後的水印
    showLabel(embedSrc,ui->label3);
    //儲存圖形
    QString fileName = QFileDialog::getSaveFileName(this,
                                                    tr("儲存加密後的圖形"),
                                                    "",
                                                    tr("image (*.bmp)"));  //需要儲存為bmp格式，若果是其他格式，可能無法解密。
    Mat m(srcImage.size(),CV_8UC3);
    embedSrc.copyTo(m);
    img = QImage((const unsigned char*)(m.data),m.cols,m.rows,m.cols*m.channels(), QImage::Format_RGB888);
    img.save(fileName);
}

void MainWindow::on_BRextract_triggered()
{
    //盲水印，隨機位置分析水印訊息
    //讀取載體圖形
    QString filename = QFileDialog::getOpenFileName(this,tr("開啟含水印圖形"),"",tr("Image File(*.bmp *.jpg *.jpeg *.png)"));
    QTextCodec *code = QTextCodec::codecForName("gb18030");
    std::string name = code->fromUnicode(filename).data();
    srcImage = cv::imread(name);
    if(!srcImage.data)
    {
        QMessageBox msgBox;
        msgBox.setText(tr("找不到資料"));
        msgBox.exec();
    }
    //srcImage=imread("a.bmp");  //用於測試。
    //取得圖形大小
    int M,N;
    M=srcImage.rows;
    N=srcImage.cols;
    //分解RGB通道
    Mat bgr[3];
    split(srcImage, bgr);
    //產生混沌序列，用來決定水印內嵌在哪一位。混沌序列chaoticInt的值為0~7
    float chaoticF[M*N];
    double t;
    bool isOK;
    //取得混沌初值。
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
    chaoticF[0]=t;
    //chaoticF[0]=0.991;   //測試
    int i=0,j=0;
    for(i=1;i<M*N;i++)
        chaoticF[i]=1-2.0*chaoticF[i-1]*chaoticF[i-1];
    int chaoticInt[M*N];
    //得到
    for(i=0;i<M*N;i++)
        chaoticInt[i]=abs((int)(chaoticF[i]*10000)%8);   //最低位是0位，最高位是7位。
    //chaoticInt[i]=abs((int)(chaoticF[i]*10000)%8)+1;   //最低位是1位，最高位是8位。
    /*
    //測試一下值
    for(i=0;i<M*N;i=i+100)
       QMessageBox::about(NULL,"number",QString::number( chaoticInt[i]));
    */
    //m.at<uchar>(i,j)
    //分析水印
    //將R通道賦給ExtractWM
    bgr[0].copyTo(ExtractWM);
    //flag是混沌序列的索引序號
    int flag=0;
    //n是chaoticInt內的值，用來表示需要分析的位置。
    int n;
    //分析水印
    for(i=0;i<M;i++)
        for(j=0;j<N;j++)
        {
            n=chaoticInt[flag];
            ExtractWM.at<uchar>(i,j)=(bgr[0].at<uchar>(i,j)>>n)%2;
            flag++;
        }
    //二進位值轉為0和255兩個值。
    threshold(ExtractWM,ExtractWM, 0, 255, THRESH_BINARY );
    //顯示分析出水印訊息
    showLabelGray(ExtractWM,ui->label5);
    //進行色彩通道的順序轉換
    cv::cvtColor(srcImage,srcImage,COLOR_BGR2RGB);
    //顯示讀取的含水印載體圖形
    showLabel(srcImage,ui->label4);
    //將分析出來的水印圖形作為RGB圖形儲存
    QString fileName = QFileDialog::getSaveFileName(this,
                                                    tr("儲存分析出來的水印圖形"),
                                                    "",
                                                    tr("image (*.bmp)"));  //儲存為bmp格式
    cvtColor(ExtractWM,ExtractWM,COLOR_GRAY2RGB);
    Mat m(ExtractWM.size(),CV_8UC3);
    ExtractWM.copyTo(m);
    img = QImage((const unsigned char*)(m.data),m.cols,m.rows,m.cols*m.channels(), QImage::Format_RGB888);
    img.save(fileName);
}

void MainWindow::on_NBRembed_triggered()
{
    //非盲水印，隨機位置內嵌水印訊息
    srcImage=imread("l64.jpg");
    int M,N;
    M=srcImage.rows;
    N=srcImage.cols;
    Mat bgr[3];

    split(srcImage, bgr);


    // cv::cvtColor(srcImage,srcImage,COLOR_BGR2RGB);
    //cvtColor( srcImage,srcImage, COLOR_RGB2GRAY );
    wmImage=imread("watermark.bmp",IMREAD_UNCHANGED );

    //cvtColor( wmImage,wmImage, COLOR_RGB2GRAY );  //先轉換成灰階圖形
    Mat wmImageShow;  //該Mat專門用來顯示用。
    // threshold(wmImage,wmImageShow, 127, 255, THRESH_BINARY );
    wmImage.copyTo(wmImageShow);
    threshold(wmImage,wmImage, 127, 1, THRESH_BINARY );   //保留最低位有效位LSB即可。

    //產生混沌序列，用來決定水印內嵌在哪一位。混沌序列chaoticInt的值為0~7
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
    //測試一下值
    for(i=0;i<M*N;i=i+100)
       QMessageBox::about(NULL,"number",QString::number( chaoticInt[i]));
    */
    //m.at<uchar>(i,j)
    //內嵌水印
    //將特定位與水印訊息進行比較。
    int flag=0;
    int n;
    for(i=0;i<M;i++)
        for(j=0;j<N;j++)
        {
            n=chaoticInt[flag];
            if(((bgr[0].at<uchar>(i,j)>>n)%2)==1&&wmImage.at<uchar>(i,j)==1)
                bgr[0].at<uchar>(i,j)=bgr[0].at<uchar>(i,j)-pow(2,n);
            else if(((bgr[0].at<uchar>(i,j)>>n)%2)==0&&wmImage.at<uchar>(i,j)==1)    //必須使用else if，若果直接使用if，則會造成重復改變。
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
                                                    tr("儲存加密後的圖形"),
                                                    "",
                                                    tr("image (*.bmp)"));  //需要儲存為bmp格式，若果是其他格式，可能無法解密。
    Mat m(srcImage.size(),CV_8UC3);
    embedSrc.copyTo(m);
    img = QImage((const unsigned char*)(m.data),m.cols,m.rows,m.cols*m.channels(), QImage::Format_RGB888);
    img.save(fileName);
}

void MainWindow::on_NBRextract_triggered()
{
    //非盲水印，隨機位置分析水印訊息
    srcImage=imread("l64.jpg");
    int M,N;
    M=srcImage.rows;
    N=srcImage.cols;
    Mat bgr[3];
    split(srcImage, bgr);
    embedSrc=imread("a.bmp");
    Mat bgrWM[3];

    split(embedSrc, bgrWM);
    //產生混沌序列，用來決定水印內嵌在哪一位。混沌序列chaoticInt的值為0~7
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
    //測試一下值
    for(i=0;i<M*N;i=i+100)
       QMessageBox::about(NULL,"number",QString::number( chaoticInt[i]));
    */
    //m.at<uchar>(i,j)




    //分析水印
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
    //顯示讀取的含水印載體圖形
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
    //讀入原始圖形,分析其第0位（最低有效位）
    QString filename = QFileDialog::getOpenFileName(this,tr("開啟原始圖形"),"",tr("Image File(*.bmp *.jpg *.jpeg *.png)"));
    QTextCodec *code = QTextCodec::codecForName("gb18030");
    std::string name = code->fromUnicode(filename).data();
    srcImage = cv::imread(name);
    if(!srcImage.data)
    {
        QMessageBox msgBox;
        msgBox.setText(tr("找不到資料"));
        msgBox.exec();
    }
    //srcImage=imread("l64.jpg");  //用於測試
    //取得原始圖形的大小
    int MM,NN;
    MM=srcImage.rows;
    NN=srcImage.cols;
    //分解圖形
    Mat bgr[3];
    split(srcImage, bgr);
    //建立一個遮罩圖形，其值均為1,即二進位的“0000 0001”。
    Mat t(MM,NN,CV_8UC1,1);
    //將遮罩圖形與各個通道進行逐位元與，得到各個通道的第1位（最低有效位）
    cv::bitwise_and(bgr[0],t,bgr[0]);
    cv::bitwise_and(bgr[1],t,bgr[1]);
    cv::bitwise_and(bgr[2],t,bgr[2]);
    //設定值化，將大於0的值調整為255，以便於顯示。
    threshold(bgr[0],bgr[0], 0, 255, THRESH_BINARY );
    threshold(bgr[1],bgr[1], 0, 255, THRESH_BINARY );
    threshold(bgr[2],bgr[2], 0, 255, THRESH_BINARY );
    //群組合各個通道
    merge(bgr,3, dstImage);
    //threshold(dstImage,dstImage, 0, 255, THRESH_BINARY );
    //調整通道順序
    cv::cvtColor(dstImage,dstImage,COLOR_BGR2RGB);
    //顯示圖形
    showLabel(dstImage,ui->label6);
}

void MainWindow::on_one_triggered()
{
    //讀入原始圖形,分析其第1位
    QString filename = QFileDialog::getOpenFileName(this,tr("開啟原始圖形"),"",tr("Image File(*.bmp *.jpg *.jpeg *.png)"));
    QTextCodec *code = QTextCodec::codecForName("gb18030");
    std::string name = code->fromUnicode(filename).data();
    srcImage = cv::imread(name);
    if(!srcImage.data)
    {
        QMessageBox msgBox;
        msgBox.setText(tr("找不到資料"));
        msgBox.exec();
    }
    //srcImage=imread("l64.jpg");  //用於測試
    //取得原始圖形的大小
    int MM,NN;
    MM=srcImage.rows;
    NN=srcImage.cols;
    //分解圖形
    Mat bgr[3];
    split(srcImage, bgr);
    //建立一個遮罩圖形，其值均為2,即為二進位的“0000 0010”。
    Mat t(MM,NN,CV_8UC1,2);
    //將遮罩圖形與各個通道進行逐位元與，得到各個通道的第2位
    cv::bitwise_and(bgr[0],t,bgr[0]);
    cv::bitwise_and(bgr[1],t,bgr[1]);
    cv::bitwise_and(bgr[2],t,bgr[2]);
    //設定值化，將大於0的值調整為255，以便於顯示。
    threshold(bgr[0],bgr[0], 0, 255, THRESH_BINARY );
    threshold(bgr[1],bgr[1], 0, 255, THRESH_BINARY );
    threshold(bgr[2],bgr[2], 0, 255, THRESH_BINARY );
    //群組合各個通道
    merge(bgr,3, dstImage);
    //threshold(dstImage,dstImage, 0, 255, THRESH_BINARY );
    //調整通道順序
    cv::cvtColor(dstImage,dstImage,COLOR_BGR2RGB);
    //顯示圖形
    showLabel(dstImage,ui->label6);
}

void MainWindow::on_two_triggered()
{
    //讀入原始圖形,分析其第2位
    QString filename = QFileDialog::getOpenFileName(this,tr("開啟原始圖形"),"",tr("Image File(*.bmp *.jpg *.jpeg *.png)"));
    QTextCodec *code = QTextCodec::codecForName("gb18030");
    std::string name = code->fromUnicode(filename).data();
    srcImage = cv::imread(name);
    if(!srcImage.data)
    {
        QMessageBox msgBox;
        msgBox.setText(tr("找不到資料"));
        msgBox.exec();
    }
    //srcImage=imread("l64.jpg");  //用於測試
    //取得原始圖形的大小
    int MM,NN;
    MM=srcImage.rows;
    NN=srcImage.cols;
    //分解圖形
    Mat bgr[3];
    split(srcImage, bgr);
    //建立一個遮罩圖形，其值均為4,即為二進位的“0000 0100”。
    Mat t(MM,NN,CV_8UC1,4);
    //將遮罩圖形與各個通道進行逐位元與，得到各個通道的第3位
    cv::bitwise_and(bgr[0],t,bgr[0]);
    cv::bitwise_and(bgr[1],t,bgr[1]);
    cv::bitwise_and(bgr[2],t,bgr[2]);
    //設定值化，將大於0的值調整為255，以便於顯示。
    threshold(bgr[0],bgr[0], 0, 255, THRESH_BINARY );
    threshold(bgr[1],bgr[1], 0, 255, THRESH_BINARY );
    threshold(bgr[2],bgr[2], 0, 255, THRESH_BINARY );
    //群組合各個通道
    merge(bgr,3, dstImage);
    //threshold(dstImage,dstImage, 0, 255, THRESH_BINARY );
    //調整通道順序
    cv::cvtColor(dstImage,dstImage,COLOR_BGR2RGB);
    //顯示圖形
    showLabel(dstImage,ui->label6);
}

void MainWindow::on_three_triggered()
{
    //讀入原始圖形,分析其第3位
    QString filename = QFileDialog::getOpenFileName(this,tr("開啟原始圖形"),"",tr("Image File(*.bmp *.jpg *.jpeg *.png)"));
    QTextCodec *code = QTextCodec::codecForName("gb18030");
    std::string name = code->fromUnicode(filename).data();
    srcImage = cv::imread(name);
    if(!srcImage.data)
    {
        QMessageBox msgBox;
        msgBox.setText(tr("找不到資料"));
        msgBox.exec();
    }
    //srcImage=imread("l64.jpg");  //用於測試
    //取得原始圖形的大小
    int MM,NN;
    MM=srcImage.rows;
    NN=srcImage.cols;
    //分解圖形
    Mat bgr[3];
    split(srcImage, bgr);
    //建立一個遮罩圖形，其值均為8,即為二進位的“0000 1000”。
    Mat t(MM,NN,CV_8UC1,8);
    //將遮罩圖形與各個通道進行逐位元與，得到各個通道的第4位
    cv::bitwise_and(bgr[0],t,bgr[0]);
    cv::bitwise_and(bgr[1],t,bgr[1]);
    cv::bitwise_and(bgr[2],t,bgr[2]);
    //設定值化，將大於0的值調整為255，以便於顯示。
    threshold(bgr[0],bgr[0], 0, 255, THRESH_BINARY );
    threshold(bgr[1],bgr[1], 0, 255, THRESH_BINARY );
    threshold(bgr[2],bgr[2], 0, 255, THRESH_BINARY );
    //群組合各個通道
    merge(bgr,3, dstImage);
    //threshold(dstImage,dstImage, 0, 255, THRESH_BINARY );
    //調整通道順序
    cv::cvtColor(dstImage,dstImage,COLOR_BGR2RGB);
    //顯示圖形
    showLabel(dstImage,ui->label6);
}

void MainWindow::on_four_triggered()
{
    //讀入原始圖形,分析其第4位
    QString filename = QFileDialog::getOpenFileName(this,tr("開啟原始圖形"),"",tr("Image File(*.bmp *.jpg *.jpeg *.png)"));
    QTextCodec *code = QTextCodec::codecForName("gb18030");
    std::string name = code->fromUnicode(filename).data();
    srcImage = cv::imread(name);
    if(!srcImage.data)
    {
        QMessageBox msgBox;
        msgBox.setText(tr("找不到資料"));
        msgBox.exec();
    }
    //srcImage=imread("l64.jpg");  //用於測試
    //取得原始圖形的大小
    int MM,NN;
    MM=srcImage.rows;
    NN=srcImage.cols;
    //分解圖形
    Mat bgr[3];
    split(srcImage, bgr);
    //建立一個遮罩圖形，其值均為16,即為二進位的“0001 0000”。
    Mat t(MM,NN,CV_8UC1,16);
    //將遮罩圖形與各個通道進行逐位元與，得到各個通道的第5位
    cv::bitwise_and(bgr[0],t,bgr[0]);
    cv::bitwise_and(bgr[1],t,bgr[1]);
    cv::bitwise_and(bgr[2],t,bgr[2]);
    //設定值化，將大於0的值調整為255，以便於顯示。
    threshold(bgr[0],bgr[0], 0, 255, THRESH_BINARY );
    threshold(bgr[1],bgr[1], 0, 255, THRESH_BINARY );
    threshold(bgr[2],bgr[2], 0, 255, THRESH_BINARY );
    //群組合各個通道
    merge(bgr,3, dstImage);
    //threshold(dstImage,dstImage, 0, 255, THRESH_BINARY );
    //調整通道順序
    cv::cvtColor(dstImage,dstImage,COLOR_BGR2RGB);
    //顯示圖形
    showLabel(dstImage,ui->label6);
}

void MainWindow::on_five_triggered()
{
    //讀入原始圖形,分析其第5位
    QString filename = QFileDialog::getOpenFileName(this,tr("開啟原始圖形"),"",tr("Image File(*.bmp *.jpg *.jpeg *.png)"));
    QTextCodec *code = QTextCodec::codecForName("gb18030");
    std::string name = code->fromUnicode(filename).data();
    srcImage = cv::imread(name);
    if(!srcImage.data)
    {
        QMessageBox msgBox;
        msgBox.setText(tr("找不到資料"));
        msgBox.exec();
    }
    //srcImage=imread("l64.jpg");  //用於測試
    //取得原始圖形的大小
    int MM,NN;
    MM=srcImage.rows;
    NN=srcImage.cols;
    //分解圖形
    Mat bgr[3];
    split(srcImage, bgr);
    //建立一個遮罩圖形，其值均為32,即為二進位的“0010 0000”。
    Mat t(MM,NN,CV_8UC1,32);
    //將遮罩圖形與各個通道進行逐位元與，得到各個通道的第6位
    cv::bitwise_and(bgr[0],t,bgr[0]);
    cv::bitwise_and(bgr[1],t,bgr[1]);
    cv::bitwise_and(bgr[2],t,bgr[2]);
    //設定值化，將大於0的值調整為255，以便於顯示。
    threshold(bgr[0],bgr[0], 0, 255, THRESH_BINARY );
    threshold(bgr[1],bgr[1], 0, 255, THRESH_BINARY );
    threshold(bgr[2],bgr[2], 0, 255, THRESH_BINARY );
    //群組合各個通道
    merge(bgr,3, dstImage);
    //threshold(dstImage,dstImage, 0, 255, THRESH_BINARY );
    //調整通道順序
    cv::cvtColor(dstImage,dstImage,COLOR_BGR2RGB);
    //顯示圖形
    showLabel(dstImage,ui->label6);
}

void MainWindow::on_six_triggered()
{
    //讀入原始圖形,分析其第6位
    QString filename = QFileDialog::getOpenFileName(this,tr("開啟原始圖形"),"",tr("Image File(*.bmp *.jpg *.jpeg *.png)"));
    QTextCodec *code = QTextCodec::codecForName("gb18030");
    std::string name = code->fromUnicode(filename).data();
    srcImage = cv::imread(name);
    if(!srcImage.data)
    {
        QMessageBox msgBox;
        msgBox.setText(tr("找不到資料"));
        msgBox.exec();
    }
    //srcImage=imread("l64.jpg");  //用於測試
    //取得原始圖形的大小
    int MM,NN;
    MM=srcImage.rows;
    NN=srcImage.cols;
    //分解圖形
    Mat bgr[3];
    split(srcImage, bgr);
    //建立一個遮罩圖形，其值均為64,即為二進位的“0100 0000”。
    Mat t(MM,NN,CV_8UC1,64);
    //將遮罩圖形與各個通道進行逐位元與，得到各個通道的第7位
    cv::bitwise_and(bgr[0],t,bgr[0]);
    cv::bitwise_and(bgr[1],t,bgr[1]);
    cv::bitwise_and(bgr[2],t,bgr[2]);
    //設定值化，將大於0的值調整為255，以便於顯示。
    threshold(bgr[0],bgr[0], 0, 255, THRESH_BINARY );
    threshold(bgr[1],bgr[1], 0, 255, THRESH_BINARY );
    threshold(bgr[2],bgr[2], 0, 255, THRESH_BINARY );
    //群組合各個通道
    merge(bgr,3, dstImage);
    //threshold(dstImage,dstImage, 0, 255, THRESH_BINARY );
    //調整通道順序
    cv::cvtColor(dstImage,dstImage,COLOR_BGR2RGB);
    //顯示圖形
    showLabel(dstImage,ui->label6);
}

void MainWindow::on_seven_triggered()
{
    //讀入原始圖形,分析其第7位
    QString filename = QFileDialog::getOpenFileName(this,tr("開啟原始圖形"),"",tr("Image File(*.bmp *.jpg *.jpeg *.png)"));
    QTextCodec *code = QTextCodec::codecForName("gb18030");
    std::string name = code->fromUnicode(filename).data();
    srcImage = cv::imread(name);
    if(!srcImage.data)
    {
        QMessageBox msgBox;
        msgBox.setText(tr("找不到資料"));
        msgBox.exec();
    }
    //srcImage=imread("l64.jpg");  //用於測試
    //取得原始圖形的大小
    int MM,NN;
    MM=srcImage.rows;
    NN=srcImage.cols;
    //分解圖形
    Mat bgr[3];
    split(srcImage, bgr);
    //建立一個遮罩圖形，其值均為128,即為二進位的“1000 0000”。
    Mat t(MM,NN,CV_8UC1,128);
    //將遮罩圖形與各個通道進行逐位元與，得到各個通道的第8位（最高位）
    cv::bitwise_and(bgr[0],t,bgr[0]);
    cv::bitwise_and(bgr[1],t,bgr[1]);
    cv::bitwise_and(bgr[2],t,bgr[2]);
    //設定值化，將大於0的值調整為255，以便於顯示。
    threshold(bgr[0],bgr[0], 0, 255, THRESH_BINARY );
    threshold(bgr[1],bgr[1], 0, 255, THRESH_BINARY );
    threshold(bgr[2],bgr[2], 0, 255, THRESH_BINARY );
    //群組合各個通道
    merge(bgr,3, dstImage);
    //threshold(dstImage,dstImage, 0, 255, THRESH_BINARY );
    //調整通道順序
    cv::cvtColor(dstImage,dstImage,COLOR_BGR2RGB);
    //顯示圖形
    showLabel(dstImage,ui->label6);
}


//*******************調整序號前！***************************
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
//*******************調整序號前！***************************

void MainWindow::on_zeroGray_triggered()
{
    //當n=0時，遮罩圖形中的值即為二進位的“0000 0001”。
    //圖形srcImage與遮罩圖形進行逐位元與運算，得到圖形srcImage的第0層。
    GrayBitImage(0);
}

void MainWindow::on_oneGray_triggered()
{
    //當n=1時，遮罩圖形中的值即為二進位的“0000 0010”。
    //圖形srcImage與遮罩圖形進行逐位元與運算，得到圖形srcImage的第1層。
    GrayBitImage(1);
}

void MainWindow::on_twoGray_triggered()
{
    //當n=2時，遮罩圖形中的值即為二進位的“0000 0100”。
    //圖形srcImage與遮罩圖形進行逐位元與運算，得到圖形srcImage的第2層。
    GrayBitImage(2);
}

void MainWindow::on_threeGray_triggered()
{
    //當n=3時，遮罩圖形中的值即為二進位的“0000 1000”。
    //圖形srcImage與遮罩圖形進行逐位元與運算，得到圖形srcImage的第3層。
    GrayBitImage(3);
}

void MainWindow::on_fourGray_triggered()
{
    //當n=4時，遮罩圖形中的值即為二進位的“0001 0000”。
    //圖形srcImage與遮罩圖形進行逐位元與運算，得到圖形srcImage的第4位。
    GrayBitImage(4);
}

void MainWindow::on_fiveGray_triggered()
{
    //當n=5時，遮罩圖形中的值即為二進位的“0010 0000”。
    //圖形srcImage與遮罩圖形進行逐位元與運算，得到圖形srcImage的第5位。
    GrayBitImage(5);
}

void MainWindow::on_sixGray_triggered()
{
    //當n=6時，遮罩圖形中的值即為二進位的“0100 0000”。
    //圖形srcImage與遮罩圖形進行逐位元與運算，得到圖形srcImage的第7位。
    GrayBitImage(6);
}

void MainWindow::on_sevenGray_triggered()
{
    //當n=7時，遮罩圖形中的值即為二進位的“1000 0000”。
    //圖形srcImage與遮罩圖形進行逐位元與運算，得到圖形srcImage的第8位。
    GrayBitImage(7);
}
void MainWindow::GrayBitImage(int n)
{
    //先將圖形轉為灰階圖形，然後分析第1層
    QString filename = QFileDialog::getOpenFileName(this,tr("開啟原始圖形"),"",tr("Image File(*.bmp *.jpg *.jpeg *.png)"));
    QTextCodec *code = QTextCodec::codecForName("gb18030");
    std::string name = code->fromUnicode(filename).data();
    srcImage = cv::imread(name);
    if(!srcImage.data)
    {
        QMessageBox msgBox;
        msgBox.setText(tr("找不到資料"));
        msgBox.exec();
    }
    //srcImage=imread("l64.jpg");  //用於測試
    //取得原始圖形的大小
    int MM,NN;
    MM=srcImage.rows;
    NN=srcImage.cols;
    //色彩空間轉換
    cv::cvtColor(srcImage,srcImage,COLOR_BGR2GRAY);
    //建立一個遮罩圖形，其值均為2^n,
    //當n=0時，即為二進位的“0000 0001”。與遮罩圖形進行逐位元與運算，得到圖形srcImage的第1層。
    //當n=1時，即為二進位的“0000 0010”。與遮罩圖形進行逐位元與運算，得到圖形srcImage的第2層。
    //當n=2時，即為二進位的“0000 0100”。與遮罩圖形進行逐位元與運算，得到圖形srcImage的第3層。
    //當n=3時，即為二進位的“0000 1000”。與遮罩圖形進行逐位元與運算，得到圖形srcImage的第4層。
    //當n=4時，即為二進位的“0001 0000”。與遮罩圖形進行逐位元與運算，得到圖形srcImage的第5位。
    //當n=5時，即為二進位的“0010 0000”。與遮罩圖形進行逐位元與運算，得到圖形srcImage的第6位。
    //當n=6時，即為二進位的“0100 0000”。與遮罩圖形進行逐位元與運算，得到圖形srcImage的第7位。
    //當n=7時，即為二進位的“1000 0000”。與遮罩圖形進行逐位元與運算，得到圖形srcImage的第8位。
    Mat t(MM,NN,CV_8UC1,pow(2,n));
    //與遮罩圖形進行逐位元與運算，得到圖形srcImage的第1位（最低有效位）。
    cv::bitwise_and(srcImage,t,dstImage);
    //將圖形內非零值轉為255以方便顯示。
    threshold(dstImage,dstImage, 0, 255, THRESH_BINARY );
    //顯示圖形。
    showLabelGray(dstImage,ui->label6);
}
//*********************調整序號前***********************************
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
//*********************調整序號前***********************************
